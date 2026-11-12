# Instructor Feedback for Milestone 2

I really like how much more focused and concrete this project has become since Milestone 1. Your question about what happens when fragments of songs circulate through TikTok gives you a strong way to study how platforms can separate music from its original lyrical context. You also developed a clear selection methodology, strong initial documentation, and useful scripts for your data work. 

The distinction between the whole song, the fragment that circulates, and the way TikTok users employ that fragment is a very promising direction. And I think your initial findings already show some very interesting patterns around how fragments are produced but also the variability in what makes a sound go viral.

## Initial Custom Dataset

I appreciate your choice of the historic Top 50 Billboard given its partnership with TikTok, which seems very clever, as well as your work trying to identify song lyrics and which songs were on the top using various sources. I also thought you did a great job in your reflection articulating some of the difficulties in collecting this data, and particularly the absence of a sound page is itself important evidence about platform instability and should remain part of the final project.

To answer one of your questions, I think the TikTok year-end lists are absolutely a helpful comparison but it might be helpful to start recording the list origin, since these lists may represent different populations, periods, and ranking methods. I would suggest recording the list, year, geography, rank, and source in structured columns, which would let you investigate how these different lists circulate on TikTok.

### Unit of Analysis & Evidence

To answer your other question, one row per song works for documenting which fragment circulated, but it becomes more difficult when assigning one `tiktok_use` or `meaning_shift` to many different videos.

You might keep the song fragment dataset as a unique dataset, while adding a smaller video-observation dataset for a subset of songs. Each observation could record:

- Which song or sound it uses.
- The date it was observed.
- Its use category.
- The evidence supporting that classification.
- Whether the example supports or complicates the song-level interpretation.
- Your certainty in the classification

You do not necessarily need to record several videos for all 46 songs. A carefully selected subset could demonstrate how varied uses become condensed into a song-level category. Alternatively, you could retain one row per song but define a consistent procedure, such as examining the first five visible videos for every sound and recording disagreement or uncertainty.

I generally like your choice to use screenshots because you can't access the URLs from the browser. But generally, I'm wondering if you need to dig into more of how do song fragments both become uploaded and what if any economic incentives exist for generating fragments. For instance, a number of song fragments might link to the actual Spotify song, so you might consider also including the existence of that link that in your dataset, but also reflecting on how the act of generating song fragments differs from uploading videos or commenting on TikTok in your final data essay.

### Themes and Categories

The fields `original_theme`, `tiktok_use`, and `meaning_shift` are central interpretive work and I appreciate that you treat them as subjective.

The final documentation could explain how you decided that a use was `aligned`, `shifted`, or `inverted`, with several examples. You might also revise the categories after reviewing all records, especially since `other` became so common. That does not mean the initial coding failed. It suggests that TikTok practices exceeded the categories you began with, which is an important finding about the difficulty of classifying platform culture.

## Computation and Reproducibility

I appreciated that you had clear documentation of all your files. You might consider adding a README file to the evidence folder just to explain the files but that is optional. I think your choice of CLI data entry tool makes sense, along with your analyze dataset script. You might consider for the final submission utilizing a Jupyter notebook to visualize some of the trends you have already started to detail.

I was curious that you noted in your AI statement says Claude corrected release years, chart peaks, evidence paths, and genre-source labels in the CSV. So I'm wondering if you double checked those changes, and also you might consider keeping the original fields and making duplicate ones for AI-correction so that you aren't erasing your initial collected data.

## Auditing the TikTok Billboard Chart

I think your proposal to use the discontinued TikTok Billboard Top 50 is very strong and could potentially expand your use of computational methods as well. In particular, I really like your idea of using archived weekly snapshots of the Billboard page in the Wayback Machine, and please reach out if you have any trouble with the code. I also like the idea of using Billboard articles to verify the data, though you also need to consider how Billboard generates its data ,so you might select one of your songs to do a deep dive into how Billboard calculated metrics for the song, especially considering its partnership with TikTok and how that provided new types of engagement to measure. You might also consider how many of the weekly pages survived and which are missing, as well as how Billboard handled remixes and other types of user-uploaded sounds when calculating popularity. 

## Scholarship

Your scholarship is well selected and clearly connected to the project. I would request that you engage with the scholarship a bit more directly in your final essay so that you can articulate how the readings are informing your choices. You might also take a look at some of our course readings on TikTok, one of our additional material readings Young, Liam Cole. “Film Box Office Charts and the Metadata of Culture.” Transcript Verlag, 2022. [https://doi.org/10.1515/9783839455616-003](https://doi.org/10.1515/9783839455616-003) that explores the history of charts in Hollywood, as well as the work of Nick Seaver who works on music recommendation systems that might be relevant.

## Priorities for the Final Project & Milestone 3

I would suggest focusing next on:

- Clarifying/determining how you want to organize the data and whether what you have created is one or two datasets.
- Once you have decided on the organization, starting to consider how you make visible the origins of the songs, whether they are from the UK or US lists, etc.
- Then working on revising and clarifying your categories. Probably considering how to preserve evidence for the use and meaning-shift interpretations, and potentially revising and documenting the categories that currently fall under `other`.
- Completing the Billboard audit with verification of that data, and consider how you might visualize the shape of this larger dataset.

Overall, this is a strong project with a clear cultural question, substantial original data collection, useful computation, and thoughtful recognition of platform instability. The main opportunity now is to make the path from observed videos to interpretive categories as transparent as the rest of the project.
