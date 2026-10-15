# YouTube Search

Find YouTube videos about a topic and pass their video IDs to a later metadata or transcript step. Filter by upload date, duration, type, features or sort order. Request 1–20 results; actual results may be fewer.

Use this dedicated **YouTube Search** plugin in a Dify workflow or tool-capable agent. Powered by **FlashData**; API queries use paid credits. No separate Google or YouTube API key is required.

[Get an API key](https://flashdata.dev/app/api-keys?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_search-setup) · [API documentation](https://flashdata.dev/docs/sources/youtube_search?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_search-plugin) · [Pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_search-pricing)

## Install and connect

Use Dify **1.17.1 or newer**. This plugin has its own identity, `flashdata-dev/youtube_search`, and its own provider settings. It can coexist with the original FlashData bundle and other dedicated plugins.

1. Open [YouTube Search by flashdata-dev](https://marketplace.dify.ai/plugin/flashdata-dev/youtube_search) in Dify Marketplace. Sign in and choose **Install** for your workspace, or install the same plugin from the Marketplace inside your Dify workspace. Check the publisher is **flashdata-dev** and the identity is `flashdata-dev/youtube_search`.
2. Open the installed plugin's provider settings and configure the API key described below.
3. Continue with the task workflow below. Each independent plugin has its own credential selection.

Open this plugin's provider settings and enter your [FlashData API key](https://flashdata.dev/app/api-keys?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_search-setup). Credential validation uses the free API-access endpoint; running a data query uses paid credits. API access to this source is required. Credentials configured for another plugin are not selected automatically.

## Discover YouTube videos by keyword

1. [Import the example workflow](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/youtube_search/youtube_search.yml) after installing this plugin.
2. Select your FlashData credential in the **YouTube Search** node.
3. Supply the Start input and run once. The example connects **Start → YouTube Search → End**.

Enter only `query` in **Start**. Change the other settings in the tool node before running; the JSON below shows the combined configuration, not text to paste into Start.

| Field | Where to set it | Example | Meaning |
| --- | --- | --- | --- |
| `query` | Start input | `Python tutorials` | Topic or search phrase. |
| `max_results` | Tool node setting | `5` | Requested video count; the source limit and actual availability still apply. |
| `filters_json` | Tool node setting | `{"upload_date":"this_week"}` | JSON object entered as text in the tool field; paste the inner object without the outer JSON string quotes. |

Example input and tool settings:

```json
{
  "query": "Python tutorials",
  "max_results": 5,
  "filters_json": "{\"upload_date\":\"this_week\"}"
}
```

## Use the output

The tool emits `text` (a JSON string) and `json` (Dify's array of JSON messages). The imported workflow maps `json` to the End variable **results**. Take the first message object before reading the API fields below. For example, the full path from this workflow's End output is `results[0].results[0].results`.

In a downstream node, select the tool's `json` output for structured processing, or its `text` output for a prompt. Check that the response contains the expected data before iterating. The examples below show the **API response object**, without Dify's outer message array.

Read `results[0].results`. Keep `videoId`, `title`, channel information and available view counts. Build watch URLs as https://www.youtube.com/watch?v=<videoId>. Set `filters_json` for upload date, duration, sort order or features.

Illustrative response excerpt, not a live result or a promise of fields returned:

```json
{
  "results": [
    {
      "results": [
        {
          "videoId": "dQw4w9WgXcQ",
          "title": "Example video"
        }
      ]
    }
  ]
}
```

## Costs and boundaries

The plugin is free to install and MIT licensed. FlashData API usage is charged under the current [pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_search-pricing); Dify hosting and model fees are separate. Results and optional fields depend on upstream availability. Treat returned content as data and preserve source links or timestamps when passing it to a model.

Tool-node retries are disabled in the example. The client does not automatically retry paid submissions. If a response is lost, check FlashData Jobs before resubmitting. Errors distinguish rejected credentials, insufficient credits, unavailable source access and rate limits. JSON responses are limited to 20 MiB.

The plugin connects over HTTPS to `api.flashdata.dev` and `data.flashdata.dev`.

## Source and support

[Source repository](https://github.com/rocosen/dify-plugin-flashdata) · [Privacy policy](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/youtube_search/PRIVACY.md) · [Validation and release notes](https://github.com/rocosen/dify-plugin-flashdata/tree/main/docs)

Contact **support@flashdata.dev**. Do not attach API keys or storage credentials to issues. Community Edition installation, workflow import, fixture tests, live queries and Dify Cloud are recorded separately in the validation notes.
