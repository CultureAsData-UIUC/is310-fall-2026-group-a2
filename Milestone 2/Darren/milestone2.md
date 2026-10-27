# TikTok Song Fragments by Darren Jin

## 1. Custom Dataset
`data/tiktok_fragments.csv` records songs from the TikTok Billboard Top 50 and the fragment of each song that circulated on TikTok. Each row is one song and its viral fragment.

- **Current size:** 0 records. 
- **Included:** Songs on the TikTok Billboard Top 50 (U.S.) between  and , plus a few widely used sounds that never charted (`chart_peak = none`).
- **Excluded:** Songs whose TikTok sound page could not be found, was removed, or was region-locked.

### Fields

| Field | Description |
|---|---|
| `item_id` | Record number (automatic) |
| `song_title`, `artist`, `release_year` | Song as released |
| `chart_peak`, `chart_weeks` | Best rank and weeks on the TikTok Billboard Top 50, or `none` |
| `tiktok_sound_name` | Sound name as TikTok shows it |
| `sound_version` | `original`, `sped up`, `slowed`, `remix`, `live`, `user upload`, `other` |
| `platform_genre` | Genre label with its platform, e.g. `pop (Apple Music)` |
| `viral_lyrics`, `snippet_length_sec` | Lyrics and length of the TikTok sound |
| `song_section` | `intro`, `verse`, `pre-chorus`, `chorus`, `post-chorus`, `bridge`, `outro`, `instrumental`, `multiple`, `unknown` |
| `original_theme` | What the full song is about (my interpretation) |
| `tiktok_use` | `dance`, `lip-sync`, `meme`, `storytime`, `transition`, `aesthetic`, `emotional`, `other` (my interpretation) |
| `meaning_shift` | `aligned`, `shifted`, `inverted`, `unclear` (my interpretation) |
| `interpretation_note` | Reason for my interpretation |
| `evidence_file`, `date_accessed` | Screenshot path and date checked |

**`meaning_shift` categories:** **aligned** = TikTok use matches the song's meaning; **shifted** = same mood, unrelated situation; **inverted** = use contradicts the meaning; **unclear** = top videos vary too much.

## 2. Two Transformations

1. **Cultural material → working representation:** I open each song's TikTok sound page and top videos, save a screenshot to `evidence/`, transcribe the fragment's lyrics, and find where it occurs in the full song.
2. **Working representation → structured data:** I enter each song with `tiktok_data_entry.py`, assigning the fields and categories above.

## 3. Computational Process

- `tiktok_data_entry.py`: Python command-line interface (Rich) that limits category fields to fixed options and saves each record to the CSV only after I confirm it.
- `analyze_dataset.py`: Counts records by section, version, use, and meaning shift, and checks for missing values and evidence files.

## 4. Audit and Connection Plan

**Audit target:** The TikTok Billboard Top 50, a weekly U.S. chart launched in September 2023 that ranks songs by TikTok activity.

**What I will investigate:**
1. What the chart counts, and whether sped-up versions and user uploads are merged into the original song.
2. Collect chart entries for my period with Python and verify a sample on billboard.com.
3. Join the chart to my dataset on `song_title` and `artist` to see which fragments, versions, and uses the chart's song-level ranking leaves out.

**Connection:** The chart counts whole songs; my dataset records the fragments that actually circulate. Comparing them shows what the ranking erases.

## 5. Reflection

## 6. Scholarly Sources

- **Liu and Taneja (2025)**, "Visibility of K-pop in the U.S.: Global Rankings, Audience Mis-aggregation, and Mainstream Attention to Niche Genre," *Convergence*, https://doi.org/10.1177/13548565251320755. Shows that Billboard charts flatten engagement into one ranking. This frames my audit of what the TikTok chart erases.
- **Sadler, Olivia (2022)**, "Defiant Amplification or Decontextualized Commercialization? Protest Music, TikTok, and Social Movements," *Social Media + Society* 8 (2), https://doi.org/10.1177/20563051221094769. Shows a song's meaning fading as it spreads on TikTok. My `tiktok_use` and `meaning_shift` fields adapt her categories.
- **Van Venrooij, Alex, Diana L. Miller, and Vaughn Schmutz (2022)**, "Race and Genre Ambiguity in the Critical Reception of Popular Music," *Sociological Inquiry*, https://doi.org/10.1111/soin.12470. Shows genre labels are judgments by gatekeepers, so I record each `platform_genre` with its source.
