#!/usr/bin/env python3
"""Report manual source-verification progress.

Structural heuristics are not evidence that a place/event is real. This tool keeps
manual review separate from parse/classification checks. Reviews live in
`audit/manual_verification.json` and are keyed by file. A file may only be marked
`reviewed` after every retained numbered entry was checked and bad entries were
removed or corrected.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENTRIES = ROOT / "audit" / "entries.json"
REVIEWS = ROOT / "audit" / "manual_verification.json"


def main() -> None:
    if not ENTRIES.exists():
        raise SystemExit("Run tools/parse_entries.py first")
    entries = json.loads(ENTRIES.read_text(encoding="utf-8"))
    reviews = json.loads(REVIEWS.read_text(encoding="utf-8"))
    by_file = Counter(e["file"] for e in entries)

    print("file                     entries  manual status          reviewed")
    print("-----------------------  -------  ---------------------  ----------")
    reviewed_entries = 0
    for filename in sorted(by_file):
        review = reviews.get(filename, {})
        status = review.get("status", "not-reviewed")
        reviewed = by_file[filename] if status == "reviewed" else 0
        reviewed_entries += reviewed
        date = review.get("reviewed_on", "-")
        print(f"{filename:23}  {by_file[filename]:7}  {status:21}  {date}")

    print("\nManual verification coverage: "
          f"{reviewed_entries}/{len(entries)} entries "
          f"({reviewed_entries / len(entries):.1%})")
    pending = [f for f in sorted(by_file) if reviews.get(f, {}).get("status") != "reviewed"]
    print("Pending files:", ", ".join(pending) if pending else "none")


if __name__ == "__main__":
    main()
