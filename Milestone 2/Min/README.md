# Min — When Does a Hit Become “Global”?

**Milestone 2: Initial custom dataset and audit plan**  
**Status:** initial 50-observation sample; source verification and expansion remain in progress.

## Research question

For one Spotify chart week, how does the platform’s country-market Top 10 differ from its Global Top 10 across the United States, Brazil, Nigeria, and South Korea? Which tracks travel into the global ranking, and which stay visible only in a country chart? What does a single global rank make comparable—and what local listening contexts does it leave out?

This narrows the original interest in Spotify, YouTube, TikTok, Apple Music, and “regions.” The first version focuses on Spotify charts because TikTok uses social-video signals while Spotify charts describe eligible streams; their metrics are not interchangeable. Country charts are treated as **platform markets**, not natural or culturally uniform regions. The four markets span North America, South America, Africa, and East Asia, but they do not represent those regions as a whole.

## What is in the dataset

[`initial_chart_sample.csv`](initial_chart_sample.csv) contains 50 chart-position records: the first ten rows in each of four country-market weekly charts plus the first ten rows in Spotify’s Global weekly chart for the week ending **October 15, 2026**. A chart position—not a unique song—is the item. The global rows are kept as separate observations so the local/global comparison can be made without pretending the chart is an audience census.

The weekly stream counts, positions, appearances, and peak ranks were transcribed from Kworb’s Spotify weekly chart pages, which mirror chart information. Spotify’s own chart URLs are included for follow-up verification. The immediate source in the CSV is therefore a third-party chart mirror, not a direct API pull. The counts should be verified against Spotify’s downloadable chart files before a final submission; where values differ, retain both versions and document the discrepancy. Spotify says its chart counts use eligibility filters and may differ from the streams shown in Spotify for Artists, so chart streams are not equivalent to all listening or royalty counts.

### Fields and categories

| Field | Meaning |
|---|---|
| `record_id` | Stable local row key: market code plus chart rank. |
| `chart_week_end` | End date of the published chart week. |
| `platform` | Platform whose chart is represented; Spotify for every record. |
| `market_code`, `market_name` | Chart’s country market or `global` aggregate. |
| `market_scope` | `country_market` or `global`. |
| `macro_region` | A simple grouping for comparison; not a claim that a region has one culture. |
| `rank` | Position as reported by the source page. |
| `track_title`, `credited_artist` | Displayed title and artist credit; capitalization/credit formatting is retained or lightly normalized for readability. |
| `weekly_streams` | Weekly chart stream count shown by the mirror. |
| `weeks_on_chart`, `peak_rank` | Chart history values shown by the mirror. |
| `source_url` | Page used for the transcription. |
| `official_chart_url` | Corresponding Spotify chart route for verification. |
| `collection_date` | Date this sample was assembled. |

## Selection and interpretation

- **Include:** ranks 1–10 from the same chart week for the four selected markets and the global chart.
- **Exclude for this first pass:** other platforms, other weeks, albums, genres, city charts, and any artist-origin coding.
- **Why this sample:** a small, fixed week makes a first comparison feasible and yields 50 auditable observations. The four markets were chosen to span several settings, not because they represent entire continents or have equivalent platform penetration.
- **What “local” means here:** listed on a country-market chart. It does not mean the artist or song is culturally “from” that market. Artist origin, language, genre, diaspora, and cultural identity are not inferred from names or chart placement.
- **What “global” means here:** Spotify’s own Global chart category. It is not a neutral sum of all music worldwide. The platform’s market availability, chart eligibility rules, user base, and ranking design shape what is visible.
- **No causal claim:** a chart position alone cannot tell us why people listened, whether a track was discovered through a recommendation, or how listening differed by population size.

## From cultural material to structured data

1. **Cultural material → working representation.** The cultural material is recorded music as it appears in Spotify’s weekly ranked charts. Each page presents a platform-curated, ranked list with a week, market label, title/artist credits, and platform-defined listening metrics. The page is already a representation of listening, not listening itself.
2. **Working representation → structured data.** I selected rows 1–10 from the four country charts and the global chart for one common week, then transcribed each position into one CSV row. I kept market, rank, title, artist credit, stream count, chart tenure, and provenance together so each record can be checked. Artist and title are not used as proxies for nationality, language, or genre. The small script validates required fields, duplicate keys, and the 10-row-per-chart sample and reports exact title/artist overlap with the global Top 10.

## Initial observation and audit plan

The sample has a potentially revealing contrast: the charts assign very different numerical ranges to the same ordinal scale (for example, a country-market No. 1 and the Global No. 1 have different stream totals). Rank is relative to each chart’s own eligible listening pool, so comparing `rank` does not mean comparing equal-sized audiences. The overlap analysis asks which exact credits appear in both a country Top 10 and the Global Top 10; this is an exploratory indicator, not a complete measure of cross-border circulation.

**Dataset to audit/compare:** Artıktay’s 2026 Zenodo release, *National music charts on YouTube and Spotify, 43 countries, May 2018 to October 2026*, DOI [10.5281/zenodo.23645386](https://doi.org/10.5281/zenodo.23645386). It provides weekly YouTube Top 100 data and sampled Spotify Top 200 data, with country-market labels and documented derivations. It is useful because it makes platform and country-chart comparison possible and exposes the construction choices that need auditing.

**Plan:** (1) inspect its data dictionary and provenance; (2) see whether it contains the October 15, 2026 Spotify snapshot for all four selected markets; if not, use the nearest shared date and record the change; (3) match tracks using Spotify track IDs where available, falling back to carefully reviewed title/artist matches; (4) compare market-to-global overlap and positions; (5) compare Spotify with YouTube only as two platform-specific chart systems, not as equivalent “streams”; (6) manually verify a small stratified sample of rows against the original platform pages and log mismatches, missing values, duplicate tracks, and unclear artist credits. The source’s every-fourth-week sampling for many Spotify markets may limit exact date matching.

## Computation

[`analyze_sample.py`](analyze_sample.py) uses only Python’s standard library to validate the CSV, count records, summarize chart stream ranges, and calculate exact title/artist overlap with the Global Top 10. Run from this directory with `python3 analyze_sample.py`. The generated [`analysis_summary.md`](analysis_summary.md) is a reproducible first look, not a finished interpretation.

## Reflection and decisions still open

**Working:** the single-week, single-platform design makes the comparison concrete; rank, date, market, and source are explicit; the choice to distinguish country-market categories from cultural identity avoids treating “Asia,” “Africa,” or “North America” as internally uniform.

**Not yet working / limitations:** this is a small convenience sample of chart leaders, not a representative sample of listening. It uses one week, only four Spotify markets, and a third-party mirror for transcription. Stream totals may not be fully comparable across markets; current internet access, paid/ad-supported use, catalog access, chart filtering, and population size may all matter. Top 10 truncation hides lower-ranked circulation. Artist origin and language have intentionally not been guessed.

**Next changes:** verify the transcription against Spotify’s direct downloads; expand to several weeks; include more markets only if the same chart and sampling rules can be followed; and define a transparent method for artist-country/language coding if that question remains central. For cross-platform comparison, keep YouTube in the audit dataset but do not add TikTok/Apple Music until their available metrics and populations can be compared responsibly.

**Feedback requested:** Is “country chart versus global chart” a sufficiently focused question about cultural measurement? Should the next iteration prioritize more weeks or more markets? What is an appropriate, evidence-based way to code an artist’s relationship to a country without reducing identity to birthplace or nationality?

## Scholarly context

- Way, S. F., Garcia-Gathright, J., & Cramer, H. (2020). “Local Trends in Global Music Streaming.” *Proceedings of the International AAAI Conference on Web and Social Media*, 14(1), 705–714. [https://doi.org/10.1609/icwsm.v14i1.7336](https://doi.org/10.1609/icwsm.v14i1.7336). Their large-scale Spotify analysis finds increasing preference for local content from 2014–2019, and shows that language and geographic proximity shape consumption. This supports treating local/global circulation as a question to investigate rather than assuming globalization makes taste uniform. The authors are Spotify researchers, which is also relevant when discussing platform access and institutional perspective.
- Prey, R. (2020). “Locating Power in Platformization: Music Streaming Playlists and Curatorial Power.” *Social Media + Society*, 6(2). [https://doi.org/10.1177/2056305120933291](https://doi.org/10.1177/2056305120933291). Prey explains that Spotify curation mediates music, advertising, and finance markets. This helps frame rankings as platform-produced visibility rather than a transparent window onto taste.
- Liu, A. Y., & Taneja, H. (2025). “Visibility of K-pop in the U.S.: Global Rankings, ‘Audience Mis-aggregation,’ and Mainstream Attention to Niche Genre.” *Convergence*, 31(3), 862–881. [https://doi.org/10.1177/13548565251320755](https://doi.org/10.1177/13548565251320755). Their analysis of Billboard’s Social 50 argues that a global aggregate can misrepresent audiences when it flattens differences in regional audience size and consumption practices. The object is not Spotify, but the measurement problem directly informs this project’s global-chart question.
- Morris, J. W., & Powers, D. (2015). “Control, Curation and Musical Experience in Streaming Music Services.” *Creative Industries Journal*, 8(2), 106–122. [https://doi.org/10.1080/17510694.2015.1090222](https://doi.org/10.1080/17510694.2015.1090222). Morris and Powers show how streaming interfaces and curation shape users’ musical experiences and access. This grounds the decision to study chart presentation as part of the platform’s representation of music.

## References and data provenance

- Spotify for Artists. [Understanding Spotify Charts](https://support.spotify.com/artists/article/understanding-spotify-charts/). Spotify explains weekly chart periods and notes that chart-eligible streams can differ from other Spotify stream figures.
- Artıktay, G. G. (2026). *National music charts on YouTube and Spotify, 43 countries, May 2018 to October 2026: weekly chart positions, home country assignments, validation sample and code* (v1.0.1). Zenodo. [https://doi.org/10.5281/zenodo.23645386](https://doi.org/10.5281/zenodo.23645386). Audit/comparison dataset; not counted above as a peer-reviewed scholarly source.
- The individual chart rows in `initial_chart_sample.csv` cite their corresponding Kworb chart pages. Kworb is a secondary display of chart data; the official Spotify routes are included per row for verification.
