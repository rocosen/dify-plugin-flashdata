import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import yaml
from dify_plugin.entities.tool import ToolConfiguration, ToolProviderConfiguration

from flashdata.parameters import SOURCES
from scripts.build_plugins import CATALOG, ROOT, build_source


class IndependentPluginsTest(unittest.TestCase):
    def test_every_source_has_a_distinct_provider_and_matching_workflow(self):
        self.assertEqual(set(CATALOG), set(SOURCES))
        self.assertEqual(len({item['name'] for item in CATALOG.values()}), 15)
        for source, item in CATALOG.items():
            with self.subTest(source=source), tempfile.TemporaryDirectory() as temp:
                directory = Path(temp) / 'plugin'
                manifest = build_source(source, directory)
                provider = ToolProviderConfiguration.model_validate(
                    yaml.safe_load((directory / 'provider/flashdata.yaml').read_text()))
                self.assertEqual(provider.identity.name, manifest['name'])
                expected = {source} | ({'get_job', 'get_job_results'} if source == 'youtube_download' else set())
                names = set()
                for path in (directory / 'tools').glob('*.yaml'):
                    tool = ToolConfiguration.model_validate(yaml.safe_load(path.read_text()))
                    names.add(tool.identity.name)
                self.assertEqual(names, expected)
                credentials = yaml.safe_load((directory / 'provider/flashdata.yaml').read_text())['credentials_for_provider']
                self.assertEqual(set(credentials), {'api_key', 'download_storage'} if source == 'youtube_download' else {'api_key'})
                for tool in expected:
                    workflow = yaml.safe_load((ROOT / 'plugins' / source / f'{tool}.yml').read_text())
                    node = next(n['data'] for n in workflow['workflow']['graph']['nodes'] if n['data']['type'] == 'tool')
                    self.assertEqual(node['tool_name'], tool)
                    self.assertEqual(node['provider_id'], f"flashdata-dev/{item['name']}/{item['name']}")
                    self.assertEqual(node['provider_name'], node['provider_id'])
                    self.assertFalse(node['retry_config']['retry_enabled'])

    def test_staged_plugins_run_in_isolation_and_only_submit_their_source(self):
        # A fresh process cannot silently import missing runtime files from the repository.
        code = r'''
import importlib, json, pathlib, sys
from unittest.mock import patch
import httpx
from flashdata.client import AUTH_URL, ASYNC_URL, QUERY_URL, FlashDataError
from flashdata.parameters import SOURCES, build_payload
from provider.flashdata import FlashDataProvider
source=sys.argv[1]
assert set(SOURCES)=={source}
assert pathlib.Path(importlib.import_module('flashdata.client').__file__).resolve().is_relative_to(pathlib.Path.cwd())
with patch('httpx.Client.request', return_value=httpx.Response(200)) as request:
    FlashDataProvider().validate_credentials({'api_key':'fixture-key'})
    assert request.call_args.args==('GET',AUTH_URL)
module=importlib.import_module('tools.'+source)
cls=getattr(module, ''.join(p.title() for p in source.split('_'))+'Tool')
credentials={'api_key':'fixture-key'}
response={'source':source,'status':'done','results':[{'example':True}]}
if source=='youtube_download':
    credentials['download_storage']=json.dumps({'storage_type':'s3','storage_url':'fixture-bucket','region':'us-east-1','access_key':'fixture-access','secret_key':'fixture-secret'})
    response={'id':'job_fixture','source':source,'status':'pending'}
with patch('httpx.Client.request', return_value=httpx.Response(200,json=response)) as request:
    result=list(cls.from_credentials(credentials).invoke({'query':'solar','video_id':'dQw4w9WgXcQ','handle':'@GoogleDevelopers'}))
    assert request.call_count==1
    assert request.call_args.args==('POST',ASYNC_URL if source=='youtube_download' else QUERY_URL)
    assert request.call_args.kwargs['json']['source']==source
    assert result[1].message.json_object==response
    assert 'fixture-secret' not in result[0].message.text
try:
    build_payload('google_news' if source!='google_news' else 'youtube_search', {'query':'solar'})
except FlashDataError:
    pass
else:
    raise AssertionError('A different source is exposed by the dedicated package')
'''
        env = dict(os.environ)
        env.pop('PYTHONPATH', None)
        for source in CATALOG:
            with self.subTest(source=source), tempfile.TemporaryDirectory() as temp:
                directory = Path(temp) / 'plugin'
                build_source(source, directory)
                result = subprocess.run([sys.executable, '-c', code, source], cwd=directory,
                                        env=env, capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)

    def test_package_sources_exclude_unrelated_tools_and_development_files(self):
        for source in CATALOG:
            with self.subTest(source=source), tempfile.TemporaryDirectory() as temp:
                directory = Path(temp) / 'plugin'
                build_source(source, directory)
                files = {str(p.relative_to(directory)) for p in directory.rglob('*') if p.is_file()}
                self.assertFalse(any(p.startswith(('tests/', 'examples/', 'plugins/', '.git', '.env')) for p in files))
                self.assertEqual(len(list((directory / 'tools').glob('*.py'))), 3 if source == 'youtube_download' else 1)
                self.assertEqual(set(json.loads((directory / 'flashdata/sources.json').read_text())['sources']), {source})
                readme = (directory / 'README.md').read_text()
                self.assertIn(f'https://flashdata.dev/docs/sources/{source}?', readme)
                self.assertIn(f'flashdata-dev/{CATALOG[source]["name"]}', readme)
