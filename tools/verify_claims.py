#!/usr/bin/env python3
"""Cross-file claim consistency checker.

Guards the failure mode this project keeps hitting: a fact is fixed in the
city file but the itinerary/README/CSV still carry the old value, or a
ledger note claims an edit that never landed.

Each rule is (label, regex that MUST match somewhere in the file) per file.
Add a rule whenever a verified fact lands in more than one file.
"""
import io, re, sys

CLAIMS = [
    ("JTBC marathon start 08:00", [
        ("seoul.md", r"08:00.{0,80}Sangam|Start is \*\*08:00"),
        ("README.md", r"JTBC Seoul Marathon\*\* \(\*\*08:00"),
        ("itinerary.md", r"\*\*08:00\*\* — watch the \*\*JTBC"),
        ("events.csv", r"JTBC Seoul Marathon.*08:00 start"),
    ]),
    ("No 07:30 marathon claim anywhere", [
        ("seoul.md", r"^(?!.*07:30.*[Mm]arathon)", "absent"),
        ("README.md", r"^(?!.*07:30.*Marathon)", "absent"),
    ]),
    ("Busan IPark opponent is Chungbuk (not Chungnam) Cheongju", [
        ("busan.md", r"Chungbuk Cheongju"),
        ("itinerary.md", r"Chungbuk Cheongju"),
        ("README.md", r"Chungbuk Cheongju"),
    ]),
    ("Wine EXPO venue is DCC, never Hanbit Tower", [
        ("daejeon-cheonan.md", r"DCC Hall II"),
        ("README.md", r"DCC Hall II"),
    ]),
    ("Kings of Convenience 20:00", [
        ("seoul.md", r"Nov 18, 2026 · 20:00|20:00\*\*, \*\*Sejong Center"),
        ("itinerary.md", r"Kings of Convenience 20:00"),
        ("events.csv", r"Kings of Convenience.*20:00"),
    ]),
    ("Incheon open-port 5-museum combined ticket is W3,400", [
        ("incheon.md", r"3,400 adult"),
        ("incheon.md", r"five open-port museums"),
    ]),
    ("Gyeongju Wolji fare W3,000 with 21:30 ticket cutoff", [
        ("gyeongju.md", r"3,000 adult.{0,60}2,000"),
        ("gyeongju.md", r"ticket office closes 21:30"),
    ]),
    ("Independence Hall winter last entry 16:00 (not 17:00)", [
        ("daejeon-cheonan.md", r"LAST ENTRY IS 16:00"),
    ]),
    ("OK Savings Bank volleyball plays at Gangseo, not Sajik", [
        ("busan.md", r"Gangseo Sports Park Indoor Gymnasium"),
        ("busan.md", r"OK Savings Bank[^\n]*Sajik Gymnasium", "absent"),
        ("events.csv", r"Gangseo Sports Park Indoor Gymnasium"),
    ]),
    ("Jagalchi closes 1st and 3rd Tuesday (Nov 3 and 17, not the Busan window)", [
        ("busan.md", r"1st and 3rd Tuesday"),
        ("busan.md", r"Tue Nov 3 and Tue Nov 17"),
    ]),
    ("KBL November FIBA break warning present", [
        ("busan.md", r"Nov 23 . Dec 1, 2026|Nov 23 - Dec 1, 2026"),
        ("events.csv", r"Window 5 runs Nov 23-Dec 1 2026"),
    ]),
    ("Culture Day is weekly since Apr 2026, not monthly", [
        ("travel-basics.md", r"EVERY WEDNESDAY"),
        ("travel-basics.md", r"Nov 4, 11 and 18"),
        ("travel-basics.md", r"last Wednesday of each month \(.Culture Day.\) is free", "absent"),
        ("jeonju.md", r"EVERY Wednesday, not just the last one"),
    ]),
    ("INAS Nov 22 last entry 17:00 noted on departure day", [
        ("incheon.md", r"last entry 17:00"),
        ("itinerary.md", r"last entry 17:00"),
    ]),
    ("National Museum renovation closure flagged", [
        ("seoul.md", r"Jan 28, 2027|Jan 2027"),
        ("itinerary.md", r"closed for renovation until Jan 2027"),
    ]),
    # CSAT (수능) falls Thu Nov 19 2026, mid-trip: nationwide flight ground-stop
    # ~13:05-13:40, 10:00 office start, roads shut near test centres. Must stay
    # flagged in all three planning files.
    ("CSAT exam day Nov 19 flagged", [
        ("travel-basics.md", r"Nov 19 is CSAT day \(수능\)"),
        ("travel-basics.md", r"Nov 19, 2026"),
        ("travel-basics.md", r"13:05"),
        ("itinerary.md", r"CSAT exam day"),
        ("README.md", r"CSAT exam day"),
    ]),
    ("Busan X the Sky adult fare is W29,000 (operator page)", [
        ("busan.md", r"29,000 adult"),
        ("sources.md", r"₩29,000 adult"),
        ("sources.md", r"₩27,000 is correct", "absent"),
    ]),
    ("GS Caltex plays at Jangchung, not Jamsil Students", [
        ("seoul.md", r"BOTH Seoul clubs play at Jangchung Arena"),
        ("events.csv", r"BOTH clubs at Jangchung Arena"),
        ("events.csv", r"GS Caltex KIXX \(Jamsil Students", "absent"),
    ]),
    ("Hanbit Tower is free, Art Space 193 is closed", [
        ("daejeon-cheonan.md", r"Tower admission is free"),
        ("daejeon-cheonan.md", r"NOT CURRENTLY OPERATING"),
        ("events.csv", r"fee dropped Jun 2021"),
        ("events.csv", r"CLOSED / not operating"),
        ("daejeon-cheonan.md", r"Tower 2500", "absent"),
    ]),
    ("BeautySum Suwon is Nov 5-7 (organizer), not Visit Suwon Nov 6-8", [
        ("suwon.md", r"Thu Nov 5–Sat Nov 7, 2026"),
        ("suwon.md", r"Do not use the Visit Suwon festival index"),
        ("events.csv", r"BeautySum Korea Suwon 2026.*2026-11-05,2026-11-07|2026-11-05,2026-11-07,BeautySum"),
        ("suwon.md", r"Nov 6–8",),  # the warning must still mention the stale listing
    ]),
    ("Korean Folk Village 2026 horror season starts Apr 11 not June", [
        ("yongin.md", r"Apr 11 – Nov 15, 2026"),
        ("events.csv", r"Yongin,2026-04-11,2026-11-15,Salgwiok"),
        ("events.csv", r"Yongin,2026-06-13,2026-11-15,Salgwiok", "absent"),
    ]),
    ("Wolmi Sea Train adult fare is W8,000 on the ICTR table", [
        ("incheon.md", r"8,000 adult"),
        ("events.csv", r"8000 adult"),
    ]),
    ("Art Center Incheon November concerts dated on venue pages", [
        ("incheon.md", r"Vadym Kholodenko"),
        ("incheon.md", r"Tallis Scholars"),
        ("incheon.md", r"SHOW_IDX=14129"),
        ("incheon.md", r"SHOW_IDX=14130"),
    ]),
    ("Gyeonggijeon 정전 closed for restoration through Dec 17", [
        ("jeonju.md", r"Thu Mar 26 – Thu Dec 17, 2026"),
        ("jeonju.md", r"cannot enter the inner 정전"),
        ("itinerary.md", r"Gyeonggijeon 정전 is closed Mar 26–Dec 17"),
        ("README.md", r"Gyeonggijeon 정전 closed for restoration through Dec 17"),
        ("events.csv", r"inner 정전 closed for restoration Mar 26-Dec 17"),
    ]),
    ("Starlight Walk official 2026 fare is W10,000 on TicketLink", [
        ("jeonju.md", r"₩10,000 per person"),
        ("jeonju.md", r"facSid=RE_0001040"),
        ("events.csv", r"Gyeonggijeon Starlight Walk.*10000"),
        ("jeonju.md", r"half the tickets sold via TicketLink", "absent"),
    ]),
    ("Daesaseupcheong only in-window date is Oct 31", [
        ("jeonju.md", r"only trip-window date is Sat Oct 31"),
        ("jeonju.md", r"Nov 7, 14 and 21 are not on the list"),
        ("events.csv", r"Only trip-window date on the official 2026 list"),
    ]),
]

def check():
    fails = []
    for label, rules in CLAIMS:
        for rule in rules:
            path, pat = rule[0], rule[1]
            mode = rule[2] if len(rule) > 2 else "present"
            try:
                s = io.open(path, encoding='utf-8-sig').read()
            except FileNotFoundError:
                fails.append(f"{label}: MISSING FILE {path}"); continue
            if mode == "absent":
                bad = re.search(pat.replace("^(?!.*", "").replace(")", "", 1), s, re.I)
                # simple absence test: the inner pattern must NOT appear
                inner = pat[len("^(?!.*"):-1] if pat.startswith("^(?!.*") else pat
                if re.search(inner, s, re.I):
                    fails.append(f"{label}: STALE VALUE still in {path}")
            else:
                if not re.search(pat, s, re.I | re.M):
                    fails.append(f"{label}: NOT FOUND in {path}")
    return fails

if __name__ == '__main__':
    f = check()
    if f:
        print("CLAIM CONSISTENCY FAILURES:")
        for x in f: print("  ✗", x)
        sys.exit(1)
    print(f"claim consistency OK ({len(CLAIMS)} multi-file claims verified)")
