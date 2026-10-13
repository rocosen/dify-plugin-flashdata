import importlib
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import httpx
import yaml
from dify_plugin.entities.tool import ToolConfiguration, ToolProviderConfiguration
from dify_plugin.errors.tool import ToolProviderCredentialValidationError

from flashdata.client import AUTH_URL, QUERY_URL, FlashDataClient, FlashDataError
from flashdata.parameters import build_payload, video_id
from provider.flashdata import FlashDataProvider


class ParametersTest(unittest.TestCase):
    def test_supported_video_urls(self):
        for value in ["dQw4w9WgXcQ", " https://youtu.be/dQw4w9WgXcQ?t=3 ",
                      "https://www.youtube.com/watch?v=dQw4w9WgXcQ&feature=share",
                      "https://m.youtube.com/shorts/dQw4w9WgXcQ",
                      "https://music.youtube.com/embed/dQw4w9WgXcQ",
                      "https://youtube.com/live/dQw4w9WgXcQ"]:
            with self.subTest(value=value):
                self.assertEqual(video_id(value), "dQw4w9WgXcQ")

    def test_rejects_invalid_video_destinations(self):
        for value in [None, "short", "https://youtube.com.evil.test/watch?v=dQw4w9WgXcQ",
                      "ftp://youtu.be/dQw4w9WgXcQ", "https://user:password@youtube.com/watch?v=dQw4w9WgXcQ",
                      "https://youtube.com/watch?v=invalid", "http://localhost/dQw4w9WgXcQ",
                      "https://youtu.be/dQw4w9WgXcQ/extra", "https://youtube.com/shorts/dQw4w9WgXcQ/extra"]:
            with self.subTest(value=value), self.assertRaises(FlashDataError):
                video_id(value)

    def test_false_is_preserved(self):
        payload = build_payload("youtube_transcript", {"video_id":"dQw4w9WgXcQ", "auto":False})
        self.assertEqual(payload["params"], {"language":"en", "auto":False})
        payload = build_payload("youtube_metadata", {"video_id":"dQw4w9WgXcQ", "include_formats":False})
        self.assertFalse(payload["params"]["include_formats"])

    def test_bounds_and_types_before_query(self):
        invalid = [{"query":" "}, {"query":"x"*2001}, {"query":"x", "num":0},
                   {"query":"x", "page":101}, {"query":"x", "num":1.5},
                   {"query":"x", "num":True}, {"query":"x", "hl":"../en"},
                   {"query":"x", "gl":"USA"}, {"query":"x", "autocorrect":"false"},
                   {"query":"x", "location":"x"*201}]
        for values in invalid:
            with self.subTest(values=values), self.assertRaises(FlashDataError):
                build_payload("google_search", values)
        self.assertEqual(build_payload("google_search", {"query":" x ", "num":3.0})["query"], "x")
        with self.assertRaises(FlashDataError):
            build_payload("youtube_search", {"query":"x", "max_results":21})


class ClientTest(unittest.TestCase):
    def test_free_provider_validation(self):
        with patch("httpx.Client.request", return_value=httpx.Response(200)) as request:
            FlashDataProvider().validate_credentials({"api_key":"fixture-key"})
        self.assertEqual(request.call_args.args, ("GET", AUTH_URL))
        self.assertIsNone(request.call_args.kwargs["json"])

    def test_auth_failure_is_safe(self):
        with patch("httpx.Client.request", return_value=httpx.Response(401, text="private server output")):
            with self.assertRaises(ToolProviderCredentialValidationError) as error:
                FlashDataProvider().validate_credentials({"api_key":"fixture-key"})
        self.assertNotIn("private server output", str(error.exception))
        self.assertIn("401", str(error.exception))

    def test_query_headers_fixed_destination_and_no_redirects(self):
        result = {"status":"done", "source":"google_search", "results":[], "usage":{"credits":0.02}}
        with patch("httpx.Client") as factory:
            client = factory.return_value.__enter__.return_value
            client.request.return_value = httpx.Response(200, json=result)
            self.assertEqual(FlashDataClient("fixture-key").query({"source":"google_search"}), result)
        self.assertEqual(client.request.call_args.args, ("POST", QUERY_URL))
        self.assertEqual(client.request.call_args.kwargs["headers"]["X-API-Key"], "fixture-key")
        self.assertFalse(factory.call_args.kwargs["follow_redirects"])
        self.assertFalse(factory.call_args.kwargs["trust_env"])
        self.assertEqual(client.request.call_count, 1)

    def test_network_failure_is_not_retried(self):
        with patch("httpx.Client.request", side_effect=httpx.ReadTimeout("secret upstream detail")) as request:
            with self.assertRaisesRegex(FlashDataError, "outcome is unknown") as error:
                FlashDataClient("fixture-key").query({})
        self.assertEqual(request.call_count, 1)
        self.assertNotIn("secret upstream detail", str(error.exception))

    def test_realtime_response_without_optional_status(self):
        result = {"results":[{"title":"Example"}], "usage":{"credits":0.02}}
        with patch("httpx.Client.request", return_value=httpx.Response(200,json=result)):
            self.assertEqual(FlashDataClient("fixture-key").query({}),result)

    def test_http_errors_are_not_retried(self):
        for status in (301,401,402,403,429,500,503,504):
            with self.subTest(status=status), patch("httpx.Client.request", return_value=httpx.Response(status, text="sensitive")) as request:
                with self.assertRaises(FlashDataError) as error:
                    FlashDataClient("fixture-key").query({})
                self.assertIn(str(status),str(error.exception))
                self.assertNotIn("sensitive",str(error.exception))
                self.assertEqual(request.call_count,1)

    def test_failed_malformed_and_incomplete_responses(self):
        for result in ([], {"status":"failed"}, {"job":{"status":"failed"}},
                       {"status":"running"}, {"status":"done", "results":None}):
            with self.subTest(result=result), patch("httpx.Client.request", return_value=httpx.Response(200,json=result)):
                with self.assertRaises(FlashDataError):
                    FlashDataClient("fixture-key").query({})
        with patch("httpx.Client.request", return_value=httpx.Response(200,text="not JSON")):
            with self.assertRaisesRegex(FlashDataError, "Check Jobs"):
                FlashDataClient("fixture-key").query({})


class SDKIntegrationTest(unittest.TestCase):
    def test_realtime_tools_load_and_emit_text_and_json(self):
        provider = ToolProviderConfiguration.model_validate(yaml.safe_load(Path("provider/flashdata.yaml").read_text()))
        self.assertEqual(len(provider.tools),17)
        for path in Path("tools").glob("*.yaml"):
            config = ToolConfiguration.model_validate(yaml.safe_load(path.read_text()))
            source = config.identity.name
            if source in ("youtube_download", "get_job", "get_job_results"):
                continue
            module = importlib.import_module("tools."+source)
            cls = getattr(module, "".join(word.title() for word in source.split("_"))+"Tool")
            result = {"source":source,"status":"done","results":[{"text":"Evidence"}],"usage":{"credits":0.01}}
            with self.subTest(source=source), patch("httpx.Client.request", return_value=httpx.Response(200,json=result)) as request:
                messages = list(cls.from_credentials({"api_key":"fixture-key"}).invoke({"query":"Dify", "video_id":"dQw4w9WgXcQ", "handle":"@GoogleDevelopers"}))
                self.assertEqual(len(messages),2)
                self.assertEqual(json.loads(messages[0].message.text),result)
                self.assertEqual(messages[1].message.json_object,result)
                self.assertEqual(request.call_args.kwargs["json"]["source"], source)

    def test_invalid_tool_input_never_makes_a_request(self):
        from tools.google_search import GoogleSearchTool
        with patch("httpx.Client.request") as request:
            with self.assertRaises(FlashDataError):
                list(GoogleSearchTool.from_credentials({"api_key":"fixture-key"}).invoke({"query":""}))
        request.assert_not_called()


if __name__ == "__main__":
    unittest.main()
