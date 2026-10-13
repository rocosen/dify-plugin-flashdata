# Task workflows for Google and YouTube

Import the YAML for your task into Dify Studio after installing FlashData 0.2.0. Select your provider credential in the tool node, supply the Start input, then run it. Each data workflow makes one billable request. Tool-node retries are disabled. The settings below are reproducible input examples, not claimed live result fixtures.

Each workflow returns the full tool JSON message array as `results`. Within its first message, use the response paths below. Download submission instead returns `receipt`; read the same job with the two companion workflows.

## Google Search: Search Google and export structured web results

Get ranked web links, titles, snippets and available SERP features for a query. Use country, language, location or time filters to narrow a research topic.

[Import workflow](google_search.yml) · [API documentation](https://flashdata.dev/docs/sources/google_search?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_search-workflow)

Start input and tool settings:

```json
{
  "query": "Dify workflow automation",
  "num": 3
}
```

Read `results[0].organic`. Keep `title`, `link`, `snippet` and `position` together when exporting sources. A snippet is a search excerpt; fetching a full page is a separate task.

## Google News: Track a topic in Google News

Find news titles, publisher links, dates and snippets about a topic. Use the source links to build a news digest; the response is search data, not full articles.

[Import workflow](google_news.yml) · [API documentation](https://flashdata.dev/docs/sources/google_news?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_news-workflow)

Start input and tool settings:

```json
{
  "query": "renewable energy",
  "tbs": "qdr:w",
  "num": 5
}
```

Read `results[0].news`. Use `title`, `link`, `source`, `date` and `snippet` to prepare a briefing. Link each headline to the article and retain the publisher. Set `tbs=qdr:w` for a past-week search.

## Google Images: Find images and their source pages

Find image URLs, thumbnails, dimensions and source pages. Use the returned metadata to select images before downloading or using them separately.

[Import workflow](google_images.yml) · [API documentation](https://flashdata.dev/docs/sources/google_images?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_images-workflow)

Start input and tool settings:

```json
{
  "query": "solar panel roof",
  "num": 5
}
```

Read `results[0].images`. Keep `imageUrl` with its source-page `link`. Filter returned `imageWidth` and `imageHeight` locally for a size requirement; unavailable dimensions stay unknown. The tool returns metadata and URLs.

## Google Shopping: Compare product listings and merchants

Search product listings with available prices, merchants and links. Capture a comparison snapshot; prices and availability can change.

[Import workflow](google_shopping.yml) · [API documentation](https://flashdata.dev/docs/sources/google_shopping?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_shopping-workflow)

Start input and tool settings:

```json
{
  "query": "usb c dock",
  "gl": "us",
  "num": 5
}
```

Read `results[0].shopping`. Compare `title`, `productId`, merchant `source`, `price` and `link`. Keep variants and currencies separate; an offer snapshot does not guarantee inventory or checkout price.

## Google Video Search: Find video results across websites

Find video pages across websites through Google Video Search. Returns links and available video metadata for a query.

[Import workflow](google_videos.yml) · [API documentation](https://flashdata.dev/docs/sources/google_videos?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_videos-workflow)

Start input and tool settings:

```json
{
  "query": "bread baking tutorial",
  "num": 5
}
```

Read `results[0].videos`. Use `title`, `link`, `source`, available `duration` and `snippet` to compare tutorials across websites. Keep the original page link so a user can inspect the video.

## Google Places: Find local businesses and places

Search places with available addresses, ratings, contact details and links. Useful for a local business shortlist; individual fields may be missing.

[Import workflow](google_places.yml) · [API documentation](https://flashdata.dev/docs/sources/google_places?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_places-workflow)

Start input and tool settings:

```json
{
  "query": "bookshops",
  "location": "London",
  "num": 5
}
```

Read `results[0].places`. Build a shortlist from `title`, `address`, `rating`, `ratingCount` and `category`. Include contact information only when returned; missing values are not zero or evidence that a business lacks them.

## YouTube Search: Discover YouTube videos by keyword

Find YouTube videos for a topic, with optional upload-date, duration, type, feature and sort filters. Request 1–20 results; actual results may be fewer.

[Import workflow](youtube_search.yml) · [API documentation](https://flashdata.dev/docs/sources/youtube_search?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_search-workflow)

Start input and tool settings:

```json
{
  "query": "Python tutorials",
  "max_results": 5,
  "filters_json": "{\"upload_date\":\"this_week\"}"
}
```

Read `results[0].results`. Keep `videoId`, `title`, channel information and available view counts. Build watch URLs as https://www.youtube.com/watch?v=<videoId>. Set `filters_json` for upload date, duration, sort order or features.

## YouTube Extended Search: Collect up to 700 YouTube search results

Run a larger YouTube search with the same filter options and a 1–700 requested-result limit. This is a separate FlashData source with its own price; the limit is not a guaranteed result count.

[Import workflow](youtube_search_extended.yml) · [API documentation](https://flashdata.dev/docs/sources/youtube_search_extended?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_search_extended-workflow)

Start input and tool settings:

```json
{
  "query": "Dify workflows",
  "max_results": 100,
  "filters_json": "{\"type\":\"video\"}"
}
```

Read `results[0].results`. Export one row per returned video and deduplicate by `videoId`. This source accepts up to 700 requested results and has a separate price from standard search; the actual count can be lower.

## YouTube Video Metadata: Read YouTube metadata and chapters

Read a video title, description, channel, available statistics, chapters and format metadata. Accepts a video ID or YouTube video URL.

[Import workflow](youtube_metadata.yml) · [API documentation](https://flashdata.dev/docs/sources/youtube_metadata?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_metadata-workflow)

Start input and tool settings:

```json
{
  "video_id": "dQw4w9WgXcQ",
  "include_chapters": true,
  "include_formats": false
}
```

Read `results[0]`. Read the title, description, channel and available statistics. Chapters and formats are optional; use `include_formats=false` when only inspecting a title or chapter list.

## YouTube Transcript: Retrieve timestamped YouTube transcripts

Retrieve existing timestamped subtitles and full text in a selected language. Defaults to automatically generated captions. No speech recognition, translation or silent fallback to another track.

[Import workflow](youtube_transcript.yml) · [API documentation](https://flashdata.dev/docs/sources/youtube_transcript?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_transcript-workflow)

Start input and tool settings:

```json
{
  "video_id": "dQw4w9WgXcQ",
  "language": "en",
  "auto": true
}
```

Read `results[0].segments` and `fullText`. Segments contain `start`, `end` and `text`, with times in seconds. Preserve timestamps for citations or convert them to SRT/WebVTT in a subsequent node. Default `auto=true` selects automatic captions.

## YouTube Captions: Retrieve uploader-provided YouTube captions

Read existing caption segments and full text in a selected language. Defaults to manual uploader captions; auto=true explicitly selects automatic captions. Availability depends on the video.

[Import workflow](youtube_captions.yml) · [API documentation](https://flashdata.dev/docs/sources/youtube_captions?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_captions-workflow)

Start input and tool settings:

```json
{
  "video_id": "dQw4w9WgXcQ",
  "language": "en",
  "auto": false
}
```

Read `results[0].segments` and `fullText`. Default `auto=false` selects uploader-provided captions. Check `languageCode` and `isAutoGenerated` before using the track. Missing captions are not generated, translated or silently replaced.

## YouTube License Metadata: Inspect YouTube Creative Commons license labels

Read the Creative Commons license classification exposed by the video metadata. The API source is youtube_trainability; this does not read creator training settings or grant training permission.

[Import workflow](youtube_trainability.yml) · [API documentation](https://flashdata.dev/docs/sources/youtube_trainability?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_trainability-workflow)

Start input and tool settings:

```json
{
  "video_id": "dQw4w9WgXcQ"
}
```

Read `results[0]` license classification. Use the returned Creative Commons license metadata as an attribute in your video records. It does not expose creator third-party training settings and does not grant permission to train on a video.

## YouTube Channel Data: Read channel data and recent videos

Retrieve a YouTube channel profile and recent videos using its handle. Request 1–100 videos; returned fields and count depend on upstream availability.

[Import workflow](youtube_channel.yml) · [API documentation](https://flashdata.dev/docs/sources/youtube_channel?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_channel-workflow)

Start input and tool settings:

```json
{
  "handle": "@GoogleDevelopers",
  "video_limit": 10
}
```

Read `results[0]` and its `videos[]`. Start from an @handle. Read channel identity and available subscriber information, then export recent videos with IDs, titles and durations. This is a recent-video snapshot, not a full channel archive.

## YouTube Autocomplete: Explore YouTube search suggestions

Get autocomplete phrases for a query prefix in a selected language and region. Use them to explore related topics; they are suggestions, not search-volume estimates.

[Import workflow](youtube_suggestions.yml) · [API documentation](https://flashdata.dev/docs/sources/youtube_suggestions?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_suggestions-workflow)

Start input and tool settings:

```json
{
  "query": "how to build",
  "language": "en",
  "region": "US"
}
```

Read `results[0]`, an array of strings. Return suggestions as a list or use them to expand a topic. To compare regions, run the same prefix with different `region` values; each query is billed. These phrases are not search-volume measurements.

## YouTube Download: Deliver YouTube video or audio to your cloud storage

Submit an asynchronous video or audio download to your configured customer storage. Returns a job ID. Use Get Job, then Get Job Results to read the upload manifest. Billed by delivered bytes under current FlashData pricing.

[Import workflow](youtube_download.yml) · [API documentation](https://flashdata.dev/docs/sources/youtube_download?utm_source=dify&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_download-workflow)

Start input and tool settings:

```json
{
  "video_id": "dQw4w9WgXcQ",
  "download_type": "audio_video",
  "video_quality": "<=720",
  "upload_metadata": false
}
```

Read submission `id`, then `output.results[0]` from Get Job Results. Configure customer storage in provider credentials, submit once and retain the job ID. Read status until completed, then inspect `file_url`, `file_size`, `downloaded_bytes`, `md5` and `output_format`. A private storage URL still requires your storage access.

## Read a download job without submitting again

1. Copy `id` from the submission receipt.
2. Import [Get Job](get_job.yml), set `job_id` to that ID and read `job.status`. For pending/processing jobs, repeat only this read later.
3. When completed, import [Get Job Results](get_job_results.yml) with the same ID. Read `output.results[0]`. Failed jobs return their status; inspect the cause before deciding whether a new paid submission is appropriate.

JSON results remain available for 24 hours after completion. Media retention and access follow your own storage settings. No workflow embeds storage credentials.
