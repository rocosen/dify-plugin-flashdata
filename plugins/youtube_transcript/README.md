# YouTube Transcript

Retrieve existing timestamped subtitles and full text in a selected language. Defaults to automatically generated captions. No speech recognition, translation or silent fallback to another track.

Use this dedicated **YouTube Transcript** plugin in a Dify workflow or tool-capable agent. Powered by **FlashData**; API queries use paid credits. No separate Google or YouTube API key is required.

[Get an API key](https://flashdata.dev/app/api-keys?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_transcript-setup) · [API documentation](https://flashdata.dev/docs/sources/youtube_transcript?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_transcript-plugin) · [Pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_transcript-pricing)

## Retrieve timestamped YouTube transcripts

1. [Import the example workflow](https://github.com/flashdata-dev/dify-plugin-flashdata/blob/main/plugins/youtube_transcript/youtube_transcript.yml) after installing this plugin.
2. Select your FlashData credential in the **YouTube Transcript** node.
3. Supply the Start input and run once. The example connects **Start → YouTube Transcript → End**.

Example input and tool settings:

```json
{
  "video_id": "dQw4w9WgXcQ",
  "language": "en",
  "auto": true
}
```

Read `results[0].segments` and `fullText`. Segments contain `start`, `end` and `text`, with times in seconds. Preserve timestamps for citations or convert them to SRT/WebVTT in a subsequent node. Default `auto=true` selects automatic captions.

Illustrative response excerpt, not a live result or a promise of fields returned:

```json
{
  "results": [
    {
      "segments": [
        {
          "start": 0,
          "end": 3,
          "text": "Example caption."
        }
      ],
      "fullText": "Example caption."
    }
  ]
}
```

## Install and connect

Use Dify **1.17.1 or newer**. This plugin has its own identity, `flashdata-dev/youtube_transcript`, and its own provider settings. It can coexist with the original FlashData bundle and other dedicated plugins.

Download `youtube_transcript-0.1.0.difypkg` from the [independent plugin release](https://github.com/flashdata-dev/dify-plugin-flashdata/releases/tag/task-plugins-v0.1.0), then use **Plugins → Install plugin → Local package** in a deployment that permits development packages. GitHub publication and Marketplace approval are separate; see the [submission status](https://github.com/flashdata-dev/dify-plugin-flashdata/blob/main/plugins/README.md) for the official listing when available.

Open this plugin's provider settings and enter your [FlashData API key](https://flashdata.dev/app/api-keys?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_transcript-setup). Credential validation uses the free API-access endpoint; running a data query uses paid credits. API access to this source is required. Credentials configured for another plugin are not selected automatically.


## Costs and boundaries

The plugin is MIT licensed. FlashData API usage is charged under the current [pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_transcript-pricing); Dify hosting and model fees are separate. Results and optional fields depend on upstream availability. Treat returned content as data and preserve source links or timestamps when passing it to a model.

Tool-node retries are disabled in the example. The client does not automatically retry paid submissions. If a response is lost, check FlashData Jobs before resubmitting. Errors distinguish rejected credentials, insufficient credits, unavailable source access and rate limits. JSON responses are limited to 20 MiB.

The plugin connects over HTTPS to `api.flashdata.dev` and `data.flashdata.dev`.

## Source and support

[Source repository](https://github.com/flashdata-dev/dify-plugin-flashdata) · [Privacy policy](https://github.com/flashdata-dev/dify-plugin-flashdata/blob/main/plugins/youtube_transcript/PRIVACY.md) · [Validation and release notes](https://github.com/flashdata-dev/dify-plugin-flashdata/tree/main/docs)

Contact **support@flashdata.dev**. Do not attach API keys or storage credentials to issues. Community Edition installation, workflow import, fixture tests, live queries and Dify Cloud are recorded separately in the validation notes.
