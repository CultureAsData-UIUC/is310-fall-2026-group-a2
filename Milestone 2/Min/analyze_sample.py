#!/usr/bin/env python3
"""Validate and summarize Min's initial Spotify chart sample (stdlib only)."""
from collections import defaultdict
from pathlib import Path
import csv

HERE = Path(__file__).resolve().parent
DATA = HERE / "initial_chart_sample.csv"
OUTPUT = HERE / "analysis_summary.md"
REQUIRED = {
    "record_id", "chart_week_end", "platform", "market_code", "market_name",
    "market_scope", "rank", "track_title", "credited_artist", "weekly_streams",
    "source_url", "official_chart_url",
}

with DATA.open(encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    missing = REQUIRED - set(reader.fieldnames or [])
    if missing:
        raise SystemExit(f"Missing required columns: {', '.join(sorted(missing))}")
    records = list(reader)

if not records:
    raise SystemExit("Dataset is empty")
ids = [r["record_id"] for r in records]
if len(ids) != len(set(ids)):
    raise SystemExit("Duplicate record_id found")

charts = defaultdict(list)
for r in records:
    charts[r["market_code"]].append(r)
for code, chart in charts.items():
    ranks = [int(r["rank"]) for r in chart]
    if sorted(ranks) != list(range(1, 11)):
        raise SystemExit(f"{code}: expected exactly ranks 1–10; got {sorted(ranks)}")
    if len({r["chart_week_end"] for r in chart}) != 1:
        raise SystemExit(f"{code}: inconsistent chart weeks")

global_chart = charts.get("global", [])
global_keys = {(r["track_title"].strip().casefold(), r["credited_artist"].strip().casefold()) for r in global_chart}
lines = [
    "# Initial chart sample: computational summary", "",
    f"- Records: **{len(records)}**", f"- Chart week ending: **{records[0]['chart_week_end']}**",
    f"- Charts: **{len(charts)}** (four country markets and one global chart)", "",
    "| Chart | Region/group | Records | Weekly stream range shown | Exact credit overlap with Global Top 10 |",
    "|---|---|---:|---:|---:|",
]
for code in sorted(charts):
    chart = charts[code]
    vals = [int(r["weekly_streams"]) for r in chart]
    matched = sum((r["track_title"].strip().casefold(), r["credited_artist"].strip().casefold()) in global_keys for r in chart) if code != "global" else 10
    lines.append(f"| {chart[0]['market_name']} | {chart[0]['macro_region']} | {len(chart)} | {min(vals):,}–{max(vals):,} | {matched}/10 |")
lines += [
    "", "## Interpretation note", "",
    "The overlap count matches normalized title-plus-credited-artist strings exactly. It is an exploratory aid, not an identity-resolution system: alternate spellings, punctuation, featured-artist formatting, or version labels can create false non-matches. Ranks and stream counts belong to separate chart populations and must not be interpreted as directly equivalent audience sizes.",
    ""
]
OUTPUT.write_text("\n".join(lines), encoding="utf-8")
print(f"Wrote {OUTPUT.name}: {len(records)} records across {len(charts)} charts")
