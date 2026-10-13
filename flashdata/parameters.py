import json
import re
from pathlib import Path

from jsonschema import Draft7Validator
from typing import Any
from urllib.parse import parse_qs, urlsplit

from flashdata.client import FlashDataError


def video_id(value: Any) -> str:
    value = value.strip() if isinstance(value, str) else ""
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", value):
        return value
    try:
        url = urlsplit(value)
        parts = url.path.split("/")
        candidate = ""
        if url.scheme in ("http", "https") and not url.username and not url.password:
            if url.hostname == "youtu.be" and len(parts) in (2, 3) and (len(parts) == 2 or parts[2] == ""):
                candidate = parts[1]
            elif url.hostname in ("youtube.com", "www.youtube.com", "m.youtube.com", "music.youtube.com"):
                if url.path == "/watch":
                    candidate = parse_qs(url.query).get("v", [""])[0]
                elif len(parts) in (3, 4) and (len(parts) == 3 or parts[3] == "") and parts[1] in ("shorts", "embed", "live"):
                    candidate = parts[2]
        if re.fullmatch(r"[A-Za-z0-9_-]{11}", candidate):
            return candidate
    except ValueError:
        pass
    raise FlashDataError("Enter an 11-character YouTube video ID or a youtube.com / youtu.be video URL.")


CATALOG = json.loads(Path(__file__).with_name("sources.json").read_text())
SOURCES = CATALOG["sources"]


def validate(value, schema, label):
    if not Draft7Validator(schema).is_valid(value):
        # Validator messages can contain input values, including storage secrets.
        raise FlashDataError(f"Invalid {label}. Check the documented fields, types and limits.")


def json_object(value, label):
    try:
        result = json.loads(value) if isinstance(value, str) else None
    except (ValueError, TypeError):
        result = None
    if not isinstance(result, dict):
        raise FlashDataError(f"{label} must be a JSON object.")
    return result


def storage_config(raw):
    storage = json_object(raw, "Download storage credential")
    validate(storage, CATALOG["storage"], "download storage credential")
    kind = storage["storage_type"]
    bucket = storage["storage_url"].strip()
    if not re.fullmatch(r"[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]", bucket) or ".." in bucket:
        raise FlashDataError("storage_url must be a bucket/container name; put folders in object_prefix.")
    storage["storage_url"] = bucket
    provider_fields = (["service_account"] if kind == "gcs" else
                       ["account_name", "sas_token"] if kind == "azure" else
                       ["access_key", "secret_key", "region"] if kind == "cos" else
                       ["access_key", "secret_key", "region", "endpoint_url"])
    if set(storage) - {"storage_type", "storage_url", "object_prefix", *provider_fields}:
        raise FlashDataError("The storage credential contains fields for a different provider.")
    if "object_prefix" in storage:
        prefix = storage["object_prefix"].strip().removesuffix("/")
        if not prefix or len(prefix) > 512 or any(
            part in (".", "..") or not re.fullmatch(r"[A-Za-z0-9._-]+", part) for part in prefix.split("/")
        ):
            raise FlashDataError("object_prefix must use safe folder names, up to 512 characters.")
        storage["object_prefix"] = prefix
    if kind == "gcs":
        account = storage.get("service_account", {})
        if (not all(account.get(k) for k in ("project_id", "client_email", "private_key"))
            or not re.fullmatch(r"[^@\s]+@[^@\s]+\.gserviceaccount\.com", account.get("client_email", ""))
            or "BEGIN PRIVATE KEY" not in account.get("private_key", "")):
            raise FlashDataError("GCS requires project_id, service-account client_email and a PEM private_key.")
    elif kind == "azure":
        sas = storage.get("sas_token", "").removeprefix("?")
        fields = parse_qs(sas)
        if (not storage.get("account_name") or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", bucket)
            or not all(fields.get(k) for k in ("sig", "se", "sv"))
            or "w" not in fields.get("sp", [""])[0] or fields.get("sr") != ["c"]
            or "\n" in sas or "\r" in sas):
            raise FlashDataError("Azure requires an account name and container SAS with write permission and expiry.")
        storage["sas_token"] = sas
    else:
        if not all(storage.get(k, "").strip() for k in ("access_key", "secret_key")):
            raise FlashDataError("Download storage requires access_key and secret_key in the provider credential.")
        if kind == "s3_compatible" and not storage.get("endpoint_url"):
            raise FlashDataError("S3-compatible storage requires endpoint_url.")
        region = storage.get("region", "")
        if ((kind == "cos" and (not re.fullmatch(r"ap-[a-z0-9-]+", region) or not re.search(r"-\d{5,}$", bucket)))
            or (kind == "bos" and region not in ("bj", "su", "hkg"))
            or (kind == "tos" and not re.fullmatch(r"(?:cn|ap|eu|us)-[a-z0-9-]+", region))):
            raise FlashDataError("Check the storage provider region and bucket name.")
    return storage


def download_options(params):
    kind = params.setdefault("download_type", "audio_video")
    formats = ("m4a", "mp3", "opus") if kind == "audio" else ("mp4", "webm", "mkv")
    params.setdefault("output_format", "m4a" if kind == "audio" else "mp4")
    if params["output_format"] not in formats:
        raise FlashDataError("output_format is incompatible with download_type.")
    selector = params.get("yt_dlp_format")
    if selector and (not selector.strip() or any(ord(c) < 32 or ord(c) == 127 for c in selector)):
        raise FlashDataError("yt_dlp_format must not contain control characters.")
    if not selector:
        if kind == "audio" and any(k in params for k in ("video_quality", "fps")):
            raise FlashDataError("video_quality and fps do not apply to audio downloads.")
        if kind == "video" and "audio_language" in params:
            raise FlashDataError("audio_language does not apply to video-only downloads.")
    if kind != "audio" and "audio_quality" in params:
        raise FlashDataError("audio_quality applies only to audio downloads.")
    seconds = {}
    for field in ("start_at", "end_at"):
        if field in params:
            h, m, s = map(int, params[field].split(":"))
            seconds[field] = h * 3600 + m * 60 + s
            if seconds[field] > 43200:
                raise FlashDataError("Clip timestamps must not exceed 12:00:00.")
    if "end_at" in seconds and seconds["end_at"] <= seconds.get("start_at", 0):
        raise FlashDataError("end_at must be later than start_at.")
    return params


def build_payload(source: str, values: dict[str, Any], storage_json=None) -> dict:
    if source not in SOURCES:
        raise FlashDataError("Unsupported FlashData tool.")
    schema = SOURCES[source]["schema"]
    args = {k: v for k, v in values.items() if k in schema["properties"] and v is not None and v != ""}
    for field in ("query", "handle"):
        if isinstance(args.get(field), str):
            args[field] = args[field].strip()
    if "video_id" in schema["properties"]:
        args["video_id"] = video_id(args.get("video_id"))
    if "filters" in schema["properties"] and values.get("filters_json") not in (None, ""):
        args["filters"] = json_object(values["filters_json"], "Search filters")
    if source != "youtube_download":
        for field, definition in schema["properties"].items():
            if "default" in definition:
                args.setdefault(field, definition["default"])
        # Preserve the four-tool release defaults for existing workflows.
        if source == "google_search":
            for field, default in {"num": 10, "page": 1, "autocorrect": True}.items():
                args.setdefault(field, default)
        if source == "youtube_search" and values.get("max_results") in (None, ""):
            args["max_results"] = 10
    validate(args, schema, source + " parameters")
    payload = {"source": source}
    for field in ("query", "video_id", "handle"):
        if field in args:
            payload[field] = args.pop(field)
    if source == "youtube_download":
        args = download_options(args)
        args["storage"] = storage_config(storage_json)
    payload["params"] = args
    return payload
