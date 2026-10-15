# YouTube Download

Deliver YouTube video or audio to your own S3 or other supported cloud storage. Submit a download once, save its job ID, then use Get Job and Get Job Results to read progress and the upload manifest. FlashData bills by delivered bytes; customer storage is required.

Use this dedicated **YouTube Download** plugin in a Dify workflow or tool-capable agent. Powered by **FlashData**; API queries use paid credits. No separate Google or YouTube API key is required.

[Get an API key](https://flashdata.dev/app/api-keys?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_download-setup) · [API documentation](https://flashdata.dev/docs/sources/youtube_download?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_download-plugin) · [Pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_download-pricing)

## Install and connect

Use Dify **1.17.1 or newer**. This plugin has its own identity, `flashdata-dev/youtube_download`, and its own provider settings. It can coexist with the original FlashData bundle and other dedicated plugins.

1. Open [YouTube Download by flashdata-dev](https://marketplace.dify.ai/plugin/flashdata-dev/youtube_download) in Dify Marketplace. Sign in and choose **Install** for your workspace, or install the same plugin from the Marketplace inside your Dify workspace. Check the publisher is **flashdata-dev** and the identity is `flashdata-dev/youtube_download`.
2. Open the installed plugin's provider settings and configure the API key described below.
3. Continue with the task workflow below. Each independent plugin has its own credential selection.

Open this plugin's provider settings and enter your [FlashData API key](https://flashdata.dev/app/api-keys?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_download-setup). Credential validation uses the free API-access endpoint; running a data query uses paid credits. API access to this source is required. Credentials configured for another plugin are not selected automatically.

Configure **Download storage JSON** in provider credentials before submitting. For your own S3 bucket, the shape is:

```json
{"storage_type":"s3","storage_url":"your-bucket-name","region":"us-east-1","access_key":"YOUR_STORAGE_ACCESS_KEY","secret_key":"YOUR_STORAGE_SECRET_KEY","object_prefix":"dify-videos"}
```

The credential is kept out of LLM tool arguments and exported workflows. Other storage providers use the fields in the API documentation. Submit once and keep the returned `id`; use **Get Job** until the job completes, then **Get Job Results** with the same ID. Poll the existing job instead of rerunning the paid download. The result contains `output.results[0]` with the upload manifest. A private storage URL is not automatically a public link.

[Get Job workflow](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/youtube_download/get_job.yml) · [Get Job Results workflow](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/youtube_download/get_job_results.yml)

JSON results expire after 24 hours; media retention follows your storage settings. Downloads reserve credits at admission and bill by actual delivered bytes.

## Deliver YouTube video or audio to your cloud storage

1. [Import the example workflow](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/youtube_download/youtube_download.yml) after installing this plugin.
2. Select your FlashData credential in the **YouTube Download** node.
3. Supply the Start input and run once. The example connects **Start → YouTube Download → End**.

Enter only `video_id` in **Start**. Change the other settings in the tool node before running; the JSON below shows the combined configuration, not text to paste into Start.

| Field | Where to set it | Example | Meaning |
| --- | --- | --- | --- |
| `video_id` | Start input | `dQw4w9WgXcQ` | YouTube video ID or supported YouTube video URL. |
| `download_type` | Tool node setting | `audio_video` | audio_video delivers video with audio; audio requests audio only. |
| `video_quality` | Tool node setting | `<=720` | Upper bound for requested video quality. |
| `upload_metadata` | Tool node setting | `false` | Whether to upload accompanying metadata to your storage. |

Example input and tool settings:

```json
{
  "video_id": "dQw4w9WgXcQ",
  "download_type": "audio_video",
  "video_quality": "<=720",
  "upload_metadata": false
}
```

## Read progress and use the delivered file

The Download tool emits `text` (a JSON string) and `json` (Dify's array of JSON messages). Its example maps `json` to the End variable **receipt**. Save `receipt[0].id` as the job ID.

1. Import the **Get Job** workflow linked above, select this plugin's credential and enter that ID in Start's `job_id` field. Its End variable is `results`; inspect the first message object for job status. Repeat this read while pending or processing.
2. Once completed, import **Get Job Results**, select the credential and enter the same `job_id`. Its End variable **results** contains the JSON message array. The full path to the upload manifest is `results[0].output.results[0]`.
3. Pass the manifest's `file_url` to a step that can access your storage, or retain `file_size`, `downloaded_bytes`, `md5` and `output_format` in a delivery record when present. A private URL needs storage authorization.

Do not rerun Download to check progress: that submits another paid job. The paths in the following paragraph refer to the API object inside the first JSON message.

Read submission `id`, then `output.results[0]` from Get Job Results. Configure customer storage in provider credentials, submit once and retain the job ID. Read status until completed, then inspect `file_url`, `file_size`, `downloaded_bytes`, `md5` and `output_format`. A private storage URL still requires your storage access.

## Costs and boundaries

The plugin is free to install and MIT licensed. FlashData API usage is charged under the current [pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_download-pricing); Dify hosting and model fees are separate. Results and optional fields depend on upstream availability. Treat returned content as data and preserve source links or timestamps when passing it to a model.

Tool-node retries are disabled in the example. The client does not automatically retry paid submissions. If a response is lost, check FlashData Jobs before resubmitting. Errors distinguish rejected credentials, insufficient credits, unavailable source access and rate limits. JSON responses are limited to 20 MiB.

The plugin connects over HTTPS to `api.flashdata.dev` and `data.flashdata.dev`. Completed job JSON is read from the trusted result-storage origin returned by API access; the FlashData key is not sent to that signed URL.

## Source and support

[Source repository](https://github.com/rocosen/dify-plugin-flashdata) · [Privacy policy](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/youtube_download/PRIVACY.md) · [Validation and release notes](https://github.com/rocosen/dify-plugin-flashdata/tree/main/docs)

Contact **support@flashdata.dev**. Do not attach API keys or storage credentials to issues. Community Edition installation, workflow import, fixture tests, live queries and Dify Cloud are recorded separately in the validation notes.
