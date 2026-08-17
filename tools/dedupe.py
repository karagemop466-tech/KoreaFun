#!/usr/bin/env python3
"""Find duplicate entries within a city file and drop the weaker copy.

Usage: python3 tools/dedupe.py <file.md> [--apply]

Two entries are duplicates when their normalised titles match on the core
proper-noun tokens (Hangul name or distinctive Latin tokens). The copy with
more substance (fields + length + sources) is kept.
"""
import os
import re
import sys
from collections import defaultdict

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NUM_RE = re.compile(r"^(#{2,3})\s+(\**\s*)(\d+)\)(.*)$", re.S)

STOP = {
    "the", "a", "an", "of", "and", "in", "at", "on", "for", "to", "with", "from",
    "korea", "korean", "city", "day", "tour", "view", "night", "nightly", "daily",
    "always", "confirmed", "watch", "free", "see", "extended", "trip", "visit",
    "seoul", "busan", "yeosu", "ulsan", "pohang", "daegu", "gyeongju", "jeonju",
    "incheon", "suwon", "yongin", "changwon", "jinhae", "daejeon", "cheonan",
    "myeongdong", "myeong", "dong", "island", "temple", "park", "market",
    "museum", "street", "beach", "hall", "village", "festival", "show", "bridge",
    "tower", "station", "center", "centre", "mountain", "bay", "sunset", "sunrise",
}


def key_of(title):
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", title)
    t = re.sub(r"[*`]", "", t)
    t = re.sub(r"—.*$", "", t)
    hang = re.findall(r"[\uac00-\ud7a3]+", t)
    lat = re.findall(r"[A-Za-z][A-Za-z'-]+", t)
    lat = [w.lower() for w in lat if w.lower() not in STOP and len(w) > 2]
    if hang:
        return ("H", "".join(sorted(set(hang))))
    if lat:
        return ("L", " ".join(sorted(set(lat))))
    return None


def main():
    fname = sys.argv[1]
    apply = "--apply" in sys.argv
    path = os.path.join(REPO, fname)
    lines = open(path, encoding="utf-8").read().split("\n")

    blocks, cur = [], {"num": None, "lines": []}
    for line in lines:
        m = NUM_RE.match(line)
        if m:
            blocks.append(cur)
            cur = {"num": int(m.group(3)), "lines": [line], "hashes": m.group(1),
                   "bold": m.group(2), "rest": m.group(4), "title": m.group(4)}
        else:
            cur["lines"].append(line)
    blocks.append(cur)

    groups = defaultdict(list)
    for b in blocks:
        if b["num"] is None:
            continue
        k = key_of(b["title"])
        if k:
            groups[k].append(b)

    def weight(b):
        body = "\n".join(b["lines"][1:])
        return (len(re.findall(r"^-\s+\*\*", body, re.M)),
                len(re.findall(r"https?://", body)), len(body))

    drop = set()
    dupes = []
    for k, g in groups.items():
        if len(g) < 2:
            continue
        best = max(g, key=weight)
        losers = [b for b in g if b is not best]
        dupes.append((k, best, losers))
        for b in losers:
            drop.add(b["num"])

    print(f"{fname}: {len(dupes)} duplicate groups, dropping {len(drop)} entries")
    for k, best, losers in dupes:
        print(f"  keep #{best['num']} {best['title'].strip()[:70]}")
        for b in losers:
            print(f"    drop #{b['num']} {b['title'].strip()[:66]}")

    if not apply:
        return

    kept = [b for b in blocks if b["num"] is None or b["num"] not in drop]
    n, out = 0, []
    for b in kept:
        if b["num"] is None:
            out += b["lines"]
            continue
        n += 1
        out += [f"{b['hashes']} {b['bold']}{n}){b['rest']}"] + b["lines"][1:]
    text = re.sub(r"\n{4,}", "\n\n\n", "\n".join(out))

    arch = os.path.join(REPO, "audit", "removed")
    os.makedirs(arch, exist_ok=True)
    with open(os.path.join(arch, f"dupes-{fname}"), "w", encoding="utf-8") as fh:
        fh.write(f"# Duplicate entries merged out of {fname}\n\n")
        for k, best, losers in dupes:
            for b in losers:
                fh.write("\n".join(b["lines"]).rstrip() + "\n\n")
    open(path, "w", encoding="utf-8").write(text)
    print(f"  -> {n} entries remain")


if __name__ == "__main__":
    main()
