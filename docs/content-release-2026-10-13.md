# Marketplace content update — 2026-10-13

This release prepares all 15 dedicated plugins at **0.1.1**, plus the separate compatibility bundle at **0.2.2**. Each dedicated identity and its task scope are retained. The package runtime, tool schemas, dependencies and API behavior are unchanged.

## Developer-facing changes

- Use each plugin's official Marketplace installation page instead of outdated local-package instructions.
- Explain concrete task uses in descriptions and guides, with accurate natural terminology such as SERP, manual captions and search suggestions.
- Separate the single Start input from settings already configured in the tool node.
- Explain Dify's outer JSON message array, the API response object and complete End-output paths. Download submission, progress reads and completed results use their own documented paths.
- Correct videoId examples in four guides; preserve the download job id field.
- State that installation is free, FlashData data queries are paid, and Dify hosting/model fees are separate.

## Verification

All 30 existing unit/SDK/HTTP-fixture tests passed. Static checks covered 15 distinct Marketplace URLs, source-specific website links, parseable JSON examples, fee disclosures, parameter tables and workflow output mapping. All 17 workflow changes only update their description's version number.

All 16 exact packages passed the official local Marketplace toolkit with zero blocking or environment failures. Each produced three review/information warning categories: external API billing terminology, declared outbound domains and dependency inventory (no known vulnerabilities in the pinned set). The toolkit does not run installation/upload checks or prove Marketplace approval. Its report and package hashes are in [the validation record](content-release-validation-2026-10-13.json).

Runtime/tool/source-schema files were compared against the previous packages and are byte-identical. The old 0.1.0 and 0.2.1 assets are preserved. New packages require their own Marketplace update review.

The prior dedicated 0.1.0 packages were installed together from Marketplace in CE, with 17 tools and 17 imported workflows; their credentials remained empty. The bundle has separate historical 0.2.0 CE evidence. Those observations do not constitute installation or execution of this patch. **0.1.1/0.2.2 CE installation, Cloud and real LLM Agent execution are not tested in this release. No new paid API query, model call or storage write was made.**

## Publication and discovery

Source changes are reviewed in [PR #5](https://github.com/flashdata-dev/dify-plugin-flashdata/pull/5). Packages use new tags [task-plugins-v0.1.1](https://github.com/flashdata-dev/dify-plugin-flashdata/releases/tag/task-plugins-v0.1.1) and [v0.2.2](https://github.com/flashdata-dev/dify-plugin-flashdata/releases/tag/v0.2.2); links become available when published. Official update PRs and the latest observed status are recorded in the [GTM Dify channel card](https://github.com/flashdata-dev/flashdata-gtm/blob/main/docs/channels/dify.md).

Before this update, the 15 dedicated 0.1.0 entries were publicly listed. The 2026-10-13 16:31–16:34 Singapore public search snapshot matched 23 of 30 fixed natural-language queries and both queries for 9 of 15 capabilities. This predates the content change and is not evidence of its effect. Public page version, served content and the same complete 30-query search set must be checked after the new packages are approved and served.

Existing attribution parameters are retained. Cross-channel visit, signup and first-use attribution work remains deferred by the user; no product deployment or new tracking integration is included.
