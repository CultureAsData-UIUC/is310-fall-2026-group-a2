# TikTok Song Fragments

**Author:** Darren Jin

## 1. Custom Dataset

`data/tiktok_fragments.csv` records 50 songs and the fragment of each that circulated on TikTok. Each row is one song.

- 46 of 50 songs recorded. The other 4 were skipped because no TikTok sound page could be found. Excluded songs are in `data/excluded_songs.csv`.
- (1) All 35 songs that reached No. 1 on the TikTok Billboard Top 50 (September 2023 to March 2025). (2) 15 songs that TikTok named in its own year-end lists (2023 to 2025) but that never reached No. 1 on Billboard's chart. Full list and sources: `songs_to_collect.md`.
- Songs whose TikTok sound page could not be found, was removed, or was region-locked. Skipped songs and the reason for each are recorded in `data/excluded_songs.csv`.
- The No. 1 list comes from Wikipedia, a secondary source, and will be verified against archived Billboard chart pages.

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

- `tiktok_data_entry.py`: Python command-line interface (Rich) that reads the 50-song list from `data/song_list.csv`, fills in each song's title, artist, and chart peak, limits category fields to fixed options, and saves each record to the CSV only after I confirm it. Skipped songs are logged with a reason.
- `analyze_dataset.py`: Counts records by section, version, use, and meaning shift, compares song section with meaning shift, lists TikTok sound names that differ from the song title, and checks for missing values and evidence files.

### Early patterns (46 records)

- **The viral fragment is not usually the chorus.** Only 16 of 46 fragments come from the chorus; 15 come from the intro, 13 from a verse, and 2 from an instrumental section.
- **Chorus fragments keep their meaning more often than intros.** Half of the chorus fragments (8 of 16) are used in line with the song's meaning, compared with only 3 of 15 intro fragments.
- **Older songs shift meaning more often.** Of the 15 songs released before 2020, 6 are used in unrelated situations (`shifted`), compared with 8 of the 31 newer songs.
- **Meaning shifts are common but rarely reversed.** 18 songs are `aligned`, 14 `shifted`, 12 `unclear`, and only 2 ("Disco" and "Beautiful Things") `inverted`.
- **`other` is the most common use** (14 of 46), ahead of dance (12) and meme (11). My use categories do not yet capture many of the ways sounds are used.
- **TikTok renames some sounds.** Four sound names differ from the released title, including the censored "MR. TAKE YA B*TCH" and "Like a Prayer" without "(Choir Version)."
- **Most sounds are the original recording** (41 of 46); 5 circulate as remixes.
- **The chart outlasts the platform.** Four songs, including No. 1 song "Alibi," no longer had a findable TikTok sound page when I checked.

### How to use this dataset

Open `data/tiktok_fragments.csv` in any spreadsheet program or with Python's `csv` module. Fields marked "my interpretation" reflect my own reading of each song and its TikTok use, and should not be treated as objective labels. Screenshots for each record are in `evidence/`, named by `item_id`. To add records or reproduce the summary above, run these commands from this folder:

```bash
pip install -r requirements.txt
python tiktok_data_entry.py
python analyze_dataset.py
```

## 4. Audit and Connection Plan

**Audit target:** The TikTok Billboard Top 50, a weekly U.S. chart "based on creations, video views and user engagement" (Billboard). Billboard discontinued it in March 2025 when its partnership with TikTok ended, so its weekly charts now survive mainly in archives such as the Wayback Machine.

**What I will investigate:**
1. Collect archived weekly chart pages from the Wayback Machine with Python and verify entries against Billboard articles.
2. Whether the chart merges sped-up versions and user uploads into the original song.
3. How Billboard's chart and TikTok's own year-end lists rank the same period differently.

**Connection:** The chart counts whole songs; my dataset records the fragments that actually circulate. Joining them on `song_title` and `artist` shows which fragments, versions, and uses the ranking leaves out.

## 5. Reflection

So far, the CLI has made my data collection more consistent. It fills in each song's title, artist, and chart peak from my song list and limits the category fields to fixed options, so I can focus on what I see on TikTok instead of retyping the same information. Saving a screenshot for each song also gives me a fixed record, even if the sound page changes later. Using all 35 No. 1 songs as the core of the dataset gave me a selection rule that does not depend on my own taste.

Some parts of the process have been harder than I expected. TikTok's website has no way to search for sounds directly, so I had to use the mobile app to find each sound page. Choosing a single `tiktok_use` value was difficult when the top videos used a sound in different ways, which is why 12 songs ended up as `unclear` and 14 used `other`. Because the TikTok Billboard Top 50 was discontinued in March 2025, I also have to rely on Wikipedia and archived pages for chart information. My TikTok feed is personalized and U.S.-based, so the top videos I see may not match what other users see.

I do not think the project needs to change direction, but some fields may change. As I continue, I may add a field for censored or renamed sound titles, since TikTok changed the names of four songs. I may also split `meaning_shift` into more specific categories and add more `tiktok_use` options, since `other` became the most common value.

I would like feedback on two questions. First, is one row per song the right unit, or should I record several videos for each song? Second, are the 15 songs from TikTok's year-end lists a fair comparison set, given that most of those lists cover the UK or the world rather than the U.S.?

## 6. Scholarly Sources

- **Liu, A. Y., and H. Taneja (2025)**, "Visibility of K-pop in the U.S.: Global Rankings, 'Audience Mis-aggregation,' and Mainstream Attention to Niche Genre," *Convergence* 31 (3): 862–881, https://doi.org/10.1177/13548565251320755. Shows that Billboard charts flatten engagement into one ranking. This frames my audit of what the TikTok chart erases.
- **Sadler, Olivia (2022)**, "Defiant Amplification or Decontextualized Commercialization? Protest Music, TikTok, and Social Movements," *Social Media + Society* 8 (2), https://doi.org/10.1177/20563051221094769. Shows a song's meaning fading as it spreads on TikTok. My `tiktok_use` and `meaning_shift` fields adapt her categories.
- **Van Venrooij, Alex, Diana L. Miller, and Vaughn Schmutz (2022)**, "Race and Genre Ambiguity in the Critical Reception of Popular Music," *Sociological Inquiry*, https://doi.org/10.1111/soin.12470. Shows genre labels are judgments by gatekeepers, so I record each `platform_genre` with its source.
