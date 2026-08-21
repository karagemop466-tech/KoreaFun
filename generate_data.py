#!/usr/bin/env python3
"""Build the small, source-first data set used by the GitHub Pages site.

The Markdown guides remain the research record. The public site intentionally publishes
only low-risk fields (name, city/area, planning state and first-party/authority links).
Detailed prose, prices and hours are not copied into data.json because those claims can
age independently and are not all covered by the line ledger.
"""

from __future__ import annotations

import html
import json
import re
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parent
GENERATED_ON = "2026-08-21"

CITY_FILES = [
    "seoul.md",
    "busan.md",
    "daejeon-cheonan.md",
    "myeongdong.md",
    "seoul-districts.md",
    "suwon.md",
    "yongin.md",
    "incheon.md",
    "jeonju.md",
    "daegu.md",
    "gyeongju.md",
    "ulsan.md",
    "pohang.md",
    "changwon-jinhae.md",
    "yeosu.md",
]

# These are secondary reports, blogs, mirrors, directories or aggregators. They can
# remain in research prose as corroboration, but never appear as an official/primary
# link on the public site.
NON_PRIMARY_HOSTS = {
    "amnews.kr",
    "asiae.co.kr",
    "basketkorea.com",
    "bbsj.kr",
    "busan.com",
    "chosun.com",
    "cosmorning.com",
    "culture.blogsailing.com",
    "digitaltoday.co.kr",
    "dkvips.com",
    "economy.chosun.com",
    "edaily.co.kr",
    "gotothefestival.co.kr",
    "hankyung.com",
    "i-rang.net",
    "idaegu.com",
    "idomin.com",
    "imaeil.com",
    "insightkorea.co.kr",
    "instagram.com",
    "joongang.co.kr",
    "joongangenews.com",
    "kbsm.net",
    "koreaherald.com",
    "ktriptips.com",
    "kyongbuk.co.kr",
    "m.blog.naver.com",
    "m.joongdo.co.kr",
    "m.ktv.go.kr",
    "mobile.busan.com",
    "munhwa.com",
    "namu.wiki",
    "news.nate.com",
    "newsis.com",
    "newsro.kr",
    "newswell.co.kr",
    "newswire.co.kr",
    "nocutnews.co.kr",
    "seouland.com",
    "shinailbo.co.kr",
    "sisa-news.com",
    "sctoday.co.kr",
    "star.ohmynews.com",
    "thepreview.co.kr",
    "tripinfo.co.kr",
    "venturesquare.net",
    "wegive.co.kr",
    "yna.co.kr",
}

TICKET_HOSTS = {
    "m.ticket.yes24.com",
    "m.ticketlink.co.kr",
    "mticket.interpark.com",
    "ticket.yes24.com",
    "tickets.interpark.com",
    "world.nol.com",
}

SOURCE_LINE_RE = re.compile(
    r"^-\s+\*\*Official\s+(?:primary\s+)?(?:contextual\s+)?sources?\b",
    re.IGNORECASE,
)
ENTRY_RE = re.compile(r"(?m)^###\s+(\d+)\)\s*(.*)$")
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")
URL_RE = re.compile(r"https?://[^\s)]+")


def hostname(url: str) -> str:
    """Return a lower-case hostname without the cosmetic www prefix."""
    host = (urlsplit(url).hostname or "").lower()
    return host[4:] if host.startswith("www.") else host


def normalize_url(url: str) -> str:
    """Normalize only safe, identity-preserving URL details."""
    url = html.unescape(url.strip().rstrip(".,;"))
    parts = urlsplit(url)
    if parts.scheme not in {"http", "https"} or not parts.netloc:
        raise ValueError(f"Not a public HTTP URL: {url}")
    # Fragments do not identify a different source for this data set.
    return urlunsplit((parts.scheme.lower(), parts.netloc, parts.path, parts.query, ""))


def clean_text(value: str) -> str:
    """Remove Markdown/HTML syntax from a short public label."""
    value = html.unescape(value)
    value = re.sub(r"\\([\[\]_*`])", r"\1", value)
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = re.sub(r"<[^>]+>", "", value)
    value = value.replace("**", "").replace("__", "").replace("`", "")
    value = re.sub(r"\s+", " ", value)
    return value.strip(" \t\r\n-*·")


def source_type(url: str) -> str:
    host = hostname(url)
    if host in TICKET_HOSTS:
        return "Authorized ticket"
    if (
        host.endswith(".go.kr")
        or host.endswith(".gov")
        or host.endswith(".gov.kr")
        or host.endswith(".unesco.org")
        or host in {"korea.net", "whc.unesco.org"}
        or "visitkorea.or.kr" in host
    ):
        return "Public authority"
    return "Operator / organizer"


def extract_sources(lines: list[str], filename: str, number: int) -> list[dict[str, str]]:
    """Extract and deduplicate links only from explicit Official source lines."""
    official_lines = [line.strip() for line in lines if SOURCE_LINE_RE.match(line.strip())]
    if not official_lines:
        raise ValueError(f"{filename} #{number}: missing an explicit Official source line")

    sources: list[dict[str, str]] = []
    seen: set[str] = set()
    for line in official_lines:
        labels_by_url: dict[str, str] = {}
        for label, raw_url in MARKDOWN_LINK_RE.findall(line):
            labels_by_url[normalize_url(raw_url)] = clean_text(label)

        for raw_url in URL_RE.findall(line):
            url = normalize_url(raw_url)
            host = hostname(url)
            if host in NON_PRIMARY_HOSTS or url in seen:
                continue
            seen.add(url)
            sources.append(
                {
                    "name": labels_by_url.get(url) or host,
                    "url": url,
                    "type": source_type(url),
                }
            )

    if not sources:
        raise ValueError(f"{filename} #{number}: no official/primary HTTP source remains")
    return sources


def status_from_header(header: str) -> tuple[str, str, str]:
    """Return a stable code, short label and conservative planning guidance."""
    if "⛔" in header or "❌" in header:
        return (
            "unavailable",
            "Unavailable",
            "Not available in the stated travel window. Read the official source before changing plans.",
        )
    if "⏳" in header:
        return (
            "recheck",
            "Re-check",
            "Not fully confirmed for the travel window. Check the official source before planning around it.",
        )
    if "👀" in header:
        return (
            "watch",
            "Watch",
            "An announcement is still pending. Treat this as a watch item, not a confirmed plan.",
        )
    if "✅" in header:
        return (
            "confirmed",
            "Confirmed",
            "Published as confirmed in the source review. Re-check the official page before booking or travel.",
        )
    return (
        "established",
        "Established",
        "The place, operator or recurring activity was source-checked. Confirm current hours and access before travel.",
    )


def seoul_district_area(number: int) -> str:
    ranges = [
        (1, 6, "Dongdaemun"),
        (7, 12, "Hongdae & Mapo"),
        (13, 16, "Itaewon & Yongsan"),
        (17, 25, "Gangnam & Seocho"),
        (26, 32, "Central Seoul"),
        (33, 35, "Dongdaemun & east Seoul"),
        (36, 37, "Hongdae & Mapo"),
        (38, 41, "Itaewon & Yongsan"),
        (42, 46, "Gangnam & Seocho"),
        (47, 52, "Central Seoul"),
        (53, 55, "Dongdaemun"),
        (56, 58, "Hongdae & Mapo"),
        (59, 61, "Itaewon & Yongsan"),
        (62, 66, "Gangnam & Seocho"),
        (67, 72, "Central Seoul"),
        (73, 75, "Dongdaemun & Sindang"),
        (76, 77, "Hongdae & Mapo"),
        (78, 82, "Itaewon & Yongsan"),
        (83, 86, "Gangnam & Seocho"),
        (87, 95, "Central Seoul"),
        (96, 96, "Dongdaemun"),
        (97, 98, "Hongdae & Mapo"),
        (99, 102, "Itaewon & Yongsan"),
        (103, 106, "Gangnam & Seocho"),
    ]
    for start, end, area in ranges:
        if start <= number <= end:
            return area
    raise ValueError(f"No Seoul district mapping for entry #{number}")


def daejeon_region(number: int) -> tuple[str, str]:
    if number == 2 or 30 <= number <= 38:
        return "Cheonan", "Cheonan"
    if number == 3:
        return "Daejeon / Cheonan", "Multi-city"
    if number == 8 or 39 <= number <= 41:
        return "Asan", "Asan"
    if 42 <= number <= 43:
        return "Gongju", "Gongju"
    if number == 44:
        return "Buyeo", "Buyeo"
    return "Daejeon", "Daejeon"


def city_and_area(filename: str, number: int) -> tuple[str, str]:
    if filename == "myeongdong.md":
        return "Seoul", "Myeong-dong"
    if filename == "seoul-districts.md":
        return "Seoul", seoul_district_area(number)
    if filename == "seoul.md":
        if number in {9, 10}:
            return "Goyang", "KINTEX"
        if number == 20:
            return "Gwacheon", "Seoul Grand Park"
        return "Seoul", "Citywide"
    if filename == "daejeon-cheonan.md":
        return daejeon_region(number)
    if filename == "changwon-jinhae.md":
        if 1 <= number <= 11:
            return "Changwon", "Jinhae"
        if 12 <= number <= 17 or number == 30:
            return "Changwon", "Masan"
        return "Changwon", "Changwon"

    city = Path(filename).stem.replace("-", " ").title()
    return city, "Citywide"


def parse_file(filename: str) -> list[dict[str, object]]:
    text = (ROOT / filename).read_text(encoding="utf-8")
    matches = list(ENTRY_RE.finditer(text))
    entries: list[dict[str, object]] = []

    for index, match in enumerate(matches):
        number = int(match.group(1))
        header = match.group(2).strip()
        body_end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[match.end() : body_end]
        # A numbered entry ends at the next level-two section if one occurs first.
        body = re.split(r"(?m)^##\s+", body, maxsplit=1)[0]
        lines = body.strip().splitlines()

        name_match = re.search(r"\*\*(.+?)\*\*", header)
        if not name_match:
            raise ValueError(f"{filename} #{number}: title is not bolded")
        name = clean_text(name_match.group(1))
        icon = clean_text(header[: name_match.start()])
        status, status_label, guidance = status_from_header(header)
        city, area = city_and_area(filename, number)
        sources = extract_sources(lines, filename, number)

        entries.append(
            {
                "id": f"{Path(filename).stem}-{number}",
                "city": city,
                "area": area,
                "name": name,
                "icon": icon,
                "status": status,
                "statusLabel": status_label,
                "planningNote": guidance,
                "officialSources": sources,
                "sourceFile": filename,
                "sourceEntry": number,
            }
        )
    return entries


def build_data() -> dict[str, object]:
    entries: list[dict[str, object]] = []
    for filename in CITY_FILES:
        entries.extend(parse_file(filename))

    entries.sort(key=lambda item: (str(item["city"]), str(item["area"]), str(item["name"])))
    source_count = sum(len(item["officialSources"]) for item in entries)
    cities = sorted({str(item["city"]) for item in entries})
    return {
        "meta": {
            "generatedOn": GENERATED_ON,
            "entryCount": len(entries),
            "cityCount": len(cities),
            "officialSourceCount": source_count,
            "scope": "Names, city/area, planning state, and official or primary links only.",
        },
        "entries": entries,
    }


def main() -> None:
    data = build_data()
    output = ROOT / "data.json"
    output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"Wrote {data['meta']['entryCount']} entries across {data['meta']['cityCount']} city groups "
        f"with {data['meta']['officialSourceCount']} official/primary links to {output.name}."
    )


if __name__ == "__main__":
    main()
