# YouTube Video Metadata

Enrich a video record with its title, description, channel, available statistics and YouTube video chapters. Accepts a video ID or YouTube video URL. Request chapters for a navigation outline; leave format metadata off when it is unnecessary.

[Get an API key](https://flashdata.dev/signup?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_metadata-task) · [API documentation](https://flashdata.dev/docs/sources/youtube_metadata?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_metadata-task) · [Pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_metadata-task)

## Setup

1. In Dify **1.17.1+**, install [YouTube Video Metadata](https://marketplace.dify.ai/plugin/flashdata-dev/youtube_metadata) by **flashdata-dev**.
2. In this plugin's provider settings, enter your FlashData API key with access to `youtube_metadata`. Key validation is free; data queries use Credits. No separate Google or YouTube key is needed.
3. Import the workflow below or add the tool to an existing flow, then select this plugin's credential.

## Read YouTube metadata and chapters

[Example workflow](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/youtube_metadata/youtube_metadata.yml): **Start → YouTube Video Metadata → End**. Select your credential, then supply the Start input.

Enter only `video_id` in **Start**. Set the remaining fields in the tool node.

| Field | Where to set it | Example | Meaning |
| --- | --- | --- | --- |
| `video_id` | Start input | `dQw4w9WgXcQ` | YouTube video ID or supported YouTube video URL. |
| `include_chapters` | Tool node setting | `true` | Include chapters when available. |
| `include_formats` | Tool node setting | `false` | Include format metadata; disabled in this example. |

## Use the output

The tool returns `text` (a JSON string) and `json` (Dify's message array). The example maps `json` to End's **results**; the full output path is `results[0].results[0]`. The paths below refer to the API object inside that first message.

Read `results[0]`. Read the title, description, channel and available statistics. Chapters and formats are optional; use `include_formats=false` when only inspecting a title or chapter list.

## Costs and limits

Free to install under MIT. API calls use [FlashData Credits](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_metadata-task); Dify/model fees are separate. Results and optional fields depend on source availability. Preserve source links and treat retrieved text as data.

Paid submissions are not retried automatically. After a timeout, check FlashData Jobs before resubmitting. Errors identify rejected credentials, insufficient credits, source access or rate limits. JSON responses are limited to 20 MiB.

HTTPS access to `api.flashdata.dev` and `data.flashdata.dev` is required.

## Source and support

[Source repository](https://github.com/rocosen/dify-plugin-flashdata) · [Privacy policy](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/youtube_metadata/PRIVACY.md) · [Validation and release notes](https://github.com/rocosen/dify-plugin-flashdata/tree/main/docs)

Contact **support@flashdata.dev**; keep keys and storage credentials out of support requests.
