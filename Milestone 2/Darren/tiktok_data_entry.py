import csv
from datetime import date
from pathlib import Path

from rich.console import Console
from rich.table import Table

console = Console()

file_path = Path("data/tiktok_fragments.csv")
file_path.parent.mkdir(exist_ok=True)

HEADER = [
    "item_id",
    "song_title",
    "artist",
    "release_year",
    "chart_peak",
    "chart_weeks",
    "tiktok_sound_name",
    "sound_version",
    "platform_genre",
    "viral_lyrics",
    "song_section",
    "snippet_length_sec",
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


console.print("TikTok Song Fragment Dataset", style="bold cyan")

guide = Table(title="What to enter for each song")
guide.add_column("Field", style="magenta")
guide.add_column("What it records")
guide.add_column("Example", style="green")
guide.add_row("song_title / artist", "The song as released", "Song Name / Artist Name")
guide.add_row("chart_peak / chart_weeks", "Best rank and weeks on the TikTok Billboard Top 50", "7 / 12  (or 'none')")
guide.add_row("tiktok_sound_name", "The sound's name as TikTok shows it", "Song Name (Sped Up)")
guide.add_row("sound_version", "Which version of the song went viral", "sped up")
guide.add_row("platform_genre", "Genre label a platform gives the song (say which platform)", "pop (Apple Music)")
guide.add_row("viral_lyrics", "The lyrics heard in the TikTok sound", "first line ... last line")
guide.add_row("song_section", "Where that part sits in the full song", "bridge")
guide.add_row("original_theme", "What the full song is about (your reading)", "breakup, regret")
guide.add_row("tiktok_use", "How most top videos use the sound", "transition")
guide.add_row("meaning_shift", "Does TikTok use match the original meaning?", "shifted")
console.print(guide)

existing_count = 0
if file_path.exists():
    with open(file_path, "r", encoding="utf-8") as f:
        existing_count = len(list(csv.reader(f))) - 1
console.print(f"\nRecords already saved: [bold]{existing_count}[/bold]")

saved_count = 0

more = "yes"
while more in ("yes", "y"):
    item_id = existing_count + saved_count + 1
    console.print(f"\n[bold cyan]--- Record {item_id} ---[/bold cyan]")

    answer = "no"
    while answer not in ("yes", "y"):

        song_title = input("Song title: ").strip()
        while song_title == "":
            console.print("  Song title can't be empty.", style="red")
            song_title = input("Song title: ").strip()

        artist = input("Artist: ").strip()
        release_year = input("Release year: ").strip()

        console.print("\n[bold]How institutions and platforms organize it[/bold]")
        chart_peak = input("Peak on TikTok Billboard Top 50 (number, or 'none'): ").strip()
        chart_weeks = input("Weeks on that chart (number, or 'none'): ").strip()
        tiktok_sound_name = input("TikTok sound name, exactly as shown: ").strip()
        sound_version = ask_choice("Sound version: ", VERSION_CHOICES)
        platform_genre = input("Platform genre label, e.g. 'pop (Apple Music)': ").strip()

        console.print("\n[bold]What actually circulates on TikTok[/bold]")
        viral_lyrics = input("Lyrics in the viral snippet (type 'none' if instrumental): ").strip()
        song_section = ask_choice("Song section: ", SECTION_CHOICES)
        snippet_length_sec = input("Snippet length in seconds: ").strip()

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
        date_accessed = date.today().isoformat()

        record = {
            "item_id": item_id,
            "song_title": song_title,
            "artist": artist,
            "release_year": release_year,
            "chart_peak": chart_peak,
            "chart_weeks": chart_weeks,
            "tiktok_sound_name": tiktok_sound_name,
            "sound_version": sound_version,
            "platform_genre": platform_genre,
            "viral_lyrics": viral_lyrics,
            "song_section": song_section,
            "snippet_length_sec": snippet_length_sec,
            "original_theme": original_theme,
            "tiktok_use": tiktok_use,
            "meaning_shift": meaning_shift,
            "interpretation_note": interpretation_note,
            "evidence_file": evidence_file,
            "date_accessed": date_accessed,
        }

        review = Table(title=f"Record {item_id}")
        review.add_column("Field", style="magenta")
        review.add_column("Value", style="yellow")
        for field in HEADER:
            review.add_row(field, str(record[field]))
        console.print(review)

        answer = input("Is this correct? (yes/no): ").strip().lower()
        if answer not in ("yes", "y"):
            console.print("Okay, let's enter this record again.\n", style="red")

    is_new_file = not file_path.exists()
    with open(file_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if is_new_file:
            writer.writerow(HEADER)
        writer.writerow([record[field] for field in HEADER])

    saved_count = saved_count + 1
    console.print("Saved!", style="green")

    more = input("\nAdd another song? (yes/no): ").strip().lower()

console.print(f"\n[bold green]{saved_count} record(s) saved this session.[/bold green]")
console.print(f"Total records in the file: {existing_count + saved_count}")
console.print(f"File location: {file_path.resolve()}")
