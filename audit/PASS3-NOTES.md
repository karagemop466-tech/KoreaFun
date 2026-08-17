# Pass 3 — re-verification + expansion working notes (2026-08-17)

Scratch ledger. Each dated claim re-checked against a live official/organizer source.

## Corrections found
| Location | Claim in repo | Source finding | Action |
|---|---|---|---|
| README.md line 81 | Wine EXPO "tastings at Hanbit Tower" | djwinefair.com: halls are Daejeon Convention Center (DCC) II | fix venue |
| events.csv Wine EXPO | hours "~10:00-18:00 typical" | official: 11:00–18:00; Nov 6 until 19:00 | fix hours |

## Verified correct (live source re-check, Aug 17 2026)
- Busan Fireworks Nov 7 — busanfireworks.com overview page "2026. 11. 07.(토)" ✓
- G-STAR Nov 19–22 BEXCO — organizer/K-GAMES announcement ✓
- MMA 2026 Nov 14–15 Gocheok, first 2-day — Kakao/Melon Jun 9 ✓
- KGMA 2026 Nov 7–8 Gocheok (3rd edition, moved from Inspire) ✓
- Cafe Show Nov 11–14 COEX; biz days 11–12, public 13–14 ✓ (matches repo)
- Yeosu World Island Exhibition Sep 5–Nov 4 ✓
- Busan Biennale Aug 29–Nov 1 ✓
- BANKSY Jul 22–Nov 3, The Hyundai Seoul ALT.1 ✓
- JTBC Seoul Marathon Nov 1, Sangam start ✓
- Seoul Outdoor Library Apr 23–Nov 1 (festival page) ✓
- Han River History Tour Apr 20–Nov 15 (festival page 396) ✓ — repo correct; the 4.3–11.30 line on the calendar index is stale
- Kings of Convenience Nov 18 Sejong Grand Theater, 20:00 ✓
- Jujutsu Kaisen in Concert Nov 7–8 Kyung Hee Grand Peace Palace (Sat 18:30 / Sun 14:00) ✓
- Leeum "Inside Other Spaces" May 5–Nov 29 ✓
- MMCA x LG OLED Christine Sun Kim Jul 31–Nov 29 ✓
- 5SOS Nov 19 KINTEX — but HALL differs by source (Hall 1 per NOL/Khan; fandom says Hall 9)
- 3rd Seoul Sculpture Festival exhibition Aug 29–Nov 30 Ttukseom/Songhyeon ✓
- BeautySum Korea Suwon Nov 5–7 Suwon Convention Center 1F ✓
- Patricia Piccinini: Kinship Jul 23–Nov 1 Suwon Museum of Art Haenggung ✓
- Incheon ArtShow Nov 19–22 Songdo Convensia ✓
- My Chemical Romance Nov 7 Paradise City ✓
- V-League 2026–27 Oct 31 – Apr 2 regular; PS Apr 5–22 ✓

## NEW corrections required
1. **KBL is no longer TBA.** KBL published the 2026–27 schedule on Aug 10, 2026: season Oct 3, 2026 – Apr 11, 2027, 54 games/team.
2. **Jamsil Indoor Gymnasium was demolished.** Seoul Samsung Thunders now share **Jamsil Students' Gymnasium** with Seoul SK Knights. seoul.md #76 and events.csv still say "Jamsil Indoor".
3. Changwon LG Sakers play no home games in October (Changwon Gymnasium refurbishment) — Nov is fine but note.
4. events.csv KBL row says "2026-27 schedule not yet published as of Aug 4, 2026" — stale.
5. README Wine EXPO venue "tastings at Hanbit Tower" → Daejeon Convention Center (DCC).
6. events.csv Wine EXPO hours "~10:00-18:00 typical" → 11:00–18:00 (Nov 6 to 19:00).

---

## Pass 3 — corrections APPLIED (Aug 17, 2026)

All items from the pending-edit queue have now been written into the repo.

### Factual corrections (things that were wrong)
1. **`README.md` + `events.csv` + `daejeon-cheonan.md` #1 — Wine EXPO venue.** Removed "tastings at Hanbit Tower". Official site (djwinefair.com/eng/0501, /1101) puts it in **DCC Hall II**, 11:00–18:00 (Nov 6 to 19:00). Added the buyers-only windows (all day Nov 6; until 14:00 Nov 7).
2. **`seoul.md` #76 + `events.csv` — KBL venue.** Jamsil Indoor Gymnasium was **demolished** (work began Mar 2026). For 2026–27 **Seoul SK and Seoul Samsung share Jamsil Students' Gymnasium**. The old "Jamsil Indoor / Jamsil Students" venue string was wrong.
3. **`busan.md` #5 + `README.md` + `events.csv` — opponent name.** "Chungnam Cheongju" → **Chungbuk Cheongju** (Chungnam Asan and Chungbuk Cheongju are different clubs; both are in K League 2).
4. **`seoul.md` #7 + `events.csv` — Cafe Show access.** Strengthened from "treated as business days" to the actual rule: **Nov 11–12 are trade-only and minors are barred**; public days are Nov 13–14 only.

### Status upgrades (⏳ → ✅), each on an official club/league source
- `seoul.md` #73, `busan.md` #6, `daejeon-cheonan.md` #3 — V-League season **Oct 31, 2026 – Apr 2, 2027** (KOVO board, Dec 10 2025).
- `seoul.md` #74 — Seoul E-Land **Nov 7 & Nov 22, both 16:30, Mokdong** (seoulelandfc.com match schedule).
- `seoul.md` #76, `busan.md` #7 — KBL season **Oct 3, 2026 – Apr 11, 2027**, released Aug 10 2026.
- `busan.md` #5 — Busan IPark **Nov 21, 14:00, Gudeok** (busanipark.com match centre).
- `daejeon-cheonan.md` #2 — Cheonan City FC vs Busan IPark **Nov 8, 14:00**, cross-confirmed on Busan's official match centre.

### Enrichment of already-correct entries
- `seoul.md` #3 Outdoor Library — Fri–Sun only; day 11:00–18:00 / night 16:00–22:00.
- `seoul.md` #4 Han River History Tour — booking mechanics (visit-hangang.seoul.kr, ≥5 days ahead, 16 courses, min 5 / max 15, 02-6953-9239) + noted the site's own stale "4.3~11.30" thumbnail.
- `seoul.md` #12 Leeum — full official title + Black Box / Ground Gallery + 11 artists.
- `seoul.md` #15 Sculpture Festival — Ttukseom Hangang Park is the main site; 15 award finalists; winners announced late Nov.
- `yongin.md` #1 Folk Village — **Fri/Sat/Sun + holidays only**; Nov 15 is the season's last night; "Adding Moonlight" named.
- `yongin.md` #8 Art Spectrum — title is now **final**, not provisional; Palais de Tokyo co-organization; 23 teams / 10 countries; side programs.

### Downgrade (honesty fix)
- `yongin.md` #7 Hyundai Translocal Series — kept, but flagged: the dates come from the Gyeonggi Cultural Foundation program announcement and the show was **not yet on NJP's own exhibition list** when checked. Re-check before travel.

### New verified entry added
- `seoul.md` #16 (new) — **Leeum, "Koo Jeong A: OUSSSMOS", Sep 5–Dec 27, 2026.** Seoul entries renumbered 16→17 onward; file now 87 entries, repo total 556. CSV rows added for this and for Art Spectrum.

### Sources that WORK for fixtures (use these, not the league pages)
- `https://www.seoulelandfc.com/match/schedule` — full season list w/ round numbers + kickoff.
- `https://www.busanipark.com/match/match_schedule.php` — same, and it doubles as a source for away fixtures (that's how Cheonan Nov 8 was cross-confirmed).
- `https://njp.ggcf.kr/exhibitions` — clean current/past exhibition list.
- `https://www.swcf.or.kr/?p=385` — Suwon Cultural Foundation full 2026 season programming table.
- `https://www.kleague.com/schedule.do?leagueId=2&year=2026&month=11` — loads but the fixture table renders client-side; returns an empty table to a fetcher. **Not usable for verification** — use club sites instead.
