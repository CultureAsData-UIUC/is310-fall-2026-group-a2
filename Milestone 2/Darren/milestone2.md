# TikTok Song Fragments

**Author:** Darren Jin

## 1. Custom Dataset

`data/tiktok_fragments.csv` records 50 songs and the fragment of each that circulated on TikTok. Each row is one song.

- **Current size:**  of 50 records. Remaining songs will be collected by November 1.
- **Included:** (1) All 35 songs that reached No. 1 on the TikTok Billboard Top 50 (September 2023 to March 2025). (2) 15 songs that TikTok named in its own year-end lists (2023 to 2025) but that never reached No. 1 on Billboard's chart. Full list and sources: `songs_to_collect.md`.
- **Excluded:** Songs whose TikTok sound page could not be found, was removed, or was region-locked.

### Fields

| Field | Description |
|---|---|
| `item_id` | Record number (automatic) |
| `song_title`, `artist`, `release_year` | Song as released |
| `chart_peak` | Best rank on the TikTok Billboard Top 50, or `none` |
| `tiktok_sound_name` | Sound name as TikTok shows it |
| `sound_version` | `original`, `sped up`, `slowed`, `remix`, `live`, `user upload`, `other` |
| `platform_genre` | Genre label with its platform, e.g. `pop (Apple Music)` |
| `viral_lyrics` | Lyrics heard in the TikTok sound |
| `song_section` | `intro`, `verse`, `pre-chorus`, `chorus`, `post-chorus`, `bridge`, `outro`, `instrumental`, `multiple`, `unknown` |
| `original_theme` | What the full song is about (my interpretation) |
| `tiktok_use` | `dance`, `lip-sync`, `meme`, `storytime`, `transition`, `aesthetic`, `emotional`, `other` (my interpretation) |
| `meaning_shift` | `aligned`, `shifted`, `inverted`, `unclear` (my interpretation) |
| `interpretation_note` | Reason for my interpretation |
| `evidence_file`, `date_accessed` | Screenshot path and date checked |

**`meaning_shift`:** **aligned** = TikTok use matches the song's meaning; **shifted** = same mood, unrelated situation; **inverted** = use contradicts the meaning; **unclear** = top videos vary too much.

## 2. Two Transformations

1. **Cultural material → working representation:** I open each song's TikTok sound page and top videos, save a screenshot to `evidence/`, transcribe the fragment's lyrics, and find where it occurs in the full song using its lyrics on Genius.
2. **Working representation → structured data:** I enter each song with `tiktok_data_entry.py`, assigning the fields and categories above.

## 3. Computational Process

- `tiktok_data_entry.py`: Python command-line interface (Rich) that limits category fields to fixed options and saves each record to the CSV only after I confirm it.
- `analyze_dataset.py`: Counts records by section, version, use, and meaning shift, and checks for missing values and evidence files.

## 4. Audit and Connection Plan

**Audit target:** The TikTok Billboard Top 50, a weekly U.S. chart "based on creations, video views and user engagement" (Billboard). Billboard discontinued it in March 2025 when its partnership with TikTok ended, so its weekly charts now survive mainly in archives such as the Wayback Machine.

**What I will investigate:**
1. Collect archived weekly chart pages from the Wayback Machine with Python and verify entries against Billboard articles.
2. Whether the chart merges sped-up versions and user uploads into the original song.
3. How Billboard's chart and TikTok's own year-end lists rank the same period differently.

**Connection:** The chart counts whole songs; my dataset records the fragments that actually circulate. Joining them on `song_title` and `artist` shows which fragments, versions, and uses the ranking leaves out.

## 5. Reflection

## 6. Scholarly Sources

- **Liu and Taneja (2025)**, "Visibility of K-pop in the U.S.: Global Rankings, Audience Mis-aggregation, and Mainstream Attention to Niche Genre," *Convergence*, https://doi.org/10.1177/13548565251320755. Shows that Billboard charts flatten engagement into one ranking. This frames my audit of what the TikTok chart erases.
- **Sadler, Olivia (2022)**, "Defiant Amplification or Decontextualized Commercialization? Protest Music, TikTok, and Social Movements," *Social Media + Society* 8 (2), https://doi.org/10.1177/20563051221094769. Shows a song's meaning fading as it spreads on TikTok. My `tiktok_use` and `meaning_shift` fields adapt her categories.
- **Van Venrooij, Alex, Diana L. Miller, and Vaughn Schmutz (2022)**, "Race and Genre Ambiguity in the Critical Reception of Popular Music," *Sociological Inquiry*, https://doi.org/10.1111/soin.12470. Shows genre labels are judgments by gatekeepers, so I record each `platform_genre` with its source.
