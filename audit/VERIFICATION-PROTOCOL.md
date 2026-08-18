# Manual verification protocol

**Started:** 2026-08-17  
**Purpose:** Replace “looks plausible” and heuristic grading with evidence-based review, one city file at a time.

## Important distinction

The existing parser, date checker, and duplicate heuristics are useful quality gates. They **cannot verify reality**. A URL in an entry proves nothing unless the linked page identifies the exact place/event and supports the claim being made. Accordingly, no unreviewed file should be described as fully verified.

Run:

```bash
python3 tools/parse_entries.py
python3 tools/verification_status.py
```

`audit/manual_verification.json` is the review ledger. A file receives `reviewed` only after every retained numbered entry passes the checklist below. Partial research stays `in-progress`, never `reviewed`.

## Source hierarchy

Use the strongest available source:

1. organizer, venue/operator, league, team, or attraction owner;
2. national or local government and official tourism portal;
3. statutory heritage, park, museum, or transport authority;
4. established reporting only as corroboration for an organizer announcement.

Ticket marketplaces, blogs, social reposts, map snippets, listicles, and generative summaries are discovery aids, not primary proof. Social media is acceptable only when it is the organizer’s official account and no durable announcement page exists; record that limitation.

## Per-entry checklist

- [ ] Exact named place/activity exists in the claimed city.
- [ ] Source is official or otherwise clearly trustworthy.
- [ ] Link is a relevant deep page, not merely an unrelated homepage.
- [ ] Description does not exaggerate what the source says.
- [ ] Event year, date, weekday, venue, and status match the source.
- [ ] A prior-year pattern is labeled TBA and is **not** presented as a 2026 event.
- [ ] Hours, prices, closure days, seasonality, and reservation rules are sourced or omitted.
- [ ] Nearby-city/day-trip content is labeled and is not used to pad the city count.
- [ ] No duplicate or differently worded version of the same activity remains.
- [ ] Source review date is visible in the rebuilt file.

## Expansion rule

Expansion happens **after** cleanup for a city. New entries must be named, discrete, useful in or near the trip window, and supported by a deep official link. Each city pass should search these categories individually:

- dated events in the trip window;
- municipal culture/performance calendar;
- sports league/team fixtures;
- museums and rotating exhibitions;
- heritage and architecture;
- parks, trails, and seasonal nature;
- markets and food experiences with a named venue or official directory;
- operator-run activities and bookable tours;
- rainy-day and evening options.

Do not add an entry solely to increase a count.

## Progress

| City file | Status | Result |
|---|---|---|
| `yeosu.md` | **Reviewed 2026-08-17** | Rebuilt 100 → 32 entries; removed fabricated places, unsupported event claims, duplicates, generic advice, and out-of-city padding; added 8 official-source activities. |
| `myeongdong.md` | **Reviewed 2026-08-17** | Rebuilt 296 → 36 entries; removed invented venues/events, stale brand branches, snack-by-snack padding, duplicates, generic advice, and attractions elsewhere in Seoul; added confirmed 2026 theater/art plus newly sourced museums and walks. |
| `yongin.md` | **Reviewed 2026-08-17** | Rebuilt 167 → 36 entries; removed fabricated Samsung venues, sports, festivals, unnamed businesses, duplicates, generic advice, and out-of-city padding; added dated 2026 Folk Village and museum programming. |
| `suwon.md` | **Reviewed 2026-08-17** | Rebuilt 211 → 37 entries; removed invented places/events, duplicated fortress components, generic advice, and out-of-city padding; added dated 2026 convention, exhibitions, performances, and final night-opening dates. |
| `jeonju.md` | **Reviewed 2026-08-17** | Rebuilt 159 → 35 entries; removed invented venues/events, repeated Hanok Village content, generic advice, and extensive out-of-city padding; added dated 2026 parade and evening/traditional performance series. |
| `incheon.md` | **Reviewed 2026-08-17** | Rebuilt 175 → 41 entries; removed fabricated events/venues, duplicate districts, obsolete airport and maglev claims, generic advice, and out-of-city padding; added current national museums and corrected post-July-2026 district sources. |
| `gyeongju.md` | **Reviewed 2026-08-17** | Rebuilt 133 → 35 entries; removed fabricated and closed attractions, duplicate heritage components, generic advice, and out-of-city padding; added two dated 2026 Arts Center exhibition programs and corrected UNESCO scope. |
| `daegu.md` | **Reviewed 2026-08-17** | Rebuilt 132 → 34 entries; removed fabricated venues/foods/events, duplicates, generic advice, and out-of-city padding; added five dated November 2026 arts programs. |
| `ulsan.md` | **Reviewed 2026-08-17** | Rebuilt 115 → 29 entries; removed fabricated and proposed attractions, unsafe factory assumptions, duplicates, generic advice, and out-of-city padding; updated Bangucheon’s 2025 UNESCO inscription. |
| `pohang.md` | **Reviewed 2026-08-17** | Rebuilt 88 → 28 entries; removed fabricated attractions/foods/events, duplicates, unsafe industrial-access claims, generic advice, and out-of-city padding. |
| `changwon-jinhae.md` | **Reviewed 2026-08-17** | Rebuilt 106 → 29 entries; removed fabricated attractions/events, cherry-season duplication, restricted-access assumptions, generic advice, and out-of-city padding; added dated November cultural programming. |
| `seoul.md` | **Reviewed 2026-08-17** | Rebuilt 363 → 86 entries. Removed semantic duplicates, generic venue types, out-of-city padding, and several “confirmed” 2026 dates that did not match live official pages (Seoul Forest 20th-anniversary festa was 2025; Beauty Travel Week Oct 29–Nov 4 was not the 2026 Beauty Week that ran in August; Mulbit Yeonhwa fall dates left as re-check). |
| `busan.md` | **Reviewed 2026-08-17** | Rebuilt 190 → 49 entries. Removed duplicate fireworks/coast/market entries and day trips counted as Busan. Fireworks Nov 7 confirmed on busanfireworks.com; G-STAR Nov 19–22 kept from organizer announcement. |
| `daejeon-cheonan.md` | **Reviewed 2026-08-17** | Rebuilt 210 → 44 entries. Removed Chungcheong-wide padding and duplicates. Wine EXPO Nov 6–8 confirmed on djwinefair.com; Asan / Gongju / Buyeo kept only as labeled day trips. |
| Nearby-city expansion (same day) | **Additive pass** | `pohang.md` +1 (VisitKorea-dated Fire & Light Festival Nov 20–22); `incheon.md` +2 (Incheon ArtShow Nov 19–22; My Chemical Romance Nov 7); `daegu.md` +1 (Daegu Art Festival Part 2 Nov 17–22). |
| Four-city line-by-line pass (2026-08-18) | **Re-check pass** | `seoul.md` +2 (MMCA Artist of the Year 2026 Jul 24–Dec 6; MMCA Deoksugung Lee Daewon Aug 6–Nov 8); `busan.md` +1 (National Gugak Center Busan). Corrected: Busan X the Sky fares (₩29,000/₩26,000, operator page), KOSEF 2024 dates, Grand Park festival status (예정), Daegu SAC-on-Screen time/venue unverified, G-STAR press-date nuance, BISCO-site-down notes, Anthropolis Part V after-trip. Details in `audit/PASS3-NOTES.md` Pass 24. |
| Ten-city sweep (2026-08-18) | **Re-check pass** | Suwon, Yongin, Incheon, Jeonju, Gyeongju, Ulsan, Pohang, Changwon, Yeosu, Daejeon/Cheonan — dated claims re-fetched against official pages. Corrected: KFV horror-season start dates (Apr 11, operator banners), Gyeongju NM Saturday night opening (20:00, Mar–Oct only — none in November), enriched Suwon archery/Eocha/Flying Suwon fares from the official experience page, added Sat/Sun Muye afternoon show. Added mid-October re-check calendar for the four completed cities to `itinerary.md`. Details in `audit/PASS3-NOTES.md` Pass 25. |
| Place-entry sweep to 100% (2026-08-18) | **Completion pass** | Every remaining 🔎 verified-place line in all 14 files checked against its cited official source (spot-fetches for riskiest claims). Corrected: Cheong Wa Dae closed **Tuesday** (was Monday). Ledger: 1,932/1,932 lines covered (100%). Details in `audit/PASS3-NOTES.md` Pass 26. |

## Next pass order

Re-check October 2026 calendars for every ⏳ item. Do not add entries solely to raise a count. Prefer dated organizer pages over city planning PDFs.

### Checks added after Pass 21
- **Is the frequency still current?** Daily → weekly is a real decay path (Yeongdo Bridge: daily 14:00 → Saturdays only). Treat "regular", "daily" and "every afternoon" as claims needing a date-stamped source, exactly like a price.
- **Can you even get in?** Advance-booking-only, capped party size and enforced time slots are as disqualifying as a closure (Hoam: no walk-ups; Leeum, same foundation, allows them). Never assume two venues under one operator share access rules.
- **How do you physically reach it?** Shuttles are seasonal (Everland↔Hoam suspended in winter). Verify the transport, not only the venue.
- **Is the published price the real price?** Where an operator runs a rotating monthly discount page, the gate fare is close to fictional (Korean Folk Village ₩37,000 → ₩17,000 with the public-transport discount).
- **Does the closure cover the whole site?** Namsangol closes its hanok interiors on Mondays but not its garden. "Closed Monday" can be partial in both directions.

### Checks added after Pass 23
- **Is a "national rule" still the rule?** Policy changes silently invalidate every entry that cites it. Culture Day moved from monthly to weekly on 2026-04-01; the repo had written off three usable days. Re-verify recurring national benefits, not just venue facts.
- **A local anomaly may be a national rule seen through a keyhole.** Daegu's "free every Wednesday" was recorded as a venue quirk; it was the nationwide change. When one venue contradicts the general rule, ask whether the general rule moved.
- **When frequency doubles, price often rises.** The Culture Day cinema ticket went ₩7,000 monthly → ₩10,000 twice monthly. A better-sounding benefit can cost more per use.
- **Negative-test a guard rule against the REAL regression.** Restore the sentence the rule exists to prevent; do not just mutate a keyword. `re.I` plus a nearby duplicate phrase can make a broken rule look healthy.
- **Never let an edit heredoc run chained to the commit.** Assert with a message, then grep the file to confirm the text landed. A failed edit inside `a && b && c` can still end in a commit whose message describes work that never happened.
