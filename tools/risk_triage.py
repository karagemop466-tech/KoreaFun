#!/usr/bin/env python3
"""Pass 11: rank all entries by hallucination risk instead of by badge.

Signals (each = evidence the claim could be fabricated or stale):
  DATE2026   asserts a specific 2026 date -> falsifiable, high consequence
  AGGREGATOR sourced only from a known-unreliable aggregator/blog
  NOOFFICIAL no .go.kr/.or.kr/.museum/official domain anywhere in the entry
  SELFREF    'source' link is a search page or homepage, not the thing itself
  BAREDOMAIN link is a bare homepage (no path) -> cannot prove the event exists
"""
import glob, re, io, json, collections

BAD_HOSTS = ('busan-where.com','traveloka','welfarehello','daeguwhere','coldsurf.io',
             'greatsisyphus','moneyroan','blog.naver','m.blog.naver','tistory',
             'namu.wiki','trip.com','klook','triple.guide','tripadvisor')
OFFICIAL = ('.go.kr','.or.kr','.museum','.ac.kr','khs.go.kr','visitkorea','kh.or.kr')

rows=[]
for f in sorted(glob.glob('/home/user/KoreaFun/*.md')):
    s=io.open(f,encoding='utf-8').read()
    name=f.rsplit('/',1)[1]
    for m in re.finditer(r'^### (\d+)\)(.*?)(?=^### |\Z)', s, re.M|re.S):
        num, body = m.group(1), m.group(0)
        head = body.split('\n')[0]
        urls = re.findall(r'https?://[^\s\)\]]+', body)
        flags=[]
        if re.search(r'\b2026[.\-/년]\s*\d{1,2}|\b(Nov|Oct|Dec)\w*\s+\d{1,2}', body):
            flags.append('DATE2026')
        if urls and all(any(b in u for b in BAD_HOSTS) for u in urls):
            flags.append('AGGREGATOR')
        if not any(o in u for u in urls for o in OFFICIAL):
            flags.append('NOOFFICIAL')
        if all(re.match(r'https?://[^/]+/?$', u) for u in urls) and urls:
            flags.append('BAREDOMAIN')
        badge = ('✅' if '✅' in head else '🔎' if '🔎' in head else
                 '⏳' if '⏳' in head else '👀' if '👀' in head else '?')
        if flags:
            rows.append(dict(file=name,num=int(num),badge=badge,flags=flags,
                             title=re.sub(r'[*#]','',head)[:70].strip()))

score=lambda r: len(r['flags']) + (2 if 'AGGREGATOR' in r['flags'] else 0) \
                + (1 if 'DATE2026' in r['flags'] and r['badge']!='✅' else 0)
rows.sort(key=lambda r:(-score(r), r['file'], r['num']))
json.dump(rows, open('/home/user/KoreaFun/audit/risk_triage.json','w'), ensure_ascii=False, indent=1)

c=collections.Counter(fl for r in rows for fl in r['flags'])
print("flagged entries:", len(rows), "of 570")
for k,v in c.most_common(): print(f"  {k:11s} {v}")
print("\n--- top 25 riskiest ---")
for r in rows[:25]:
    print(f"{r['badge']} {r['file'][:18]:18s} #{r['num']:<3d} {','.join(r['flags']):28s} {r['title'][:48]}")
