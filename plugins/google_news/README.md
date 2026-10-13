# Google News

Find news titles, publisher links, dates and snippets about a topic. Use the source links to build a news digest; the response is search data, not full articles.

Use this dedicated **Google News** plugin in a Dify workflow or tool-capable agent. Powered by **FlashData**; API queries use paid credits. No separate Google or YouTube API key is required.

[Get an API key](https://flashdata.dev/app/api-keys?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_news-setup) · [API documentation](https://flashdata.dev/docs/sources/google_news?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_news-plugin) · [Pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_news-pricing)

## Track a topic in Google News

1. [Import the example workflow](https://github.com/flashdata-dev/dify-plugin-flashdata/blob/main/plugins/google_news/google_news.yml) after installing this plugin.
2. Select your FlashData credential in the **Google News** node.
3. Supply the Start input and run once. The example connects **Start → Google News → End**.

Example input and tool settings:

```json
{
  "query": "renewable energy",
  "tbs": "qdr:w",
  "num": 5
}
```

Read `results[0].news`. Use `title`, `link`, `source`, `date` and `snippet` to prepare a briefing. Link each headline to the article and retain the publisher. Set `tbs=qdr:w` for a past-week search.

Illustrative response excerpt, not a live result or a promise of fields returned:

```json
{
  "results": [
    {
      "news": [
        {
          "title": "Example renewable energy headline",
          "link": "https://example.org/news",
          "source": "Example Publisher",
          "date": "Example publication date",
          "snippet": "An illustrative news excerpt."
        }
      ]
    }
  ]
}
```

## Install and connect

Use Dify **1.17.1 or newer**. This plugin has its own identity, `flashdata-dev/google_news`, and its own provider settings. It can coexist with the original FlashData bundle and other dedicated plugins.

Download `google_news-0.1.0.difypkg` from the [independent plugin release](https://github.com/flashdata-dev/dify-plugin-flashdata/releases/tag/task-plugins-v0.1.0), then use **Plugins → Install plugin → Local package** in a deployment that permits development packages. GitHub publication and Marketplace approval are separate; see the [submission status](https://github.com/flashdata-dev/dify-plugin-flashdata/blob/main/plugins/README.md) for the official listing when available.

Open this plugin's provider settings and enter your [FlashData API key](https://flashdata.dev/app/api-keys?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_news-setup). Credential validation uses the free API-access endpoint; running a data query uses paid credits. API access to this source is required. Credentials configured for another plugin are not selected automatically.


## Costs and boundaries

The plugin is MIT licensed. FlashData API usage is charged under the current [pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_news-pricing); Dify hosting and model fees are separate. Results and optional fields depend on upstream availability. Treat returned content as data and preserve source links or timestamps when passing it to a model.

Tool-node retries are disabled in the example. The client does not automatically retry paid submissions. If a response is lost, check FlashData Jobs before resubmitting. Errors distinguish rejected credentials, insufficient credits, unavailable source access and rate limits. JSON responses are limited to 20 MiB.

The plugin connects over HTTPS to `api.flashdata.dev` and `data.flashdata.dev`.

## Source and support

[Source repository](https://github.com/flashdata-dev/dify-plugin-flashdata) · [Privacy policy](https://github.com/flashdata-dev/dify-plugin-flashdata/blob/main/plugins/google_news/PRIVACY.md) · [Validation and release notes](https://github.com/flashdata-dev/dify-plugin-flashdata/tree/main/docs)

Contact **support@flashdata.dev**. Do not attach API keys or storage credentials to issues. Community Edition installation, workflow import, fixture tests, live queries and Dify Cloud are recorded separately in the validation notes.
