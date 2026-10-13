# Independent Google and YouTube plugins for Dify

Each row is a separate plugin identity, package and Marketplace submission target. A tool inside the original bundle does not count as a separate Marketplace entry. These 15 task plugins share tested source code but expose only their own task; YouTube Download includes its two job readers.

GitHub packages, submitted review requests, live Marketplace pages and search discovery are tracked separately. The original `flashdata-dev/flashdata` bundle remains compatible and is not counted among the 15 task entries.

| Plugin | Identity | Package version | Documentation / workflow |
| --- | --- | --- | --- |
| Google Search | `flashdata-dev/google_search` | 0.1.0 | [Guide](google_search/README.md) · [Workflow](google_search/google_search.yml) |
| Google News | `flashdata-dev/google_news` | 0.1.0 | [Guide](google_news/README.md) · [Workflow](google_news/google_news.yml) |
| Google Images | `flashdata-dev/google_images` | 0.1.0 | [Guide](google_images/README.md) · [Workflow](google_images/google_images.yml) |
| Google Shopping | `flashdata-dev/google_shopping` | 0.1.0 | [Guide](google_shopping/README.md) · [Workflow](google_shopping/google_shopping.yml) |
| Google Video Search | `flashdata-dev/google_videos` | 0.1.0 | [Guide](google_videos/README.md) · [Workflow](google_videos/google_videos.yml) |
| Google Places | `flashdata-dev/google_places` | 0.1.0 | [Guide](google_places/README.md) · [Workflow](google_places/google_places.yml) |
| YouTube Search | `flashdata-dev/youtube_search` | 0.1.0 | [Guide](youtube_search/README.md) · [Workflow](youtube_search/youtube_search.yml) |
| YouTube Extended Search | `flashdata-dev/youtube_search_extended` | 0.1.0 | [Guide](youtube_search_extended/README.md) · [Workflow](youtube_search_extended/youtube_search_extended.yml) |
| YouTube Video Metadata | `flashdata-dev/youtube_metadata` | 0.1.0 | [Guide](youtube_metadata/README.md) · [Workflow](youtube_metadata/youtube_metadata.yml) |
| YouTube Transcript | `flashdata-dev/youtube_transcript` | 0.1.0 | [Guide](youtube_transcript/README.md) · [Workflow](youtube_transcript/youtube_transcript.yml) |
| YouTube Captions | `flashdata-dev/youtube_captions` | 0.1.0 | [Guide](youtube_captions/README.md) · [Workflow](youtube_captions/youtube_captions.yml) |
| YouTube License Metadata | `flashdata-dev/youtube_trainability` | 0.1.0 | [Guide](youtube_trainability/README.md) · [Workflow](youtube_trainability/youtube_trainability.yml) |
| YouTube Channel Data | `flashdata-dev/youtube_channel` | 0.1.0 | [Guide](youtube_channel/README.md) · [Workflow](youtube_channel/youtube_channel.yml) |
| YouTube Autocomplete | `flashdata-dev/youtube_suggestions` | 0.1.0 | [Guide](youtube_suggestions/README.md) · [Workflow](youtube_suggestions/youtube_suggestions.yml) |
| YouTube Download | `flashdata-dev/youtube_download` | 0.1.0 | [Guide](youtube_download/README.md) · [Workflow](youtube_download/youtube_download.yml) |

## Build

From the repository root, using the existing Python 3.12 environment and official Dify CLI:

```sh
.venv/bin/python scripts/build_plugins.py --cli dify
```

Outputs are under `dist/task-plugins/`, including SHA256SUMS and packages.json. Use `--source google_news` to build one package into a separate `--output` directory. Each package is self-contained: the builder copies the shared runtime, selects only its source schema/tools, sets a unique manifest/provider identity, and includes its own README/privacy policy. No network download or generation step runs when users install a package.

`plugins/catalog.json` controls versions and display metadata. Edit each task's README/PRIVACY and workflow here; do not change a published version in place. Workflow examples point to the independent provider, not the aggregate provider. `scripts.build_plugins.workflow` can regenerate the initial workflow shape from the original examples.

## Publication status

As of 2026-10-13, all 15 version 0.1.0 packages are [released](https://github.com/flashdata-dev/dify-plugin-flashdata/releases/tag/task-plugins-v0.1.0) and submitted separately to the official Marketplace repository. All 15 pull requests are open; the 30 official checks passed. Human review and public listing verification remain pending. Package publication and successful checks do not mean Marketplace approval or search visibility.

| Plugin | Official submission | Review status |
| --- | --- | --- |
| Google Search | [#3304](https://github.com/langgenius/dify-plugins/pull/3304) | Open; automated checks passed; awaiting review |
| Google News | [#3305](https://github.com/langgenius/dify-plugins/pull/3305) | Open; automated checks passed; awaiting review |
| Google Images | [#3306](https://github.com/langgenius/dify-plugins/pull/3306) | Open; automated checks passed; awaiting review |
| Google Shopping | [#3307](https://github.com/langgenius/dify-plugins/pull/3307) | Open; automated checks passed; awaiting review |
| Google Video Search | [#3308](https://github.com/langgenius/dify-plugins/pull/3308) | Open; automated checks passed; awaiting review |
| Google Places | [#3309](https://github.com/langgenius/dify-plugins/pull/3309) | Open; automated checks passed; awaiting review |
| YouTube Search | [#3310](https://github.com/langgenius/dify-plugins/pull/3310) | Open; automated checks passed; awaiting review |
| YouTube Extended Search | [#3311](https://github.com/langgenius/dify-plugins/pull/3311) | Open; automated checks passed; awaiting review |
| YouTube Video Metadata | [#3312](https://github.com/langgenius/dify-plugins/pull/3312) | Open; automated checks passed; awaiting review |
| YouTube Transcript | [#3313](https://github.com/langgenius/dify-plugins/pull/3313) | Open; automated checks passed; awaiting review |
| YouTube Captions | [#3314](https://github.com/langgenius/dify-plugins/pull/3314) | Open; automated checks passed; awaiting review |
| YouTube License Metadata | [#3315](https://github.com/langgenius/dify-plugins/pull/3315) | Open; automated checks passed; awaiting review |
| YouTube Channel Data | [#3316](https://github.com/langgenius/dify-plugins/pull/3316) | Open; automated checks passed; awaiting review |
| YouTube Autocomplete | [#3317](https://github.com/langgenius/dify-plugins/pull/3317) | Open; automated checks passed; awaiting review |
| YouTube Download | [#3318](https://github.com/langgenius/dify-plugins/pull/3318) | Open; automated checks passed; awaiting review |

The existing `flashdata-dev/flashdata` bundle is maintained separately for compatibility; [update PR #3303](https://github.com/langgenius/dify-plugins/pull/3303) does not replace these dedicated submissions. See [validation notes](../docs/independent-plugins-2026-10-13.md) for the exact test scope. Dify Cloud and real model-agent execution have not been tested for this split.
