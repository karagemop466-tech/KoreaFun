#!/usr/bin/env python3
"""Classify each entry as SOLID / WEAK / FILLER.

Conservative: an entry is only FILLER when it is BOTH generic/unverifiable in
name AND lacking the substance that would let a traveller act on it. Anything
naming a real, checkable place keeps at least WEAK.
"""
import json
import os
import re
from collections import Counter, defaultdict

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = json.load(open(os.path.join(REPO, "audit", "entries.json"), encoding="utf-8"))

# Words that, as the *head* of a title, denote a category rather than a place.
GENERIC_HEAD = re.compile(
    r"\b(local|modern|traditional|specialt(y|ies)|options?|scene|trail|alley|"
    r"district|dist\.|street|bar|pub|cafe|caf\u00e9|bakery|dessert|restaurants?|"
    r"spa|massage|sauna|shopping|grocery|market|mall|boutique|nightlife|"
    r"live music|pub crawl|walk|tour|visit|experience|zone|quarter|mile|area)\b",
    re.I)

# A proper-noun-ish signal: Hangul, or a capitalised Korean place/brand token.
PROPER = re.compile(r"[\uac00-\ud7a3]|\b(?:[A-Z][a-z]{2,}(?:-?[a-z]+)?)\b")

CITY = (r"Yeosu|Ulsan|Pohang|Daegu|Gyeongju|Jeonju|Incheon|Suwon|Yongin|"
        r"Changwon|Jinhae|Busan|Seoul|Daejeon|Cheonan|Masan|Myeongdong")

# Nonsense / corruption signals
BAD_SCRIPT = re.compile("[\u0900-\u097F\u0C00-\u0C7F\u0980-\u09FF\u0B80-\u0BFF"
                        "\u0A80-\u0AFF\u0400-\u04FF\u0590-\u05FF\u0600-\u06FF\u0E00-\u0E7F]")


def title_is_generic(title):
    """True when the title names no specific entity beyond '<City> <category>'."""
    t = re.sub(r"^[^\w\uac00-\ud7a3]+", "", title)  # strip leading emoji
    if re.search(r"[\uac00-\ud7a3]", t):
        return False  # has Hangul -> a real named place
    # remove the city name, then see what proper nouns remain
    rest = re.sub(CITY, " ", t, flags=re.I)
    rest = re.sub(r"\([^)]*\)", " ", rest)
    # tokens that look like a distinct proper name (not a generic category word)
    tokens = re.findall(r"\b[A-Z][A-Za-z'\-]{2,}\b", rest)
    tokens = [w for w in tokens if not GENERIC_HEAD.fullmatch(w)
              and w.lower() not in {"korean", "korea", "the", "and", "for", "with",
                                    "nov", "november", "october", "autumn", "winter",
                                    "family", "kids", "day", "night", "sunset",
                                    "sunrise", "coastal", "seaside", "riverside",
                                    "indoor", "outdoor", "free", "new", "old",
                                    "east", "west", "north", "south", "central"}]
    has_generic = bool(GENERIC_HEAD.search(rest))
    return has_generic and not tokens


def score(e):
    body = "\n".join(e["body"]).strip()
    f = e["fields"]
    has_src = bool(e["urls"])
    # a source that is more than a bare city-portal homepage
    hosts = {re.sub(r"https?://", "", u).split("/")[0] for u in e["urls"]}
    paths = [u for u in e["urls"] if len(re.sub(r"https?://[^/]+", "", u).strip("/")) > 3]
    specific_src = bool(paths) or len(hosts - {
        "www.pohang.go.kr", "www.gyeongju.go.kr", "www.suwon.go.kr", "www.ulsan.go.kr",
        "www.yeosu.go.kr", "www.changwon.go.kr", "www.daegu.go.kr", "www.yongin.go.kr",
        "www.incheon.go.kr", "www.daejeon.go.kr", "www.cheonan.go.kr", "www.jeonju.go.kr",
        "tour.jeonju.go.kr", "english.visitbusan.net", "english.visitseoul.net",
        "english.visitkorea.or.kr", "korean.visitkorea.or.kr"}) > 0

    has_what = "what" in f
    has_price = any(k in f for k in ("price", "cost", "admission", "tickets"))
    has_hours = any(k in f for k in ("hours", "when", "dates", "season", "when/where", "date"))
    has_notes = any("note" in k for k in f)
    pts = sum([has_src, has_what, has_price, has_hours, has_notes])
    n = len(body)

    corrupt = bool(BAD_SCRIPT.search(e["title_raw"] + body))
    generic = title_is_generic(e["title"])

    # Cross-reference stubs ("see busan.md") are navigational, not activities.
    xref = bool(re.match(r"^\s*[-*]?\s*\**(Just|See|\*\*)?", body)) and n < 120 and "see " in body.lower()

    if corrupt:
        return "FILLER", pts, n, "corrupt-text"
    if generic and not specific_src:
        return "FILLER", pts, n, "generic-unsourced"
    if generic and n < 220:
        return "FILLER", pts, n, "generic-thin"
    if xref:
        return "FILLER", pts, n, "xref-stub"
    # Long, detailed entries are substantive even if they use non-standard
    # field labels (e.g. per-venue sub-headings instead of What/Hours/Price).
    if n < 90 or (pts <= 1 and n < 250):
        return "FILLER", pts, n, "no-substance"
    if n < 200 or pts <= 3 or not has_src:
        return "WEAK", pts, n, "thin-or-unsourced"
    return "SOLID", pts, n, ""


byfile = defaultdict(Counter)
rows = []
for e in E:
    cls, pts, n, why = score(e)
    byfile[e["file"]][cls] += 1
    rows.append({**{k: e[k] for k in ("file", "num", "line", "title")},
                 "cls": cls, "pts": pts, "len": n, "why": why})

json.dump(rows, open(os.path.join(REPO, "audit", "classification.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)

tot = Counter()
print(f"{'file':22s} {'n':>4s} {'SOLID':>6s} {'WEAK':>5s} {'FILLER':>7s}")
for fn in sorted(byfile):
    c = byfile[fn]
    tot.update(c)
    print(f"{fn:22s} {sum(c.values()):4d} {c['SOLID']:6d} {c['WEAK']:5d} {c['FILLER']:7d}")
print(f"{'TOTAL':22s} {sum(tot.values()):4d} {tot['SOLID']:6d} {tot['WEAK']:5d} {tot['FILLER']:7d}")
print()
print("FILLER reasons:", Counter(r["why"] for r in rows if r["cls"] == "FILLER").most_common())
