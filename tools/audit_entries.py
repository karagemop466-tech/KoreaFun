#!/usr/bin/env python3
"""Heuristic quality audit over parsed entries -> audit/flags.json + report."""
import json
import os
import re
import unicodedata
from collections import Counter, defaultdict

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = json.load(open(os.path.join(REPO, "audit", "entries.json"), encoding="utf-8"))

# Script blocks that should never appear in a Korea guide (Hangul/Han/Latin only)
BAD_SCRIPT = re.compile(
    "[\u0900-\u097F"   # Devanagari
    "\u0C00-\u0C7F"    # Telugu
    "\u0980-\u09FF"    # Bengali
    "\u0B80-\u0BFF"    # Tamil
    "\u0A80-\u0AFF"    # Gujarati
    "\u0400-\u04FF"    # Cyrillic
    "\u0590-\u05FF"    # Hebrew
    "\u0600-\u06FF"    # Arabic
    "\u0E00-\u0E7F"    # Thai
    "\u3040-\u30FF"    # Kana (JP) - suspicious in a Korea guide
    "]"
)

flags = defaultdict(list)


def add(entry, code, detail=""):
    flags[code].append({
        "file": entry["file"], "line": entry["line"], "num": entry["num"],
        "title": entry["title"], "detail": detail,
    })


for e in E:
    body = "\n".join(e["body"])
    full = e["title_raw"] + "\n" + body

    m = BAD_SCRIPT.findall(full)
    if m:
        names = sorted({unicodedata.name(c, "?").split()[0] for c in m})
        add(e, "foreign_script", f"{''.join(sorted(set(m)))} ({','.join(names)})")

    if not e["urls"]:
        add(e, "no_source")

    # very thin entries (likely padding/filler)
    if len(body.strip()) < 120:
        add(e, "thin_entry", f"{len(body.strip())} chars")

    f = e["fields"]
    if "what" not in f:
        add(e, "no_what")
    if not any(k in f for k in ("hours", "when", "dates", "when/where", "season", "date")):
        add(e, "no_hours")
    if not any(k in f for k in ("price", "cost", "tickets", "admission")):
        add(e, "no_price")

    # generic city-portal-only sourcing (weak verification)
    hosts = {re.sub(r"https?://", "", u).split("/")[0] for u in e["urls"]}
    portal = {"www.pohang.go.kr", "www.gyeongju.go.kr", "www.suwon.go.kr", "www.ulsan.go.kr",
              "www.yeosu.go.kr", "www.changwon.go.kr", "www.daegu.go.kr", "www.yongin.go.kr",
              "www.incheon.go.kr", "www.daejeon.go.kr", "www.cheonan.go.kr", "www.jeonju.go.kr",
              "tour.jeonju.go.kr", "english.visitbusan.net", "english.visitseoul.net",
              "english.visitkorea.or.kr", "korean.visitkorea.or.kr"}
    if hosts and hosts <= portal:
        add(e, "portal_only_source")

    # broken / placeholder text
    if re.search(r"\bTBD\b.*\bTBD\b", body) or "lorem" in body.lower():
        add(e, "placeholder")

# duplicate detection
def norm(t):
    t = t.lower()
    t = re.sub(r"\([^)]*\)", " ", t)
    t = re.sub(r"[^a-z0-9가-힣 ]", " ", t)
    stop = {"the", "a", "of", "and", "in", "at", "on", "for", "to", "korea", "korean",
            "seoul", "busan", "festival", "market", "museum", "park", "temple", "tour",
            "street", "center", "centre", "hall", "beach", "village", "station", "day"}
    toks = [w for w in t.split() if w not in stop and len(w) > 2]
    return " ".join(sorted(set(toks)))


by_file = defaultdict(list)
for e in E:
    by_file[e["file"]].append(e)

dups = []
for fname, ents in by_file.items():
    seen = defaultdict(list)
    for e in ents:
        key = norm(e["title"])
        if key:
            seen[key].append(e)
    for key, group in seen.items():
        if len(group) > 1:
            dups.append({
                "file": fname, "key": key,
                "entries": [{"num": g["num"], "line": g["line"], "title": g["title"]} for g in group],
            })

# exact-title duplicates across whole corpus within same file already covered.
out = {"flags": dict(flags), "duplicates": dups}
json.dump(out, open(os.path.join(REPO, "audit", "flags.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)

print("=== FLAG SUMMARY ===")
for k, v in sorted(flags.items(), key=lambda x: -len(x[1])):
    print(f"{k:24s} {len(v)}")
print(f"{'duplicate_title_groups':24s} {len(dups)}")
print("\n=== per-file foreign_script / thin / no_source ===")
for fname in sorted(by_file):
    fs = sum(1 for x in flags["foreign_script"] if x["file"] == fname)
    th = sum(1 for x in flags["thin_entry"] if x["file"] == fname)
    ns = sum(1 for x in flags["no_source"] if x["file"] == fname)
    dp = sum(len(d["entries"]) - 1 for d in dups if d["file"] == fname)
    print(f"{fname:22s} n={len(by_file[fname]):4d} script={fs:3d} thin={th:3d} nosrc={ns:3d} dupextra={dp:3d}")
