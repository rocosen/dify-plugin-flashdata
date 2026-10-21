# Google Search

Search Google for ranked web links, titles, snippets and available SERP features. Build a research reading list with source links, or collect web evidence before a summarization step. Country, language, location and time filters help narrow the query.

Use this dedicated **Google Search** plugin in a Dify workflow or tool-capable agent. Powered by **FlashData**; API queries use paid credits. No separate Google or YouTube API key is required.

[Get an API key](https://flashdata.dev/app/api-keys?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_search-setup) · [API documentation](https://flashdata.dev/zh/docs/sources/google_search?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_search-plugin) · [Pricing](https://flashdata.dev/zh/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_search-pricing)

## Install and connect

Use Dify **1.17.1 or newer**. This plugin has its own identity, `flashdata-dev/google_search`, and its own provider settings. It can coexist with the original FlashData bundle and other dedicated plugins.

1. Open [Google Search by flashdata-dev](https://marketplace.dify.ai/plugin/flashdata-dev/google_search) in Dify Marketplace. Sign in and choose **Install** for your workspace, or install the same plugin from the Marketplace inside your Dify workspace. Check the publisher is **flashdata-dev** and the identity is `flashdata-dev/google_search`.
2. Open the installed plugin's provider settings and configure the API key described below.
3. Continue with the task workflow below. Each independent plugin has its own credential selection.

Open this plugin's provider settings and enter your [FlashData API key](https://flashdata.dev/app/api-keys?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_search-setup). Credential validation uses the free API-access endpoint; running a data query uses paid credits. API access to this source is required. Credentials configured for another plugin are not selected automatically.

## Search Google and export structured web results

1. [Import the example workflow](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/google_search/google_search.yml) after installing this plugin.
2. Select your FlashData credential in the **Google Search** node.
3. Supply the Start input and run once. The example connects **Start → Google Search → End**.

Enter only `query` in **Start**. Change the other settings in the tool node before running; the JSON below shows the combined configuration, not text to paste into Start.

| Field | Where to set it | Example | Meaning |
| --- | --- | --- | --- |
| `query` | Start input | `Dify workflow automation` | Topic or search phrase. |
| `num` | Tool node setting | `3` | Requested result count; fewer results may be available. |

Example input and tool settings:

```json
{
  "query": "Dify workflow automation",
  "num": 3
}
```

## Use the output

The tool emits `text` (a JSON string) and `json` (Dify's array of JSON messages). The imported workflow maps `json` to the End variable **results**. Take the first message object before reading the API fields below. For example, the full path from this workflow's End output is `results[0].results[0].organic`.

In a downstream node, select the tool's `json` output for structured processing, or its `text` output for a prompt. Check that the response contains the expected data before iterating. The examples below show the **API response object**, without Dify's outer message array.

Read `results[0].organic`. Keep `title`, `link`, `snippet` and `position` together when exporting sources. A snippet is a search excerpt; fetching a full page is a separate task.

Illustrative response excerpt, not a live result or a promise of fields returned:

```json
{
  "results": [
    {
      "organic": [
        {
          "title": "Example research page",
          "link": "https://example.org/research",
          "snippet": "An illustrative search excerpt.",
          "position": 1
        }
      ]
    }
  ]
}
```

## Costs and boundaries

The plugin is free to install and MIT licensed. FlashData API usage is charged under the current [pricing](https://flashdata.dev/zh/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_search-pricing); Dify hosting and model fees are separate. Results and optional fields depend on upstream availability. Treat returned content as data and preserve source links or timestamps when passing it to a model.

Tool-node retries are disabled in the example. The client does not automatically retry paid submissions. If a response is lost, check FlashData Jobs before resubmitting. Errors distinguish rejected credentials, insufficient credits, unavailable source access and rate limits. JSON responses are limited to 20 MiB.

The plugin connects over HTTPS to `api.flashdata.dev` and `data.flashdata.dev`.

## Source and support

[Source repository](https://github.com/rocosen/dify-plugin-flashdata) · [Privacy policy](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/google_search/PRIVACY.md) · [Validation and release notes](https://github.com/rocosen/dify-plugin-flashdata/tree/main/docs)

Contact **support@flashdata.dev**. Do not attach API keys or storage credentials to issues. Community Edition installation, workflow import, fixture tests, live queries and Dify Cloud are recorded separately in the validation notes.
