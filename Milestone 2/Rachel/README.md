# Music Collaboration Dataset 

## Overview 
Welcome, for my milestone 2 dataset, I explored collaborations between pop artists and artists from either Rap or Hip-hop between 2010 and 2025. 

## Initial Documentation 

For my custom dataset, I wanted to focus on the collaborations between pop artists and artists from other genres-- more specifically Rap and Hip-hop-- between 2010 and 2025. I wanted to explore how these collaborations are represented through artist credits, song versions, and record labels. It contains 57 songs, with information such as the song title, who the artist and collaborating artist are, song versions, collaboration credit, and record labels. 

### Data Collection
Through this, I collected infroamtion about the songs by researching their releases and credits through MusicBrainz. As for the information I gather, I organized them in Microsoft Excel before converting it into a CSV file for my Python program.

I decided to focus on pop artists because I've been listening to their music more recently, which made me interested in exploring their collaborations with artists from other genres, particulary Hip-hop and Rap since I've been fond of those genres as well. I thought this would be an interesting topic to research because collaborations between pop and hip-hop/rap artists seemed common in popular music. I also expected there would be enough songs for a dataset.

While collecting the data, I had to consider what specific information I had to include and how to represent them. For example, some songs have multiple versions (like remixes) while others have different release dates or record labels depending on the release. Thus, I chose to include the song version to distinguish these differences.

Though, while doing so, some releases didn't have the record label on MusicBrainz. Instead of assuming the label, I recorded them as "Unknown" and included notes with explanations regarding each of them.

### Data Transformation
The first transformation involved turning music collaborations into information that could be documented. First, I researched songs and their release dates, then selected details that I found relevant to this dataset which were artist names, collaboration credits and song versions.

The second transformation involved organizing the information into a structured dataset. I created different columns in Microsoft Excel to do so. That way iy would be easy for me to look back at all my data if I wanted a full view of it instead of it being straight into code. Converting it into CSV file allows my Python program to read and display the information for the users.

The transformations required me to make decisions about what information to include and how to categorize them. An example of this could be distinguishing original songs from remixes to give users the information that they may need, otherwise they could have been overlooked. 

### Limitations 
One limiatationg is that my dataset doesn't include all the pop artists and artists from other genres during 2010-2025. Some information on MusicBrainz was incomplete or difficult to interpret, especially when it came to record labels. My dataet is still in progress so I plan on reviewing the information for accuracy. Along with that, some songs had different record labels when it came to international releases. Though I mainly focused on English-language or US based collaborations, the same song could have multiple releases with different label information. Due to this, my dataset may not accurately represent every label associated with a song.

### Dataset Columns

| Column | Description |
|---|---|
| ID | Unique identifier for each entry |
| Song Title | Title of the collaboration |
| Release Year | Year recorded for the selected song |
| Pop Artist | Pop artist involved in the collaboration |
| Collaborating Artist | Hip-hop/rap artist involved |
| Collaborator Genre | Genre classification of the collaborating artist |
| Collaboration Credit | How the artists are credited |
| Song Version | Original version, remix, etc. |
| Song/ Release Label | Record label listed for the selected release |
| Notes | Additional information or uncertainties |
| Pop Artist Label | Label information for the pop artist, if collected |
| Collaborator Label | Label information for the collaborating artist, if collected |
| Verification Status | Whether the entry has been reviewed |
| Notes / Issues | Outstanding questions or problems |

## Audit and Connection Plan 
For the second half of my project, I plan to audit MusicBrainz, which is the database I've been using to research information on music collaborations. While collecting songs for my dataset, I noticed that some songs had multiple releases with different record labels, release dates, or missing information. This made me interested in how MusicBrainz organize and represent music collaborations.

For my audit, I want to focus on how MusicBrainz organizes record label information through different releases of the same song. I want to look more closely at a small selection of songs from my dataset and compare their release information to understand why the labels may differ or be missing. I plan to select around 3–5 songs from my dataset and compare their different releases on MusicBrainz, focusing on record labels and missing information.

This will help me understand how MusicBrainz represents music information and how those differences can affect the information I include in my own dataset.

.

## Computational Process 
For the computational part of my project, I turned my Excel sheet into a CSV file and created a Python CLI to allow users to explore my music collaboration dataset. This allows the users to interact with the program and explore the infromation in different ways instead of looking through the spread sheet itself. Along with that, the program provides 5 different options: viewing all collaborations, searching for collaborations by artist, exploring collaboration credits, exploring record labels, and exploring song versions.

If users were ever interested in a specific artists' collaborations with others, they can just type in their name or see the record labels the artists' songs are affiliated with.

Through the use of CLI, it helped me understand how it sould be used to make cultural information easier to search and compare.



To interact with my program, make sure `music_cli.py` and
`music_collaborations.csv` are saved in the same folder.

Open the terminal in that folder and run:

```bash
python3 music_cli.py
```

The program will display a menu with different options.
Enter the number corresponding to the option you want to explore.

## Scholarly Sources 
Coddington, Amy. How Hip Hop Became Hit Pop : Radio, Rap, and Race. University of
          California Press, 2023. EBSCOhost,
          research.ebsco.com/plink/8d17c5c3-08ac-3b06-b341-a1327510f9fe.

    This scholarly source explores how hip-hop became more mainstream through radio stations during the 1980s and early 1990s. They mention how radio stations and music industry influenced hip-hop's popularity and how artists began combining elements of pop and rap to appeal to a wider audience. This connects back to my dataset because I'm focusing on the collaborations between pop and hip-hop/rap artists from 2010 to 2025. Though it focuses on an earlier period, it provides historical context for how the two genres became connected in popular music.

Barrett, Margaret. “‘Creative Collaboration’: An ‘Eminence’ Study of Teaching and
          Learning in Music Composition.” Psychology of Music, vol. 34, no. 2, Apr. 2006,
          pp. 195–218. EBSCOhost, https://doi.org/10.1177/0305735606061852.

    Barret's article explores how music composition can involve collaboration instead of just working alone. Through their research on a somposer-teacher and student-composer, they explain how working together by sharing ideas, problem solving, and supporting one another can be a part of the creative process, This relates tomy dataset because I'm looking into collaborations between pop artists and hip-hop/rap artists. Though they focus on teaching andf learning music composition instead of popular music collaborations, it helps understand how collaborations can involve different creative contribution and how they may not bw fully represented through artist credits.
    
Tyree, Tia C. M., and Christin Smith. “An Analysis of Women Rappers’ Lyrical and
          Video Performances in Hip Hop Collaborations.” Howard Journal of Communications,
          vol. 36, no. 5, Oct. 2025, pp. 572–89. EBSCOhost,
          https://doi.org/10.1080/10646175.2024.2396587.
    Tyree and Smith in "An Analysis of Women Rappers’ Lyrical and Video Performances in Hip Hop Collaborations", examines how women rappers are represented through collaborations with other artists. They analyze song and music videos from 2015 to 2019 and found that while they can provide opportunities, it can also reinforce stereotypes, competition, and objectification. This relates to my dataset on collaborations because between pop and hip-hop/rap artists, including collaborations involving female rappers. Their research helps me understand how music collaborations can have cultural meanings beyond just the artists involved. Along with that, they selected songs using specific criteria which provides as an example for how scholars make decisions when building datasets.


Together, these sources helped me understand the history of pop and hip-hop, the creative process behind music collaborations, and how collaborations can represent different cultural meanings that may not be reflected in my dataset.

# Reflection 
So far, I think my project is going well since I was able to collect 57 songs and organize them. Especially when it came to the Python CLI, I like how users are able to interact with it to explore the collaborations instead of having to look through the spreadsheet itself. 

Though, in the process, it was difficult to find consistent information on record labels on MusicBrainz. Some songs had multiple releases with different labels, while others had missing information. This made it difficult to decide which information to include in my dataset. I would like feedback on whether my approach for recording these labels is alright and whether there are better ways to represent songs with multiple releases. 

For now, I like the direction of my project because I was able to collect enough data and create a working program. Though, I may need to make adjustments to how I organize certain information as I continue reviewing my dataset.