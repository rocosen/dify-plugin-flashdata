# FlashData workflow examples

These Dify DSL files contain no API keys, model keys or workspace credential IDs. Install the FlashData plugin and authorize the provider before importing one through **Studio → Import DSL file**. If Dify asks for a credential, select your own FlashData credential on the tool node.

| File | Start input | Behavior |
| --- | --- | --- |
| `google_search.yml` | `query` | One Google search, requesting 3 results |
| `youtube_search.yml` | `query` | One YouTube search, requesting 1 result |
| `youtube_metadata.yml` | `video_id` | One metadata request, chapters enabled, format metadata disabled |
| `youtube_transcript.yml` | `video_id` | One English manual-caption request (`auto=false`) |

Each workflow is **Start → FlashData tool → End**, returning the full API response in the tool's JSON message array. No LLM is required for these examples. Each run can consume FlashData credits. Retries are disabled. Choose a video with the requested captions, or change the language/automatic-caption parameter on the tool node.

The plugin dependency is intentionally not an automatic Marketplace download: until the plugin is listed, install the `.difypkg` from the source repository's Releases first. These examples target Dify 1.17.1 (DSL 0.7.0).

To build a research agent, enable the FlashData tools in an Agent and use the instruction and example request in the main README. That requires a separately configured model with tool calling support.
