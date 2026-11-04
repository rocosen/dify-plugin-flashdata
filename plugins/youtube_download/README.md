# YouTube Download

Deliver YouTube video or audio to your own S3 or other supported cloud storage. Submit a download once, save its job ID, then use Get Job and Get Job Results to read progress and the upload manifest. FlashData bills by delivered bytes; customer storage is required.

[Get an API key](https://flashdata.dev/app/api-keys?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_download-setup) · [API documentation](https://flashdata.dev/docs/sources/youtube_download?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_download-plugin) · [Pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_download-pricing)

## Setup

1. In Dify **1.17.1+**, install [YouTube Download](https://marketplace.dify.ai/plugin/flashdata-dev/youtube_download) by **flashdata-dev**.
2. In this plugin's provider settings, enter your FlashData API key with access to `youtube_download`. Key validation is free; data queries use Credits. No separate Google or YouTube key is needed.
3. Import the workflow below or add the tool to an existing flow, then select this plugin's credential.

Configure **Download storage JSON** in provider credentials before submitting. For your own S3 bucket, the shape is:

```json
{"storage_type":"s3","storage_url":"your-bucket-name","region":"us-east-1","access_key":"YOUR_STORAGE_ACCESS_KEY","secret_key":"YOUR_STORAGE_SECRET_KEY","object_prefix":"dify-videos"}
```

The credential is kept out of LLM tool arguments and exported workflows. Other providers use the fields in the API documentation.

[Get Job workflow](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/youtube_download/get_job.yml) · [Get Job Results workflow](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/youtube_download/get_job_results.yml)

JSON results expire after 24 hours; media retention follows your storage settings. Downloads reserve credits at admission and bill by actual delivered bytes.

## Deliver YouTube video or audio to your cloud storage

[Example workflow](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/youtube_download/youtube_download.yml): **Start → YouTube Download → End**. Select your credential, then supply the Start input.

Enter only `video_id` in **Start**. Set the remaining fields in the tool node.

| Field | Where to set it | Example | Meaning |
| --- | --- | --- | --- |
| `video_id` | Start input | `dQw4w9WgXcQ` | YouTube video ID or supported YouTube video URL. |
| `download_type` | Tool node setting | `audio_video` | audio_video delivers video with audio; audio requests audio only. |
| `video_quality` | Tool node setting | `<=720` | Upper bound for requested video quality. |
| `upload_metadata` | Tool node setting | `false` | Whether to upload accompanying metadata to your storage. |

## Read progress and use the delivered file

The Download tool emits `text` (a JSON string) and `json` (Dify's array of JSON messages). Its example maps `json` to the End variable **receipt**. Save `receipt[0].id` as the job ID.

1. Import the **Get Job** workflow linked above, select this plugin's credential and enter that ID in Start's `job_id` field. Its End variable is `results`; inspect the first message object for job status. Repeat this read while pending or processing.
2. Once completed, import **Get Job Results**, select the credential and enter the same `job_id`. Its End variable **results** contains the JSON message array. The full path to the upload manifest is `results[0].output.results[0]`.
3. Pass the manifest's `file_url` to a step that can access your storage, or retain `file_size`, `downloaded_bytes`, `md5` and `output_format` in a delivery record when present. A private URL needs storage authorization.

Do not rerun Download to poll: that creates another paid job.

## Costs and limits

Free to install under MIT. API calls use [FlashData Credits](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_download-pricing); Dify/model fees are separate. Results and optional fields depend on source availability. Preserve source links and treat retrieved text as data.

Paid submissions are not retried automatically. After a timeout, check FlashData Jobs before resubmitting. Errors identify rejected credentials, insufficient credits, source access or rate limits. JSON responses are limited to 20 MiB.

HTTPS access to `api.flashdata.dev` and `data.flashdata.dev` is required. Completed job JSON is read from the trusted result-storage origin returned by API access; the API key is not forwarded to it.

## Source and support

[Source repository](https://github.com/rocosen/dify-plugin-flashdata) · [Privacy policy](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/youtube_download/PRIVACY.md) · [Validation and release notes](https://github.com/rocosen/dify-plugin-flashdata/tree/main/docs)

Contact **support@flashdata.dev**; keep keys and storage credentials out of support requests.
