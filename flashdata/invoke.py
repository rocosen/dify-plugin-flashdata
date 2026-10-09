import json

from flashdata.client import FlashDataClient
from flashdata.parameters import build_payload


def invoke(tool, source, parameters):
    payload = build_payload(source, parameters)
    result = FlashDataClient(tool.runtime.credentials.get("api_key")).query(payload)
    # Text is available to Agents; JSON preserves the full API response for workflows.
    yield tool.create_text_message(json.dumps(result, ensure_ascii=False))
    yield tool.create_json_message(result)
