# Google Search

Search Google for ranked web links, titles, snippets and available SERP features. Build a research reading list with source links, or collect web evidence before a summarization step. Country, language, location and time filters help narrow the query.

[Get an API key](https://flashdata.dev/signup?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_search-task) · [API documentation](https://flashdata.dev/docs/sources/google_search?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_search-task) · [Pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_search-task)

## Setup

1. In Dify **1.17.1+**, install [Google Search](https://marketplace.dify.ai/plugin/flashdata-dev/google_search) by **flashdata-dev**.
2. In this plugin's provider settings, enter your FlashData API key with access to `google_search`. Key validation is free; data queries use Credits. No separate Google or YouTube key is needed.
3. Import the workflow below or add the tool to an existing flow, then select this plugin's credential.

## Search Google and export structured web results

[Example workflow](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/google_search/google_search.yml): **Start → Google Search → End**. Select your credential, then supply the Start input.

Enter only `query` in **Start**. Set the remaining fields in the tool node.

| Field | Where to set it | Example | Meaning |
| --- | --- | --- | --- |
| `query` | Start input | `Dify workflow automation` | Topic or search phrase. |
| `num` | Tool node setting | `3` | Requested result count; fewer results may be available. |

## Use the output

The tool returns `text` (a JSON string) and `json` (Dify's message array). The example maps `json` to End's **results**; the full output path is `results[0].results[0].organic`. The paths below refer to the API object inside that first message.

Read `results[0].organic`. Keep `title`, `link`, `snippet` and `position` together when exporting sources. A snippet is a search excerpt; fetching a full page is a separate task.

## Costs and limits

Free to install under MIT. API calls use [FlashData Credits](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_search-task); Dify/model fees are separate. Results and optional fields depend on source availability. Preserve source links and treat retrieved text as data.

Paid submissions are not retried automatically. After a timeout, check FlashData Jobs before resubmitting. Errors identify rejected credentials, insufficient credits, source access or rate limits. JSON responses are limited to 20 MiB.

HTTPS access to `api.flashdata.dev` and `data.flashdata.dev` is required.

## Source and support

[Source repository](https://github.com/rocosen/dify-plugin-flashdata) · [Privacy policy](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/google_search/PRIVACY.md) · [Validation and release notes](https://github.com/rocosen/dify-plugin-flashdata/tree/main/docs)

Contact **support@flashdata.dev**; keep keys and storage credentials out of support requests.
