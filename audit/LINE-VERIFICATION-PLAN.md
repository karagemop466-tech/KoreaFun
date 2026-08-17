# Line-by-line verification plan

**Goal:** every factual line in all 14 city files checked against an official
or trusted source, with a durable, tamper-evident record of what was checked,
when, and against what.

---

## 1. The scale (measured, not estimated)

| Metric | Count |
| --- | --- |
| Entries | 570 |
| Non-blank body lines | **1,803** |
| — carrying a checkable claim | **1,231 (68%)** |
| — pure prose/advice (nothing to verify) | 572 (32%) |
| Source (URL) lines | 572 |
| Distinct source domains | 315 |
| **Already covered** (seeded from 101 entry-level verifications) | **496 (27%)** |
| **Remaining unchecked** | **1,307** |
| — of those, hard claims (price/time/date/access) | **425** |
| — of those, source URLs to test | ~590 |

The 425 hard-claim lines are the ones that can ruin a day (wrong price, wrong
hours, closed that weekday). They are the priority; prose is marked `prose`
in bulk and costs nothing.

---

## 2. How verification is recorded

`tools/lineledger.py` + `audit/line-ledger.json`.

Each row is keyed **`file#entry:sha1(line-text)`**. The hash is the mechanism
that makes this trustworthy:

> **Any edit to a line changes its hash, so the old row retires and the line
> reappears as `unchecked`.** A verified line cannot silently drift. If an
> edit is reverted, the original row is *revived with its verdict intact*.

This was tested in both directions before adoption (mutate → requeues;
restore → revives).

### Verdicts

| Verdict | Meaning |
| --- | --- |
| `unchecked` | not yet looked at |
| `verified` | claim checked against a source and correct |
| `corrected` | claim was wrong; the **rewritten** line is what carries this mark |
| `sourced` | a URL line that was fetched and does support the entry |
| `dead` | URL unreachable/404 — needs replacing |
| `unresolved` | checked, but **no authoritative answer exists yet** (honest state, e.g. K League fixtures, Kimjang dates) |
| `prose` | no factual claim to verify |

`unresolved` matters: some questions are correctly unanswerable, and the
right output is the mechanism plus when to re-check — not a fabricated
answer.

### Commands

```bash
python3 tools/lineledger.py init      # rebuild rows after any edit (idempotent)
python3 tools/lineledger.py stats     # coverage overall + per file
python3 tools/lineledger.py plan      # domain-grouped work batches
python3 tools/lineledger.py next 15 seoul   # next lines to work
python3 tools/lineledger.py entry seoul.md#39   # one entry, line by line
python3 tools/lineledger.py mark <key> verified "<url>" "<note>"
python3 tools/lineledger.py audit     # integrity: marked-without-source, dead, unresolved
python3 tools/lineledger.py report    # regenerate audit/VERIFICATION-STATUS.md
```

---

## 3. Batch, don't grind line-by-line

Working strictly top-to-bottom would mean re-fetching the same site dozens of
times. **Batch by source domain** — one fetch clears several lines at once:

| Lines | Domain | Files served |
| --- | --- | --- |
| 37 | `yeosu.go.kr` | yeosu |
| 28 | `tour.jeonju.go.kr` | jeonju |
| 17 | `incheon.go.kr` | incheon |
| 17 | `suwon.go.kr` | suwon |
| 16 | `english.visitbusan.net` | busan |
| 16 | `gyeongju.go.kr` | gyeongju |
| 16 | `pohang.go.kr` | pohang |
| 14 | `hc.unesco.org` | 5 files |
| 14 | `english.visitseoul.net` | myeongdong, seoul |
| 14 | `yongin.go.kr` | yongin |

The top ~10 domains cover ~190 source lines. Cross-file domains
(`hc.unesco.org`, `kbl.or.kr`, `koreabaseball.com`, `knps.or.kr`) are
especially efficient and also catch cross-file drift.

### The unit of work: one entry, all its lines

Domain batching selects *which* entries to pull up, but the actual pass is
**entry-shaped** — open an entry, verify every line in it, mark them all,
move on. This is what caught the Jangyongyeong ceremony ending before the
trip: the answer was on the same page, three lines below the line being
checked. Reading whole pages, and whole entries, is where the findings are.

---

## 4. Session structure

Roughly 40–60 claim-lines per working session, in this shape:

1. `lineledger.py plan` → pick the top unchecked domain.
2. Fetch that domain's key pages **once**; read them fully.
3. Work every entry that cites it, line by line.
4. Rewrite wrong lines; add the missing detail that makes the line usable.
5. `parse_entries.py` → `lineledger.py init` → `verify_claims.py`.
6. Bulk-mark the batch; commit with the finding in the message.
7. `lineledger.py report` to refresh the public status table.

**Ordering across sessions** — thinnest coverage and highest risk first:

| Priority | Files | Why |
| --- | --- | --- |
| 1 | `pohang`, `daejeon-cheonan`, `gyeongju`, `changwon-jinhae`, `ulsan` | lowest coverage (10–16%) |
| 2 | `incheon`, `daegu`, `yeosu`, `jeonju` | mid coverage, many hard claims |
| 3 | `busan`, `myeongdong`, `yongin`, `suwon` | partially done |
| 4 | `seoul` | already 51%, but the largest file |
| 5 | guide files (`README`, `itinerary`, `travel-basics`, `walking-maps`) | not entry-shaped; audited separately — Pass 10 found 7 wrong claims here |

---

## 5. Standing rules (learned the hard way)

- **Prefer the operator** over aggregators, and over the city tourism page.
- **Read the whole page**, not the matching line — adjacent facts are where
  the findings are.
- **Re-test "dead" sources.** `craftmuseum.seoul.go.kr` and
  `seoulsky.lotteworld.com` were both written off, and both work. A 502 is a
  snapshot, not a verdict. Only one *path* is usually dead.
- **Check the season.** November is the winter schedule for most heritage
  sites — quoting summer hours has caused two real errors already.
- **Silence about price is a defect.** 77 ticketable venues state neither a
  price nor "free"; readers assume free.
- **A hedge is not neutral.** "Confirm admission" reads as "probably free".
- **Verify the scope of a restriction** — over-correction is also an error.
- **A correction in one file does not propagate.** Run `verify_claims.py`.
- **Audit the correction log itself** — one logged "fix" ran backwards.
- **An honest range beats a confident wrong number** (Dae Jang Geum Park).
- **The ledger is line-shaped, so it cannot see a missing fact.** CSAT day was
  invisible to it. Periodically ask what *isn't* in the guide.

---

## 6. Definition of done

- `lineledger.py stats` → 100% covered, every file.
- `lineledger.py audit` → zero marked-without-source; zero undated; every
  `dead` line replaced; every `unresolved` line carries a re-check trigger.
- `verify_claims.py` passes; `parse_entries.py` still reports 570 entries.
- `audit/VERIFICATION-STATUS.md` regenerated and committed.
