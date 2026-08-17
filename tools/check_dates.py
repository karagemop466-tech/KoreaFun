#!/usr/bin/env python3
"""Verify every stated 2026 weekday-plus-date pair, and flag dates that fall
outside the trip window (2026-10-31 .. 2026-11-22)."""
import datetime
import glob
import os
import re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRIP_START = datetime.date(2026, 10, 31)
TRIP_END = datetime.date(2026, 11, 22)

MONTHS = {m: i for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}
DAYS = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}

# e.g. "Sat Nov 7, 2026" / "Sat Nov 7" / "Wed Nov 25, 2026"
D = r"(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)[a-z]*"
M = r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*"
# Ranges such as "Sat-Sun Nov 14-15" pair FIRST weekday with FIRST date, so
# capture the optional trailing "-Dow" and "-DD" and only check the pair.
PAT = re.compile(
    rf"\b({D})(?:\s*[-\u2013]\s*{D})?\.?,?\s+"
    rf"({M})\.?\s+"
    rf"(\d{{1,2}})(?:\s*[-\u2013]\s*\d{{1,2}})?\b(?:,?\s*(\d{{4}}))?")

bad = out = 0
for path in sorted(glob.glob(os.path.join(REPO, "*.md"))
                   + glob.glob(os.path.join(REPO, "*.csv"))):
    for ln, line in enumerate(open(path, encoding="utf-8"), 1):
        prior = re.search(r"\(20\d\d[:\s]", line)
        for dow, mon, day, yr in PAT.findall(line):
            if prior and not yr:
                continue
            year = int(yr) if yr else 2026
            if year != 2026:
                continue
            try:
                d = datetime.date(year, MONTHS[mon[:3]], int(day))
            except ValueError:
                continue
            name = os.path.basename(path)
            if d.weekday() != DAYS[dow[:3]]:
                real = list(DAYS)[d.weekday()]
                print(f"WRONG DAY  {name}:{ln}  '{dow} {mon} {day}' "
                      f"is actually {real}")
                print(f"           {line.strip()[:100]}")
                bad += 1
            elif not (TRIP_START <= d <= TRIP_END) and MONTHS[mon[:3]] in (10, 11, 12):
                print(f"OUT OF TRIP {name}:{ln}  {d} ({dow})")
                out += 1

print(f"\n{bad} wrong weekday, {out} outside trip window")
