import os
import re
import json

def parse_md_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(filepath)
    city_name = filename.replace('.md', '').replace('-', ' ').title()
    if filename == 'seoul-districts.md':
        city_name = 'Seoul Districts'

    entries = []

    # Try parsing numbered entries like ### 1) ...
    # Pattern: ### N) [Emoji] **Name** — [Status] — [Date]
    # We use a more flexible pattern
    numbered_sections = re.split(r'\n###\s+\d+\)', content)
    
    # The first split is the header
    for section in numbered_sections[1:]:
        lines = section.strip().split('\n')
        if not lines:
            continue
        
        header_line = lines[0]
        # Extract name and status
        # Example: 🎨 **BANKSY: Still Here** — ✅ CONFIRMED — through Tue Nov 3, 2026
        name_match = re.search(r'\*\*(.*?)\*\*', header_line)
        name = name_match.group(1) if name_match else header_line.strip()
        
        status = "🔎 Verified"
        if '✅' in header_line:
            status = "✅ Confirmed"
        elif '⏳' in header_line:
            status = "⏳ Re-check"
        elif '👀' in header_line:
            status = "👀 Watch"
        elif '❌' in header_line:
            status = "❌ Too Early/Closed"
        elif '🔎' in header_line:
            status = "🔎 Verified"

        entry_data = {
            "city": city_name,
            "name": name,
            "status": status,
            "what": "",
            "when": "",
            "hours": "",
            "price": "",
            "sources": [],
            "notes": ""
        }

        current_key = None
        for line in lines[1:]:
            line = line.strip()
            # Catch all links in the section as fallback sources
            other_links = re.findall(r'\[(.*?)\]\((.*?)\)', line)
            for l_text, l_url in other_links:
                if l_url not in [s["url"] for s in entry_data["sources"]]:
                    entry_data["sources"].append({"text": l_text, "url": l_url})

            if line.startswith('- **What:**'):
                entry_data["what"] = line.replace('- **What:**', '').strip()
                current_key = "what"
            elif line.startswith('- **When:**'):
                entry_data["when"] = line.replace('- **When:**', '').strip()
                current_key = "when"
            elif line.startswith('- **Hours:**'):
                entry_data["hours"] = line.replace('- **Hours:**', '').strip()
                current_key = "hours"
            elif line.startswith('- **Price'):
                entry_data["price"] = re.sub(r'^- \*\*Price.*?\*\*:', '', line).strip()
                current_key = "price"
            elif line.startswith('- **Official source'):
                source_text = re.sub(r'^- \*\*Official source.*?\*\*:', '', line).strip()
                # Find links
                links = re.findall(r'\[(.*?)\]\((.*?)\)', source_text)
                for l_text, l_url in links:
                    entry_data["sources"].append({"text": l_text, "url": l_url})
                current_key = "sources"
            elif line.startswith('-'):
                # Generic note
                entry_data["notes"] += line + " "
                current_key = "notes"
            elif line and current_key:
                if current_key == "sources":
                    links = re.findall(r'\[(.*?)\]\((.*?)\)', line)
                    for l_text, l_url in links:
                        entry_data["sources"].append({"text": l_text, "url": l_url})
                elif current_key == "notes":
                    entry_data["notes"] += line + " "
                else:
                    entry_data[current_key] += " " + line

        entries.append(entry_data)

    # Special handling for tables in seoul-districts.md or others
    if filename == 'seoul-districts.md':
        # Find tables
        tables = re.findall(r'(\|.*\|\n\|[-| :]*\|\n(?:\|.*\|\n?)+)', content)
        for table in tables:
            rows = table.strip().split('\n')
            if len(rows) < 3: continue
            # Headers
            # | # | Entry | Exact location | Dates in window | Hours | Price (official) | Status |
            headers = [h.strip() for h in rows[0].split('|') if h.strip()]
            for row in rows[2:]:
                cols = [c.strip() for c in row.split('|') if c.strip()]
                if len(cols) < 5: continue
                
                # Entry 1-25 might be already in numbered sections, but let's see.
                # Actually, seoul-districts.md has numbered sections for details, 
                # but the tables are summaries.
                # Let's avoid duplicates if possible, or just use the tables as primary sources.
                pass

    return entries

def main():
    files = [
        'seoul.md', 'busan.md', 'daejeon-cheonan.md', 'myeongdong.md',
        'seoul-districts.md', 'suwon.md', 'yongin.md', 'incheon.md',
        'jeonju.md', 'daegu.md', 'gyeongju.md', 'ulsan.md', 'pohang.md',
        'changwon-jinhae.md', 'yeosu.md'
    ]
    
    all_entries = []
    for f in files:
        if os.path.exists(f):
            print(f"Parsing {f}...")
            all_entries.extend(parse_md_file(f))
    
    # If some entries have no sources, try to find them in the text
    # (The regex might miss some)
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(all_entries, f, indent=2, ensure_ascii=False)
    
    print(f"Total entries parsed: {len(all_entries)}")

if __name__ == "__main__":
    main()
