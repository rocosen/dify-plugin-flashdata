import re
from typing import Any
from urllib.parse import urlsplit
from uuid import uuid4

import httpx

AUTH_URL = "https://api.flashdata.dev/v2/api-access"
QUERY_URL = "https://data.flashdata.dev/v1/queries/realtime"
ASYNC_URL = "https://data.flashdata.dev/v1/queries"
JOBS_URL = "https://api.flashdata.dev/v2/jobs"


class FlashDataError(ValueError):
    """An actionable error that never includes credentials or raw server output."""


class FlashDataClient:
    def __init__(self, api_key: Any):
        if not isinstance(api_key, str) or not api_key.strip():
            raise FlashDataError("Configure your FlashData API key in the tool provider.")
        self.api_key = api_key.strip()

    def _request(self, method: str, url: str, body: dict | None = None, *, authenticated=True) -> httpx.Response:
        try:
            # No redirects or retries: a lost POST response may already be billed.
            with httpx.Client(timeout=httpx.Timeout(120.0, connect=15.0),
                              follow_redirects=False, trust_env=False) as client:
                response = client.request(method, url, json=body, headers={
                    **({"X-API-Key": self.api_key} if authenticated else {}),
                    "X-Request-Id": str(uuid4()),
                    "Accept": "application/json",
                })
                if len(response.content) > 20 * 1024 * 1024:
                    raise FlashDataError("Result exceeds the plugin's 20 MiB limit. Retrieve it from FlashData Jobs; do not repeat the query.")
                return response
        except FlashDataError:
            raise
        except (httpx.HTTPError, ValueError):
            if method == "POST":
                raise FlashDataError(
                    "The query outcome is unknown and may already be charged. "
                    "Check Jobs in the FlashData console before submitting again."
                ) from None
            raise FlashDataError("Could not complete this read. Retry the read later; do not resubmit the query.") from None

    @staticmethod
    def _check_status(response: httpx.Response) -> None:
        if response.status_code == 200:
            return
        messages = {
            401: "FlashData rejected the API key. Check or replace it in the provider settings.",
            402: "Insufficient FlashData credits. Add credits in the FlashData console.",
            403: "This FlashData account or key cannot access the requested source.",
            429: "FlashData rate or quota limit reached. Wait before trying again.",
        }
        message = messages.get(response.status_code, "FlashData returned an unexpected HTTP response.")
        raise FlashDataError(f"{message} HTTP {response.status_code}. No automatic retry was made.")

    def validate_credentials(self) -> None:
        self._check_status(self._request("GET", AUTH_URL))

    def query(self, payload: dict) -> dict:
        response = self._request("POST", QUERY_URL, payload)
        self._check_status(response)
        try:
            data = response.json()
        except ValueError:
            data = None
        if not isinstance(data, dict):
            raise FlashDataError("The query response could not be read. Check Jobs before submitting again.")
        job = data.get("job")
        if data.get("status") == "failed" or (isinstance(job, dict) and job.get("status") == "failed"):
            raise FlashDataError("FlashData could not complete the query. Check its details in Jobs.")
        if data.get("status") not in (None, "done", "completed") or not isinstance(data.get("results"), list):
            raise FlashDataError("No completed result was returned. Check Jobs before submitting again.")
        return data

    @staticmethod
    def _json(response):
        try:
            data = response.json()
        except ValueError:
            data = None
        if not isinstance(data, dict):
            raise FlashDataError("FlashData returned unreadable data. Check Jobs before submitting a new query.")
        return data

    def submit_download(self, payload):
        response = self._request("POST", ASYNC_URL, payload)
        self._check_status(response)
        data = self._json(response)
        if not isinstance(data.get("id"), str) or data.get("status") not in ("pending", "processing"):
            raise FlashDataError("The submission receipt could not be read. Check Jobs before submitting again.")
        return data

    @staticmethod
    def _job_id(value):
        if not isinstance(value, str) or not re.fullmatch(r"job_[A-Za-z0-9-]{1,100}", value):
            raise FlashDataError("Enter the job_id returned by the download submission.")
        return value

    def get_job(self, job_id):
        response = self._request("GET", f"{JOBS_URL}/{self._job_id(job_id)}")
        self._check_status(response)
        data = self._json(response)
        if not isinstance(data.get("job"), dict):
            raise FlashDataError("The job status could not be read. Retry this read; do not submit a new query.")
        return data

    def get_job_results(self, job_id):
        status = self.get_job(job_id)
        if status["job"].get("status") != "completed":
            return status
        identity = self._request("GET", AUTH_URL)
        self._check_status(identity)
        origin = self._json(identity).get("result_origin")
        link = self._request("GET", f"{JOBS_URL}/{job_id}/results")
        if link.status_code != 302:
            self._check_status(link)
            raise FlashDataError("No result link was returned. Retry this read; do not resubmit the query.")
        try:
            trusted = urlsplit(origin) if isinstance(origin, str) else None
            target = urlsplit(link.headers.get("location", ""))
            if (not trusted or trusted.scheme != "https" or not trusted.hostname
                or trusted.username or trusted.password or trusted.path not in ("", "/")
                or trusted.query or trusted.fragment or target.scheme != "https"
                or target.username or target.password or target.fragment
                or (target.hostname, target.port) != (trusted.hostname, trusted.port)):
                raise ValueError()
        except ValueError:
            raise FlashDataError("The result link is not from FlashData's trusted result storage.") from None
        # Signed storage URLs authenticate themselves. Never forward the API key.
        result = self._request("GET", target.geturl(), authenticated=False)
        self._check_status(result)
        return {**status, "output": self._json(result)}
