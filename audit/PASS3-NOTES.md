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

---

## Pass 4 — expansion (Aug 17, 2026)

Focus: the four city files with the fewest dated trip-window events (Ulsan 0, Pohang 1, Changwon 2, Yeosu 1), plus opportunistic finds in Seoul/Gyeongju/Jeonju. Every addition below was taken from a `.go.kr` or the institution's own domain.

### Added (6 new entries, 555 → 562)
| File | # | Entry | Dates | Source domain |
|---|---|---|---|---|
| ulsan.md | 30 | 국민화가 이중섭 / Lee Jung-seop retrospective (w/ MMCA, ~100 works, ₩1,000) | Oct 15 2026–Jan 17 2027 | ulsan.go.kr |
| ulsan.md | 31 | Ulsan Philharmonic 254th subscription concert | Nov 13 2026 | ulsan.go.kr |
| gyeongju.md | 3 | Wolseong stele fragments reunited after 83 years (free) | Apr 13–Dec 31 2026 | gyeongju.museum.go.kr |
| jeonju.md | 4 | Seogosa nahan/arhat statues special exhibition (free) | Sep 16–Nov 29 2026 | museum.go.kr |
| seoul.md | 17 | Chusa Kim Jeong-hui and His Companions (free) | Aug 11–Nov 22 2026 | museum.go.kr |
| seoul.md | 18 | Newly Donated Works 2 (free) | Jul 27–Nov 15 2026 | museum.go.kr |

Ulsan previously had **no** dated trip-window entry at all; it now has two, and its header note was rewritten accordingly. Renumbering was applied and every file re-verified as sequentially numbered 1..N.

### Useful closure/scheduling facts captured
- **Gyeongju National Museum takes an irregular closed day on the 2nd Monday of November → Mon Nov 9, 2026.** Recorded in the entry.
- National Museum of Korea (Seoul) runs late to **21:00 on Wed and Sat**.
- Korean Folk Village night opening is **Fri/Sat/Sun + holidays only**, last night Nov 15.

### Checked and deliberately NOT added (negative results worth keeping)
- **Daegu International Opera Festival (23rd)** — runs Oct 2–31, 2026, i.e. it ends on trip day 1 and the finale 〈미인〉 was Oct 30–31 at Daegu Arts Center. Too marginal to sell; also the Daegu Opera House itself is closed for remodelling, which is why the festival scattered across other venues.
- **Andy Warhol: The Business of Art (Daegu)** — closes **Oct 25**, before arrival. Deliberately excluded. Its successor slot (2026 Young Artists, Nov 3–Dec 27) is already daegu.md #1.
- **Yeosu** — the city's own November 2026 culture calendar (`yeosu.go.kr/tour/culture_festa/month_event?date=2026-11-01`) renders **completely empty**. No November event exists to add yet; the Island Expo (already yeosu.md #1) ends Nov 4.
- **Changwon** — `cwcf.or.kr` month view ignores the year/month querystring and always returns the current month, so November could not be read. Not guessed. Retry `art_info_month.asp` closer to the date.
- **Ulsan Industrial Festival** — Oct 8–11, 2026, before the trip.
- **Gyeongju Daereungwon Stone Wall Festival** — April (cherry blossom), not November.
- **Jeonju Hanji Culture Festival** — spring (the Apr 17–May 17 industrial fair), not November.
- **National Museum of Korea blockbusters** — *Our Table* closes Oct 25 and *Amazing Thailand* closes Sep 6; both miss the window. Only the two free themed shows above overlap.

### Additional dead sources (do not retry)
- `sema.seoul.go.kr/ex/exList` → HTTP 500.
- `dgfca.or.kr/event/search/list` → renders nav only, no event rows to a fetcher.
- `festival.phcf.or.kr/fireWorks/intro.do` → redirects to a phcf.or.kr 404. Pohang festival dates therefore still rest on the VisitKorea KFES page only, which is why pohang.md #29 stays ⏳ — the VisitKorea page itself admits its program copy is still 2025's.
- `ulsan.go.kr/s/uac/main.ulsan` → error page; the working Ulsan venue calendar is `ulsan.go.kr/ucac/art/main.do`.

---

## Pass 5 — CONFIRMED re-verification queue (Aug 17, 2026)

Re-checked the ~24 entries still carrying an unverified ✅ CONFIRMED badge. Every one was opened against its own organizer page, not an aggregator.

### Verified clean, upgraded with hard detail
| Entry | What the source added |
|---|---|
| seoul #9 Jason Mraz | Artist site tour list: **Nov 14, Seoul at KINTEX**. Correct. |
| seoul #10 5SOS | **Replaced setlist.fm sourcing** with NOL Interpark's official notice: Nov 19, **19:30**, Hall 1, standing only, ₩143k/154k/320k, ages 12+. |
| myeongdong #1 Anthropolis IV | NTCK page confirms **Oct 28–Nov 21**, Myeongdong Theater, dir. Seo Ji-hye. |
| myeongdong #2 GanaArt Collection | SeMA listing confirms **Apr 16–Nov 22**, Seosomun. |
| suwon #2 Haenggung night opening | City page: **Fri/Sat/Sun + holidays, 18:00–21:30**, ₩2,000/1,500/1,000. Only **Oct 31 + Nov 1** are in window. |
| suwon #6 Thumbelina | Apr 28–**Nov 15**, Ilwol Arboretum. Confirmed. |
| suwon #7 Blanc Black Panorama | Feb 12, 2026–**Mar 1, 2027**. Confirmed on museum + city. |
| suwon #8 Bongsudang Banquet | Foundation calendar: standing exhibition **to Dec 31, 2026**, food-culture hall. Deep-linked. |
| yongin #9 Football City Yongin | City portal: **Mar 20–Dec 6**, Yongin City Museum, 031-6193-4796. Deep-linked. |
| jeonju #1 Yeonhui Parade | **Saturdays Apr 18–Oct 31, 15:00**, Namcheongyo→Gyeonggijeon route. Final show = trip day 1. |
| jeonju #2 Gyeonggijeon Starlight Walk | **Fridays June–Nov**; Sep–Nov entries **19:30 / 20:30**. Nov 6, 13, 20 in window. |
| daegu #3 / #5 | Annual calendar confirms **Oct 27–Nov 15** and **Sep 8–Nov 8** exactly as written. |
| gyeongju #1 / #2 | Foundation listing adds **free, 10:00–18:00 (last entry 17:30)** for both. |
| changwon #1 SAC on Screen | Programme page confirms the **November title is 늙은 부부이야기**, 15:00, **free**, B1 screening room, monthly Wednesday. |
| changwon #2 Maria Kim | **Nov 17, 11:00**, Seongsan Art Hall Small Theater, **₩20,000**, 60 min, ages 7+, sales close Nov 16. |

### Downgraded — could not be confirmed
- **yongin #7 Hyundai Translocal Series: ✅ → ⏳ ANNOUNCED BUT UNLISTED.** Second check of NJP's own exhibition page: still not listed, and NJP's *upcoming exhibitions* section is **empty**. Only the foundation's annual plan carries the Nov 5 date. Entry now tells the reader to go for 별, 괘卦 instead, which is confirmed through Feb 2027.
- **jeonju #3 Daesaseupcheong Saturdays: ✅ → ⏳ NOVEMBER DATES UNPOSTED.** The series exists and is listed May–Nov, but no November date list has been published; the related Gyeonggijeon Saturday performance is only documented for the earlier season.
- **daegu #4 SAC on Screen Othello** — kept ✅ (the Nov 7 date is on the venue's own calendar) but **removed the invented "Suchang Hall" venue and the assumed 14:00 start**, neither of which the source states.

### Added during verification
- **seoul #19 《조숙진: 지나가는 자리》**, SeMA Nam-Seoul, **Jul 29–Nov 15, 2026**, free — surfaced on SeMA's current-exhibition list while checking myeongdong #2.

### Link repair
- **pohang #29** — dead `festival.phcf.or.kr` microsite swapped for `phcf.or.kr`, with an explicit note that VisitKorea is currently the only live listing. Added venue (Yeongildae Beach), free admission, 054-289-7852.

### Newly usable source patterns
- `cwcf.or.kr/art_info/art_info_view.asp?p_idx=<N>` renders **full detail tables** (dates, times, prices, booking rules) — the Changwon month calendar is the broken part, not the site. **p_idx 9001–9004 = the Sep/Oct/Nov/Dec morning concerts.** This resolves the "Changwon has no dated find" gap.
- `w.daeguartfactory.kr/front/schedule/list.php?sc_ymd=2026` returns the **whole year** in one table (the unparameterised URL does not).
- `sema.seoul.go.kr/kr/whatson/landing?whatsonMenuDivList=EX&whenType=FROM_TODAY` lists every SeMA branch show with dates. Note `sema.seoul.go.kr/ex/exList` is a dead 500 and the per-exhibition `detail?exNo=` pages render empty.
- `suwon.go.kr/culture/ingCultureView.do?ctrSeqNo=<N>` gives full event detail incl. prices.

---

## Pass 6 — ⏳/👀 backlog triage (Aug 17, 2026)

Went through the ~78 pending items. Most are honest by design — generic venue entries that say "check the calendar" for a stadium or arts hall, which is the correct answer when fixtures genuinely aren't published. Effort went to the **entries making a specific dated claim**, since those are the ones that can be wrong.

### 🚨 Dead official domain — Korea Sale FESTA
**`koreasalefesta.co.kr` and `koreasalefesta.kr` no longer belong to the festival.** Both now serve the login screen of **"MEDIOS", a contact-lens manufacturing execution system**. The domains appear to have lapsed between editions.

This link was cited in **four files** (`seoul.md` #28, `itinerary.md`, `sources.md`, `travel-basics.md`) plus `events.csv`. All five replaced with the **korea.kr government policy newsroom**, and each now carries an explicit warning not to trust content served from the old addresses.

This is exactly the failure mode the protocol warns about: **a live HTTP 200 is not proof.** The domain resolved fine — it just wasn't the festival any more. Worth re-testing periodically on other `.co.kr` event domains.

Also note: every blog claiming firm 2026 Korea Sale FESTA dates traced back to **one content-farm domain** (`hub.greatsisyphus.com`), whose own pages contradict each other (Nov 1–15 vs Nov 1–30), claim phone calls made on dates in the future relative to the post date, and call **Nov 1 a Friday when it is a Sunday**. Ignored entirely.

### Date correction — SeMA Lynn Hershman Leeson
The city's 2026 planning PDF said **Oct 1, 2026 – Feb 7, 2027**. SeMA's own upcoming-exhibitions listing says **Oct 21, 2026 – Feb 21, 2027**. Museum's own page wins; entry upgraded to ✅ with the discrepancy documented. Full title: 《린 허쉬만 리슨: 나의 [나]들》, Seosomun main branch. Still covers the whole trip either way.

### Price correction — Myeongdong NANTA
File listed "Premium ₩70,000, VIP ₩60,000, S ₩50,000, **A ₩40,000**". The operator's own page lists **VIP ₩70,000 / S ₩60,000 / A ₩50,000** — three tiers, not four, and different tier names. Corrected. Also upgraded ⏳ → ✅: it is an **open run** playing daily since Oct 2009, so there was never a "November 2026 schedule" to wait for. Times captured: Mon–Fri 17/20, Sat 14/17/20, Sun+holiday 14/17.

### Upgraded ⏳ → ✅ with real programme detail
- **seoul #20 Seoul Grand Park Autumn Festival** — festival page found (`festacode=465`). Themed 《예술로 물드는 피노키오의 숲》; forest open-air gallery among the maples, participatory installations, acoustic concerts. **Oct 31–Nov 8**, opens on arrival day. Tel 02-500-7335.
- **daegu #35 Daegu Art Festival Part 2** — venue confirmed as **Daegu Culture & Arts Center exhibition rooms 6–13**, Nov 17–22.

### Left ⏳ deliberately — and why that is the right answer
- **seoul #25 Changgyeonggung Mulbit Yeonhwa (fall).** Only the **spring** run (Apr 24–May 3) has an official Korea Heritage page. The Sep 8–Nov 8 fall window appears **only on blogs**, and the one detailed source visibly mixes in **2025** dates. The existing entry already says "do not treat as confirmed" — that wording stands and is correct. Note the 2025 fall run was Sep 10–Nov 8, so a similar 2026 window is plausible but must not be stated as fact.
- **seoul #21/#22 Seoul Craft Museum.** The museum's own site is **down** — `craftmuseum.seoul.go.kr/main` returns HTTP 502 and every sub-path 404s. Only a February press release about the 2026 roadmap exists, and it names exhibitions without firm dates. Nothing verifiable to add.
- **Sports entries** (FC Seoul, KBO Korean Series, Pohang Steelers, Daegu FC, NC Dinos, LG Sakers, KT Sonicboom, Ulsan HD, Gyeongnam FC, Jeonbuk, WKBL). League fixture sites render client-side and remain unreadable; postseason entries are genuinely undetermined until October. ⏳/👀 is accurate.
- **Yeosu Big-O Show / Expo site.** `expo2012.kr/kor/main.do` now **404s**. No replacement schedule found; left ⏳ rather than guessing.

### Newly confirmed dead/unusable URLs
- `koreasalefesta.co.kr`, `koreasalefesta.kr` — **repurposed, not merely dead.**
- `craftmuseum.seoul.go.kr/main` → 502; `/exhibition/current`, `/kor/html/sub02/0201.html` → 404.
- `sema.seoul.go.kr/ex/exList` → 500; `sema.seoul.go.kr/kr/whatson/exhibition/detail?exNo=<id>` renders an **empty shell** (fields blank, "상시") — the *landing* list URL is the only usable SeMA endpoint.
- `expo2012.kr/kor/main.do` → 404.
- `kh.or.kr/kha/programs/list.do` → error page.
- `seoulcraftmuseum.org` → fetch failure.
- `grandpark.seoul.go.kr/main/ko.do` → 500. Use `festival.seoul.go.kr` instead.
