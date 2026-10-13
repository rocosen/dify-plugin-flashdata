# YouTube Download — FlashData Privacy Policy

Effective date: 2026-10-13. Contact: support@flashdata.dev.

This policy applies to the independent `youtube_download` Dify plugin and the `youtube_download` FlashData source.

## Information processed

The plugin reads the FlashData API key from the credential configured in Dify. It sends the key only as an `X-API-Key` header to FlashData's HTTPS APIs. Credential verification calls `api.flashdata.dev/v2/api-access` without a search query.

Download execution sends the YouTube video ID, download options, storage credential and generated request identifier to the asynchronous API described below. YouTube URLs are parsed locally; the plugin does not fetch the supplied URL. Job receipts, statuses and result metadata are returned to Dify.

For YouTube Download, the plugin reads the optional customer storage JSON from Dify provider credentials and sends it only in the download request to `data.flashdata.dev/v1/queries`. This can include bucket/container names, object prefixes and storage credentials. FlashData workers use them to deliver media to your storage provider. They are not LLM tool parameters and are not included in exported workflow examples or tool outputs. Use credentials scoped to the intended destination.

Job reads use `api.flashdata.dev/v2/jobs/{id}`. A completed result is retrieved via a signed HTTPS URL whose origin must match the trusted origin returned by FlashData API access. That request does not include the FlashData API key. The result JSON includes media destination URLs and upload metadata; the plugin does not download the media itself. JSON results expire after 24 hours, while media retention follows customer storage settings.

## Storage and logs

The plugin itself has no persistent storage, telemetry or explicit request logging. It does not intentionally include credentials or raw server errors in error messages. This does not imply that Dify or FlashData has zero retention.

Dify manages the configured credential and may retain workflow inputs, tool outputs, execution history and platform logs according to the workspace or deployment settings. If a workflow sends results to a model or another service, that service also receives the data selected by the workflow owner; the plugin does not control those later steps.

FlashData processes authentication, queries, jobs, usage, billing and security records under its [service privacy policy](https://flashdata.dev/legal/privacy). Records may be retained for operation, security, accounting and legal requirements. YouTube requests use YouTube retrieval components and related infrastructure. These upstreams receive the inputs needed to fulfill the query. The plugin contacts the two FlashData domains and the authenticated result-storage origin. Media delivery from FlashData workers also involves the customer-selected cloud storage provider.

Relevant third-party notices: [Google/YouTube privacy policy](https://policies.google.com/privacy). For Dify Cloud, see [Dify's privacy policy](https://dify.ai/privacy); for self-hosted Dify, consult your deployment operator.

## Choices and requests

Use only data you are authorized to process. Do not enter credentials, precise personal location or unnecessary personal information in search queries. Revoke or replace your FlashData API key to stop its future use, and remove the credential or plugin from Dify when no longer needed. Dify history and third-party records must be managed separately. Contact support@flashdata.dev for FlashData retention, deletion or privacy requests.
