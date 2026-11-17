# Task plugin content and icons — 2026-11-17

Version 0.1.6 updates the 15 existing independent Marketplace plugins: six Google plugins use the color Google G, and nine YouTube plugins use the red play icon. Each task guide receives small edits to the introduction or example input instructions. Google Search adds a clearly labeled illustrative result item. Existing titles and short descriptions are retained.

## Review and comparisons

The current 0.1.5 public pages were read before editing. Google tasks were compared with [Google/SerpApi](https://marketplace.dify.ai/plugin/langgenius/google), [SearchApi](https://marketplace.dify.ai/plugin/langgenius/searchapi), [Serper](https://marketplace.dify.ai/plugin/langgenius/serper) and [Serply.io](https://marketplace.dify.ai/plugin/langgenius/websearch), matching only relevant search verticals. Their multi-tool scopes are not copied into individual task descriptions.

YouTube search, metadata and channel guides were compared with [YouTube](https://marketplace.dify.ai/plugin/langgenius/youtube) and [GetYouTubeTranscript](https://marketplace.dify.ai/plugin/tubeagentkit/getyoutubetranscript). Transcript/captions were compared with [Transcript](https://marketplace.dify.ai/plugin/langgenius/transcript) and GetYouTubeTranscript; [Arcmira](https://marketplace.dify.ai/plugin/arcmira/arcmira) was treated as passage search/monitoring, a different task from fetching one transcript. The existing autocomplete, license and cloud-delivery guides were checked against their actual tool schemas and workflows; no exact dedicated Marketplace competitor was verified for those tasks in this bounded review.

Installed counts are adoption signals, not traffic, unique users or evidence that copy causes ranking. Brand-asset sources are documented in [_assets/README.md](../_assets/README.md).

## Validation

- 31 unit/SDK/HTTP-fixture tests passed, including isolated execution of all 15 staged packages and the Google/YouTube icon regression check.
- Official Dify CLI v0.6.10 built all 15 final packages.
- All 15 passed the official local Marketplace package validator, including per-package PR capability-disclosure checks, with zero blocking or execution failures. These 15 runs used `--offline` for the dependency network lookup.
- An additional online Google Search validation found no known vulnerabilities in the three pinned dependencies. The dependency bytes are identical across the packages; this is a bounded check, not a guarantee about all transitive dependencies.
- Each final package was compared byte-for-byte with its released 0.1.5 counterpart. Only `manifest.yaml` (version), `README.md` and `_assets/icon.svg` changed. Runtime Python, requirements, provider credentials, tool schemas and privacy text are identical.
- Final packaged README/icon bytes match source. Titles, plugin identities, provider/tool IDs, permissions, existing paid-API semantics and workflow files are unchanged.
- Both SVG icons were rendered for visual inspection. Google remains multicolor and YouTube red/white.

The validator flags existing API billing language for manual interpretation and reports outbound domains. It also heuristically warns that connection requirements may be missing, although each README explicitly names the HTTPS hosts. No runtime or connection change was made to satisfy a keyword heuristic.

No live API/model calls, customer-storage writes, Community Edition reinstall or Dify Cloud run were performed for this documentation/icon update. Local validation does not confer Marketplace approval. The aggregate plugin remains version 0.2.6 and is outside this release.

## Packages and publication

Publish as `task-plugins-v0.1.6`, preserving all earlier releases. Each package must be submitted separately under its existing `flashdata-dev` identity. Existing 0.1.5 public pages remain the current version until Dify approves and serves the updates.

| Plugin | Icon | Package SHA-256 |
| --- | --- | --- |
| google_search | Google | `7d33c08b8e06bfb3a8f8c1ad6091ea03170c4f8c33446718c562e4bc4a1451a8` |
| google_news | Google | `2b6560e8fdc387b0094f9db5df6b2dcf4eea6db357e350af7ae2d9cad837cdfe` |
| google_images | Google | `043607d058acff4064aaa65c3e278ea8ad62dc745ffe711c5bf7a250d673e5c8` |
| google_shopping | Google | `2908b7a8ddfbc35c4d2de0cb1b093acba47179cd64d4f6ad4d3177e87f4cdf44` |
| google_videos | Google | `1ce8be4cbdd6628d41d2e2fdcfed5450031619d38b504663ec2dd9797a080397` |
| google_places | Google | `5bed66fa04a3a51957f962db03c126db0ca35f59db31e25cfc12466255b03844` |
| youtube_search | YouTube | `ea718895a92bc8203be2f45fb2e8c3bb5381026dee28d3b64a5ce11b689c0eba` |
| youtube_search_extended | YouTube | `dfed13266d9bdc655c84d6f38621ffff349c375f575a684ec9db6627d81ee3ac` |
| youtube_metadata | YouTube | `62e3076ded7d2a9ecae4094abd23a24d22f2bb20fc3ac0252933a52ae84684ed` |
| youtube_transcript | YouTube | `0bc85742cb51d4aa22c31a0b7095e482503f40c515ad8d45e4032dd849e425df` |
| youtube_captions | YouTube | `750b837a92cff50bc1c7b0d7be8d273a65426da4d523e81a6ed0560292616126` |
| youtube_trainability | YouTube | `6383d1365ed64b83ae9e017e6a4629645437a03d0f19e75203b5cfd584274de4` |
| youtube_channel | YouTube | `673b4cedede575ecd33883f5ab0c214ba4c8977b49bda21ada641ad46489c8c3` |
| youtube_suggestions | YouTube | `90295fe2b431aec96c4372805cfa58c99ca95283b409cdc32624c93e887d3529` |
| youtube_download | YouTube | `5f9399b8feaffc13f60448b0ad9beb9eb8c14870d998f647025ffabec0ab3389` |
