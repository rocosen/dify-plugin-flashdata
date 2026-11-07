# Google Places

Find local businesses and places for a query and location, such as bookshops in London. Return available addresses, ratings, categories and contact details. Missing fields remain unknown rather than being filled in by a model.

[Get an API key](https://flashdata.dev/signup?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_places-task) · [API documentation](https://flashdata.dev/docs/sources/google_places?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_places-task) · [Pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_places-task)

## Setup

1. In Dify **1.17.1+**, install [Google Places](https://marketplace.dify.ai/plugin/flashdata-dev/google_places) by **flashdata-dev**.
2. In this plugin's provider settings, enter your FlashData API key with access to `google_places`. Key validation is free; data queries use Credits. No separate Google or YouTube key is needed.
3. Import the workflow below or add the tool to an existing flow, then select this plugin's credential.

## Find local businesses and places

[Example workflow](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/google_places/google_places.yml): **Start → Google Places → End**. Select your credential, then supply the Start input.

Enter only `query` in **Start**. Set the remaining fields in the tool node.

| Field | Where to set it | Example | Meaning |
| --- | --- | --- | --- |
| `query` | Start input | `bookshops` | Topic or search phrase. |
| `location` | Tool node setting | `London` | Location used for the places search. |
| `num` | Tool node setting | `5` | Requested result count; fewer results may be available. |

## Use the output

The tool returns `text` (a JSON string) and `json` (Dify's message array). The example maps `json` to End's **results**; the full output path is `results[0].results[0].places`. The paths below refer to the API object inside that first message.

Read `results[0].places`. Read `title`, `address`, `rating`, `ratingCount` and `category`. Include contact information only when returned; missing values are not zero or evidence that a business lacks them.

## Costs and limits

Free to install under MIT. API calls use [FlashData Credits](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_places-task); Dify/model fees are separate. Results and optional fields depend on source availability. Preserve source links and treat retrieved text as data.

Paid submissions are not retried automatically. After a timeout, check FlashData Jobs before resubmitting. Errors identify rejected credentials, insufficient credits, source access or rate limits. JSON responses are limited to 20 MiB.

HTTPS access to `api.flashdata.dev` and `data.flashdata.dev` is required.

## Source and support

[Source repository](https://github.com/rocosen/dify-plugin-flashdata) · [Privacy policy](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/google_places/PRIVACY.md) · [Validation and release notes](https://github.com/rocosen/dify-plugin-flashdata/tree/main/docs)

Contact **support@flashdata.dev**; keep keys and storage credentials out of support requests.
