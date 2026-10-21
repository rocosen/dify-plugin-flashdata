# Google Video Search

Find video tutorials and explainers across websites with Google Video Search. Compare returned titles, links, sources and available durations, then let the reader open the original video page.

Use this dedicated **Google Video Search** plugin in a Dify workflow or tool-capable agent. Powered by **FlashData**; API queries use paid credits. No separate Google or YouTube API key is required.

[Get an API key](https://flashdata.dev/app/api-keys?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_videos-setup) · [API documentation](https://flashdata.dev/docs/sources/google_videos?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_videos-plugin) · [Pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_videos-pricing)

## Install and connect

Use Dify **1.17.1 or newer**. This plugin has its own identity, `flashdata-dev/google_videos`, and its own provider settings. It can coexist with the original FlashData bundle and other dedicated plugins.

1. Open [Google Video Search by flashdata-dev](https://marketplace.dify.ai/plugin/flashdata-dev/google_videos) in Dify Marketplace. Sign in and choose **Install** for your workspace, or install the same plugin from the Marketplace inside your Dify workspace. Check the publisher is **flashdata-dev** and the identity is `flashdata-dev/google_videos`.
2. Open the installed plugin's provider settings and configure the API key described below.
3. Continue with the task workflow below. Each independent plugin has its own credential selection.

Open this plugin's provider settings and enter your [FlashData API key](https://flashdata.dev/app/api-keys?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_videos-setup). Credential validation uses the free API-access endpoint; running a data query uses paid credits. API access to this source is required. Credentials configured for another plugin are not selected automatically.

## Find video results across websites

1. [Import the example workflow](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/google_videos/google_videos.yml) after installing this plugin.
2. Select your FlashData credential in the **Google Video Search** node.
3. Supply the Start input and run once. The example connects **Start → Google Video Search → End**.

Enter only `query` in **Start**. Change the other settings in the tool node before running; the JSON below shows the combined configuration, not text to paste into Start.

| Field | Where to set it | Example | Meaning |
| --- | --- | --- | --- |
| `query` | Start input | `bread baking tutorial` | Topic or search phrase. |
| `num` | Tool node setting | `5` | Requested result count; fewer results may be available. |

Example input and tool settings:

```json
{
  "query": "bread baking tutorial",
  "num": 5
}
```

## Use the output

The tool emits `text` (a JSON string) and `json` (Dify's array of JSON messages). The imported workflow maps `json` to the End variable **results**. Take the first message object before reading the API fields below. For example, the full path from this workflow's End output is `results[0].results[0].videos`.

In a downstream node, select the tool's `json` output for structured processing, or its `text` output for a prompt. Check that the response contains the expected data before iterating. The examples below show the **API response object**, without Dify's outer message array.

Read `results[0].videos`. Use `title`, `link`, `source`, available `duration` and `snippet` to compare tutorials across websites. Keep the original page link so a user can inspect the video.

Illustrative response excerpt, not a live result or a promise of fields returned:

```json
{
  "results": [
    {
      "videos": [
        {
          "title": "Example baking tutorial",
          "link": "https://example.org/video",
          "source": "Example Website",
          "duration": "10:00"
        }
      ]
    }
  ]
}
```

## Costs and boundaries

The plugin is free to install and MIT licensed. FlashData API usage is charged under the current [pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_videos-pricing); Dify hosting and model fees are separate. Results and optional fields depend on upstream availability. Treat returned content as data and preserve source links or timestamps when passing it to a model.

Tool-node retries are disabled in the example. The client does not automatically retry paid submissions. If a response is lost, check FlashData Jobs before resubmitting. Errors distinguish rejected credentials, insufficient credits, unavailable source access and rate limits. JSON responses are limited to 20 MiB.

The plugin connects over HTTPS to `api.flashdata.dev` and `data.flashdata.dev`.

## Source and support

[Source repository](https://github.com/rocosen/dify-plugin-flashdata) · [Privacy policy](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/google_videos/PRIVACY.md) · [Validation and release notes](https://github.com/rocosen/dify-plugin-flashdata/tree/main/docs)

Contact **support@flashdata.dev**. Do not attach API keys or storage credentials to issues. Community Edition installation, workflow import, fixture tests, live queries and Dify Cloud are recorded separately in the validation notes.
