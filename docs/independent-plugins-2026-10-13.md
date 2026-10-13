# Independent Dify plugins — 2026-10-13

The 15 Google and YouTube sources now have 15 independent plugin identities, package files, task guides, privacy policies and importable workflows. A single aggregate Marketplace card does not provide 15 separate entries. The original `flashdata-dev/flashdata` bundle remains a compatibility package and is not counted as one of these dedicated entries.

## Implementation and validation

- `plugins/catalog.json` defines the 15 identities/display metadata and version 0.1.0 for each plugin. The runtime remains canonical under `flashdata/`, `provider/` and `tools/`; `scripts/build_plugins.py` builds self-contained packages from these shared files.
- Each package contains only its source schema and business tool. YouTube Download additionally includes Get Job/Get Job Results. Ordinary plugins expose only the API key credential; customer storage is exposed only by YouTube Download.
- The original bundle identity, tool IDs, parameters and runtime behavior are unchanged. Independent workflow examples use `flashdata-dev/<name>/<name>` and require that dedicated plugin's credential.
- 30 unit/SDK/HTTP-fixture tests passed, including isolated subprocess invocation of all 15 package source trees. These tests do not perform billable queries.
- Official local validator: 15/15 final packages, zero blocking failures. Billing terms/network domains/dependency details are review information. See [validation](independent-plugins-validation-2026-10-13.md).
- Dify Community Edition 1.17.1 / daemon 0.6.10-local: all 15 final packages installed concurrently, 17 tools discovered, 17 workflows imported and saved provider/tool identities read back. Each import returned no missing dependency entries. The original aggregate plugin and its workflows remain installed. See [CE evidence](independent-plugins-ce-2026-10-13.json).
- Initial candidate privacy text was narrowed to each source, then all final packages were rebuilt/scanned and installed via Dify's credential-preserving package replacement flow. CE unique identifiers in the evidence belong to those final packages.
- No new paid source query, storage write, or model call was made. Cloud and real LLM Agent execution remain untested. Prior bundle live API results are not claimed as dedicated-plugin live test evidence.

## Release and Marketplace

[Release task-plugins-v0.1.0](https://github.com/flashdata-dev/dify-plugin-flashdata/releases/tag/task-plugins-v0.1.0) groups 15 independently versioned 0.1.0 packages. Package file hashes are listed in [the manifest](independent-plugins-packages-2026-10-13.json) and SHA256SUMS. A shared source repository or Release does not merge the plugin identities.

Each Marketplace PR adds exactly one package under `flashdata-dev/<plugin-name>/`. The publication register in [plugins/README](../plugins/README.md) records the resulting review URLs. GitHub release publication, official review acceptance, Marketplace synchronization and non-brand search discovery remain separate milestones. No listing is marked live until its actual Marketplace page is checked.

Medium risk is disclosed for data-query plugins (external user query/public data processing), and High for download storage credentials and remote writes. The agreement checkbox remains unchecked pending a canonical document, as in the previously accepted bundle submission; no new legal acceptance is claimed.
