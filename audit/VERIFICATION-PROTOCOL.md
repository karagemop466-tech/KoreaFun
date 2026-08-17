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
| Remaining 13 files | **Not yet manually reviewed under this protocol** | Existing content remains a research queue, regardless of earlier heuristic “SOLID” labels. |

## Next pass order

Prioritize files with the greatest current source risk: `myeongdong.md`, `yongin.md`, `suwon.md`, `jeonju.md`, `incheon.md`, `gyeongju.md`, `daegu.md`, `ulsan.md`, `pohang.md`, `changwon-jinhae.md`, then re-audit the three previously described as “core” (`seoul.md`, `busan.md`, `daejeon-cheonan.md`). This order is based on missing-source and weak-source counts, not an assumption that the later files are verified.
