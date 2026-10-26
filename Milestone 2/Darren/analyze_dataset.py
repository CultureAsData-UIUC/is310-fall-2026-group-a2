import csv
from collections import Counter
from pathlib import Path

from rich.console import Console
from rich.table import Table

console = Console()

file_path = Path("data/tiktok_fragments.csv")

if not file_path.exists():
    console.print(f"No dataset found at {file_path}. Run tiktok_data_entry.py first.", style="red")
    raise SystemExit

with open(file_path, "r", encoding="utf-8") as f:
    records = list(csv.DictReader(f))

console.print(f"[bold cyan]TikTok Song Fragment Dataset[/bold cyan]: {len(records)} records\n")


def show_counts(field, title):
    """Print how many records have each value of one field."""
    counts = Counter(record[field] for record in records)
    table = Table(title=title)
    table.add_column(field, style="magenta")
    table.add_column("Count", justify="right")
    table.add_column("Share", justify="right")
    for value, count in counts.most_common():
        table.add_row(value, str(count), f"{count / len(records):.0%}")
    console.print(table)


show_counts("song_section", "Which section of the song circulates")

show_counts("sound_version", "Which version of the song circulates")

show_counts("tiktok_use", "How the sound is used on TikTok")
show_counts("meaning_shift", "Does the TikTok use match the song's meaning?")

sections = sorted(set(record["song_section"] for record in records))
shifts = ["aligned", "shifted", "inverted", "unclear"]
cross = Table(title="Song section x meaning shift")
cross.add_column("song_section", style="magenta")
for shift in shifts:
    cross.add_column(shift, justify="right")
for section in sections:
    row = [section]
    for shift in shifts:
        n = sum(1 for r in records if r["song_section"] == section and r["meaning_shift"] == shift)
        row.append(str(n))
    cross.add_row(*row)
console.print(cross)

renamed = [r for r in records if r["song_title"].lower() not in r["tiktok_sound_name"].lower()]
console.print(
    f"\nSound name does not contain the song title: [bold]{len(renamed)}[/bold] of {len(records)} records"
)
for r in renamed:
    console.print(f"  #{r['item_id']} {r['song_title']}  ->  TikTok sound: '{r['tiktok_sound_name']}'")

not_charted = [r for r in records if r["chart_peak"].lower() in ("none", "")]
console.print(f"\nNot on the TikTok Billboard Top 50: [bold]{len(not_charted)}[/bold] of {len(records)} records")

missing = Table(title="Missing values check (empty or 'unknown')")
missing.add_column("Field", style="magenta")
missing.add_column("Missing", justify="right")
for field in records[0].keys():
    n = sum(1 for r in records if r[field].strip().lower() in ("", "unknown"))
    if n > 0:
        missing.add_row(field, str(n))
if missing.row_count > 0:
    console.print(missing)
else:
    console.print("\nNo empty or 'unknown' values.", style="green")

no_evidence = [r for r in records if not Path(r["evidence_file"]).exists()]
console.print(f"\nRecords whose evidence file is not in the folder yet: [bold]{len(no_evidence)}[/bold]")
for r in no_evidence:
    console.print(f"  #{r['item_id']} {r['song_title']}: {r['evidence_file']}")
