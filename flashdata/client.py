from typing import Any
from uuid import uuid4

import httpx

AUTH_URL = "https://api.flashdata.dev/v2/api-access"
QUERY_URL = "https://data.flashdata.dev/v1/queries/realtime"


class FlashDataError(ValueError):
    """An actionable error that never includes credentials or raw server output."""


class FlashDataClient:
    def __init__(self, api_key: Any):
        if not isinstance(api_key, str) or not api_key.strip():
            raise FlashDataError("Configure your FlashData API key in the tool provider.")
        self.api_key = api_key.strip()

    def _request(self, method: str, url: str, body: dict | None = None) -> httpx.Response:
        try:
            # No redirects or retries: a lost POST response may already be billed.
            with httpx.Client(timeout=httpx.Timeout(120.0, connect=15.0),
                              follow_redirects=False, trust_env=False) as client:
                return client.request(method, url, json=body, headers={
                    "X-API-Key": self.api_key,
                    "X-Request-Id": str(uuid4()),
                    "Accept": "application/json",
                })
        except (httpx.HTTPError, ValueError):
            if method == "POST":
                raise FlashDataError(
                    "The query outcome is unknown and may already be charged. "
                    "Check Jobs in the FlashData console before submitting again."
                ) from None
            raise FlashDataError("Could not reach FlashData to validate the key. Try again later.") from None

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
