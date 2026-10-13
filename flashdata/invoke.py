import json

from flashdata.client import FlashDataClient
from flashdata.parameters import build_payload


def invoke(tool, source, parameters):
    client = FlashDataClient(tool.runtime.credentials.get("api_key"))
    if source in ("get_job", "get_job_results"):
        result = getattr(client, source)(parameters.get("job_id"))
    else:
        payload = build_payload(source, parameters, tool.runtime.credentials.get("download_storage"))
        result = client.submit_download(payload) if source == "youtube_download" else client.query(payload)
    # Text is available to Agents; JSON preserves the full API response for workflows.
    yield tool.create_text_message(json.dumps(result, ensure_ascii=False))
    yield tool.create_json_message(result)
