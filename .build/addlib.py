# -*- coding: utf-8 -*-
import io

def block(n, e, level):
    emoji, title, status, what, hours, price, src, notes = e
    h = "#" * level
    return (
        f"{h} {n}) {emoji} {title} — {status}\n"
        f"- **What:** {what}\n"
        f"- **Hours:** {hours}\n"
        f"- **Price:** {price}\n"
        f"- **Official source:** {src}\n"
        f"- **Beginner notes:** {notes}\n"
    )

def append(path, entries, start, level, marker, city, intro=None):
    txt = io.open(path, encoding="utf-8").read()
    assert marker in txt, f"marker not found in {path}: {marker!r}"
    if intro is None:
        intro = (f"*Added from official city tourism portals, national heritage/museum sites, "
                 f"and each venue's own official page. Status legend: "
                 f"✅ confirmed · ⏳ TBA · 👀 watch · 🔁 always on.*")
    parts = [f"\n---\n\n## 🆕 More verified {city} events & activities (expansion set)\n\n{intro}\n\n"]
    for i, e in enumerate(entries):
        parts.append(block(start + i, e, level) + "\n")
    new = txt.replace(marker, "".join(parts).rstrip("\n") + "\n" + marker, 1)
    io.open(path, "w", encoding="utf-8").write(new)
    print(f"{path}: added {len(entries)} -> #{start}..#{start+len(entries)-1}")
