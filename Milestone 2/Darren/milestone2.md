# TikTok Song Fragments: What Charts Count and What Circulates

**Author:** Darren Jin · **Group theme:** How platforms and institutions organize music into genres, rankings, and other categories

**Research question:** What unit do TikTok and Billboard use to count songs, and what parts of a song, and what context, disappear along the way?

The TikTok Billboard Top 50 ranks whole songs, but what circulates on TikTok is usually a 15 to 30 second fragment, often under a different sound name ("Sped Up", "original sound - username") or an altered recording. Each record places three layers side by side:

1. **How institutions and platforms organize the song:** chart rank, sound name, sound version, genre label
2. **What circulates:** the fragment's lyrics, section, and length
3. **My interpretation:** the song's theme, how TikTok uses the fragment, and whether that use matches the original meaning

Dataset

`data/tiktok_fragments.csv`: one row per song and its viral fragment. Current size: TODO. Target: 50 to 60. Evidence screenshots are in `evidence/`, named by `item_id`.

**Selection:** Songs on the TikTok Billboard Top 50 (U.S.) between TODO and TODO, plus a few widely used sounds that never charted (`chart_peak = none`). Excluded: songs with no findable, removed, or region-locked sound page. TODO: other exclusions.

### Fields

| Field | Description | Source |
|---|---|---|
| `item_id`, `date_accessed` | Record number and check date (automatic) | Script |
| `song_title`, `artist`, `release_year` | Song as released | Fact |
| `chart_peak`, `chart_weeks` | Best rank and weeks on the TikTok Billboard Top 50, or `none` | Fact |
| `tiktok_sound_name` | Sound name exactly as TikTok shows it | Transcribed |
| `sound_version` | `original`, `sped up`, `slowed`, `remix`, `live`, `user upload`, `other` | Judgment |
| `platform_genre` | Genre label with its platform, e.g. `pop (Apple Music)` | Fact |
| `viral_lyrics`, `snippet_length_sec` | Lyrics and length of the TikTok sound | Transcribed |
| `song_section` | `intro`, `verse`, `pre-chorus`, `chorus`, `post-chorus`, `bridge`, `outro`, `instrumental`, `multiple`, `unknown` | Judgment |
| `original_theme` | What the full song is about | **Interpretation** |
| `tiktok_use` | `dance`, `lip-sync`, `meme`, `storytime`, `transition`, `aesthetic`, `emotional`, `other` | **Interpretation** |
| `meaning_shift` | `aligned`, `shifted`, `inverted`, `unclear` (defined below) | **Interpretation** |
| `interpretation_note` | Why I decided the above | **Interpretation** |
| `evidence_file` | Screenshot path | Me |

**Category definitions**
- `meaning_shift`: **aligned** matches the song's meaning; **shifted** keeps the mood in an unrelated situation; **inverted** contradicts it (e.g. a grief song used for comedy); **unclear** means top videos vary too much.
- `tiktok_use` adapts Sadler's (2022) categories (lip-sync, dance, trend, meme). I added others because TODO.
- `song_section` follows the structure on TODO (Genius / official lyrics). Fragments crossing sections are `multiple`.

## 3. Two transformations

**1. Cultural material → working representation:** I record the song's chart peak and weeks, open its TikTok sound page and top TODO videos, save a screenshot (URLs change often), transcribe the fragment, and locate it in the full song. *Lost:* TODO (e.g. my feed is personalized and U.S.-based; a screenshot captures one moment).

**2. Working representation → structured data:** I enter each song with `tiktok_data_entry.py`, which limits category fields to fixed options and saves a record only after I confirm it. *Lost:* TODO (e.g. a varied trend becomes one `tiktok_use` value).

## 4. Computational process

- `tiktok_data_entry.py`: Rich command-line interface that appends confirmed records to the CSV
- `analyze_dataset.py`: counts by section, version, use, and meaning shift; section × shift table; renamed sounds; missing values and evidence files

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python tiktok_data_entry.py
python analyze_dataset.py
```

**Early patterns:** TODO (2 to 3 sentences from `analyze_dataset.py`, e.g. is it usually the chorus? how often is the sound sped up?)

## 5. Audit plan: the TikTok Billboard Top 50

Launched in September 2023, this weekly U.S. chart turns TikTok activity into a Billboard-style ranking, an institution organizing a platform's music, which is my group's theme. TODO: quote Billboard's methodology.

**Plan:**
1. Collect weekly entries for my period into a CSV with Python and verify a sample on billboard.com. TODO: check scraping terms; otherwise enter by hand with my CLI.
2. Document what the chart counts and whether sped-up versions and user uploads merge into the original song.
3. Join to my dataset on `song_title` and `artist`: Do altered sounds still chart as the original? Do high-charting songs share fragment sections? Which widely used sounds never chart?

**Connection:** My unit is the fragment; the chart's is the song. Comparing them shows what the ranking flattens. Following Liu and Taneja (2025), the chart presents itself as a neutral measure while constructing what counts.

## 6. Reflection

TODO (in my own words): What is working? What is not? How many records do I have, and my plan and dates to reach 50? What might change? What feedback do I need?

## 7. Scholarly sources

- **Liu and Taneja (2025)**, "Visibility of K-pop in the U.S.: Global Rankings, Audience Mis-aggregation, and Mainstream Attention to Niche Genre," *Convergence*, https://doi.org/10.1177/13548565251320755 (TODO: full names). Billboard's social charts flatten worldwide engagement into one ranking ("audience mis-aggregation"). This frames my audit: a chart position is an artifact of its metric.
- **Sadler, Olivia (2022)**, "Defiant Amplification or Decontextualized Commercialization? Protest Music, TikTok, and Social Movements," *Social Media + Society* 8 (2), https://doi.org/10.1177/20563051221094769. Shows a protest song's meaning fading into lip-syncs and memes. My `tiktok_use` and `meaning_shift` fields adapt her coding to many songs.
- **Van Venrooij, Alex, Diana L. Miller, and Vaughn Schmutz (2022)**, "Race and Genre Ambiguity in the Critical Reception of Popular Music," *Sociological Inquiry*, https://doi.org/10.1111/soin.12470. Genre labels are gatekeepers' judgments, so I record `platform_genre` with its source.
- **Seaver, Nick (2022)**, *Computing Taste*, University of Chicago Press, https://doi.org/10.7208/chicago/9780226822969. TODO: how it explains which fragments TikTok surfaces.
- **DeNora, Tia (2000)**, *Music in Everyday Life*, Cambridge University Press. Music's meaning is built in use, so `meaning_shift` records a change in use, not a "wrong" reading.