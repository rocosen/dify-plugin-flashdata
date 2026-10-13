# Google News — FlashData Privacy Policy

Effective date: 2026-10-13. Contact: support@flashdata.dev.

This policy applies to the independent `google_news` Dify plugin and the `google_news` FlashData source.

## Information processed

The plugin reads the FlashData API key from the credential configured in Dify. It sends the key only as an `X-API-Key` header to FlashData's HTTPS APIs. Credential verification calls `api.flashdata.dev/v2/api-access` without a search query.

Tool execution sends the `google_news` source, search query, selected search options (including broad location if supplied), and a generated request identifier to `data.flashdata.dev/v1/queries/realtime`. API responses, including result metadata, source links and usage information, are returned to Dify. This plugin does not fetch arbitrary input URLs.

## Storage and logs

The plugin itself has no persistent storage, telemetry or explicit request logging. It does not intentionally include credentials or raw server errors in error messages. This does not imply that Dify or FlashData has zero retention.

Dify manages the configured credential and may retain workflow inputs, tool outputs, execution history and platform logs according to the workspace or deployment settings. If a workflow sends results to a model or another service, that service also receives the data selected by the workflow owner; the plugin does not control those later steps.

FlashData processes authentication, queries, jobs, usage, billing and security records under its [service privacy policy](https://flashdata.dev/legal/privacy). Records may be retained for operation, security, accounting and legal requirements. Google searches may be processed through Serper and related infrastructure. These upstreams receive the inputs needed to fulfill the query. This dedicated plugin contacts only the two FlashData API domains; it does not expose media-download, storage-write or job-reader tools.

Relevant third-party notices: [Serper privacy policy](https://serper.dev/privacy) and [Google/YouTube privacy policy](https://policies.google.com/privacy). For Dify Cloud, see [Dify's privacy policy](https://dify.ai/privacy); for self-hosted Dify, consult your deployment operator.

## Choices and requests

Use only data you are authorized to process. Do not enter credentials, precise personal location or unnecessary personal information in search queries. Revoke or replace your FlashData API key to stop its future use, and remove the credential or plugin from Dify when no longer needed. Dify history and third-party records must be managed separately. Contact support@flashdata.dev for FlashData retention, deletion or privacy requests.
