#!/usr/bin/env python3
"""Find single-day events that collide, across every city file.

A traveler can't be in Busan and Incheon on the same evening. Entries are
verified one at a time, so cross-file collisions are invisible to per-entry
review. This scans headers for single-date November 2026 claims and groups.
"""
import glob, re, io, collections

MON = {'Oct':10,'Nov':11,'Dec':12,'October':10,'November':11,'December':12}
hits = collections.defaultdict(list)

for f in sorted(glob.glob('/home/user/KoreaFun/*.md')):
    name = f.rsplit('/',1)[1]
    if name in ('README.md','itinerary.md','walking-maps.md','travel-basics.md','sources.md'):
        continue
    s = io.open(f, encoding='utf-8').read()
    for m in re.finditer(r'^### (\d+)\)(.*?)(?=^### |\Z)', s, re.M|re.S):
        head = m.group(0).split('\n')[0]
        title = re.sub(r'[*#]', '', head).strip()
        # only single-day claims: "Sat Nov 7, 2026" not "Nov 7-9" / "through Nov 8"
        for mm in re.finditer(r'\b(Oct|Nov|Dec|October|November|December)\w*\s+(\d{1,2}),?\s*2026', head):
            span = head[max(0,mm.start()-12):mm.end()+3]
            if re.search(r'through|–|—|-\s*\w*\s*\d', span.replace('Nov','').replace('Oct','')):
                continue
            hits[(MON[mm.group(1)], int(mm.group(2)))].append((name, m.group(1), title[:70]))

print("=== SINGLE-DAY EVENT COLLISIONS (2+ entries claiming the same date) ===\n")
for d in sorted(hits):
    rows = hits[d]
    cities = {r[0] for r in rows}
    if len(rows) < 2: continue
    flag = "  <-- MULTI-CITY, physically exclusive" if len(cities) > 1 else ""
    print(f"--- 2026-{d[0]:02d}-{d[1]:02d}  ({len(rows)} entries, {len(cities)} cities){flag}")
    for r in rows:
        print(f"      {r[0]:20s} #{r[1]:<3s} {r[2]}")
    print()
