# YouTube Transcript

Retrieve an existing YouTube transcript as timestamped subtitle segments and full text. Use the text for a video summary and preserve timestamps for citations. The default selects automatic captions; this tool does not perform speech recognition, translation or fallback to another track.

[Get an API key](https://flashdata.dev/signup?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_transcript-task) · [API documentation](https://flashdata.dev/docs/sources/youtube_transcript?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_transcript-task) · [Pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_transcript-task)

## Setup

1. In Dify **1.17.1+**, install [YouTube Transcript](https://marketplace.dify.ai/plugin/flashdata-dev/youtube_transcript) by **flashdata-dev**.
2. In this plugin's provider settings, enter your FlashData API key with access to `youtube_transcript`. Key validation is free; data queries use Credits. No separate Google or YouTube key is needed.
3. Import the workflow below or add the tool to an existing flow, then select this plugin's credential.

## Retrieve timestamped YouTube transcripts

[Example workflow](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/youtube_transcript/youtube_transcript.yml): **Start → YouTube Transcript → End**. Select your credential, then supply the Start input.

Enter only `video_id` in **Start**. Set the remaining fields in the tool node.

| Field | Where to set it | Example | Meaning |
| --- | --- | --- | --- |
| `video_id` | Start input | `dQw4w9WgXcQ` | YouTube video ID or supported YouTube video URL. |
| `language` | Tool node setting | `en` | Caption language. |
| `auto` | Tool node setting | `true` | Select automatic captions when true; uploader-provided captions when false. |

## Use the output

The tool returns `text` (a JSON string) and `json` (Dify's message array). The example maps `json` to End's **results**; the full output path is `results[0].results[0].segments`. The paths below refer to the API object inside that first message.

Read `results[0].segments` and `results[0].fullText`. Segments contain `start`, `end` and `text`, with times in seconds. Preserve timestamps for citations or convert them to SRT/WebVTT in a subsequent node. Default `auto=true` selects automatic captions.

## Costs and limits

Free to install under MIT. API calls use [FlashData Credits](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_transcript-task); Dify/model fees are separate. Results and optional fields depend on source availability. Preserve source links and treat retrieved text as data.

Paid submissions are not retried automatically. After a timeout, check FlashData Jobs before resubmitting. Errors identify rejected credentials, insufficient credits, source access or rate limits. JSON responses are limited to 20 MiB.

HTTPS access to `api.flashdata.dev` and `data.flashdata.dev` is required.

## Source and support

[Source repository](https://github.com/rocosen/dify-plugin-flashdata) · [Privacy policy](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/youtube_transcript/PRIVACY.md) · [Validation and release notes](https://github.com/rocosen/dify-plugin-flashdata/tree/main/docs)

Contact **support@flashdata.dev**; keep keys and storage credentials out of support requests.
