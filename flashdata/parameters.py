import re
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


def build_payload(source: str, values: dict[str, Any]) -> dict:
    params = {}
    payload = {"source": source, "params": params}
    if source in ("google_search", "youtube_search"):
        query = values.get("query")
        if not isinstance(query, str) or not 1 <= len(query.strip()) <= 2000:
            raise FlashDataError("Query must contain between 1 and 2,000 characters.")
        payload["query"] = query.strip()
    elif source in ("youtube_metadata", "youtube_transcript"):
        payload["video_id"] = video_id(values.get("video_id"))
    else:
        raise FlashDataError("Unsupported FlashData tool.")

    defaults = {
        "google_search": {"num": 10, "page": 1, "autocorrect": True},
        "youtube_search": {"max_results": 10},
        "youtube_metadata": {"include_chapters": True, "include_formats": True},
        "youtube_transcript": {"language": "en", "auto": True},
    }[source]
    fields = list(defaults) + (["gl", "hl", "location", "tbs"] if source == "google_search" else [])
    for field in fields:
        value = values.get(field)
        if value is None or value == "":
            value = defaults.get(field)
        if value is None:
            continue
        if field in ("num", "page", "max_results"):
            maximum = 20 if field == "max_results" else 100
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not 1 <= value <= maximum or int(value) != value:
                raise FlashDataError(f"{field} must be an integer between 1 and {maximum}.")
            value = int(value)
        elif field in ("autocorrect", "include_chapters", "include_formats", "auto"):
            if not isinstance(value, bool):
                raise FlashDataError(f"{field} must be true or false.")
        elif field in ("hl", "language", "gl"):
            pattern = r"[A-Za-z]{2}" if field == "gl" else r"[A-Za-z0-9-]{1,35}"
            if not isinstance(value, str) or not re.fullmatch(pattern, value):
                raise FlashDataError(f"{field} must be a valid {'country' if field == 'gl' else 'language'} code.")
        elif not isinstance(value, str) or len(value) > 200:
            raise FlashDataError(f"{field} must be at most 200 characters.")
        params[field] = value
    return payload
