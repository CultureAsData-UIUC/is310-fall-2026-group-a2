# AI Usage & Research Methodology Log

**Assignment**: Mass Digitization, Digital Libraries, and Data Retirement  
**Course**: IS 310: Culture As Data (Fall 2026)  
**Group**: Group A2  
**Date**: September 8, 2026  

---

## 1. AI Tools Utilized

* **Tool**: Google Antigravity IDE (powered by Google DeepMind / Gemini 3.7 Flash)
* **Purpose**: Collaborative brainstorming, automated querying of public repository metadata, synthesizing literature readings, generating structured comparative markdown tables, and drafting the research report.

---

## 2. Research Methodology & Discovery Trail

In compliance with the assignment instructions, this document records the exact steps, queries, and tools used to locate and verify all archival materials, catalog records, datasets, and literature references:

### A. African American Periodical Poetry Dataset Discovery
* **Tool / Method**: Python API inspection and GitHub raw data fetching via `urllib.request`.
* **Repository Queried**: `https://github.com/melaniewalsh/responsible-datasets-in-context`
* **Data File Located**: `datasets/aa-periodical-poetry/African-American-Periodical-Poetry_1900-1928-Created-by-Amardeep-Singh-and-Kate-Hennessey,-Lehigh-University.csv`
* **Dataset Scope Verified**: 983 total rows across 28 distinct venues, including *The Crisis* (275 poems), *Opportunity* (106 poems), and *Black Opals* (29 poems).
* **Poems Selected**:
  1. Langston Hughes, *"The Negro Speaks of Rivers"* (*The Crisis*, June 1921).
  2. Gwendolyn B. Bennett, *"Heritage"* (*Opportunity*, December 1923).
  3. Lewis Alexander, *"Japanese Hokku Poems"* (*Black Opals*, Christmas 1927).

### B. HathiTrust Catalog & Digital Library Investigation
* **Tool / Method**: Direct catalog search and bibliographic cross-referencing on HathiTrust Digital Library (`catalog.hathitrust.org`).
* **Records Identified**:
  - *The Crisis*: [Catalog Record 101643349](https://catalog.hathitrust.org/Record/101643349) / [Record 000523098](https://catalog.hathitrust.org/Record/000523098) (Full View, University of Michigan / Harvard digital copies). Located Volume 22, Number 2 (June 1921), poem on page 71 (issue page 17).
  - *Opportunity: A Journal of Negro Life*: [Catalog Record 000505963](https://catalog.hathitrust.org/Record/000505963) (Full View for Volume 1, 1923; search-only for later copyrighted volumes). Located Volume 1, Number 12 (December 1923), page 371.
  - *Black Opals*: Searched catalog; identified archival silence. Verified that *Black Opals* (published in Philadelphia, 1927–1928, run of only ~250 copies) was not digitized in HathiTrust full view and survives primarily in the Schomburg Center and Lehigh University’s bespoke digital recovery project.

### C. Assigned Literature Analysis
* **Brewster Kahle (2007)**: *"Universal Access to All Knowledge"*, *The American Archivist* 70(1): 23–31. Analyzed Kahle's Library of Alexandria metaphor, open access imperative, and critique of private corporate library silos.
* **Amardeep Singh & Kate Hennessey (2024)**: *"African American Periodical Poetry (1900-1928) – Responsible Datasets in Context"*. Analyzed the editorial curation of metadata, tagging subjectivity, author recovery, and the tension between material pages and machine-readable rows.
* **Jennifer Ding, Jan Diehm, & Michelle McGhee (2021)**: *"Can Data Die? Tracking the Lenna Image"*, *The Pudding*. Analyzed the history of Lena Forsén's 1972 centerfold, the 50-year normalization of gendered bias in computer vision, subject consent refusal, and institutional de-indexing (including the IEEE April 2024 ban).

### D. Group A2 Topic Investigation: Music, Sound, and Audio Culture
* **Acoustic Digitization**: Researched Nyquist-Shannon sampling rates (44.1kHz vs 96kHz), IRENE 3D optical laser scanning for historic shellac/wax grooved media at the Library of Congress, and Optical Music Recognition (OMR) polyphonic complexity.
* **Oldest & Newest Sound Archives**: Investigated the UCSB Cylinder Audio Archive (1890s wax cylinders) and IMSLP (500,000+ public domain scores) vs. modern AI audio datasets (Google MusiCaps on Hugging Face) and Free Music Archive 2.0 with JSON-LD and MusicBrainz identifiers.
* **Ethics & Refusal in Sound**: Examined the *Amen Break* (Gregory Coleman royalties failure), non-consensual voice cloning (*Heart on My Sleeve*), and Indigenous sacred audio governance under the CARE Principles and Traditional Knowledge (TK) Labels.

---

## 3. Prompts & Interaction Summary

1. **Prompt**: Analyze assignment requirements for "Mass Digitization, Digital Libraries, and Data Retirement" for IS 310, integrating Group A2's semester topic of Music.
2. **Action Taken**: Formulated a comprehensive implementation plan outlining repository structure, hands-on HathiTrust case studies, comparison with the Lenna image, deep exploration of music digital objects, and class presentation synthesis.
3. **Prompt**: Execute the approved implementation plan.
4. **Action Taken**: Created root `README.md`, created `mass-digitization/README.md` with complete answers to all 15 prompts across HathiTrust, Music, and Synthesis, and documented AI workflow.
