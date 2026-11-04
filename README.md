# Google Search & YouTube Tools

**Looking for a dedicated plugin?** [Browse the 15 independent Google and YouTube plugins](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/README.md), each with its own package, provider identity, task guide and workflow. The bundle documented below remains available for existing workflows; it is one Marketplace entry, not 15 separate listings.

Search Google, monitor news, retrieve YouTube transcripts, inspect channels or deliver video and audio to your own storage from a Dify workflow. **FlashData provides 15 source tools with structured JSON output**, plus two tools for reading asynchronous jobs.

Each tool includes an importable workflow. Installation is free; **API calls use paid FlashData Credits**. Dify/model fees are separate.

[Get an API key](https://flashdata.dev/app/api-keys?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=plugin-setup) · [Pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=plugin-pricing) · [Source code](https://github.com/rocosen/dify-plugin-flashdata) · [Workflow examples](https://github.com/rocosen/dify-plugin-flashdata/tree/main/examples)

## Choose a tool

| Tool / task | Input | Output |
| --- | --- | --- |
| [Google Search](https://flashdata.dev/docs/sources/google_search?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_search-workflow) — Search Google and export structured web results | `query` | `results[0].organic` |
| [Google News](https://flashdata.dev/docs/sources/google_news?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_news-workflow) — Track a topic in Google News | `query` | `results[0].news` |
| [Google Images](https://flashdata.dev/docs/sources/google_images?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_images-workflow) — Find images and their source pages | `query` | `results[0].images` |
| [Google Shopping](https://flashdata.dev/docs/sources/google_shopping?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_shopping-workflow) — Compare product listings and merchants | `query` | `results[0].shopping` |
| [Google Video Search](https://flashdata.dev/docs/sources/google_videos?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_videos-workflow) — Find video results across websites | `query` | `results[0].videos` |
| [Google Places](https://flashdata.dev/docs/sources/google_places?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_places-workflow) — Find local businesses and places | `query` | `results[0].places` |
| [YouTube Search](https://flashdata.dev/docs/sources/youtube_search?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_search-workflow) — Discover YouTube videos by keyword | `query` | `results[0].results` |
| [YouTube Extended Search](https://flashdata.dev/docs/sources/youtube_search_extended?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_search_extended-workflow) — Collect up to 700 YouTube search results | `query` | `results[0].results` |
| [YouTube Video Metadata](https://flashdata.dev/docs/sources/youtube_metadata?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_metadata-workflow) — Read YouTube metadata and chapters | `video_id` | `results[0]` |
| [YouTube Transcript](https://flashdata.dev/docs/sources/youtube_transcript?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_transcript-workflow) — Retrieve timestamped YouTube transcripts | `video_id` | `results[0].segments` and `fullText` |
| [YouTube Captions](https://flashdata.dev/docs/sources/youtube_captions?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_captions-workflow) — Retrieve uploader-provided YouTube captions | `video_id` | `results[0].segments` and `fullText` |
| [YouTube License Metadata](https://flashdata.dev/docs/sources/youtube_trainability?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_trainability-workflow) — Inspect YouTube Creative Commons license labels | `video_id` | `results[0]` license classification |
| [YouTube Channel Data](https://flashdata.dev/docs/sources/youtube_channel?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_channel-workflow) — Read channel data and recent videos | `handle` | `results[0]` and its `videos[]` |
| [YouTube Autocomplete](https://flashdata.dev/docs/sources/youtube_suggestions?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_suggestions-workflow) — Explore YouTube search suggestions | `query` | `results[0]`, an array of strings |
| [YouTube Download](https://flashdata.dev/docs/sources/youtube_download?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_download-workflow) — Deliver YouTube video or audio to your cloud storage | `video_id` | submission `id`, then `output.results[0]` from Get Job Results |

The table uses paths inside the FlashData API response. Dify wraps that response in the tool's `json` message array: take its first object before reading these paths. The example End variable **results** is that array, so Google Search organic results are at `results[0].results[0].organic`. The tool also emits the API response as a JSON string in `text`.

**Get Job** reads an existing job's status. **Get Job Results** retrieves its completed JSON result without submitting another query. Both accept the `job_id` from the download receipt.

## Setup

1. In Dify **1.17.1+**, install [Google Search & YouTube Tools](https://marketplace.dify.ai/plugin/flashdata-dev/flashdata) by **flashdata-dev**. For a single tool, choose its [independent plugin](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/README.md).
2. Enter your FlashData API key in provider settings. The key needs access to the requested sources. Validation is free; no Google or YouTube key is needed.
3. Import a [workflow](https://github.com/rocosen/dify-plugin-flashdata/blob/main/examples/README.md), select the credential in its tool node and supply the Start input. Leave **Download storage JSON** empty unless downloading media.

For example, the [Google News workflow](https://github.com/rocosen/dify-plugin-flashdata/blob/main/examples/google_news.yml) takes a query such as `renewable energy` and returns article metadata. Connect a later node to format a briefing with publisher links; snippets are not full articles.

## Deliver YouTube video or audio to your storage

In provider settings, put the storage configuration in **Download storage JSON**. This optional secret credential is used only by YouTube Download; it is not an LLM tool argument or embedded in exported workflow YAML.

Example shape for your own S3 bucket; replace the placeholders with your storage settings:

```json
{
  "storage_type": "s3",
  "storage_url": "your-bucket-name",
  "region": "us-east-1",
  "access_key": "YOUR_STORAGE_ACCESS_KEY",
  "secret_key": "YOUR_STORAGE_SECRET_KEY",
  "object_prefix": "dify-videos"
}
```

`storage_url` is the bucket/container name, not an object URL. S3-compatible destinations also need `endpoint_url`. Azure uses `account_name` and a container `sas_token` with write permission; GCS uses a `service_account` object. See the [full storage contract](https://flashdata.dev/docs/sources/youtube_download?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=download-storage) for all supported providers.

1. Import the **YouTube Download** workflow and submit a video once. `audio_video` produces video with audio; choose `audio` for audio only. Omitting `output_format` uses `mp4` for video or `m4a` for audio.
2. Save the returned `id`. Run **Get Job** with that ID to read progress. Repeat the read later while pending or processing; do not rerun the download node to poll.
3. When completed, run **Get Job Results** with the same ID. Its `output.results[0]` contains the upload manifest, including `file_url` and `file_size`. A private object URL is not automatically a public download link.

JSON results are available for 24 hours after completion. Media retention follows your storage settings. Downloads reserve credits at admission and are billed by actual delivered bytes; consult current pricing before submitting a large job.

## Costs, limits and errors

Every data query consumes FlashData Credits under current [pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=plugin-pricing). Standard YouTube Search accepts 1–20 requested results; Extended Search accepts 1–700 and has a separate price. Actual result counts and fields depend on upstream availability. License metadata does not grant training or reuse rights.

Inputs are validated before submission. The plugin distinguishes rejected credentials (401), insufficient credits (402), source access (403) and rate limits (429), and never automatically retries paid POSTs. If a response is lost, check FlashData Jobs before submitting again. Result reads can be retried independently. Result JSON larger than 20 MiB must be retrieved outside this plugin.

Transcript selects existing automatic captions by default; Captions selects uploader-provided tracks. Neither generates, translates or silently replaces a missing track. Batch submission is not supported.

## Support

[Privacy policy](PRIVACY.md) · [Security policy](SECURITY.md) · [MIT license](LICENSE). Contact **support@flashdata.dev** for account or security matters. Do not attach API keys or storage credentials to issues.

[Validation notes](https://github.com/rocosen/dify-plugin-flashdata/tree/main/docs) record installation, workflow and fixture checks separately.
