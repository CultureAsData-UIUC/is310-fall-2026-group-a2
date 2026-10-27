import csv
from pathlib import Path

from rich.console import Console
from rich.table import Table

console = Console()

file_path = Path("data/tiktok_fragments.csv")

if not file_path.exists():
    console.print("No dataset found. Run tiktok_data_entry.py first.", style="red")
    exit()

records = []
with open(file_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        records.append(row)

total = len(records)
console.print(f"Total records: {total}\n", style="bold cyan")

category_fields = ["song_section", "sound_version", "tiktok_use", "meaning_shift"]

for field in category_fields:
    counts = {}
    for record in records:
        value = record[field]
        if value in counts:
            counts[value] = counts[value] + 1
        else:
            counts[value] = 1

    table = Table(title=f"Records by {field}")
    table.add_column(field, style="magenta")
    table.add_column("Count", justify="right")
    table.add_column("Percent", justify="right")
    for value in counts:
        percent = round(counts[value] / total * 100)
        table.add_row(value, str(counts[value]), f"{percent}%")
    console.print(table)

shifts = ["aligned", "shifted", "inverted", "unclear"]

sections = []
for record in records:
    if record["song_section"] not in sections:
        sections.append(record["song_section"])

cross = Table(title="Song section vs. meaning shift")
cross.add_column("song_section", style="magenta")
for shift in shifts:
    cross.add_column(shift, justify="right")

for section in sections:
    row = [section]
    for shift in shifts:
        count = 0
        for record in records:
            if record["song_section"] == section and record["meaning_shift"] == shift:
                count = count + 1
        row.append(str(count))
    cross.add_row(*row)
console.print(cross)

console.print("\nTikTok sound names that do not include the song title:", style="bold")
renamed_count = 0
for record in records:
    if record["song_title"].lower() not in record["tiktok_sound_name"].lower():
        renamed_count = renamed_count + 1
        console.print(f"  #{record['item_id']} {record['song_title']} -> '{record['tiktok_sound_name']}'")
console.print(f"Total: {renamed_count} of {total}")

not_charted = 0
for record in records:
    if record["chart_peak"].lower() == "none":
        not_charted = not_charted + 1
console.print(f"\nNot on the TikTok Billboard Top 50: {not_charted} of {total}", style="bold")

console.print("\nMissing values (empty or 'unknown'):", style="bold")
missing_found = False
for field in records[0]:
    missing = 0
    for record in records:
        if record[field].strip().lower() in ("", "unknown"):
            missing = missing + 1
    if missing > 0:
        console.print(f"  {field}: {missing}")
        missing_found = True
if not missing_found:
    console.print("  None", style="green")

console.print("\nRecords without an evidence file in the folder:", style="bold")
no_evidence = 0
for record in records:
    if not Path(record["evidence_file"]).exists():
        no_evidence = no_evidence + 1
        console.print(f"  #{record['item_id']} {record['song_title']}: {record['evidence_file']}")
console.print(f"Total: {no_evidence} of {total}")
