# YouTube License Metadata

Read the Creative Commons license classification exposed by YouTube video metadata and keep it alongside a research record. The API source is youtube_trainability. It does not read creator third-party training settings or grant training or reuse permission.

[Get an API key](https://flashdata.dev/app/api-keys?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_trainability-setup) · [API documentation](https://flashdata.dev/docs/sources/youtube_trainability?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_trainability-plugin) · [Pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_trainability-pricing)

## Setup

1. In Dify **1.17.1+**, install [YouTube License Metadata](https://marketplace.dify.ai/plugin/flashdata-dev/youtube_trainability) by **flashdata-dev**.
2. In this plugin's provider settings, enter your FlashData API key with access to `youtube_trainability`. Key validation is free; data queries use Credits. No separate Google or YouTube key is needed.
3. Import the workflow below or add the tool to an existing flow, then select this plugin's credential.

## Inspect YouTube Creative Commons license labels

[Example workflow](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/youtube_trainability/youtube_trainability.yml): **Start → YouTube License Metadata → End**. Select your credential, then supply the Start input.

Enter `video_id` in **Start**.

| Field | Where to set it | Example | Meaning |
| --- | --- | --- | --- |
| `video_id` | Start input | `dQw4w9WgXcQ` | YouTube video ID or supported YouTube video URL. |

## Use the output

The tool returns `text` (a JSON string) and `json` (Dify's message array). The example maps `json` to End's **results**; the full output path is `results[0].results[0]`. The paths below refer to the API object inside that first message.

Read `results[0]` license classification. Use the returned Creative Commons license metadata as an attribute in your video records. It does not expose creator third-party training settings and does not grant permission to train on a video.

## Costs and limits

Free to install under MIT. API calls use [FlashData Credits](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_trainability-pricing); Dify/model fees are separate. Results and optional fields depend on source availability. Preserve source links and treat retrieved text as data.

Paid submissions are not retried automatically. After a timeout, check FlashData Jobs before resubmitting. Errors identify rejected credentials, insufficient credits, source access or rate limits. JSON responses are limited to 20 MiB.

HTTPS access to `api.flashdata.dev` and `data.flashdata.dev` is required.

## Source and support

[Source repository](https://github.com/rocosen/dify-plugin-flashdata) · [Privacy policy](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/youtube_trainability/PRIVACY.md) · [Validation and release notes](https://github.com/rocosen/dify-plugin-flashdata/tree/main/docs)

Contact **support@flashdata.dev**; keep keys and storage credentials out of support requests.
