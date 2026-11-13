# Instructor Feedback for Milestone 2

I really like how substantially you narrowed this project after Milestone 1. Focusing on one Spotify chart week across four country markets and the Global chart gives you a much clearer object of study than trying to compare Spotify, YouTube, TikTok, and Apple Music all at once.

Your revised question is strong because it asks not simply which songs are popular, but how Spotify constructs “local” and “global” popularity through separate ranked markets. I especially appreciate your recognition that these are platform-defined markets rather than natural cultural regions, and that neither rank nor stream count provides a neutral measurement of audience size. Country charts versus the Global chart is therefore a sufficiently focused question about cultural measurement. The care you take not to treat either chart as a complete or neutral account of taste is one of the strongest parts of the project.

## Initial Custom Dataset

I think your current initial dataset is strong, and defining one row as one chart position is a sensible choice. It allows the same track to appear separately in a country chart and the Global chart without treating those appearances as duplicate records. Your stable IDs and consistent ten-row sample also make the dataset straightforward to validate.

I would recommend prioritizing additional weeks over additional markets for the next stage. One week gives you a useful snapshot, but it cannot show whether the observed overlap is typical or produced by a temporary release cycle. Following the same four markets across several shared weeks would let you investigate persistence, change, and movement into or out of the Global chart without making the project geographically unmanageable. You could add another market later if the existing comparison reveals a specific reason to do so, but expanding both weeks and markets at once may make it harder to explain what produced a pattern.

The current `macro_region` field may not be doing much analytical work. Since you correctly explain that Brazil does not represent South America, Nigeria does not represent Africa, and South Korea does not represent East Asia, assigning each market a continental category could inadvertently restore the regional generalizations you are trying to avoid. You might remove that field unless you develop a specific reason to use it.

Your current overlap results are potentially interesting:

- Five of the U.S. Top 10 entries also appear in the Global Top 10.
- None of the exact South Korean, Nigerian, or Brazilian Top 10 credits appear in the Global Top 10.
- The same rank represents substantially different stream totals across markets.

These findings support your question about what becomes visible through a Global chart. However, the Global chart is not independent from the country charts: streams from those markets contribute to its totals, but markets with different numbers of Spotify users cannot contribute equally. The result therefore does not necessarily show that music from one market is culturally less important. It shows how Spotify’s aggregate ranking distributes visibility under unequal market conditions.

The zero-overlap findings should also be manually checked. Exact title-and-artist matching can miss the same recording when featured artists, punctuation, transliteration, or version labels differ. Spotify track IDs would provide a more stable match than text alone if you decide to use them.

Your reflection already identifies the central limits of the current evidence: one week, Top 10 truncation, unequal market conditions, and reliance on a third-party mirror. Continue treating those limits as findings about what these charts can measure rather than simply as weaknesses to eliminate in the dataset.

### Provenance and Preservation

I appreciate that you clearly identify Kworb as the immediate source rather than describing the records as a direct Spotify API collection. That transparency is important.

The current Kworb URLs display the latest weekly chart and change over time. A future reader following the U.S. source URL will not necessarily see the October 15 chart you transcribed. For the final project, I would suggest preserving the exact source material through downloaded chart files, archived pages, dated screenshots, or another stable snapshot. The dated Spotify chart route is more specific, but you should also record whether it remained publicly accessible and downloadable.

As you verify the records, consider adding fields such as:

- `verification_source`
- `verification_date`
- `verification_status`
- `reported_streams_kworb`
- `reported_streams_spotify`
- `discrepancy_note`

This would turn differences between the mirror and Spotify into audit evidence rather than silently replacing one value with another.

## Audit Dataset Plan

Your independent 50-row transcription provides a useful validation sample for the much larger Zenodo dataset. However, the two datasets currently represent almost the same kind of chart information. For the final project, make sure the custom dataset contributes something beyond being a smaller copy of the existing dataset.

One possibility is the evidence-based artist relationship or language coding you mention. I would avoid assigning one nationality based only on birthplace, names, or Wikidata. Instead, you might record several kinds of relationships separately, such as birthplace, residence, professional market, language, or self-identification, along with the source supporting each claim. You do not need to resolve an artist into one “true” country.

You could also keep the custom work focused on chart comparison itself by manually documenting discrepancies, alternate credits, versions, and ambiguous matches. That interpretive validation could become the custom contribution without requiring you to classify every artist’s identity.

I think the Artıktay dataset is a promising audit target because it includes charts at a scale you could not reasonably collect yourself. Its every-fourth-week Spotify sampling also creates a concrete methodological limitation to investigate.

I would encourage you to audit more than whether its rankings match your sample. The Zenodo documentation explains that artist home countries were derived through Wikidata, overrides, and a validation process. It also notes that AI-assisted code and agents contributed to parts of the workflow. This creates several strong audit questions:

- What does the dataset mean by an artist’s “home country”?
- How are collaborations involving artists from different countries handled?
- What happens when Wikidata is missing, contradictory, or overly reductive?
- Which records were manually overridden, and why?
- How was the validation sample selected and reviewed?
- Does every-fourth-week sampling change conclusions about brief chart appearances?
- How much of the AI-assisted workflow can you assess, and how might those tools have shaped the resulting data?

These questions connect directly to your concern about how cultural identity becomes compressed into platform and database categories.

Overall, your computation seems relevant and reproducible. I particularly appreciated the note warning that exact string matching is not identity resolution. For the next stage, you might focus your computational work on matching with Spotify track IDs and producing a mismatch report for manual review. You might also add a field recording the match method and confidence rather than treating every match as equally certain.

## Scholarship

The scholarship you cite is particularly strong and all seem relevant. Way, Garcia-Gathright, and Cramer provide a direct foundation for local music consumption; Prey and Morris and Powers help frame charts as platform curation; Liu and Taneja give you language for explaining audience mis-aggregation.

Continue using these works to interpret the chart structure. For example, the lack of local-to-global overlap could be discussed as a measurement problem rather than evidence that one country’s listeners have more globally relevant taste. You might also bring in some of our course readings, including this one from additional materials that explores the histories of charts in the context of Hollywood films: Young, Liam Cole. “Film Box Office Charts and the Metadata of Culture.” Transcript Verlag, 2022. [https://doi.org/10.1515/9783839455616-003](https://doi.org/10.1515/9783839455616-003).

## Priorities for the Final Project

- Preserve and verify evidence for the chart week already collected.
- Expand the same four markets across several shared weeks before adding more markets.
- Match records with Spotify track IDs where possible and document alternate credits, versions, uncertain matches, and discrepancies.
- Audit the Zenodo dataset's provenance, sampling schedule, validation process, AI-assisted workflow, and artist-country assignments.
- Make the custom contribution visible through manual verification and discrepancy documentation rather than simply reproducing chart rows.
- Add artist-country or language fields only if they remain necessary, and preserve multiple relationships, sources, and uncertainty rather than assigning one definitive identity.
- Clarify your use or non-use of AI in the final documentation and data essay.

Overall, this is a strong and carefully framed project. You have moved from a very broad comparison of platforms and regions to a feasible investigation of how Spotify constructs local and global visibility. Your reflection shows that you already understand many of the project's most important interpretive limits. The next step is to turn provenance, sampling, and matching uncertainty into audit evidence, while using several weeks to determine whether the patterns in this first snapshot persist.
