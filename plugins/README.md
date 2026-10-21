# Independent Google and YouTube plugins for Dify

Each row is a separate public Marketplace plugin with its own identity and package. A tool inside the original bundle does not count as a separate Marketplace entry. These 15 task plugins share tested source code but expose only their own task; YouTube Download includes its two job readers.

GitHub packages, submitted review requests, live Marketplace pages and search discovery are tracked separately. The original `flashdata-dev/flashdata` bundle remains compatible and is not counted among the 15 task entries.

| Plugin | Identity | Source/package version | Documentation / workflow |
| --- | --- | --- | --- |
| [Google Search](https://marketplace.dify.ai/plugin/flashdata-dev/google_search) | `flashdata-dev/google_search` | 0.1.2 | [Guide](google_search/README.md) · [Workflow](google_search/google_search.yml) |
| [Google News](https://marketplace.dify.ai/plugin/flashdata-dev/google_news) | `flashdata-dev/google_news` | 0.1.2 | [Guide](google_news/README.md) · [Workflow](google_news/google_news.yml) |
| [Google Images](https://marketplace.dify.ai/plugin/flashdata-dev/google_images) | `flashdata-dev/google_images` | 0.1.2 | [Guide](google_images/README.md) · [Workflow](google_images/google_images.yml) |
| [Google Shopping](https://marketplace.dify.ai/plugin/flashdata-dev/google_shopping) | `flashdata-dev/google_shopping` | 0.1.2 | [Guide](google_shopping/README.md) · [Workflow](google_shopping/google_shopping.yml) |
| [Google Video Search](https://marketplace.dify.ai/plugin/flashdata-dev/google_videos) | `flashdata-dev/google_videos` | 0.1.2 | [Guide](google_videos/README.md) · [Workflow](google_videos/google_videos.yml) |
| [Google Places](https://marketplace.dify.ai/plugin/flashdata-dev/google_places) | `flashdata-dev/google_places` | 0.1.2 | [Guide](google_places/README.md) · [Workflow](google_places/google_places.yml) |
| [YouTube Search](https://marketplace.dify.ai/plugin/flashdata-dev/youtube_search) | `flashdata-dev/youtube_search` | 0.1.2 | [Guide](youtube_search/README.md) · [Workflow](youtube_search/youtube_search.yml) |
| [YouTube Extended Search](https://marketplace.dify.ai/plugin/flashdata-dev/youtube_search_extended) | `flashdata-dev/youtube_search_extended` | 0.1.2 | [Guide](youtube_search_extended/README.md) · [Workflow](youtube_search_extended/youtube_search_extended.yml) |
| [YouTube Video Metadata](https://marketplace.dify.ai/plugin/flashdata-dev/youtube_metadata) | `flashdata-dev/youtube_metadata` | 0.1.2 | [Guide](youtube_metadata/README.md) · [Workflow](youtube_metadata/youtube_metadata.yml) |
| [YouTube Transcript](https://marketplace.dify.ai/plugin/flashdata-dev/youtube_transcript) | `flashdata-dev/youtube_transcript` | 0.1.2 | [Guide](youtube_transcript/README.md) · [Workflow](youtube_transcript/youtube_transcript.yml) |
| [YouTube Captions](https://marketplace.dify.ai/plugin/flashdata-dev/youtube_captions) | `flashdata-dev/youtube_captions` | 0.1.2 | [Guide](youtube_captions/README.md) · [Workflow](youtube_captions/youtube_captions.yml) |
| [YouTube License Metadata](https://marketplace.dify.ai/plugin/flashdata-dev/youtube_trainability) | `flashdata-dev/youtube_trainability` | 0.1.2 | [Guide](youtube_trainability/README.md) · [Workflow](youtube_trainability/youtube_trainability.yml) |
| [YouTube Channel Data](https://marketplace.dify.ai/plugin/flashdata-dev/youtube_channel) | `flashdata-dev/youtube_channel` | 0.1.2 | [Guide](youtube_channel/README.md) · [Workflow](youtube_channel/youtube_channel.yml) |
| [YouTube Autocomplete](https://marketplace.dify.ai/plugin/flashdata-dev/youtube_suggestions) | `flashdata-dev/youtube_suggestions` | 0.1.2 | [Guide](youtube_suggestions/README.md) · [Workflow](youtube_suggestions/youtube_suggestions.yml) |
| [YouTube Download](https://marketplace.dify.ai/plugin/flashdata-dev/youtube_download) | `flashdata-dev/youtube_download` | 0.1.2 | [Guide](youtube_download/README.md) · [Workflow](youtube_download/youtube_download.yml) |

## Build

From the repository root, using the existing Python 3.12 environment and official Dify CLI:

```sh
.venv/bin/python scripts/build_plugins.py --cli dify
```

Outputs are under `dist/task-plugins/`, including SHA256SUMS and packages.json. Use `--source google_news` to build one package into a separate `--output` directory. Each package is self-contained: the builder copies the shared runtime, selects only its source schema/tools, sets a unique manifest/provider identity, and includes its own README/privacy policy. No network download or generation step runs when users install a package.

`plugins/catalog.json` controls versions and display metadata. Edit each task's README/PRIVACY and workflow here; do not change a published version in place. Workflow examples point to the independent provider, not the aggregate provider. `scripts.build_plugins.workflow` can regenerate the initial workflow shape from the original examples.

## Publication status

As of 2026-10-13, all 15 version 0.1.0 packages are [released](https://github.com/rocosen/dify-plugin-flashdata/releases/tag/task-plugins-v0.1.0), approved and publicly listed in Dify Marketplace. All 15 official submission pull requests are merged; the 30 automated checks passed. Public listing, search discovery and successful workflow execution remain separate checks.

Version **0.1.1** updates Marketplace installation instructions, task descriptions, workflow parameter tables and Dify output mapping, and corrects four videoId examples. The runtime and task boundaries are unchanged. The original 0.1.0 assets remain intact. GitHub package publication and Marketplace approval are separate; see the [0.1.1 release record](../docs/content-release-2026-10-13.md) for validation and submission tracking. Until the update is approved and served, a Marketplace page may still show 0.1.0.

Version **0.1.2** includes the migrated `rocosen/dify-plugin-flashdata` repository and workflow links in the installation packages. Plugin/provider/tool identities, credentials and runtime behavior are unchanged. Existing 0.1.1 workflow examples remain compatible. As of 2026-10-18, Marketplace still serves 0.1.0; the earlier 0.1.1 update PRs cannot be read from the current authorized GitHub account, so their review status is unknown. Package release does not imply Marketplace approval. See the [repository-link release record](../docs/repository-link-release-2026-10-18.md).

| Plugin | Official submission | Review status |
| --- | --- | --- |
| Google Search | [#3304](https://github.com/langgenius/dify-plugins/pull/3304) | Merged; approved; 0.1.0 publicly listed |
| Google News | [#3305](https://github.com/langgenius/dify-plugins/pull/3305) | Merged; approved; 0.1.0 publicly listed |
| Google Images | [#3306](https://github.com/langgenius/dify-plugins/pull/3306) | Merged; approved; 0.1.0 publicly listed |
| Google Shopping | [#3307](https://github.com/langgenius/dify-plugins/pull/3307) | Merged; approved; 0.1.0 publicly listed |
| Google Video Search | [#3308](https://github.com/langgenius/dify-plugins/pull/3308) | Merged; approved; 0.1.0 publicly listed |
| Google Places | [#3309](https://github.com/langgenius/dify-plugins/pull/3309) | Merged; approved; 0.1.0 publicly listed |
| YouTube Search | [#3310](https://github.com/langgenius/dify-plugins/pull/3310) | Merged; approved; 0.1.0 publicly listed |
| YouTube Extended Search | [#3311](https://github.com/langgenius/dify-plugins/pull/3311) | Merged; approved; 0.1.0 publicly listed |
| YouTube Video Metadata | [#3312](https://github.com/langgenius/dify-plugins/pull/3312) | Merged; approved; 0.1.0 publicly listed |
| YouTube Transcript | [#3313](https://github.com/langgenius/dify-plugins/pull/3313) | Merged; approved; 0.1.0 publicly listed |
| YouTube Captions | [#3314](https://github.com/langgenius/dify-plugins/pull/3314) | Merged; approved; 0.1.0 publicly listed |
| YouTube License Metadata | [#3315](https://github.com/langgenius/dify-plugins/pull/3315) | Merged; approved; 0.1.0 publicly listed |
| YouTube Channel Data | [#3316](https://github.com/langgenius/dify-plugins/pull/3316) | Merged; approved; 0.1.0 publicly listed |
| YouTube Autocomplete | [#3317](https://github.com/langgenius/dify-plugins/pull/3317) | Merged; approved; 0.1.0 publicly listed |
| YouTube Download | [#3318](https://github.com/langgenius/dify-plugins/pull/3318) | Merged; approved; 0.1.0 publicly listed |

The existing `flashdata-dev/flashdata` bundle is maintained separately for compatibility; [update PR #3303](https://github.com/langgenius/dify-plugins/pull/3303) does not replace these dedicated submissions. See [validation notes](../docs/independent-plugins-2026-10-13.md) for the exact test scope. Dify Cloud and real model-agent execution have not been tested for this split.
