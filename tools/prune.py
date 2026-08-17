#!/usr/bin/env python3
"""Remove FILLER entries from a city file and renumber the survivors.

Usage: python3 tools/prune.py <file.md> [--dry-run]

Also drops any '## section' heading left with no entries under it, and archives
what it removed to audit/removed/<file>.md so nothing is lost silently.
"""
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NUM_RE = re.compile(r"^(#{2,3})\s+(\**\s*)(\d+)\)(.*)$", re.S)


def load_targets(fname):
    rows = json.load(open(os.path.join(REPO, "audit", "classification.json"), encoding="utf-8"))
    return {r["num"] for r in rows if r["file"] == fname and r["cls"] == "FILLER"}


def main():
    fname = sys.argv[1]
    dry = "--dry-run" in sys.argv
    path = os.path.join(REPO, fname)
    kill = load_targets(fname)
    lines = open(path, encoding="utf-8").read().split("\n")

    # Split into blocks: (kind, heading_num, lines)
    blocks = []
    cur = {"num": None, "lines": []}
    for line in lines:
        m = NUM_RE.match(line)
        if m:
            blocks.append(cur)
            cur = {"num": int(m.group(3)), "lines": [line], "hashes": m.group(1),
                   "bold": m.group(2), "rest": m.group(4)}
        else:
            cur["lines"].append(line)
    blocks.append(cur)

    removed, kept = [], []
    for b in blocks:
        if b["num"] is not None and b["num"] in kill:
            removed.append(b)
        else:
            kept.append(b)

    # Renumber sequentially
    n = 0
    out = []
    for b in kept:
        if b["num"] is None:
            out += b["lines"]
            continue
        n += 1
        head = f"{b['hashes']} {b['bold']}{n}){b['rest']}"
        out += [head] + b["lines"][1:]

    text = "\n".join(out)
    # collapse 3+ blank lines, and drop empty trailing sections
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    # remove '## heading' immediately followed by another heading or EOF
    text = re.sub(r"\n#{2,3} [^\n]*\n+(?=\n?#{2} )", "\n", text)
    text = re.sub(r"\n---\n+(?=\n*---)", "\n", text)

    print(f"{fname}: {len(blocks)-1} entries -> kept {n}, removed {len(removed)}")
    if dry:
        for b in removed[:200]:
            print("   REMOVE", b["num"], b["lines"][0][:100])
        return

    arch_dir = os.path.join(REPO, "audit", "removed")
    os.makedirs(arch_dir, exist_ok=True)
    with open(os.path.join(arch_dir, fname), "w", encoding="utf-8") as fh:
        fh.write(f"# Removed from {fname} (unverifiable / filler entries)\n\n")
        for b in removed:
            fh.write("\n".join(b["lines"]).rstrip() + "\n\n")
    open(path, "w", encoding="utf-8").write(text)


if __name__ == "__main__":
    main()
