# YouTube Channel Data

Retrieve a YouTube channel profile and recent videos using its handle. Request 1–100 videos; returned fields and count depend on upstream availability.

Use this dedicated **YouTube Channel Data** plugin in a Dify workflow or tool-capable agent. Powered by **FlashData**; API queries use paid credits. No separate Google or YouTube API key is required.

[Get an API key](https://flashdata.dev/app/api-keys?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_channel-setup) · [API documentation](https://flashdata.dev/docs/sources/youtube_channel?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_channel-plugin) · [Pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_channel-pricing)

## Install and connect

Use Dify **1.17.1 or newer**. This plugin has its own identity, `flashdata-dev/youtube_channel`, and its own provider settings. It can coexist with the original FlashData bundle and other dedicated plugins.

1. Open [YouTube Channel Data by flashdata-dev](https://marketplace.dify.ai/plugin/flashdata-dev/youtube_channel) in Dify Marketplace. Sign in and choose **Install** for your workspace, or install the same plugin from the Marketplace inside your Dify workspace. Check the publisher is **flashdata-dev** and the identity is `flashdata-dev/youtube_channel`.
2. Open the installed plugin's provider settings and configure the API key described below.
3. Continue with the task workflow below. Each independent plugin has its own credential selection.

Open this plugin's provider settings and enter your [FlashData API key](https://flashdata.dev/app/api-keys?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_channel-setup). Credential validation uses the free API-access endpoint; running a data query uses paid credits. API access to this source is required. Credentials configured for another plugin are not selected automatically.

## Read channel data and recent videos

1. [Import the example workflow](https://github.com/flashdata-dev/dify-plugin-flashdata/blob/main/plugins/youtube_channel/youtube_channel.yml) after installing this plugin.
2. Select your FlashData credential in the **YouTube Channel Data** node.
3. Supply the Start input and run once. The example connects **Start → YouTube Channel Data → End**.

Example input and tool settings:

```json
{
  "handle": "@GoogleDevelopers",
  "video_limit": 10
}
```

Read `results[0]` and its `videos[]`. Start from an @handle. Read channel identity and available subscriber information, then export recent videos with IDs, titles and durations. This is a recent-video snapshot, not a full channel archive.

Illustrative response excerpt, not a live result or a promise of fields returned:

```json
{
  "results": [
    {
      "videos": [
        {
          "videoId": "dQw4w9WgXcQ",
          "title": "Example recent upload"
        }
      ]
    }
  ]
}
```

## Costs and boundaries

The plugin is free to install and MIT licensed. FlashData API usage is charged under the current [pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_channel-pricing); Dify hosting and model fees are separate. Results and optional fields depend on upstream availability. Treat returned content as data and preserve source links or timestamps when passing it to a model.

Tool-node retries are disabled in the example. The client does not automatically retry paid submissions. If a response is lost, check FlashData Jobs before resubmitting. Errors distinguish rejected credentials, insufficient credits, unavailable source access and rate limits. JSON responses are limited to 20 MiB.

The plugin connects over HTTPS to `api.flashdata.dev` and `data.flashdata.dev`.

## Source and support

[Source repository](https://github.com/flashdata-dev/dify-plugin-flashdata) · [Privacy policy](https://github.com/flashdata-dev/dify-plugin-flashdata/blob/main/plugins/youtube_channel/PRIVACY.md) · [Validation and release notes](https://github.com/flashdata-dev/dify-plugin-flashdata/tree/main/docs)

Contact **support@flashdata.dev**. Do not attach API keys or storage credentials to issues. Community Edition installation, workflow import, fixture tests, live queries and Dify Cloud are recorded separately in the validation notes.
