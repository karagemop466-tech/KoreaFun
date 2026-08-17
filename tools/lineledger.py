#!/usr/bin/env python3
"""Line-level verification ledger for the KoreaFun guide.

Every non-blank body line of every entry gets its own row, keyed by
(file, entry number, content hash). Because the key includes a hash of the
line text, ANY edit to a line makes it a new row in `unchecked` state --
edits automatically requeue themselves, and a verified line can never
silently drift.

Verdicts
--------
  unchecked   not yet looked at
  verified    claim checked against a source and correct
  corrected   claim was wrong; line rewritten (the NEW line is what's marked)
  sourced     a source line whose URL was fetched and supports the entry
  dead        a source line whose URL is dead/unreachable (needs replacing)
  unresolved  checked, but no authoritative answer exists yet (honest state)
  prose       no factual claim to verify (narrative/advice only)

Usage
-----
  python3 tools/lineledger.py init            rebuild rows from entries.json
  python3 tools/lineledger.py stats           coverage summary
  python3 tools/lineledger.py plan            per-domain work batches
  python3 tools/lineledger.py next [N] [pfx]  next N unchecked lines
  python3 tools/lineledger.py entry <key>     show one entry's lines + state
  python3 tools/lineledger.py audit           integrity checks
  python3 tools/lineledger.py report          write audit/VERIFICATION-STATUS.md
"""
import json, io, os, re, sys, hashlib, collections
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENTRIES = os.path.join(ROOT, 'audit', 'entries.json')
LEDGER = os.path.join(ROOT, 'audit', 'line-ledger.json')

VERDICTS = ('unchecked', 'verified', 'corrected', 'sourced',
            'dead', 'unresolved', 'prose')
DONE = ('verified', 'corrected', 'sourced', 'prose')  # count as covered


def norm(s):
    return re.sub(r'\s+', ' ', s.strip())


def lid(file, num, text):
    h = hashlib.sha1(norm(text).encode('utf-8')).hexdigest()[:10]
    return f"{file}#{num}:{h}"


def classify(s):
    """Best-guess claim kind -- used for batching, not for truth."""
    if 'http' in s:
        return 'SOURCE'
    if re.search(r'₩[\d,]+|\d[\d,]{2,}\s*원', s):
        return 'PRICE'
    if re.search(r'\d{1,2}:\d{2}', s):
        return 'TIME'
    if re.search(r'\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b'
                 r'|\d{4}-\d{2}-\d{2}|\b20\d\d\b', s):
        return 'DATE'
    if re.search(r'closed|휴관|free|무료|reserv|book|ticket|admission'
                 r'|sold out|age|discount', s, re.I):
        return 'ACCESS'
    return 'PROSE'


def domains(s):
    return [m.lower().lstrip('www.')
            for m in re.findall(r'https?://([^/)\s\]]+)', s)]


def load():
    if not os.path.exists(LEDGER):
        return {}
    return json.load(io.open(LEDGER, encoding='utf-8'))


def save(d):
    json.dump(d, io.open(LEDGER, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1, sort_keys=True)


def entries():
    return json.load(io.open(ENTRIES, encoding='utf-8'))


def cmd_init():
    led = load()
    seen, added, revived = set(), 0, 0
    for e in entries():
        f, n = e['file'], e['num']
        for i, ln in enumerate(e.get('body', [])):
            if not ln.strip():
                continue
            k = lid(f, n, ln)
            seen.add(k)
            if k not in led:
                led[k] = {'file': f, 'entry': n, 'text': norm(ln),
                          'kind': classify(ln), 'verdict': 'unchecked',
                          'checked_on': None, 'sources': [], 'note': ''}
                added += 1
            elif led[k].get('retired'):
                # Text came back (e.g. an edit was reverted) -> revive the row
                # WITH its previous verdict, so restored text keeps its history.
                del led[k]['retired']
                revived += 1
    # Lines that no longer exist (entry edited/removed) -> retire, don't delete.
    retired = 0
    for k, v in led.items():
        if k not in seen and not v.get('retired'):
            v['retired'] = True
            retired += 1
    save(led)
    live = sum(1 for v in led.values() if not v.get('retired'))
    print(f"init: +{added} new, {revived} revived, {retired} retired, {live} live rows")


def live_rows(led, prefix=None):
    return {k: v for k, v in led.items()
            if not v.get('retired') and (not prefix or v['file'].startswith(prefix))}


def cmd_stats(prefix=None):
    led = live_rows(load(), prefix)
    c = collections.Counter(v['verdict'] for v in led.values())
    tot = len(led)
    covered = sum(c[x] for x in DONE)
    print(f"LINE LEDGER: {tot} live lines | covered {covered} ({100*covered//max(tot,1)}%)")
    for v in VERDICTS:
        if c[v]:
            print(f"  {v:11s} {c[v]:5d}")
    print("\nby file (covered/total):")
    per = collections.defaultdict(lambda: [0, 0])
    for v in led.values():
        per[v['file']][1] += 1
        if v['verdict'] in DONE:
            per[v['file']][0] += 1
    for f in sorted(per, key=lambda x: -per[x][1]):
        d, t = per[f]
        bar = '#' * int(20 * d / max(t, 1))
        print(f"  {f:22s} {d:4d}/{t:<4d} {100*d//max(t,1):3d}% {bar}")


def cmd_plan():
    """Group unchecked SOURCE lines by domain: one fetch clears many lines."""
    led = live_rows(load())
    dom = collections.defaultdict(list)
    for k, v in led.items():
        if v['verdict'] != 'unchecked':
            continue
        for d in domains(v['text']):
            dom[d].append(k)
    ranked = sorted(dom.items(), key=lambda kv: -len(kv[1]))
    print(f"{len(ranked)} domains carry unchecked source lines.")
    print("Batching by domain -- one fetch can clear several lines.\n")
    for d, ks in ranked[:30]:
        files = sorted({led[k]['file'].replace('.md', '') for k in ks})
        print(f"  {len(ks):3d}  {d:34s} {','.join(files[:5])}")


def cmd_next(n=15, prefix=None):
    led = live_rows(load(), prefix)
    rows = [(k, v) for k, v in led.items() if v['verdict'] == 'unchecked']
    order = {'PRICE': 0, 'TIME': 1, 'DATE': 2, 'ACCESS': 3, 'SOURCE': 4, 'PROSE': 5}
    rows.sort(key=lambda kv: (order.get(kv[1]['kind'], 9),
                              kv[1]['file'], kv[1]['entry']))
    for k, v in rows[:int(n)]:
        print(f"[{v['kind']:6s}] {k}\n    {v['text'][:150]}")


def cmd_entry(key):
    led = load()
    f, num = key.split('#')
    rows = [(k, v) for k, v in led.items()
            if v['file'] == f and str(v['entry']) == str(num) and not v.get('retired')]
    if not rows:
        print(f"no live lines for {key}")
        return
    for k, v in rows:
        mark = '.' if v['verdict'] == 'unchecked' else '+'
        print(f" {mark} [{v['verdict']:10s}] {k.split(':')[1]}  {v['text'][:120]}")


def cmd_mark(key, verdict, srcs='', note=''):
    led = load()
    if key not in led:
        print(f"NO SUCH LINE: {key}")
        sys.exit(1)
    if verdict not in VERDICTS:
        print(f"bad verdict {verdict}; want one of {VERDICTS}")
        sys.exit(1)
    led[key].update(verdict=verdict, checked_on=str(date.today()),
                    sources=[s for s in srcs.split('|') if s], note=note)
    save(led)
    print(f"{key} -> {verdict}")


def cmd_audit():
    led = load()
    live = live_rows(led)
    bad = [k for k, v in live.items()
           if v['verdict'] in ('verified', 'corrected', 'sourced')
           and not v['sources']]
    nodate = [k for k, v in live.items()
              if v['verdict'] != 'unchecked' and not v['checked_on']]
    dead = [k for k, v in live.items() if v['verdict'] == 'dead']
    unres = [k for k, v in live.items() if v['verdict'] == 'unresolved']
    print(f"live lines: {len(live)}")
    print(f"  verified/corrected/sourced WITHOUT a source url: {len(bad)}")
    for k in bad[:10]:
        print(f"     {k}")
    print(f"  marked but undated: {len(nodate)}")
    print(f"  DEAD source lines needing replacement: {len(dead)}")
    for k in dead[:15]:
        print(f"     {k}  {live[k]['text'][:90]}")
    print(f"  unresolved (open questions): {len(unres)}")
    for k in unres[:15]:
        print(f"     {k}  {live[k]['note'][:90]}")


def cmd_report():
    led = live_rows(load())
    per = collections.defaultdict(lambda: collections.defaultdict(lambda: [0, 0]))
    fileagg = collections.defaultdict(lambda: [0, 0])
    for v in led.values():
        per[v['file']][v['entry']][1] += 1
        fileagg[v['file']][1] += 1
        if v['verdict'] in DONE:
            per[v['file']][v['entry']][0] += 1
            fileagg[v['file']][0] += 1
    tot = sum(x[1] for x in fileagg.values())
    cov = sum(x[0] for x in fileagg.values())
    out = ["# Line-level verification status", "",
           f"_Generated by `tools/lineledger.py report` on {date.today()}._", "",
           f"**{cov} / {tot} lines verified ({100*cov//max(tot,1)}%).**", "",
           "A line is *covered* when its verdict is `verified`, `corrected`,",
           "`sourced` or `prose`. Editing any line changes its hash, which",
           "returns it to `unchecked` automatically.", "",
           "| File | Lines verified | % | Entries fully verified |",
           "| --- | --- | --- | --- |"]
    for f in sorted(fileagg, key=lambda x: -fileagg[x][1]):
        d, t = fileagg[f]
        full = sum(1 for e, (a, b) in per[f].items() if a == b)
        out.append(f"| `{f}` | {d}/{t} | {100*d//max(t,1)}% | {full}/{len(per[f])} |")
    io.open(os.path.join(ROOT, 'audit', 'VERIFICATION-STATUS.md'),
            'w', encoding='utf-8').write("\n".join(out) + "\n")
    print(f"wrote audit/VERIFICATION-STATUS.md ({cov}/{tot} = {100*cov//max(tot,1)}%)")


if __name__ == '__main__':
    a = sys.argv[1:] or ['stats']
    cmd = a[0]
    if cmd == 'init':
        cmd_init()
    elif cmd == 'stats':
        cmd_stats(a[1] if len(a) > 1 else None)
    elif cmd == 'plan':
        cmd_plan()
    elif cmd == 'next':
        cmd_next(a[1] if len(a) > 1 else 15, a[2] if len(a) > 2 else None)
    elif cmd == 'entry':
        cmd_entry(a[1])
    elif cmd == 'mark':
        cmd_mark(a[1], a[2], a[3] if len(a) > 3 else '', a[4] if len(a) > 4 else '')
    elif cmd == 'audit':
        cmd_audit()
    elif cmd == 'report':
        cmd_report()
    else:
        print(__doc__)
