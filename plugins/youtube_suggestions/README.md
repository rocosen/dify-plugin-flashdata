# YouTube Autocomplete

Get YouTube autocomplete search suggestions for a query prefix, language and region. Use the phrases to explore related topics before choosing a search query. Suggestions do not include search-volume estimates.

[Get an API key](https://flashdata.dev/app/api-keys?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_suggestions-setup) · [API documentation](https://flashdata.dev/docs/sources/youtube_suggestions?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_suggestions-plugin) · [Pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_suggestions-pricing)

## Setup

1. In Dify **1.17.1+**, install [YouTube Autocomplete](https://marketplace.dify.ai/plugin/flashdata-dev/youtube_suggestions) by **flashdata-dev**.
2. In this plugin's provider settings, enter your FlashData API key with access to `youtube_suggestions`. Key validation is free; data queries use Credits. No separate Google or YouTube key is needed.
3. Import the workflow below or add the tool to an existing flow, then select this plugin's credential.

## Explore YouTube search suggestions

[Example workflow](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/youtube_suggestions/youtube_suggestions.yml): **Start → YouTube Autocomplete → End**. Select your credential, then supply the Start input.

Enter only `query` in **Start**. Set the remaining fields in the tool node.

| Field | Where to set it | Example | Meaning |
| --- | --- | --- | --- |
| `query` | Start input | `how to build` | Topic or search phrase. |
| `language` | Tool node setting | `en` | Suggestion language. |
| `region` | Tool node setting | `US` | Region code for autocomplete suggestions. |

## Use the output

The tool returns `text` (a JSON string) and `json` (Dify's message array). The example maps `json` to End's **results**; the full output path is `results[0].results[0]`. The paths below refer to the API object inside that first message.

Read `results[0]`, an array of strings. Return suggestions as a list or use them to expand a topic. To compare regions, run the same prefix with different `region` values; each query is billed. These phrases are not search-volume measurements.

## Costs and limits

Free to install under MIT. API calls use [FlashData Credits](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_suggestions-pricing); Dify/model fees are separate. Results and optional fields depend on source availability. Preserve source links and treat retrieved text as data.

Paid submissions are not retried automatically. After a timeout, check FlashData Jobs before resubmitting. Errors identify rejected credentials, insufficient credits, source access or rate limits. JSON responses are limited to 20 MiB.

HTTPS access to `api.flashdata.dev` and `data.flashdata.dev` is required.

## Source and support

[Source repository](https://github.com/rocosen/dify-plugin-flashdata) · [Privacy policy](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/youtube_suggestions/PRIVACY.md) · [Validation and release notes](https://github.com/rocosen/dify-plugin-flashdata/tree/main/docs)

Contact **support@flashdata.dev**; keep keys and storage credentials out of support requests.
