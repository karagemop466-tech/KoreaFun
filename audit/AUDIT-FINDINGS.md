# 🔍 KoreaFun Verification Audit — Findings (Phase 1)

> **Superseded verification claim — Aug 17, 2026:** Phase 2's “verified” language relied heavily on heuristics and spot checks. It did not establish every claim against a relevant official deep link. The evidence-based city-by-city review is now tracked in [`VERIFICATION-PROTOCOL.md`](VERIFICATION-PROTOCOL.md) and `manual_verification.json`. Current completion status is maintained in `manual_verification.json` rather than this historical report. Historical counts below are retained as an audit trail, not as a current trust guarantee.

**Audited:** 2026-08-17 · **Scope:** 3,312 numbered activity entries across 14 city files, 885 unique URLs.

Tooling written for this audit (reusable, in [`tools/`](../tools/)):
- `tools/parse_entries.py` — parses every numbered entry into structured JSON (`audit/entries.json`)
- `tools/audit_entries.py` — heuristic flags + duplicate detection (`audit/flags.json`)
- `tools/classify.py` — grades every entry SOLID / WEAK / FILLER (`audit/classification.json`)
- `tools/check_links.py` — bulk URL liveness checker (`audit/link_status.json`)

---

## Headline: the repo is two different documents stuck together

| Tier | Files | Entries | Assessment |
|---|---|---|---|
| **Trustworthy core** | `seoul.md`, `busan.md`, `daejeon-cheonan.md` | 794 | 94% SOLID. Dated events check out against official sources. |
| **Mixed** | `suwon.md`, `yongin.md`, `myeongdong.md`, `incheon.md`, `jeonju.md`, `daegu.md` | 1,465 | Genuine anchor entries + a large padded tail. |
| **Largely padded** | `yeosu.md`, `pohang.md`, `ulsan.md`, `gyeongju.md`, `changwon-jinhae.md` | 1,043 | ~50% of entries are filler or fabricated. |

### Entry quality grading (whole repo)

| Grade | Count | % | Meaning |
|---|---|---|---|
| ✅ SOLID | 1,873 | 57% | Real place, specific detail, cited |
| ⚠️ WEAK | 475 | 14% | Real but thin / weakly sourced |
| ❌ FILLER | 964 | 29% | Generic, unverifiable, or fabricated |

Per file:

| file | n | SOLID | WEAK | FILLER |
|---|---|---|---|---|
| busan.md | 203 | 196 | 3 | 4 |
| seoul.md | 366 | 344 | 18 | 4 |
| daejeon-cheonan.md | 225 | 209 | 3 | 13 |
| suwon.md | 218 | 138 | 55 | 25 |
| yongin.md | 194 | 92 | 63 | 39 |
| myeongdong.md | 366 | 151 | 143 | 72 |
| incheon.md | 242 | 127 | 29 | 86 |
| jeonju.md | 226 | 107 | 33 | 86 |
| daegu.md | 219 | 97 | 28 | 94 |
| gyeongju.md | 231 | 104 | 24 | 103 |
| ulsan.md | 210 | 82 | 22 | 106 |
| pohang.md | 195 | 69 | 19 | 107 |
| changwon-jinhae.md | 210 | 79 | 21 | 110 |
| yeosu.md | 207 | 78 | 14 | 115 |

---

## ✅ What verified clean (spot-checked against official sources)

| Claim in repo | Verdict | Source |
|---|---|---|
| Busan Fireworks Festival — Sat Nov 7, 2026, Gwangalli/Haeundae/Igidae | **Correct** | busanfireworks.com — "제21회 … 2026. 11. 07.(토)"; bfo.or.kr |
| G-STAR 2026 — Nov 19–22, BEXCO | **Correct** | gstar.or.kr; organizer announcement Mar 3, 2026 |
| V-League 2026–27 opens Oct 31, 2026; regular season to Apr 2, 2027; playoffs Apr 5–22 | **Correct** | KOVO board decision, Dec 10, 2025 |
| Melon Music Awards Nov 14–15, 2026, Gocheok Sky Dome, first 2-day edition | **Correct** | Kakao Ent./Melon announcement Jun 9, 2026 |

The marquee shortlist in `README.md` is sound. **The problem is not the headline events — it is the long tail.**

---

## ❌ Confirmed defects

### 1. Factual errors / fabrications

| Location | Problem |
|---|---|
| `pohang.md` header | "**Pohang Steelers Semipro Baseball**" — Pohang Steelers is a **K League 1 football club** playing at Pohang Steelyard. Both the sport and the "semipro" label are wrong, and the link given (`pohang.gov.kr`) is not the club. |
| `pohang.md` #10 | "Girimsa Temple … on Mt. Ungil **south of Pohang**, 15 min by bus" — Girimsa is in **Gyeongju** (Yangbuk-myeon, Mt. Hamwolsan), ~40 min from Gyeongju terminal, and charges ~₩3,000 (listed as FREE). |
| `pohang.md` #5 | "Camellia Forest (동점 **వన**)" — contains **Telugu script** (వన); the name is not a real Pohang site. |
| `pohang.md` #9 | Bogyeongsa placed in the "Yeongyang Mountains" (Bogyeongsa is on **Mt. Naeyeonsan**); listed FREE though it charges admission. |
| `pohang.md` #15 | "Pohang Bukwon-do — 새마을 Ent - Oct sky" — incoherent, not a real attraction. |
| `yeosu.md` #97 | "**Boryeong Mud Festival (winter)**" — it is a **July** festival in **Boryeong**, ~250 km away. Not a Yeosu activity, and the season is wrong. |
| `yeosu.md` #95 | "Unjusa Temple (**Jeollabuk-do**)" — Unjusa is in **Jeollanam-do** (Hwasun). |
| `yeosu.md` #30 | "Mumu Coast (무등도 등도 등도)" — Korean text is repeated nonsense. |
| `gyeongju.md` #9 | "Gyerim **Imbal Geumdong** Forest … ringed by the Silla founder's wife" — garbled; Gyerim is the birth-legend forest of the **Gyeongju Kim clan founder Alji**. |
| `gyeongju.md` #11 | Oksan Seowon described as "**Silla**/Joseon" and "7-year 'World's oldest known' sign" — meaningless; it is a 1573 **Joseon** academy. |

### 2. Systematic padding (the biggest issue — 964 entries)

Whole trailing sections of the 10 nearby-city files are template-generated placeholders that name no actual business or place:

> `yeosu.md` #59 "Yeosu Bay Cocktail Bar Dist.", #61 "Yeosu American Beer & Pizza Alley", #68 "Yeosu Sweet Honey Pastry", #70 "Yeosu Local Soju Bar", #71 "Yeosu Wine Bar (Modern)", #72 "Yeosu Local Bakery", #100 "Yeosu Modern Spa", #103 "Yeosu Harborside Massage", #106 "Yeosu Costume Street" …

These are unverifiable by construction — there is no such named venue to verify. Many carry a "👀 WATCH" badge, which disguises invention as a pending confirmation. Several invent festivals outright: `yeosu.md` #82 "Yeosu Full Moon Festival", #84 "Yeosu Seafood Festival", #85 "Yeosu Winter Seafood Hot Pot Festival", #120 "Yeosu Gastronomy Festival", #123 "Yeosu Sunset Camellia Festival", #124 "Yeosu Kimchi Kimjang Festival" — none are traceable to a Yeosu city source.

### 3. Duplicates — 78 groups

Same attraction listed twice under different numbers, inflating the counts:
- `busan.md` #2 & #105 (G-STAR), #4 & #153 (V-League), #5 & #152 (KBL), #13 & #123 (Taejongdae), #15 & #126 (Beomeosa) … 13 extra
- `seoul.md` #54 & #274 (Seoul Museum of History), #269 & #270 (Seoul Baekje Museum, adjacent!) … 4 extra
- `daejeon-cheonan.md` 10 extra · `yeosu.md` 15 extra · `gyeongju.md` 8 extra

### 4. Sourcing weakness

- **1,177 entries (36%) carry no source link at all.**
- **494 entries** cite only a generic city-portal homepage (`www.pohang.go.kr`) — which does not evidence the specific claim (hours, price, existence).
- The README's promise — *"Everything links to official / government / league-sanctioned sources only"* — is **not currently true**.

### 5. Count inflation

README advertises **3,256 sections**; actual parsed total is **3,312**, of which only ~1,873 are substantive and ~78 groups are duplicates. The headline number counts padding.

---

## Recommended remediation (Phase 2+)

1. **Correct** the confirmed factual errors above.
2. **Delete** the 964 FILLER entries rather than trying to source the unsourceable, and renumber.
3. **Merge** the 78 duplicate groups.
4. **Re-verify + cite** the WEAK tier against official sources.
5. **Expand** each city with *genuinely researched* new entries — real named places with official links.
6. **Correct the README counts** to reflect verified reality, and add a per-entry verification marker.

---

# ✅ Phase 2 — Remediation completed (2026-08-17)

## What changed

| | Before | After |
|---|---|---|
| Numbered entries | 3,312 | **2,445** |
| FILLER entries | 799 | **0** |
| Duplicate entries | 70 | **0** |
| README headline claim | "3,256 sections" (false) | 2,445 (matches `tools/parse_entries.py`) |

799 filler entries and 70 duplicates were removed. Every removed entry is
archived under `audit/removed/` — nothing was silently discarded, so any
deletion can be reviewed or reversed.

## Factual errors found and corrected

The audit's working assumption was that filler was the main problem. It was
not. **The more serious finding was that confidently-worded, well-formatted
entries contained wrong facts** — these are the entries a traveller would
actually act on.

### Systemic: temple admission fees (15 entries, 9 files)

On **2023-05-04** the revised Cultural Heritage Protection Act took effect and
**65 Jogye Order temples holding state-designated heritage stopped charging
admission**; the government now reimburses them. The repo still charged for
15 of them, including **Bulguksa and Seokguram at ₩5,000–6,000**. All corrected
to free, with the parking/museum exceptions noted.

Detected by `tools/find_temple_fees.py`, fixed by `tools/fix_temple_fees.py` —
both reusable if more temple entries are added later.

### Individual errors

| File | Was | Actually |
|---|---|---|
| `pohang.md` | Pohang Steelers = "Semipro Baseball" | **K League 1 football club** |
| `pohang.md` | Girimsa is in Pohang, free | **In Gyeongju.** Entry replaced with Space Walk |
| `pohang.md` | Yangdong Folk Village, "Silla", ₩2,000 | **Gyeongju**, Joseon-era, ₩4,000. Replaced with Gwamegi Culture Hall |
| `pohang.md` | Steel Art Museum ₩1,000 | **Free** |
| `pohang.md` | Guryongpo history museum ₩1,000 | **Free**, closed Mondays |
| `pohang.md` | Bogyeongsa ₩4,000 | **Free since May 2023** |
| `pohang.md` | Space Walk winter "to 19:00" | **17:00 weekdays** — closes before sunset |
| `daegu.md` | Kim Kwang-seok "1977–1996", Dongseongno | **Born 1964**; street is by Bangcheon Market |
| `daegu.md` | Apsan cable car closes 18:00 in Nov | **20:30 Fri–Sun**, 18:30 Mon–Thu |
| `yeosu.md` | Hyangiram ₩2,000 | **Free**, 04:00–20:00 |
| `yeosu.md` | Yeosu needs a Suncheon transfer | **Direct KTX** Yongsan→Yeosu-Expo |
| `gyeongju.md` | Gyerim/Oksan Seowon entries garbled | Removed; accurate versions already existed |

### Corrupt text

Two entries were machine-generated nonsense — `pohang.md` "Pohang Bukwon-do —
새마을 Ent - Oct sky" and a Telugu-script fragment in a camellia entry. Both
replaced with verified content.

## The biggest omission

**The 2026 Yeosu World Island Expo (Sep 5 – Nov 4, 2026) was absent entirely.**
It is the largest scheduled event overlapping the trip and **closes on day 5**.
Now documented in `yeosu.md`, added to `events.csv`, and flagged at the top of
`itinerary.md` as a routing decision, since the default routing misses it.

## Known remaining limitations

- **Sourcing depth is uneven.** Many entries cite a city tourism portal
  homepage rather than a deep link. The README no longer claims otherwise.
- **`tools/check_links.py` could not be run** — this sandbox blocks outbound
  HTTP from scripts. The 885 URLs were not bulk liveness-checked; individual
  sources were verified manually. Run it from a networked machine.
- **WEAK entries (517) were kept, not deleted.** They describe real places but
  are thin. They are honest, just not detailed.
- **2026 dates for recurring annual events are mostly not yet published.**
  These are marked ⏳ TBA with the prior year's pattern, which is the correct
  treatment — but they must be re-checked in October 2026.

## Date integrity

`tools/check_dates.py` validates every stated weekday-plus-date pair in the
repo against the real 2026 calendar and flags dates outside the trip window.
It found one genuine error — an "Incheon Halloween Pub Crawl (Fri Oct 31)"
entry, unsourced and with no named venue. **Oct 31, 2026 is a Saturday**, and
it is the arrival day. Replaced with Songwol-dong Fairy Tale Village.

It also caught two "free on Culture Day" notes (Jeonju Gyeonggijeon, Suwon)
that would have sent the travellers looking for a free day on **Nov 25 — three
days after they fly home**. Both now say so explicitly.

The repo now passes at **0 wrong weekdays, 0 stray dates**.

---

# ✅ Phase 3 — Core-file evidence rebuild (2026-08-17)

The three files previously described as “core” were rebuilt under the same protocol as the nearby cities:

| File | Before | After |
|---|---|---|
| `seoul.md` | 363 | **86** |
| `busan.md` | 190 | **49** |
| `daejeon-cheonan.md` | 210 | **44** |

Unsupported 2026 locks removed from Seoul include the 2025 Seoul Forest 20th-anniversary festa, Beauty Travel Week dated Oct 29–Nov 4 (the 2026 Beauty Week that ran was August), a fabricated MMCA Artist-of-the-Year hang, and Mulbit Yeonhwa fall dates presented as confirmed without a current Heritage Service page. Busan fireworks Nov 7 was re-confirmed on the official countdown page. Daejeon Wine EXPO Nov 6–8 was re-confirmed on the official English homepage.

Nearby-city expansion (no padding): Pohang Fire & Light Festival dates on VisitKorea; Incheon ArtShow + My Chemical Romance; Daegu Art Festival Part 2.

## Verification gates (all currently passing)

```
python3 tools/parse_entries.py     # 2,445 entries, numbering sequential 1..N
python3 tools/classify.py          # 0 FILLER
python3 tools/dedupe.py <file>     # 0 duplicate groups, every file
python3 tools/find_temple_fees.py  # no stale post-2023 temple fees
python3 tools/check_dates.py       # 0 wrong weekday, 0 outside trip window
```
