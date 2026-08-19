#!/usr/bin/env python3
"""Parse KoreaFun city markdown files into a structured entry inventory.

Every activity is a '### N) Title — status' heading followed by bullet fields.
Outputs audit/entries.json
"""
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CITY_FILES = [
    "seoul.md", "seoul-districts.md", "myeongdong.md", "busan.md", "daejeon-cheonan.md",
    "suwon.md", "yongin.md", "incheon.md", "jeonju.md", "daegu.md",
    "gyeongju.md", "ulsan.md", "pohang.md", "changwon-jinhae.md", "yeosu.md",
]

HEAD_RE = re.compile(r"^#{2,3}\s+(.*)$")
NUM_RE = re.compile(r"^\**\s*(\d+)\)\s*(.*)$")
URL_RE = re.compile(r"https?://[^\s)\]<>\"']+")
FIELD_RE = re.compile(r"^-\s+\*\*([^:*]+):?\*\*:?\s*(.*)$")


def strip_md(s):
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = s.replace("**", "").replace("`", "").strip()
    return s


def parse_file(path):
    entries = []
    section = None
    cur = None
    lines = open(path, encoding="utf-8").read().split("\n")
    for i, line in enumerate(lines):
        if line.startswith("## ") and not NUM_RE.match(line[3:].strip()):
            section = strip_md(line[3:])
        m = HEAD_RE.match(line)
        if m:
            if cur:
                entries.append(cur)
                cur = None
            raw = m.group(1).strip()
            nm = NUM_RE.match(raw)
            if not nm:
                continue
            num = int(nm.group(1))
            rest = nm.group(2)
            # split off the trailing status segment(s) on em dash
            parts = [p.strip() for p in re.split(r"\s+—\s+", rest)]
            title = strip_md(parts[0])
            tail = " — ".join(parts[1:])
            cur = {
                "file": os.path.basename(path),
                "line": i + 1,
                "section": section,
                "num": num,
                "title": title,
                "title_raw": rest,
                "status_tail": strip_md(tail),
                "body": [],
                "fields": {},
                "urls": [],
            }
            continue
        if cur is not None:
            if line.startswith("#") or (line.startswith("---") and len(line) > 2):
                entries.append(cur)
                cur = None
                continue
            cur["body"].append(line)
            fm = FIELD_RE.match(line)
            if fm:
                key = fm.group(1).strip().lower()
                cur["fields"][key] = strip_md(fm.group(2))
            cur["urls"] += URL_RE.findall(line)
    if cur:
        entries.append(cur)
    return entries


def main():
    all_entries = []
    for f in CITY_FILES:
        p = os.path.join(REPO, f)
        if not os.path.exists(p):
            print("MISSING", f, file=sys.stderr)
            continue
        e = parse_file(p)
        all_entries += e
        print(f"{f}: {len(e)} entries")
    out = os.path.join(REPO, "audit", "entries.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(all_entries, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("total", len(all_entries), "->", out)


if __name__ == "__main__":
    main()
