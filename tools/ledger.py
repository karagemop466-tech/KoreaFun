#!/usr/bin/env python3
"""Per-entry verification ledger.

Every one of the 570 entries gets a row keyed by file+num, carrying the
verdict of an INDIVIDUAL check: what was checked, against which URL, on
what date, and what changed. Survives across sessions so no entry is
silently skipped or needlessly re-verified.

Verdicts:
  unchecked  - never individually verified
  confirmed  - claim matched a source that names the exact event/place
  corrected  - a claim was wrong and has been fixed
  softened   - could not confirm; wording weakened / badge downgraded
  removed    - unverifiable and deleted
"""
import json, io, os, sys, re, hashlib

LEDGER = '/home/user/KoreaFun/audit/verification-ledger.json'
ENTRIES = '/home/user/KoreaFun/audit/entries.json'

def body_hash(e):
    return hashlib.sha1('\n'.join(e.get('body', [])).encode('utf-8')).hexdigest()[:10]

def load():
    entries = json.load(io.open(ENTRIES, encoding='utf-8'))
    led = {}
    if os.path.exists(LEDGER):
        led = json.load(io.open(LEDGER, encoding='utf-8'))
    changed = 0
    for e in entries:
        k = f"{e['file']}#{e['num']}"
        h = body_hash(e)
        if k not in led:
            led[k] = {"file": e['file'], "num": e['num'],
                      "title": e['title'], "badge": e['status_tail'][:2].strip(),
                      "verdict": "unchecked", "checked_on": None,
                      "sources": [], "note": "", "body_hash": h}
            changed += 1
        else:
            led[k]['title'] = e['title']
            # entry edited since it was verified -> needs a fresh look
            if led[k].get('body_hash') != h and led[k]['verdict'] != 'unchecked':
                led[k]['stale'] = True
            led[k]['body_hash'] = h
    return entries, led, changed

def save(led):
    with io.open(LEDGER, 'w', encoding='utf-8') as f:
        json.dump(led, f, ensure_ascii=False, indent=1, sort_keys=True)

def mark(key, verdict, sources, note, date="2026-08-18"):
    _, led, _ = load()
    if key not in led:
        print("NO SUCH ENTRY", key); return
    led[key].update(verdict=verdict, checked_on=date,
                    sources=sources if isinstance(sources, list) else [sources],
                    note=note)
    led[key].pop('stale', None)
    save(led)
    print(f"{key}: {verdict}")

def stats():
    _, led, new = load(); save(led)
    from collections import Counter
    c = Counter(v['verdict'] for v in led.values())
    tot = len(led)
    done = tot - c['unchecked']
    print(f"LEDGER: {tot} entries | verified {done} ({100*done//tot}%) | new rows {new}")
    for k, v in c.most_common():
        print(f"  {k:10s} {v}")
    st = [k for k, v in led.items() if v.get('stale')]
    if st: print(f"  STALE (edited since check): {len(st)} -> {st[:5]}")

def nxt(n=12, fltr=None):
    entries, led, _ = load(); save(led)
    ent = {f"{e['file']}#{e['num']}": e for e in entries}
    out = []
    for k, v in led.items():
        if v['verdict'] != 'unchecked' and not v.get('stale'): continue
        if fltr and not k.startswith(fltr): continue
        e = ent.get(k, {})
        body = ' '.join(e.get('body', []))
        urls = re.findall(r'https?://[^\s\)]+', body)
        hosts = {re.sub(r'^www\.', '', u.split('/')[2]) for u in urls if len(u.split('/')) > 2}
        # prioritise: asserts a 2026 date, and leans on a non-official host
        dated = bool(re.search(r'2026', e.get('status_tail', '') + body))
        official = any(h.endswith(('.go.kr', '.or.kr')) for h in hosts)
        score = (2 if dated else 0) + (0 if official else 1) + (1 if not urls else 0)
        out.append((-score, k, v['badge'], e.get('title', '')[:52], ','.join(sorted(hosts))[:58]))
    out.sort()
    print(f"{'KEY':22s} {'B':3s} {'TITLE':54s} HOSTS")
    for _, k, b, t, h in out[:n]:
        print(f"{k:22s} {b:3s} {t:54s} {h}")
    print(f"\n({len([o for o in out])} remaining{' in '+fltr if fltr else ''})")

if __name__ == '__main__':
    a = sys.argv[1:]
    if not a or a[0] == 'stats': stats()
    elif a[0] == 'next': nxt(int(a[1]) if len(a) > 1 else 12, a[2] if len(a) > 2 else None)
    elif a[0] == 'mark': mark(a[1], a[2], a[3].split('|'), a[4])
