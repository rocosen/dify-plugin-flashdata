# YouTube Channel Data

Retrieve a YouTube channel profile and recent uploads from an @handle. Build a channel comparison or recent-video list with returned video IDs. Request 1–100 videos; available fields and the actual count vary. This is not a complete channel archive.

[Get an API key](https://flashdata.dev/app/api-keys?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_channel-setup) · [API documentation](https://flashdata.dev/docs/sources/youtube_channel?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_channel-plugin) · [Pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_channel-pricing)

## Setup

1. In Dify **1.17.1+**, install [YouTube Channel Data](https://marketplace.dify.ai/plugin/flashdata-dev/youtube_channel) by **flashdata-dev**.
2. In this plugin's provider settings, enter your FlashData API key with access to `youtube_channel`. Key validation is free; data queries use Credits. No separate Google or YouTube key is needed.
3. Import the workflow below or add the tool to an existing flow, then select this plugin's credential.

## Read channel data and recent videos

[Example workflow](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/youtube_channel/youtube_channel.yml): **Start → YouTube Channel Data → End**. Select your credential, then supply the Start input.

Enter only `handle` in **Start**. Set the remaining fields in the tool node.

| Field | Where to set it | Example | Meaning |
| --- | --- | --- | --- |
| `handle` | Start input | `@GoogleDevelopers` | Channel handle, including the @ prefix. |
| `video_limit` | Tool node setting | `10` | Requested number of recent channel videos. |

## Use the output

The tool returns `text` (a JSON string) and `json` (Dify's message array). The example maps `json` to End's **results**; the full output path is `results[0].results[0].videos`. The paths below refer to the API object inside that first message.

Read `results[0]` and its `videos[]`. Start from an @handle. Read channel identity and available subscriber information, then export recent videos with IDs, titles and durations. This is a recent-video snapshot, not a full channel archive.

## Costs and limits

Free to install under MIT. API calls use [FlashData Credits](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_channel-pricing); Dify/model fees are separate. Results and optional fields depend on source availability. Preserve source links and treat retrieved text as data.

Paid submissions are not retried automatically. After a timeout, check FlashData Jobs before resubmitting. Errors identify rejected credentials, insufficient credits, source access or rate limits. JSON responses are limited to 20 MiB.

HTTPS access to `api.flashdata.dev` and `data.flashdata.dev` is required.

## Source and support

[Source repository](https://github.com/rocosen/dify-plugin-flashdata) · [Privacy policy](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/youtube_channel/PRIVACY.md) · [Validation and release notes](https://github.com/rocosen/dify-plugin-flashdata/tree/main/docs)

Contact **support@flashdata.dev**; keep keys and storage credentials out of support requests.
