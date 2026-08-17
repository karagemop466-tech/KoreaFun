#!/usr/bin/env python3
"""Replace stale temple admission prices with the post-2023 free-entry fact.

On 2023-05-04 the revised Cultural Heritage Protection Act took effect and 65
Jogye Order temples holding state-designated heritage stopped charging the
cultural-heritage admission fee; the government reimburses them. Parking is
still charged, and on-site museums keep separate tickets.
"""
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NOTE = ("**FREE** — cultural-heritage admission was **abolished on May 4, 2023** "
        "for the 65 Jogye Order temples holding state-designated heritage "
        "(the government reimburses the temple). Parking is still charged"
        "{extra}. Older guidebooks still quote {old} — there is no entry fee.")

# (file, entry number, old price substring, extra clause)
FIXES = [
    ("daegu.md", 157, "Adult **₩2,500**", ""),
    ("daegu.md", 190, "Adult **₩2,500**", ""),
    ("daejeon-cheonan.md", 150, "Temple entry **₩4,000**",
     "; Songnisan National Park itself is free"),
    ("daejeon-cheonan.md", 173, "Small admission around **₩3,000**", ""),
    ("gyeongju.md", 1, "Adult **₩5,000** (~$3.50); youth ₩3,500; child ₩2,500",
     "; the on-site Bulguksa Museum is a separate ₩2,000"),
    ("gyeongju.md", 2, "Adult **₩5,000** (combined with Bulguksa usually **₩7,000**)", ""),
    ("gyeongju.md", 44, "Adult ₩3,000", ""),
    ("gyeongju.md", 45, "Adult **₩6,000**; youth ₩4,000; child ₩3,000",
     "; the on-site Bulguksa Museum is a separate ₩2,000"),
    ("gyeongju.md", 46, "Adult **₩6,000**", ""),
    ("gyeongju.md", 104, "Adult **₩3,000**", ""),
    ("incheon.md", 189, "Adult **₩4,000**", ""),
    ("jeonju.md", 188, "Adult **₩4,000**", ""),
    ("suwon.md", 182, "**₩1,500**", ""),
    ("ulsan.md", 61, "Adult **₩3,000**", ""),
    ("yeosu.md", 89, "Adult **₩3,000**", ""),
]

NUM_RE = re.compile(r"^(#{2,3})\s+\**\s*(\d+)\)")


def apply(fname, num, old, extra, dry):
    path = os.path.join(REPO, fname)
    lines = open(path, encoding="utf-8").read().split("\n")
    cur = None
    for i, line in enumerate(lines):
        m = NUM_RE.match(line)
        if m:
            cur = int(m.group(2))
        if cur != num:
            continue
        if line.lstrip().startswith("- **Price") and old in line:
            oldq = re.sub(r"\*", "", old).strip()
            new = "- **Price:** " + NOTE.format(extra=extra, old=oldq)
            print(f"{fname} #{num}\n  - {line.strip()[:90]}\n  + {new[:110]}")
            if not dry:
                lines[i] = new
                open(path, "w", encoding="utf-8").write("\n".join(lines))
            return True
    print(f"!! {fname} #{num}: no match for {old!r}")
    return False


dry = "--apply" not in sys.argv
ok = sum(apply(*f, dry) for f in FIXES)
print(f"\n{ok}/{len(FIXES)} {'would be' if dry else ''} fixed")
