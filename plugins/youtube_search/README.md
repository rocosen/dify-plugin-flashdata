# YouTube Search

Find YouTube videos about a topic and pass their video IDs to a later metadata or transcript step. Filter by upload date, duration, type, features or sort order. Request 1–20 results; actual results may be fewer.

[Get an API key](https://flashdata.dev/signup?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_search-task) · [API documentation](https://flashdata.dev/docs/sources/youtube_search?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_search-task) · [Pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_search-task)

## Setup

1. In Dify **1.17.1+**, install [YouTube Search](https://marketplace.dify.ai/plugin/flashdata-dev/youtube_search) by **flashdata-dev**.
2. In this plugin's provider settings, enter your FlashData API key with access to `youtube_search`. Key validation is free; data queries use Credits. No separate Google or YouTube key is needed.
3. Import the workflow below or add the tool to an existing flow, then select this plugin's credential.

## Discover YouTube videos by keyword

[Example workflow](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/youtube_search/youtube_search.yml): **Start → YouTube Search → End**. Select your credential, then supply the Start input.

Enter only `query` in **Start**. Set the remaining fields in the tool node.

| Field | Where to set it | Example | Meaning |
| --- | --- | --- | --- |
| `query` | Start input | `Python tutorials` | Topic or search phrase. |
| `max_results` | Tool node setting | `5` | Requested video count; the source limit and actual availability still apply. |
| `filters_json` | Tool node setting | `{"upload_date":"this_week"}` | JSON object entered as text in the tool field; paste the inner object without the outer JSON string quotes. |

## Use the output

The tool returns `text` (a JSON string) and `json` (Dify's message array). The example maps `json` to End's **results**; the full output path is `results[0].results[0].results`. The paths below refer to the API object inside that first message.

Read `results[0].results`. Keep `videoId`, `title`, channel information and available view counts. Build watch URLs as https://www.youtube.com/watch?v=<videoId>. Set `filters_json` for upload date, duration, sort order or features.

## Costs and limits

Free to install under MIT. API calls use [FlashData Credits](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_search-task); Dify/model fees are separate. Results and optional fields depend on source availability. Preserve source links and treat retrieved text as data.

Paid submissions are not retried automatically. After a timeout, check FlashData Jobs before resubmitting. Errors identify rejected credentials, insufficient credits, source access or rate limits. JSON responses are limited to 20 MiB.

HTTPS access to `api.flashdata.dev` and `data.flashdata.dev` is required.

## Source and support

[Source repository](https://github.com/rocosen/dify-plugin-flashdata) · [Privacy policy](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/youtube_search/PRIVACY.md) · [Validation and release notes](https://github.com/rocosen/dify-plugin-flashdata/tree/main/docs)

Contact **support@flashdata.dev**; keep keys and storage credentials out of support requests.
