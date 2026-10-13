import json
from pathlib import Path
import unittest
from unittest.mock import patch

import httpx
import yaml
from dify_plugin.entities.tool import ToolConfiguration
from flashdata.client import ASYNC_URL, AUTH_URL, JOBS_URL, FlashDataClient, FlashDataError
from flashdata.parameters import SOURCES, build_payload, storage_config
from tools.youtube_download import YoutubeDownloadTool
from tools.get_job import GetJobTool
from tools.get_job_results import GetJobResultsTool

STORAGE = {'storage_type':'s3','storage_url':'fixture-bucket','region':'us-east-1','access_key':'fixture-access','secret_key':'fixture-secret'}
VIDEO = 'dQw4w9WgXcQ'
JOB = 'job_00000000-0000-4000-8000-000000000001'


class CapabilitiesTest(unittest.TestCase):
    def test_google_sources_are_independent_and_preserve_false(self):
        for source in ['google_search','google_news','google_images','google_shopping','google_videos','google_places']:
            with self.subTest(source=source):
                payload = build_payload(source, {'query':' solar ','num':3,'gl':'gb','autocorrect':False})
                self.assertEqual(payload['source'], source)
                self.assertEqual(payload['query'], 'solar')
                self.assertFalse(payload['params']['autocorrect'])
        self.assertNotIn('num', build_payload('google_news', {'query':'solar'})['params'])

    def test_extended_search_and_filters_contract(self):
        values = {'query':'python', 'max_results':700, 'filters_json':'{"subtitles":false,"sort_by":"upload_date"}'}
        payload = build_payload('youtube_search_extended', values)
        self.assertEqual(payload['params']['max_results'],700)
        self.assertFalse(payload['params']['filters']['subtitles'])
        for extra in [{'max_results':701},{'max_results':True},{'filters_json':'[]'},
                      {'filters_json':'{"sort_by":"newest"}'},{'filters_json':'{"unknown":true}'}]:
            with self.subTest(extra=extra), self.assertRaises(FlashDataError):
                build_payload('youtube_search_extended', {'query':'python',**extra})

    def test_captions_transcript_and_channel_differ(self):
        self.assertFalse(build_payload('youtube_captions', {'video_id':VIDEO})['params']['auto'])
        self.assertTrue(build_payload('youtube_transcript', {'video_id':VIDEO})['params']['auto'])
        self.assertEqual(build_payload('youtube_trainability', {'video_id':VIDEO})['params'],{})
        self.assertEqual(build_payload('youtube_channel', {'handle':'@GoogleDevelopers'})['handle'],'@GoogleDevelopers')
        self.assertEqual(build_payload('youtube_suggestions', {'query':'how to'})['params'],{'language':'en','region':'US'})
        for source,values in [('youtube_channel',{'handle':'x','video_limit':101}),('youtube_suggestions',{'query':'x','region':'USA'})]:
            with self.subTest(source=source), self.assertRaises(FlashDataError):build_payload(source,values)

    def test_download_semantics_and_credentials(self):
        body=build_payload('youtube_download',{'video_id':VIDEO,'download_type':'audio'},json.dumps(STORAGE))
        self.assertEqual(body['params']['output_format'],'m4a')
        self.assertNotIn('video_quality',body['params'])
        self.assertEqual(body['params']['storage'],STORAGE)
        bad=[{'download_type':'audio','video_quality':'<=720'}, {'download_type':'audio','output_format':'mp4'},
             {'download_type':'video','audio_language':'original'}, {'audio_quality':'128'},
             {'start_at':'00:01:00','end_at':'00:00:59'}, {'end_at':'13:00:00'},
             {'fps':'>=241'}, {'yt_dlp_format':'best\n'}, {'upload_metadata':'false'}]
        for extra in bad:
            with self.subTest(extra=extra), self.assertRaises(FlashDataError):
                build_payload('youtube_download',{'video_id':VIDEO,**extra},json.dumps(STORAGE))

    def test_storage_failures_do_not_expose_values(self):
        bad=[None, 'not-json-secret', '{}', json.dumps({**STORAGE,'storage_url':'https://bucket/file'}),
             json.dumps({**STORAGE,'secret_key':None}), json.dumps({**STORAGE,'object_prefix':'../escape'}),
             json.dumps({**STORAGE,'unknown-secret':'DO-NOT-LEAK'}),
             json.dumps({'storage_type':'gcs','storage_url':'fixture-bucket'}),
             json.dumps({'storage_type':'azure','storage_url':'fixture-bucket','account_name':'fixture','sas_token':'secret'})]
        for value in bad:
            with self.subTest(value=value),self.assertRaises(FlashDataError) as error:storage_config(value)
            self.assertNotIn('DO-NOT-LEAK',str(error.exception))
            self.assertNotIn('not-json-secret',str(error.exception))

    def test_storage_never_enters_tool_schema_or_dsl(self):
        for path in Path('tools').glob('*.yaml'):
            config=ToolConfiguration.model_validate(yaml.safe_load(path.read_text()))
            self.assertFalse(any(p.name in ('storage','download_storage','access_key','secret_key') for p in config.parameters))
        for path in Path('examples').glob('*.yml'):
            text=path.read_text()
            self.assertNotIn('secret_key',text)
            self.assertNotIn('download_storage',text)
            data=yaml.safe_load(text)
            tool=data['workflow']['graph']['nodes'][1]['data']
            config=yaml.safe_load(Path('tools',tool['tool_name']+'.yaml').read_text())
            self.assertLessEqual(set(tool['tool_parameters']),{p['name'] for p in config['parameters']})
            self.assertFalse(tool['retry_config']['retry_enabled'])
        self.assertEqual(len(SOURCES),15)
        self.assertTrue(all(Path('examples',source+'.yml').exists() for source in SOURCES))


class AsyncLifecycleTest(unittest.TestCase):
    def test_submission_emits_receipt_without_storage(self):
        receipt={'id':JOB,'source':'youtube_download','status':'pending','usage':{'credits':0}}
        tool=YoutubeDownloadTool.from_credentials({'api_key':'fixture-key','download_storage':json.dumps(STORAGE)})
        with patch('httpx.Client.request',return_value=httpx.Response(200,json=receipt)) as request:
            messages=list(tool.invoke({'video_id':VIDEO}))
        self.assertEqual(request.call_args.args,('POST',ASYNC_URL))
        self.assertEqual(request.call_count,1)
        self.assertEqual(request.call_args.kwargs['json']['params']['storage'],STORAGE)
        self.assertEqual(messages[1].message.json_object,receipt)
        self.assertNotIn('fixture-secret',messages[0].message.text)

    def test_missing_storage_never_submits(self):
        with patch('httpx.Client.request') as request,self.assertRaises(FlashDataError):
            list(YoutubeDownloadTool.from_credentials({'api_key':'fixture-key'}).invoke({'video_id':VIDEO}))
        request.assert_not_called()

    def test_submit_timeout_does_not_retry(self):
        with patch('httpx.Client.request',side_effect=httpx.ReadTimeout('private')) as request,self.assertRaisesRegex(FlashDataError,'outcome is unknown'):
            FlashDataClient('fixture-key').submit_download({})
        self.assertEqual(request.call_count,1)

    def test_pending_or_failed_job_does_not_submit_or_fetch_results(self):
        for state in ('pending','processing','failed'):
            response={'job':{'id':JOB,'status':state}}
            with patch('httpx.Client.request',return_value=httpx.Response(200,json=response)) as request:
                messages=list(GetJobResultsTool.from_credentials({'api_key':'fixture-key'}).invoke({'job_id':JOB}))
            self.assertEqual(messages[1].message.json_object,response)
            self.assertEqual(request.call_count,1)
            self.assertEqual(request.call_args.args,('GET',f'{JOBS_URL}/{JOB}'))

    def test_job_status_helper(self):
        response={'job':{'id':JOB,'status':'processing'}}
        with patch('httpx.Client.request',return_value=httpx.Response(200,json=response)):
            messages=list(GetJobTool.from_credentials({'api_key':'fixture-key'}).invoke({'job_id':JOB}))
        self.assertEqual(messages[1].message.json_object,response)

    def test_completed_result_follows_only_trusted_origin_without_api_key(self):
        origin='https://results.example.test'
        output={'results':[{'file_url':'s3://fixture-bucket/video.mp4','file_size':123}]}
        responses=[httpx.Response(200,json={'job':{'id':JOB,'status':'completed'}}),
                   httpx.Response(200,json={'result_origin':origin}),
                   httpx.Response(302,headers={'location':origin+'/receipt.json?signature=fixture'}),
                   httpx.Response(200,json=output)]
        with patch('httpx.Client.request',side_effect=responses) as request:
            messages=list(GetJobResultsTool.from_credentials({'api_key':'fixture-key'}).invoke({'job_id':JOB}))
        self.assertEqual(messages[1].message.json_object['output'],output)
        self.assertEqual(request.call_args_list[1].args,('GET',AUTH_URL))
        self.assertEqual(request.call_args_list[2].args,('GET',f'{JOBS_URL}/{JOB}/results'))
        self.assertNotIn('X-API-Key',request.call_args_list[-1].kwargs['headers'])
        self.assertTrue(all(c.args[0]=='GET' for c in request.call_args_list))

    def test_untrusted_result_urls_stop_before_fetch(self):
        for url in ['https://evil.test/file','http://results.example.test/file','https://user:pass@results.example.test/file','https://results.example.test:444/file','https://results.example.test/file#fragment']:
            responses=[httpx.Response(200,json={'job':{'status':'completed'}}),
                       httpx.Response(200,json={'result_origin':'https://results.example.test'}),
                       httpx.Response(302,headers={'location':url})]
            with self.subTest(url=url),patch('httpx.Client.request',side_effect=responses) as request,self.assertRaises(FlashDataError):
                FlashDataClient('fixture-key').get_job_results(JOB)
            self.assertEqual(request.call_count,3)

    def test_expired_results_and_invalid_job_id(self):
        responses=[httpx.Response(200,json={'job':{'status':'completed'}}),
                   httpx.Response(200,json={'result_origin':'https://results.example.test'}),httpx.Response(410)]
        with patch('httpx.Client.request',side_effect=responses) as request,self.assertRaisesRegex(FlashDataError,'410'):
            FlashDataClient('fixture-key').get_job_results(JOB)
        self.assertEqual(request.call_count,3)
        for value in ['../secrets','https://example.test/x',None,'job_x?query=x']:
            with patch('httpx.Client.request') as request,self.assertRaises(FlashDataError):FlashDataClient('fixture-key').get_job(value)
            request.assert_not_called()

if __name__=='__main__':unittest.main()
