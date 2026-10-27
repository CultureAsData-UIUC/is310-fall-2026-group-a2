import csv
from datetime import date
from pathlib import Path

from rich.console import Console
from rich.table import Table

console = Console()

song_list_path = Path("data/song_list.csv")
file_path = Path("data/tiktok_fragments.csv")
excluded_path = Path("data/excluded_songs.csv")

HEADER = [
    "item_id",
    "song_title",
    "artist",
    "release_year",
    "chart_peak",
    "tiktok_sound_name",
    "sound_version",
    "platform_genre",
    "viral_lyrics",
    "song_section",
    "original_theme",
    "tiktok_use",
    "meaning_shift",
    "interpretation_note",
    "evidence_file",
    "date_accessed",
]

SECTION_CHOICES = ["intro", "verse", "pre-chorus", "chorus", "post-chorus", "bridge", "outro", "instrumental", "multiple", "unknown"]
VERSION_CHOICES = ["original", "sped up", "slowed", "remix", "live", "user upload", "other"]
USE_CHOICES = ["dance", "lip-sync", "meme", "storytime", "transition", "aesthetic", "emotional", "other"]
SHIFT_CHOICES = ["aligned", "shifted", "inverted", "unclear"]


def ask_choice(question, choices):
    """Keep asking until the answer is one of the allowed choices."""
    console.print(f"  [dim]Options: {', '.join(choices)}[/dim]")
    answer = input(question).strip().lower()
    while answer not in choices:
        console.print("  Please type one of the options exactly.", style="red")
        answer = input(question).strip().lower()
    return answer


songs = []
with open(song_list_path, "r", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        songs.append(row)

done_ids = []
if file_path.exists():
    with open(file_path, "r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            done_ids.append(row["item_id"])
if excluded_path.exists():
    with open(excluded_path, "r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            done_ids.append(row["item_id"])

console.print("TikTok Song Fragment Dataset", style="bold cyan")

guide = Table(title="What to enter for each song")
guide.add_column("Field", style="magenta")
guide.add_column("What it records")
guide.add_column("Example", style="green")
guide.add_row("tiktok_sound_name", "The sound's name as TikTok shows it", "Song Name (Sped Up)")
guide.add_row("sound_version", "Which version of the song went viral", "sped up")
guide.add_row("platform_genre", "Genre label a platform gives the song (say which platform)", "pop (Apple Music)")
guide.add_row("viral_lyrics", "The lyrics heard in the TikTok sound", "first words ... last words")
guide.add_row("song_section", "Where that part sits in the full song", "bridge")
guide.add_row("original_theme", "What the full song is about (your reading)", "breakup, regret")
guide.add_row("tiktok_use", "How most top videos use the sound", "transition")
guide.add_row("meaning_shift", "Does TikTok use match the original meaning?", "shifted")
console.print(guide)

console.print(f"\nSongs finished or skipped: [bold]{len(done_ids)}[/bold] of {len(songs)}")

saved_count = 0
skipped_count = 0

for song in songs:
    if song["item_id"] in done_ids:
        continue

    item_id = int(song["item_id"])
    console.print(f"\n[bold cyan]--- #{item_id}: {song['song_title']} ({song['artist']}) ---[/bold cyan]")

    action = input("Enter this song now? (yes / skip / quit): ").strip().lower()
    while action not in ("yes", "y", "skip", "quit"):
        console.print("  Please type yes, skip, or quit.", style="red")
        action = input("Enter this song now? (yes / skip / quit): ").strip().lower()

    if action == "quit":
        break

    if action == "skip":
        reason = input("Why are you skipping it? (e.g. no TikTok sound page found): ").strip()
        is_new_file = not excluded_path.exists()
        with open(excluded_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if is_new_file:
                writer.writerow(["item_id", "song_title", "artist", "reason", "date_checked"])
            writer.writerow([item_id, song["song_title"], song["artist"], reason, date.today().isoformat()])
        skipped_count = skipped_count + 1
        console.print("Skipped and recorded in excluded_songs.csv.", style="yellow")
        continue

    answer = "no"
    while answer not in ("yes", "y"):
        release_year = input("Release year: ").strip()

        chart_peak = song["chart_peak"]
        if chart_peak == "":
            chart_peak = input("Peak on TikTok Billboard Top 50 (number, or 'none'): ").strip()

        console.print("\n[bold]How TikTok and platforms organize it[/bold]")
        tiktok_sound_name = input("TikTok sound name, exactly as shown: ").strip()
        sound_version = ask_choice("Sound version: ", VERSION_CHOICES)
        platform_genre = input("Platform genre label, e.g. 'pop (Apple Music)': ").strip()

        console.print("\n[bold]What actually circulates on TikTok[/bold]")
        viral_lyrics = input("Lyrics in the viral snippet (type 'none' if instrumental): ").strip()
        song_section = ask_choice("Song section: ", SECTION_CHOICES)

        console.print("\n[bold]Your interpretation[/bold]")
        original_theme = input("Theme of the full song: ").strip()
        tiktok_use = ask_choice("Main TikTok use: ", USE_CHOICES)
        meaning_shift = ask_choice("Meaning shift: ", SHIFT_CHOICES)
        interpretation_note = input("Why did you decide this? (1-2 sentences): ").strip()

        console.print("\n[bold]Evidence[/bold]")
        default_evidence = f"evidence/{item_id:03d}.png"
        evidence_file = input(f"Evidence file name (press Enter for {default_evidence}): ").strip()
        if evidence_file == "":
            evidence_file = default_evidence

        record = {
            "item_id": item_id,
            "song_title": song["song_title"],
            "artist": song["artist"],
            "release_year": release_year,
            "chart_peak": chart_peak,
            "tiktok_sound_name": tiktok_sound_name,
            "sound_version": sound_version,
            "platform_genre": platform_genre,
            "viral_lyrics": viral_lyrics,
            "song_section": song_section,
            "original_theme": original_theme,
            "tiktok_use": tiktok_use,
            "meaning_shift": meaning_shift,
            "interpretation_note": interpretation_note,
            "evidence_file": evidence_file,
            "date_accessed": date.today().isoformat(),
        }

        review = Table(title=f"Record #{item_id}")
        review.add_column("Field", style="magenta")
        review.add_column("Value", style="yellow")
        for field in HEADER:
            review.add_row(field, str(record[field]))
        console.print(review)

        answer = input("Is this correct? (yes/no): ").strip().lower()
        while answer not in ("yes", "y", "no", "n"):
            console.print("  Please type yes or no.", style="red")
            answer = input("Is this correct? (yes/no): ").strip().lower()
        if answer in ("no", "n"):
            console.print("Okay, let's enter this song again.\n", style="red")

    is_new_file = not file_path.exists()
    with open(file_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if is_new_file:
            writer.writerow(HEADER)
        writer.writerow([record[field] for field in HEADER])

    saved_count = saved_count + 1
    console.print("Saved!", style="green")

console.print(f"\n[bold green]{saved_count} song(s) saved and {skipped_count} skipped this session.[/bold green]")
console.print(f"Songs finished or skipped in total: {len(done_ids) + saved_count + skipped_count} of {len(songs)}")
console.print(f"File location: {file_path.resolve()}")
