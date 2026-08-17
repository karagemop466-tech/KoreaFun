#!/usr/bin/env python3
"""Check every unique URL in the repo markdown for liveness.

Writes audit/link_status.json  {url: {"status": int|str, "final": str}}
Uses stdlib only. Concurrent. Retries once on transient failure.
"""
import concurrent.futures as cf
import glob
import json
import os
import re
import ssl
import sys
import urllib.error
import urllib.request

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL_RE = re.compile(r"https?://[^\s)\]<>\"'|]+")
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE


def collect():
    urls = set()
    for p in glob.glob(os.path.join(REPO, "*.md")) + glob.glob(os.path.join(REPO, "*.csv")):
        txt = open(p, encoding="utf-8").read()
        for u in URL_RE.findall(txt):
            urls.add(u.rstrip(".,;"))
    return sorted(urls)


def probe(url):
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method, headers={
                "User-Agent": UA,
                "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
                "Accept-Language": "en,ko;q=0.8",
            })
            with urllib.request.urlopen(req, timeout=25, context=CTX) as r:
                return {"status": r.status, "final": r.url}
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (403, 405, 400, 501):
                continue
            return {"status": e.code, "final": url}
        except Exception as e:  # noqa: BLE001
            if method == "HEAD":
                continue
            return {"status": type(e).__name__, "final": str(e)[:120]}
    return {"status": "ERR", "final": ""}


def main():
    urls = collect()
    print(len(urls), "unique urls", flush=True)
    out_path = os.path.join(REPO, "audit", "link_status.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    res = {}
    if os.path.exists(out_path):
        try:
            res = json.load(open(out_path))
        except Exception:
            res = {}
    todo = [u for u in urls if u not in res]
    print(len(todo), "to check", flush=True)
    done = 0
    with cf.ThreadPoolExecutor(max_workers=24) as ex:
        futs = {ex.submit(probe, u): u for u in todo}
        for f in cf.as_completed(futs):
            u = futs[f]
            try:
                res[u] = f.result()
            except Exception as e:  # noqa: BLE001
                res[u] = {"status": "FATAL", "final": str(e)[:100]}
            done += 1
            if done % 50 == 0:
                print(done, "/", len(todo), flush=True)
                json.dump(res, open(out_path, "w"), indent=0)
    json.dump(res, open(out_path, "w"), indent=0)
    bad = {u: v for u, v in res.items() if not (isinstance(v["status"], int) and v["status"] < 400)}
    print("DONE. bad/unreachable:", len(bad), "of", len(res), flush=True)


if __name__ == "__main__":
    main()
