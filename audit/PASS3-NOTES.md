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

## Pass 7 — Pohang deep pass (Aug 17)

Pohang was the weakest file in the repo: 29 entries and **zero ✅ CONFIRMED**. Root cause was a dead
source, not a lack of real events — the old microsite `festival.phcf.or.kr` 404s, so earlier passes had
nothing authoritative to cite and left everything at ⏳.

**Breakthrough:** `phcf.or.kr` (Pohang Cultural Foundation) is fully server-side rendered and exposes
per-festival detail pages keyed by a stable id:
`phcf.or.kr/phcf/festival_detail/view.do?festivalId=<ID>` and
`phcf.or.kr/phcf/festival/submain.do?festival_id=<ID>`, indexed from
`phcf.or.kr/phcf/current_festivals/view.do`. This is now the canonical Pohang source.

### Corrections
| # | Change |
|---|---|
| pohang 29 | **Dates corrected Nov 20–22 → Nov 14–22, 2026**; ⏳→✅. Organizer's own 2026 page states `2026. 11. 14(토) ~ 11. 22(일)` with **국제불꽃쇼 on Sat Nov 21**. VisitKorea still shows only Nov 20–22 and openly labels its program copy as 2025 content. Renamed to the correct English title (Fireworks, not "Fire & Light"). Dead `festival.phcf.or.kr` link removed from the entry and from events.csv. |

Documented the volatility explicitly: this festival has run in **June 2025, late May 2024, July 2018 and
November 2021** — any date found outside the 2026 page is worthless. Also noted the 2025 edition had its
last two days cancelled for weather.

### Additions
| # | Entry | Status |
|---|---|---|
| pohang 30 | **Pohang Steel Art Festival 2026**, Oct 24–Nov 15 | ✅ dates posted; venue/theme still 미정 |
| pohang 31 | **Pohang International Music Festival** | 👀 WATCH — 2026 dates unposted |

Music festival left at WATCH deliberately: it hits the trip window every year (2024 Nov 1–8, 2025 Nov 7–13)
but the foundation page still renders the **2025** run and the festival's own domain `mfph.kr` **404s**.
Recorded the useful planning fact that 2025 tickets were free and sold out in eight minutes.

Counts: pohang 29 → 31, total 563 → 565. events.csv 166 → 168 rows.

### Dead ends found this pass
- `poma.pohang.go.kr` (Pohang Museum of Steel Art) — **WAF-blocked**, every path returns a firewall
  interception page. Not link rot; do not retry.
- `phcf.or.kr/performance/list.do` and `/phcf/culture_event/list.do` → "잘못된 접근" error page.
  The working city-wide listing is **`pohang.go.kr/portal/prfrmexhbt/list.do?mid=0206050000`**.
- `mfph.kr` — 404.

## Pass 8 — Yeosu deep pass + backlog clearance (Aug 17)

### The important catch: Big-O Show no longer exists as a ticketed product
`yeosu.md` #12 described a **ticketed** multimedia show and warned it "is not a free nightly fountain."
That is now backwards. Yeosu City's official listing is titled **빅오 해상분수쇼** and states
*"해상분수쇼는 남녀노소 누구나 자유롭게 관람이 가능합니다."* Korean coverage attributes the change to the
cost of staging the full production. The ₩18,000–25,000 P/S-seat prices still all over blogs and
aggregators describe a **discontinued** show.

Also pulled the real operating rules, which materially change planning:
**Apr 18 – Nov 8 2026, Wed–Sun only, closed Mon/Tue, 20:00 in November.**
Within the Oct 31–Nov 22 trip that leaves only **Nov 4, 5, 6, 7, 8**. Entry rewritten and upgraded to ✅.

### Yeosu Island Expo — hours, prices and a day-by-day for the overlap
`yeosu2026.or.kr` is server-rendered and exposes `/content/4_1` (hours + full price table) and
`/expo_schedule` (day-by-day programme grid). Added official hours (main venue 10:00–21:00, last entry
20:00; sub-venues 10:00–18:00) and the full price ladder (₩15,000/9,000/6,000 standard, group and
concession tiers, ₩32,000 family) to #1, plus a readiness warning — Korean reporting through mid-2026
repeatedly flagged construction delays and thin facilities on the sub-venue islands.

### Additions
| # | Entry | Status |
|---|---|---|
| yeosu 33 | **Yeosu Night Sea Fireworks Festival**, Sat Oct 31 | ✅ |
| yeosu 34 | **2026 Yeosu Island Food Festival**, Sat Oct 31 | ✅ (title + date only) |
| yeosu 35 | **Day-by-day guide to the Oct 31–Nov 4 Expo overlap** | ✅ |
| seoul 91 | **SeMA Seoseoul 《김희천: 두더지들》**, Aug 20–Nov 8 | ✅ |
| suwon 38 | **정조테마공연장 마당놀이터**, to Nov 7 (+정조 K 스테이지 to Nov 1) | ✅ |

The fireworks festival is a genuinely valuable find: it lands on **arrival day**, and the Expo schedule
puts it and the island food festival at the same site on the same evening. Corroborated by the mayor's
Nov 2025 statement that the 2026 edition would move into the Exhibition period. Note the dedicated
microsite `yeosu.go.kr/ysff` **still shows the 2025 event**, so the Expo schedule is the citable source.

Yeosu #31 city-tour bus upgraded ⏳→✅ with the official night-course timetable effective Sep 1 2026,
fares (₩10,000/₩5,000) and operator phone — plus the seasonal catch that the Odongdo stop is not run in
winter and its music fountain is Mar–Oct only, substituted with the Hamel Lighthouse.

### seoul #25 Changgyeonggung Mulbit Yeonhwa — RESOLVED ⏳→✅
Previous passes could not confirm the autumn run and correctly refused to trust the blogs. The
**Korea Heritage Agency's own** Changgyeonggung programme page (`kh.or.kr/cms/content/view/1526`)
publishes the 2026 전체상영 schedule: **Apr 24–May 3** and **Sep 8–Nov 8, starting 16:40**.
So the autumn window the blogs claimed was right, but it is now sourced from the operator.

Critical planning consequence captured in the entry: the **full 8-scene show ends Nov 8**, and outside
the 전체상영 windows the programme drops **제2경 대춘당지 and 제5경 소춘당지** — the two headline water
pieces. Also captured: ₩1,000 entry (free under 24 / over 65 / hanbok), no booking, closed Mondays,
20:00 entry cutoff, no parking until Dec 31 2026, and the official rain rule (3 mm+ forecast at 13:00
cancels scenes 2 and 5).

Counts: total 565 → 570. events.csv 168 → 174 rows.

### Dead ends this pass
- `craftmuseum.seoul.go.kr/exhibition/current` — still the museum's own "page not found". Seoul Craft
  Museum (#21/#22) stays ⏳; **still no basis to confirm those exhibition windows.**
- `kh.or.kr/cont/view/fest/month/menu/210?searchDate=202611` — service-error page. The month calendar
  needs a valid `idx`; the durable source is the per-palace CMS page `cms/content/view/1526`.
- `mfph.kr` 404 (from Pass 7) unchanged.

---

## Pass 10 — hallucination hunt inside already-✅ content (price/phone claims)

Earlier passes all asked the same question: *"can I promote this ⏳ entry to ✅?"* That question never
re-examines material already marked good. Pass 10 inverts it: **take the falsifiable claims the repo
already asserts as fact and try to break them.** Two claim types are cheap to falsify — prices and
phone numbers — so those were swept exhaustively (`grep '₩[0-9]'` → 50 hits; a phone-format grep → 10).

The hit rate was alarming. **Seven of the ~12 hard claims checked were wrong**, and every one of them
sat in a file no pass had ever audited, because `walking-maps.md` and `travel-basics.md` contain no
`### N)` entries and so are invisible to the per-entry verification protocol.

### Corrections made

| Claim | Repo said | Actually | Source |
|---|---|---|---|
| N Seoul Tower observatory | ₩21,000 | **₩29,000** / ₩23,000 child-senior | `nseoultower.co.kr/visit/use2.asp` |
| Seoul Sky (Lotte World Tower) | ₩31,000 | **₩33,000** / ₩29,000 youth-senior | `seoulsky.lotteworld.com/price/info/ticket` |
| Songdo Marine Cable Car | ₩17,000 / ₩22,000 crystal | **₩19,000 / ₩24,000** | `busanaircruise.co.kr` price panel |
| Hanbit Tower observatory | ₩2,500 | **free since June 2021** | Daejeon Marketing Corp. announcement |
| The Art Space 193 | ₩15,000, presented as open | **현재 미운영 — not currently operating** | Shinsegae store page `storeCd=SC00060` |
| BANKSY: Still Here | ₩18,000 adult | **₩23,000 adult**; ₩18,000 is the 3–18 rate | Interpark/NOL + YES24 ticket notices |
| Museum Kimchikan class | "~₩16,000" stated flatly | unverifiable — now flagged, base fees added | kimchimuseum listings |

Verified-correct and left alone (now carrying hours as well): Namsan Cable Car ₩15,000/₩12,000;
Busan Tower ₩12,000/₩9,000 (rebranded *Busan Diamond Tower*); Gyeongbokgung/Changdeokgung ₩3,000
(+₩5,000 Huwon); Gwangjang Market street-food ballparks; Cheonan City FC **Sun Nov 8, 14:00 vs Busan
IPark** (K League 2 R32 — the fixture is real).

**Palace-fee warning for future passes:** the National Heritage Agency announced on Aug 5 2026 that it
will publish a new palace/tomb fee schedule **in November 2026**, effective **Jan 1 2027**. The ₩3,000
prices are correct *for this trip* but will be stale immediately after it. Do not "helpfully" update
them to a rumoured number — nothing is published yet.

### A date claim the guides asserted but the city file forbade

`walking-maps.md` billed Hanbit Plaza as the "anchor site for … Noodle Festival **Nov 7–9**", and
`itinerary.md` built Day 8 around a "⏳ Nov 7–9 pattern". But `daejeon-cheonan.md` #4 explicitly says
2025 ran Nov 7–9 and **"do not copy that weekend into 2026"**. `noodle-dj.com` re-fetched this pass is
still titled *2025 누들대전축제* with 2025-dated programme blocks. The caveat had been written once, in
the city file, and then quietly contradicted by the two files a traveller actually reads on the day.
Both now state the dates are unannounced.

### Method note carried forward

An official page can itself be wrong (Pass 10's yongin #9: the city portal prints the malformed phone
number `031-6193-4796`; the museum's real number is **031-324-4796**, corroborated across four
independent sources). Where the repo faithfully copied an upstream error, the entry now documents the
error rather than silently substituting the right value.

**Structural lesson:** verification coverage was being measured in ✅ badges, but the badge system only
covers `### N)` entries. The two guide files that carry the most day-of-operational detail
(`walking-maps.md`, `travel-basics.md`) have no badges and had therefore never been checked once.
`travel-basics.md` (8 remaining ₩ claims) is the next target.

---

## Pass 11 — verifying the claims the traveler actually acts on

Pass 10 showed the badge system hides unverified material. Pass 11 applies that lesson to the
570 entries themselves. Verifying all 570 by hand is not achievable in one sitting, so the pass
triages by **consequence**: a wrong opening time for a free park costs nothing, a wrong date for a
₩175,000 sold-out concert costs the trip. Two new tools rank the work instead of guessing:

- `tools/risk_triage.py` — flags entries by hallucination risk signals (asserts a 2026 date, sourced
  only from an aggregator, no official domain, bare-homepage "proof"). 360 of 570 carry at least one
  flag; 238 rest on a bare homepage, which cannot prove an event exists.
- `tools/clash_check.py` — finds single-day events colliding across city files. Per-entry review can
  never catch these, because each entry is individually correct.

### travel-basics.md — the other unbadged file

Same blind spot as `walking-maps.md`. Corrections: T-money card fee (~₩3,000–4,000, non-refundable,
not "~₩4,000"); KTX Seoul–Busan pinned at **₩59,800** with the ₩52,600 SRT alternative; taxi entry
gained the **22:00–04:00 surcharge (40% at 23:00–02:00)** and out-of-city surcharge.

The serious fix was the Climate Card. Prices were right, but the entry said only "excludes KTX and
intercity buses" — omitting that **the Incheon Airport AREX stretch is not covered** (only Gimpo–Seoul
Station), nor AREX Express, nor the Shinbundang Line, nor GTX, nor 광역 buses. A traveler landing at
ICN on Oct 31 holding a Climate Card would have been stuck at the gate.

### Confirmed correct — no change

Busan Fireworks **Nov 7** (busanfireworks.com's own countdown), G-STAR **Nov 19–22**, MMA **Nov 14–15**,
Cafe Show **Nov 11–14**, Busan Biennale **Aug 29–Nov 1**, Sculpture Festival exhibition **to Nov 30**,
Folk Village night season **to Nov 15**, palace fees **₩3,000** (+₩5,000 Huwon), Cheonan FC **Nov 8**,
Busan IPark **Nov 21 vs Chungbuk Cheongju**, E-Land **Nov 7 vs Jeonnam 16:30**.

### Wrong or dangerously incomplete — fixed

| Entry | Problem |
|---|---|
| incheon #43 MCR | Date right, but entry omitted that it was **postponed from Apr 18** and is **effectively sold out**. Added prices and ualive's resale-voiding policy. |
| seoul #5 KGMA | "Organizer announcement" with no link → replaced with official `kgma-is.com`. That site still shows **stale Inspire Arena shuttle info** from the prior edition; flagged. |
| seoul #9 Jason Mraz | Bare artist page → NOL listing with hall, 19:00, standing-only prices. |
| seoul #13 MMCA | Vague "site-specific digital work" → full title, artist, 72-panel OLED spec. |
| yongin #2/#3 | **No mention of the 13+ age limit** or health restrictions on either horror attraction. |
| itinerary Nov 21 | Said "Busan IPark vs **Chungnam** Cheongju" — not a real club. `busan.md` and README both correctly say **Chungbuk** Cheongju. Exactly the 충북/충남 conflation `AUDIT-FINDINGS.md` warns about, surviving in the one file a traveler reads on the day. |
| itinerary Nov 1 | Still told the reader to "**re-check** whether Mulbit Yeonhwa is running" — Pass 8 resolved that weeks ago. Replaced with the confirmed run plus the rain rule. |

### What the clash detector found

**Nov 7 holds five confirmed events across four cities** — Busan Fireworks, KGMA Day 1, MCR at
Paradise City, E-Land vs Jeonnam, plus Wine EXPO Day 2. Every entry was individually accurate and
none of them said so. The itinerary now lists all five and states plainly that four must be dropped.

**Nov 22 is departure day** and carried four events including E-Land's 16:30 finale in Seoul while the
plan has the traveler in Busan — Busan→Seoul is 2.5 hrs, ICN another ~1.5. Marked unrealistic, with
Incheon ArtShow noted as the one option actually near the airport.

**Structural lesson:** correctness per entry is not correctness of the guide. Both of these were
composition errors invisible to any per-entry check.

### Pass 11b — the cross-file consistency problem, confirmed as systemic

Three separate bugs this pass shared one shape: **a city file was right and the file the traveler
actually reads on the day was wrong.**

1. `busan.md` and README said Busan IPark host **Chungbuk** Cheongju on Nov 21. `itinerary.md` said
   **Chungnam** — a different club entirely, and precisely the 충북/충남 conflation `AUDIT-FINDINGS.md`
   already warns about.
2. `daejeon-cheonan.md` #1 carried a note saying the Hanbit Tower venue error "has been corrected."
   It had been corrected *in that entry only*. `itinerary.md` Day 7 and `walking-maps.md` line 139
   still sent the reader to Hanbit Plaza for the Wine EXPO, which is at DCC Hall II.
3. `itinerary.md` Day 2 still instructed the reader to "re-check whether Mulbit Yeonhwa is running"
   three passes after Pass 8 confirmed it.

A fix is not done when the entry is fixed. `tools/clash_check.py` and the grep discipline in the
Errors section exist because of this, and both need running whenever a claim changes.

**Also corrected:** the Wine EXPO buyers-only rule was overstated in the opposite direction — the
entry told the reader Friday was closed to the public when only the *business zone* is restricted.
Over-warning is a real cost too: it deletes a usable day from a 23-day trip.

**Verified, no change needed:** ulsan #30 Lee Jung-seop, gyeongju shared-gallery run to Dec 13,
jeonju #2 session times, suwon #1 dates, busan #5 and seoul #78 fixtures.

**Queue still open:** busan #6 (V-League fixtures unreleased), daegu #3/#5, daejeon #3, gyeongju
#1/#2, myeongdong #3, seoul #1/#2/#6/#8/#10/#11/#77, yongin #5/#6/#8; remaining travel-basics FX and
transfer-cost claims.


### Pass 12 — individual entry verification begins

Started the one-by-one sweep with `tools/ledger.py`, which gives every entry its own verdict,
sources, check date and note, and marks an entry **stale** if its text changes after being verified
(so an edit cannot silently inherit an old pass).

**seoul #2 JTBC Marathon — wrong start time.** Guide said 07:30; organizer and registration
listings say **08:00**. Fixed in `seoul.md`, `README.md`, `itinerary.md` and `events.csv`. Also added
the road-closure warning: the course runs Sangam→Yeouido→Gangnam→Jamsil across the first full
morning, so buses/taxis are unusable until early afternoon.

**seoul #11 Jujutsu Kaisen — stub upgraded.** Three lines and a bare link became: Sat 18:30 /
Sun 14:00, 140 min, five price tiers, **ages 14+ hard cutoff**, and the observation that the Sunday
matinee dodges the four-way Nov 7 clash.

**seoul #21/#22 Craft Museum — a dead source came back.** Earlier passes recorded
`craftmuseum.seoul.go.kr` as entirely down and left both entries stranded on a city planning PDF.
**The site is reachable again.** #21 is now a real entry built from the museum's own exhibition list
(three shows confirmed to run during the trip, free admission, Monday closure, no car park). #22
stays provisional but now cites the SMG annual-plan PDF that actually names 《공예풍경(가제)》 with the
Oct 26–Nov 15 window — and states plainly that the museum's live page does not list it yet.

**Lesson: re-test dead sources.** A host that 502s during one pass may simply have been having a bad
day. The "broken URL" list in this file is a snapshot, not a permanent verdict.


### Pass 13 — sweeping the four untouched files

Daegu, Myeongdong, Yeosu and Changwon-Jinhae had **zero** individually-verified entries. All four
now have their dated/bookable entries checked against operator sources.

**The pattern in Daegu: badged ✅ CONFIRMED while the body said "verify this."** daegu #4 (SAC on
Screen *Othello*) asserted the date but left start time, price and booking method as "confirm on the
notice board." The operator publishes all three: **14:00, Suchang Hall 3F, free, no reservation,
first-come, arrive 10 minutes early** — and it is the final film of a 16-title season. A ✅ badge
should mean the entry is actionable, not merely that a date exists.

**The find in Changwon: an entry pointing at nothing.** #27 Gyeongnam FC said "confirm home fixtures
through the league." The club's own fixture list shows **no home game a visitor can attend**: the
Oct 31 home match is arrival day, Nov 7 and Nov 21 are both away, and the next home game is Nov 29 —
a week after departure. Now stated outright and redirected to Busan IPark (Nov 21) and Seoul E-Land
(Nov 7), both already verified.

**Yeosu came out clean.** #33 fireworks and #34 island food festival both appear *verbatim* in the
10.31 엑스포장 cell of the organizer's schedule, and #35's day-by-day breakdown matched the official
table line for line including the Nov 4 폐막식 and the Oct 30–Nov 1 yacht regatta. Whoever built these
entries worked from the primary source.

**Myeongdong #1** gained what a ticketed run needs: Korean premiere of Schimmelpfennig's five-play
cycle, director, the fact that it is **Korean-language with no surtitle information published**, the
booking line's limited hours, and the 푸른티켓 ₩5,000 under-24 fare.

**Running total: 62/570 individually verified.** Still no fabricated events found — the failure mode
remains staleness, omission, and detail left unfinished.


### Pass 14 — prices, fixtures, and a correction that ran backwards

**The worst find so far is a "fix" that made things wrong.** `sources.md` carried the row
*"Busan X the Sky — Prices corrected (₩27,000 → ₩29,000)"*. Visit Busan's official listing gives
**₩27,000 adult / ₩24,000 child-senior**. So an earlier pass took the correct figure, replaced it
with a wrong one, and logged that as a correction — the audit trail actively asserted the error.
Both `busan.md` and `sources.md` are fixed, and the row now records which direction is right.

That prompted auditing every other price correction logged in `sources.md`. The other two were
genuine: Korean Folk Village ₩25,000 → **₩37,000** (operator fare page) and Wooyang ₩8,000 →
**₩15,000** (VisitKorea). Both rows now carry the full breakdown and a verification date so the
direction cannot be misread again. **A correction log is only useful if the corrections are audited
too.**

**New tool: `tools/verify_claims.py`.** Every serious bug here has had one shape — a fact fixed in
the city file while `itinerary.md` / `README.md` / `events.csv` keep the old value. This pass an
itinerary edit *silently failed its assertion* while the ledger recorded it as done, which is the
same failure wearing a different hat. The tool encodes the multi-file facts as assertions and fails
loudly on drift. Tested by re-injecting the original Chungnam/Chungbuk bug — it catches it and
exits 1. Run it after any pass that changes a claim.

**Entries that pointed at nothing, now resolved:**

| Entry | Was | Now |
|---|---|---|
| suwon #35 | "check official fixtures" | **Two real home games**: Suwon Samsung (top of K League 2) host Yongin Nov 8 and Gyeongnam Nov 21, both 14:00. Both clash with existing plans; said so. |
| busan #11 | "confirm on the operator site" | Full post-May-2026 fares: Beach Train ₩10,000–16,000, Sky Capsule ₩50,000–60,000/capsule, package ₩73,000–111,000, first departures moved earlier. |
| yongin #1 | "use the operator's live pages" | ₩37,000/₩30,000/₩26,000, ride access included, and the fact that advance online booking is **20–30% cheaper than the gate**. |

**incheon #42 resolved the departure-day problem.** INAS runs Nov 22 **10:00–18:00, last entry
17:00**, at Songdo Convensia ~30–40 min from ICN. Of the four events competing for that date it is
the only one compatible with a flight — G-STAR is in Busan and the E-Land finale is in Seoul.

**69/570 verified. Still zero fabricated events.**


### Pass 15 — the four thinnest files, and a league-wide structural answer

**Five entries in five cities all said "check official fixtures" for K League 1 clubs.** The league's
own competition regulations explain why none of them could be answered: 2026 runs a **33-round
regular phase to Oct 25**, then a **Final Round (34–38) from Oct 31 to Dec 6**, and those last five
fixtures are only drawn *after* the regular season ends. So at review **no November date existed for
any K League 1 club** — Pohang, Jeonbuk, Ulsan HD, FC Seoul, Daejeon Hana alike. Any site publishing
one is guessing.

What *is* knowable, and now stated in all five entries: the final-round window **covers the entire
trip**, and each club is allocated **2–3 home games** within it, so each of these clubs will probably
host while the travellers are in Korea — the date simply cannot be known until the league's
single late-October announcement. **"We can't know yet, here's exactly why, here's when to look" is
a better answer than "check the fixtures."**

This also surfaced a conflation risk: `seoul.md` has **FC Seoul** (K League 1, no dates possible) and
**Seoul E-Land** (K League 2, Mokdong, Nov 7 and Nov 22 *already confirmed*). Entry #79 now says so
explicitly.

**Gyeongju: "the museum is free" was half true.** Gyeongju Arts Center runs free and ticketed
galleries simultaneously — Gallery Dal (B1) and Gallery Space I (4F) are free, but Gallery Hae (4F)
headline shows charge (₩10,000 adult for the 2026 한수원 special). Entry #2 now tells you to check
which gallery a show is in. The weekend shuttle bus also ran only Aug 13–Oct 18 — finished before
the trip.

**Clean confirmations:** gyeongju #1, jeonju #4 (the Seogosa arhat show matched the museum page
exactly, 가제 marker included), ulsan #31 (Philharmonic Nov 13 — recovered via the city culture
portal after the venue's own page proved to be an empty client-rendered shell; gained 19:30–21:15
runtime, age rating, phone).

**78/570 verified. Every city file now has multiple verified entries. Still zero fabrications.**

## Pass 16 — trip-wide finding: CSAT day, and priced-place verification

### The big one: Nov 19 is 수능 (CSAT) day and the repo never mentioned it
Grep confirmed zero occurrences of 수능/CSAT/Suneung across every .md and
events.csv before this pass. The 2027 CSAT is fixed for **Thu Nov 19, 2026**
(MOE, korea.kr/briefing/pressReleaseView.do?newsId=156646031) — day 20 of the
trip, and the day the itinerary moves Seoul→Busan by KTX.

Why it matters even though it is NOT a public holiday:
- **Nationwide aircraft ground-stop ~13:05–13:40** during English listening.
  Consistent across 2024/2025/2026 exams; 140–156 flights retimed each year.
- Public offices and most big firms start **10:00**, subways add trains
  06:00–08:10 → the usual morning crush shifts.
- **No vehicles within 200 m of any test centre**, and test centres are
  ordinary neighbourhood schools → unpredictable taxi detours all morning.
- Post-exam evening (~17:40 on) is one of the liveliest nights of the year.

Added as travel-basics §6b, an itinerary Day-20 warning, and a README month-
table row. Encoded as **claim #8 in tools/verify_claims.py** across all three
files, negative-tested in both directions (removing the itinerary phrase and
altering the 13:05 time each produce exit 1).

Lesson: **the ledger is entry-shaped, so it cannot surface a missing
trip-wide fact.** Every entry can be individually correct while the guide
omits something that reshapes a whole day. Worth a deliberate sweep for
date-specific national events (elections, exam days, holidays) rather than
waiting for an entry to imply them.

### Priced/hours place entries (the new worklist)
Fixed the triage script (entries.json `body` is a list of lines — join before
regex). 261 unchecked entries assert a price, an opening time or a closed-day.
Worked the top of that list:
- suwon #26 Ilwol Arboretum — ₩4,000 adult confirmed; **over-65s and under-7s
  free with ID** was missing.
- yongin #10 Everland — entry said "don't assume ₩62,000" but gave no number.
  Now carries the real season-tier table (A/B/C/D 62/52/46/68k) plus the fact
  that telecom and card discounts (40–50%) don't stack.
- suwon #14 Yeonmudae archery — ₩3,000/10 arrows confirmed; trip falls in the
  **winter** season (to 17:00, not 17:30), half-hourly slots, no 12:00–13:00.
- myeongdong #3 NANTA — prior pass's price correction re-verified as correct.
- incheon #14 Maritime Museum — hours right, but **two Greece exhibitions run
  the whole trip** and were absent from the entry.
- incheon #13 Emigration History — closure rule was wrong-by-omission: also
  **closed the day after any public holiday**.
- myeongdong #21 BOK Money Museum — **weekend visits require prior booking**;
  the daily 14:00 docent tour is **reserved for foreign visitors**.

Pattern holding at 89 entries: still zero fabrications. The recurring defect
is omission of the one detail that changes whether you get in.
