# Instructor Feedback for Milestone 2

I really like the focus on collaborations between pop artists and hip-hop or rap artists. Looking at how collaborations are represented through artist credits, versions, releases, and record labels gives you a useful way to study not only the songs themselves but also how the music industry and a platform like MusicBrainz describe collaborative work.

You have also made substantial progress, from data collection to creating a CLI to experimenting with the MusicBrainz API and even documenting your collection decisions, as well as reflecting on missing and conflicting label information. I especially appreciated that you did not silently fill in unavailable label information and instead began recording uncertainty.

The main opportunity now is to make the selection process, unit of analysis, and provenance more precise. The dataset currently contains useful information, but several central fields remain empty or unverified. I would focus on validating and documenting these 57 records rather than adding more songs.

## Initial Custom Dataset

Your stated focus is pop collaborations with hip-hop or rap artists between 2010 and 2025. The current dataset includes 57 songs released between 2010 and 2023 and centers on nine pop artists. That is a reasonable sample, but the documentation does not yet explain how those nine artists or 57 songs were selected.

For the final project, I would suggest clarifying:

- How you decided which artists count as pop artists
- How you decided which collaborators count as hip-hop or rap artists
- Why these nine pop artists were selected
- How you searched for collaborations for each artist
- Whether every qualifying collaboration was included or only selected examples
- Why the stated period ends in 2025 when the current records end in 2023

You do not need to claim that the dataset represents every pop and rap collaboration from this period. Describing it as an intentional sample would be more accurate, but another researcher should be able to understand how you constructed that sample and what it can and cannot represent.

The `Collaborator Genre` column is currently blank for all 57 records. Because genre is what determines whether a collaborator belongs in the dataset, this field is central rather than optional. I would prioritize verifying it and documenting the source and criteria used for each classification. Genre labels are often contested, and MusicBrainz genre information may be incomplete or derived from user-contributed tags. You might therefore record both the source's terminology and your own inclusion decision rather than presenting genre as an unquestionable fact.

### Unit of Analysis and Dataset Structure

At present, one row seems to represent one selected song collaboration, but the inclusion of `Song Version` and `Song/ Release Label` makes the unit somewhat ambiguous. A recording can appear on several releases, and those releases can have different dates, labels, countries, or formats. A remix can also involve a different collaboration from the original recording.

Since your audit question focuses on differing labels across releases, I would suggest choosing one of two approaches:

1. Keep one row per song or recording and state clearly which release supplies the date and label represented in that row.
2. Create a second, smaller release-level dataset for the three to five songs in your audit, with one row for each MusicBrainz release you inspect.

The second option may be especially useful. It would let the 57-row dataset remain a manageable collaboration dataset while the audit dataset demonstrates how one song can lead to several release records with different metadata. You could connect the two through a stable song or recording identifier.

The `Collaboration Credit` field also needs more precise documentation of how its values are assigned. Values such as `Featured`, `Joint`, `Featured (Rihanna)`, and `Featured (Ariana)` mix the type of credit with the identity of the featured artist. Consider separating these into fields such as `credit_type` and `featured_artist`, or define exactly what each current value means and from whose perspective it is recorded.

Several other columns are not yet being used:

- `Pop Artist Label` is blank for every row.
- `Collaborator Label` is blank for every row.
- `Notes / Issues` is blank for every row.
- Every `Verification Status` value is currently `Needs Review`.

You might either complete these fields or remove those that no longer serve the research question. Empty columns can be useful during collection, but the final documentation should distinguish planned fields from completed evidence. Though also realize you might be still in the middle of data collection, so mostly just flagging for you to consider moving forward!

## Provenance and Validation

The largest documentation gap is record-level provenance. The README explains that you used MusicBrainz, but the CSV does not preserve the MusicBrainz URLs or identifiers associated with each song, recording, artist, release, or label. Without those references, it will be difficult for you or another researcher to verify why a particular date, credit, version, or label appears in the dataset.

I would suggest adding fields such as:

- `musicbrainz_recording_id`
- `musicbrainz_release_id`
- `source_url`
- `date_accessed`
- `verification_status`
- `verification_note`

MusicBrainz distinguishes among artists, recordings, releases, and release groups. Those distinctions are especially relevant to the problems you have already encountered. The final essay should explain which kind of MusicBrainz entity provided each field and why you selected one release when several were available.

Your label data also shows why validation matters. The column currently includes values such as `Republic Records`, `Universal Republic Records`, `Warner Bros. Records`, `Warner Records`, combined labels, a blank value, `Unknown`, and `N/A`. Some of these differences may be historically meaningful rather than simple inconsistencies. Instead of immediately standardizing them, preserve the source value and consider adding a separate cleaned value only when you can document the reason for the change.

## Computational Work

The CLI is a useful way to explore the dataset by artist, collaboration credit, label, and version. It also makes the structure of the CSV visible to a user. For the final submission, I would suggest adding a short description of what each menu option helps a researcher investigate rather than presenting the interface only as an alternative way to view the spreadsheet.

The MusicBrainz script is a helpful start, but it currently searches for Ariana Grande and retrieves genres for that one artist. It does not yet validate the 57 collaboration records or collect the release and label evidence described in the audit plan. I would frame it as an initial API experiment and then extend it for the smaller audit sample. For example, the script might retrieve all releases associated with three to five selected recordings and save their release IDs, dates, countries, and label information to a CSV. That output could make the platform's metadata structure and missingness directly inspectable.

I also appreciate the AI log's discussion of debugging and character encoding. The `Appétit` problem is relevant evidence about how cultural text can be altered when CSV encodings are handled incorrectly. You might briefly discuss that issue in your process reflection and record which encoding users should use when opening the data.

## Auditing MusicBrainz

MusicBrainz is a strong audit target because it is both the source you used and a structured, collaboratively maintained representation of music. Your proposed close examination of three to five songs would provide useful depth, but I would not make those examples the full audit.

Instead, I suggest first using the MusicBrainz API to audit metadata coverage across all 57 collaboration records. For each song, you could record whether a confident recording match was found, how many releases are associated with it, how often label and genre information is available, whether credits differ across releases, and whether MusicBrainz agrees with your custom dataset. This would give the audit a systematic scale without requiring you to collect more songs.

You could then select three to five especially complicated cases for a closer release-level analysis. These cases could help explain why labels, dates, versions, or artist credits differ and what those differences reveal about MusicBrainz’s underlying data model and community editing practices.

Rather than deciding which single label is the correct one for a song, you might show that the answer depends on which release is being represented. That would turn the inconsistency you encountered into one of the project's central findings: music metadata is organized around different cultural objects, and collapsing releases into a single song row can hide those distinctions.

## Scholarship and Interpretation

You include three relevant scholarly sources and explain their relationship to the project. Barrett's discussion of collaboration in music composition is interesting, but its focus on composer-teacher and student-composer relationships is further from your dataset's focus on commercially released popular music. You can still use it if you explain how it helps you distinguish creative collaboration from the narrower forms of collaboration visible in release metadata. Otherwise, you might look for scholarship on featured artists, remix culture, genre crossover, music metadata, or the political economy of record labels.

I would also be careful about treating a featured credit as a complete account of creative collaboration. MusicBrainz can document credited performers and releases, but it may not show every producer, songwriter, sample, contractual relationship, or uncredited contribution. This distinction could become part of your argument about what platform metadata makes visible and what it leaves out.

## Priorities for the Final Project

I would suggest focusing next on:

- Explaining how the nine pop artists and 57 songs were selected.
- Verifying and documenting the genre classifications that define inclusion in the dataset.
- Clarifying whether one row represents a song, recording, version, or selected release.
- Adding MusicBrainz identifiers, source URLs, and access or verification information.
- Defining the collaboration-credit categories more consistently. Distinguish credited collaboration from broader creative and industrial relationships.
- Completing or removing the currently empty fields and reviewing the records still marked `Needs Review`.
- Audit MusicBrainz metadata coverage and consistency across all 57 songs, as well as extending the MusicBrainz code to collect or compare the release and label metadata used in that audit.
- Closely analyze three to five complicated release histories. Compare artist credits, labels, genres, dates, countries, and versions across releases.
- Using the final essay to distinguish credited collaboration from the broader creative and industrial relationships behind a recording.

Overall, this is a thoughtful and feasible project with a clear connection between the custom dataset and the proposed audit. You have already identified the most productive problem: the same song does not necessarily have one stable release date or label. The next step is to preserve enough record-level evidence to investigate that complexity rather than resolving it into a single apparently definitive value.
