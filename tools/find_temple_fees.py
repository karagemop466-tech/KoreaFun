#!/usr/bin/env python3
"""Locate entries that still charge admission for temples on the 2023
Jogye Order / Cultural Heritage Administration free list."""
import glob
import os
import re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Temples whose cultural-heritage admission was abolished 2023-05-04
FREE_LIST = [
    "Bulguksa", "Seokguram", "Beomeosa", "Haeinsa", "Tongdosa", "Donghwasa",
    "Hwaeomsa", "Songgwangsa", "Naksansa", "Woljeongsa", "Magoksa", "Sudeoksa",
    "Jeondeungsa", "Yongjusa", "Baekyangsa", "Baegyangsa", "Seonunsa",
    "Naejangsa", "Bongjeongsa", "Buseoksa", "Girimsa", "Heungguksa",
    "Hyangiram", "Bogyeongsa", "Beopjusa", "Silsangsa", "Golgulsa",
    "Unjusa", "Daeheungsa", "Muwisa", "Dogapsa", "Taeansa", "Guryongsa",
    "Jikjisa", "Gounsa", "Boriam", "Pagyesa", "Gapsa", "Beopjusa",
]
NUM_RE = re.compile(r"^(#{2,3})\s+\**\s*(\d+)\)(.*)$")
PRICE_RE = re.compile(r"^-\s+\*\*Price:?\*\*:?\s*(.*)$", re.I)
MONEY = re.compile(r"₩\s?([\d,]+)")

for path in sorted(glob.glob(os.path.join(REPO, "*.md"))):
    lines = open(path, encoding="utf-8").read().split("\n")
    cur = None
    for i, line in enumerate(lines):
        m = NUM_RE.match(line)
        if m:
            cur = (int(m.group(2)), m.group(3).strip(), i + 1)
        if cur is None:
            continue
        pm = PRICE_RE.match(line)
        if not pm:
            continue
        price = pm.group(1)
        title = cur[1]
        for t in FREE_LIST:
            if t.lower() in title.lower():
                # ignore templestay / cable car / museum add-ons
                if re.search(r"templestay|cable|museum|stay|program", title, re.I):
                    continue
                if MONEY.search(price) and "free" not in price.lower():
                    print(f"{os.path.basename(path)}:{cur[2]} #{cur[0]} [{t}]")
                    print(f"    {title[:80]}")
                    print(f"    PRICE: {price[:110]}")
                break
