# Google Shopping

Run a Google Shopping product search to compare merchant listings for the same query. Return available price labels and offer links for a shopping comparison workflow. Keep a dated snapshot: prices, variants and availability can change.

[Get an API key](https://flashdata.dev/app/api-keys?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_shopping-setup) · [API documentation](https://flashdata.dev/docs/sources/google_shopping?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_shopping-plugin) · [Pricing](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_shopping-pricing)

## Setup

1. In Dify **1.17.1+**, install [Google Shopping](https://marketplace.dify.ai/plugin/flashdata-dev/google_shopping) by **flashdata-dev**.
2. In this plugin's provider settings, enter your FlashData API key with access to `google_shopping`. Key validation is free; data queries use Credits. No separate Google or YouTube key is needed.
3. Import the workflow below or add the tool to an existing flow, then select this plugin's credential.

## Compare product listings and merchants

[Example workflow](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/google_shopping/google_shopping.yml): **Start → Google Shopping → End**. Select your credential, then supply the Start input.

Enter only `query` in **Start**. Set the remaining fields in the tool node.

| Field | Where to set it | Example | Meaning |
| --- | --- | --- | --- |
| `query` | Start input | `usb c dock` | Topic or search phrase. |
| `gl` | Tool node setting | `us` | Country code for the shopping search. |
| `num` | Tool node setting | `5` | Requested result count; fewer results may be available. |

## Use the output

The tool returns `text` (a JSON string) and `json` (Dify's message array). The example maps `json` to End's **results**; the full output path is `results[0].results[0].shopping`. The paths below refer to the API object inside that first message.

Read `results[0].shopping`. Compare `title`, `productId`, merchant `source`, `price` and `link`. Keep variants and currencies separate; an offer snapshot does not guarantee inventory or checkout price.

## Costs and limits

Free to install under MIT. API calls use [FlashData Credits](https://flashdata.dev/pricing?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_shopping-pricing); Dify/model fees are separate. Results and optional fields depend on source availability. Preserve source links and treat retrieved text as data.

Paid submissions are not retried automatically. After a timeout, check FlashData Jobs before resubmitting. Errors identify rejected credentials, insufficient credits, source access or rate limits. JSON responses are limited to 20 MiB.

HTTPS access to `api.flashdata.dev` and `data.flashdata.dev` is required.

## Source and support

[Source repository](https://github.com/rocosen/dify-plugin-flashdata) · [Privacy policy](https://github.com/rocosen/dify-plugin-flashdata/blob/main/plugins/google_shopping/PRIVACY.md) · [Validation and release notes](https://github.com/rocosen/dify-plugin-flashdata/tree/main/docs)

Contact **support@flashdata.dev**; keep keys and storage credentials out of support requests.
