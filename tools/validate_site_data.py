#!/usr/bin/env python3
"""Fail closed when public site data drifts from the reviewed Markdown corpus.

This is a deterministic production-data check, not a claim that every remote page is
currently reachable. It verifies every emitted row, field, mapping and URL against the
strict source-first generator and its secondary-host exclusions.
"""

from __future__ import annotations

import ipaddress
import json
import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import generate_data  # noqa: E402

EXPECTED_ENTRY_COUNT = 700
EXPECTED_CITY_COUNT = 20
ENTRY_FIELDS = {
    "id",
    "city",
    "area",
    "name",
    "icon",
    "status",
    "statusLabel",
    "planningNote",
    "officialSources",
    "sourceFile",
    "sourceEntry",
}
SOURCE_FIELDS = {"name", "url", "type"}
META_FIELDS = {
    "generatedOn",
    "entryCount",
    "cityCount",
    "officialSourceCount",
    "scope",
}
ALLOWED_STATUSES = {"confirmed", "established", "recheck", "watch", "unavailable"}
ALLOWED_SOURCE_TYPES = {"Public authority", "Operator / organizer", "Authorized ticket"}
CONTROL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
MARKUP_RE = re.compile(r"<[^>]*>|\[[^\]]*\]\([^)]*\)|\*\*|__|`")

BASE_LOCATIONS = {
    "busan.md": ("Busan", "Citywide"),
    "changwon-jinhae.md": ("Changwon", "Changwon"),
    "daegu.md": ("Daegu", "Citywide"),
    "gyeongju.md": ("Gyeongju", "Citywide"),
    "incheon.md": ("Incheon", "Citywide"),
    "jeonju.md": ("Jeonju", "Citywide"),
    "pohang.md": ("Pohang", "Citywide"),
    "suwon.md": ("Suwon", "Citywide"),
    "ulsan.md": ("Ulsan", "Citywide"),
    "yeosu.md": ("Yeosu", "Citywide"),
    "yongin.md": ("Yongin", "Citywide"),
}
SEOUL_DISTRICT_RANGES = [
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


class DuplicateKeyError(ValueError):
    """Raised when JSON contains a duplicate object key."""


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(f"duplicate JSON key: {key!r}")
        result[key] = value
    return result


def host_is_local_or_private(host: str) -> bool:
    if host.lower() in {"localhost", "localhost.localdomain"} or host.lower().endswith(".local"):
        return True
    try:
        address = ipaddress.ip_address(host.strip("[]"))
    except ValueError:
        return False
    return not address.is_global


def expected_location(filename: str, number: int) -> tuple[str, str]:
    """Resolve source records independently of the production generator."""
    if filename == "myeongdong.md":
        return "Seoul", "Myeong-dong"
    if filename == "seoul.md":
        if number in {9, 10}:
            return "Goyang", "KINTEX"
        if number == 20:
            return "Gwacheon", "Seoul Grand Park"
        return "Seoul", "Citywide"
    if filename == "seoul-districts.md":
        for start, end, area in SEOUL_DISTRICT_RANGES:
            if start <= number <= end:
                return "Seoul", area
        raise ValueError(f"unmapped Seoul district record #{number}")
    if filename == "daejeon-cheonan.md":
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
    if filename == "changwon-jinhae.md":
        if 1 <= number <= 11:
            return "Changwon", "Jinhae"
        if 12 <= number <= 17 or number == 30:
            return "Changwon", "Masan"
        return "Changwon", "Changwon"
    if filename in BASE_LOCATIONS:
        return BASE_LOCATIONS[filename]
    raise ValueError(f"unknown source file {filename!r}")


def validate_url(url: Any, where: str, errors: list[str]) -> None:
    if not isinstance(url, str):
        errors.append(f"{where}: URL is not a string")
        return
    if CONTROL_RE.search(url) or any(character.isspace() for character in url) or "\\" in url:
        errors.append(f"{where}: URL contains unsafe whitespace, control characters, or backslashes")
        return

    parts = urlsplit(url)
    if parts.scheme not in {"http", "https"}:
        errors.append(f"{where}: URL scheme must be HTTP(S): {url!r}")
    if not parts.hostname:
        errors.append(f"{where}: URL has no hostname: {url!r}")
        return
    if parts.username is not None or parts.password is not None:
        errors.append(f"{where}: URL must not contain credentials: {url!r}")
    if host_is_local_or_private(parts.hostname):
        errors.append(f"{where}: URL points to a local/private host: {url!r}")
    try:
        _ = parts.port
    except ValueError:
        errors.append(f"{where}: URL has an invalid port: {url!r}")


def validate_text(value: Any, where: str, errors: list[str], *, allow_empty: bool = False) -> None:
    if not isinstance(value, str):
        errors.append(f"{where}: expected a string")
        return
    if not allow_empty and not value.strip():
        errors.append(f"{where}: text is empty")
    if value != value.strip() or CONTROL_RE.search(value) or MARKUP_RE.search(value):
        errors.append(f"{where}: text is not sanitized: {value!r}")
    if generate_data.clean_text(value) != value:
        errors.append(f"{where}: text changes when passed through clean_text: {value!r}")


def validate_shape(data: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict) or set(data) != {"meta", "entries"}:
        return ["top level must contain exactly 'meta' and 'entries'"]

    meta = data["meta"]
    entries = data["entries"]
    if not isinstance(meta, dict) or set(meta) != META_FIELDS:
        errors.append(f"meta fields differ from expected fields: {sorted(META_FIELDS)}")
    if not isinstance(entries, list):
        return errors + ["entries must be an array"]

    if len(entries) != EXPECTED_ENTRY_COUNT:
        errors.append(f"expected {EXPECTED_ENTRY_COUNT} entries, found {len(entries)}")

    ids: set[str] = set()
    source_records: set[tuple[str, int]] = set()
    city_area_pairs: set[tuple[str, str]] = set()
    source_total = 0

    for index, entry in enumerate(entries):
        where = f"entries[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{where}: entry must be an object")
            continue
        if set(entry) != ENTRY_FIELDS:
            errors.append(f"{where}: fields differ from expected fields for {entry.get('id', 'unknown')}")
            continue

        entry_id = entry["id"]
        if not isinstance(entry_id, str) or not re.fullmatch(r"[a-z0-9-]+-\d+", entry_id):
            errors.append(f"{where}.id: invalid ID {entry_id!r}")
        elif entry_id in ids:
            errors.append(f"{where}.id: duplicate ID {entry_id!r}")
        else:
            ids.add(entry_id)

        for field in ("city", "area", "name", "statusLabel", "planningNote", "sourceFile"):
            validate_text(entry[field], f"{where}.{field}", errors)
        validate_text(entry["icon"], f"{where}.icon", errors, allow_empty=True)

        source_file = entry["sourceFile"]
        source_entry = entry["sourceEntry"]
        if source_file not in generate_data.CITY_FILES:
            errors.append(f"{where}.sourceFile: unknown guide {source_file!r}")
        if not isinstance(source_entry, int) or isinstance(source_entry, bool) or source_entry < 1:
            errors.append(f"{where}.sourceEntry: expected a positive integer")
        elif isinstance(source_file, str) and source_file in generate_data.CITY_FILES:
            source_record = (source_file, source_entry)
            if source_record in source_records:
                errors.append(f"{where}: duplicate source record {source_file} #{source_entry}")
            source_records.add(source_record)

            expected_id = f"{Path(source_file).stem}-{source_entry}"
            if entry_id != expected_id:
                errors.append(f"{where}.id: expected {expected_id!r}, found {entry_id!r}")
            try:
                expected_city, expected_area = expected_location(source_file, source_entry)
            except ValueError as error:
                errors.append(f"{where}: {error}")
            else:
                if (entry["city"], entry["area"]) != (expected_city, expected_area):
                    errors.append(
                        f"{where}: expected location {(expected_city, expected_area)!r}, "
                        f"found {(entry['city'], entry['area'])!r}"
                    )

        if entry["status"] not in ALLOWED_STATUSES:
            errors.append(f"{where}.status: unknown state {entry['status']!r}")

        if isinstance(entry["city"], str) and isinstance(entry["area"], str):
            city_area_pairs.add((entry["city"], entry["area"]))

        sources = entry["officialSources"]
        if not isinstance(sources, list) or not sources:
            errors.append(f"{where}.officialSources: every entry needs at least one source")
            continue

        seen_urls: set[str] = set()
        source_total += len(sources)
        for source_index, source in enumerate(sources):
            source_where = f"{where}.officialSources[{source_index}]"
            if not isinstance(source, dict) or set(source) != SOURCE_FIELDS:
                errors.append(f"{source_where}: source fields must be {sorted(SOURCE_FIELDS)}")
                continue
            validate_text(source["name"], f"{source_where}.name", errors)
            validate_url(source["url"], f"{source_where}.url", errors)
            validate_text(source["type"], f"{source_where}.type", errors)
            if source["type"] not in ALLOWED_SOURCE_TYPES:
                errors.append(f"{source_where}.type: unknown source role {source['type']!r}")
            if isinstance(source["url"], str):
                host = generate_data.hostname(source["url"])
                if host in generate_data.NON_PRIMARY_HOSTS:
                    errors.append(f"{source_where}.url: forbidden secondary host {host!r}")
                if source["url"] in seen_urls:
                    errors.append(f"{source_where}.url: duplicate URL in entry")
                seen_urls.add(source["url"])
                expected_type = generate_data.source_type(source["url"])
                if source["type"] != expected_type:
                    errors.append(
                        f"{source_where}.type: expected {expected_type!r}, found {source['type']!r}"
                    )

    cities = {city for city, _area in city_area_pairs}
    if len(cities) != EXPECTED_CITY_COUNT:
        errors.append(f"expected {EXPECTED_CITY_COUNT} cities, found {len(cities)}")

    if isinstance(meta, dict):
        expected_meta_values = {
            "entryCount": len(entries),
            "cityCount": len(cities),
            "officialSourceCount": source_total,
        }
        for key, expected in expected_meta_values.items():
            if meta.get(key) != expected:
                errors.append(f"meta.{key}: expected {expected}, found {meta.get(key)!r}")

    return errors


def first_difference(expected: Any, actual: Any, path: str = "root") -> str | None:
    """Return a concise path to the first value that differs."""
    if type(expected) is not type(actual):
        return f"{path}: expected {type(expected).__name__}, found {type(actual).__name__}"
    if isinstance(expected, dict):
        if list(expected) != list(actual):
            return f"{path}: object keys/order differ"
        for key in expected:
            difference = first_difference(expected[key], actual[key], f"{path}.{key}")
            if difference:
                return difference
        return None
    if isinstance(expected, list):
        if len(expected) != len(actual):
            return f"{path}: expected {len(expected)} items, found {len(actual)}"
        for index, (expected_item, actual_item) in enumerate(zip(expected, actual)):
            difference = first_difference(expected_item, actual_item, f"{path}[{index}]")
            if difference:
                return difference
        return None
    if expected != actual:
        return f"{path}: expected {expected!r}, found {actual!r}"
    return None


def main() -> int:
    data_path = ROOT / "data.json"
    try:
        data = json.loads(data_path.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicate_keys)
    except (OSError, json.JSONDecodeError, DuplicateKeyError) as error:
        print(f"FAIL: could not parse {data_path.name}: {error}", file=sys.stderr)
        return 1

    errors = validate_shape(data)

    try:
        expected = generate_data.build_data()
    except Exception as error:  # The strict generator provides useful file/entry context.
        errors.append(f"strict regeneration failed: {error}")
    else:
        difference = first_difference(expected, data)
        if difference:
            errors.append(f"data.json is stale or differs from the reviewed corpus: {difference}")

    if errors:
        print(f"FAIL: {len(errors)} site-data validation error(s):", file=sys.stderr)
        for error in errors[:100]:
            print(f"  - {error}", file=sys.stderr)
        if len(errors) > 100:
            print(f"  - …and {len(errors) - 100} more", file=sys.stderr)
        return 1

    role_counts: dict[str, int] = {role: 0 for role in sorted(ALLOWED_SOURCE_TYPES)}
    for entry in data["entries"]:
        for source in entry["officialSources"]:
            role_counts[source["type"]] += 1

    print(
        "PASS: "
        f"{len(data['entries'])} unique entries; "
        f"{data['meta']['cityCount']} city groups; "
        f"{data['meta']['officialSourceCount']} official/primary links."
    )
    for role, count in role_counts.items():
        print(f"  {role}: {count}")
    print("  Every row matches strict regeneration from its Markdown source record.")
    print("  URL safety, sanitization, mappings, schema, and secondary-host exclusions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
