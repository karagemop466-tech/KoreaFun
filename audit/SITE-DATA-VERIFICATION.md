# Public site data verification

**Verification date:** 2026-08-21  
**Public artifact:** [`data.json`](../data.json)  
**Generator:** [`generate_data.py`](../generate_data.py)  
**Validator:** [`tools/validate_site_data.py`](../tools/validate_site_data.py)

## Result

| Check | Result |
|---|---:|
| Public rows | **700 / 700 passed** |
| Unique row IDs | **700 / 700** |
| Rows with one or more explicit official/primary links | **700 / 700** |
| City groups | **20** |
| Emitted links | **990** |
| Public authority links | **515** |
| Operator / organizer links | **462** |
| Authorized ticket links | **13** |
| Forbidden secondary hosts emitted | **0** |
| Rows matching strict regeneration from their source record | **700 / 700** |

The public data validator passed after the final regeneration. It checks each row rather than accepting aggregate counts as proof.

## What “verified” means here

The public site is deliberately narrower than the research guides. It publishes only:

- the source-record title;
- a deterministic city and area mapping;
- a conservative planning state derived from the reviewed heading;
- generic re-check guidance; and
- links extracted from an explicit `Official source`, `Official sources`, or `Official primary source` field.

It does **not** republish the guides’ detailed descriptions, prices, opening hours, transport times, or other fast-changing claims. Omitting those fields is intentional: the current claim ledger does not provide complete live coverage for every detailed line.

A source role describes why a link is eligible for the public index:

- **Public authority:** a government, public museum, heritage body, official tourism body, or comparable public institution;
- **Operator / organizer:** the named venue, attraction, team, event organizer, cultural foundation, or other first-party operator;
- **Authorized ticket:** a ticket seller used by the venue or production.

A source link is evidence to inspect, not a guarantee that an event will occur or that a venue will be open. The planning state and re-check note remain visible in every row.

## Verification layers

### 1. Manual source review

The 15 Markdown source files are recorded as reviewed in [`manual_verification.json`](manual_verification.json) under the criteria in [`VERIFICATION-PROTOCOL.md`](VERIFICATION-PROTOCOL.md). The protocol requires the exact named place/activity, city, source relevance, dates, status, and scope to be checked. It also requires prior-year patterns to remain unconfirmed.

### 2. Strict source extraction

`generate_data.py` parses all 700 numbered records. It fails when a record has no explicit official-source field or when no eligible HTTP(S) link remains after filtering. Links in ordinary prose, corroboration-only fields, and secondary reporting are not fallback sources.

The generator also:

- normalizes URLs without changing their identity;
- strips fragments;
- removes Markdown and HTML from public labels;
- deduplicates links within each row;
- applies explicit city/area mappings, including Seoul districts and nearby-city records; and
- excludes a maintained set of news, blog, mirror, directory, social, and aggregator hosts.

### 3. Deterministic row-by-row validation

`tools/validate_site_data.py` independently parses `data.json`, rejects duplicate JSON keys, and checks:

- exactly 700 entries and 20 city groups;
- unique, well-formed IDs;
- the exact expected metadata, entry, and source schemas;
- at least one official/primary source per row;
- safe public HTTP(S) URLs with no credentials, local/private hosts, unsafe whitespace, control characters, or invalid ports;
- sanitized text with no leaked Markdown or HTML;
- allowed planning states and source roles;
- no duplicate URL within a row;
- no forbidden secondary hostname;
- role classification for every source URL;
- metadata totals against actual rows and links; and
- exact field-for-field equality with a fresh strict regeneration from all 15 Markdown files.

The final equality check catches stale output, source-role changes, mapping changes, row omissions, row additions, altered names, source changes, and ordering drift.

### 4. Interface checks

The production page was served through a local HTTP server and all four required assets (`index.html`, `data.json`, `app.js`, and `styles.css`) were fetched and compared byte-for-byte with the workspace files. Additional checks covered JavaScript syntax, Python compilation, unique HTML IDs, required controls, local-only CSS/JavaScript, URL-safe DOM rendering through `textContent`, responsive table/card rules, and Git diff whitespace errors.

## Reproduce the result

From the repository root:

```bash
python3 generate_data.py
python3 tools/validate_site_data.py
node --check app.js
python3 -m py_compile generate_data.py tools/validate_site_data.py
git diff --check
```

Expected validator summary:

```text
PASS: 700 unique entries; 20 cities; 990 official/primary links.
  Authorized ticket: 13
  Operator / organizer: 462
  Public authority: 515
  Every row matches strict regeneration from its Markdown source record.
  URL safety, sanitization, mappings, schema, and secondary-host exclusions passed.
```

## Limits and maintenance rule

This validation proves the public JSON matches the reviewed source records and contains an eligible link for every row. It does not turn URL liveness into semantic proof, and it does not guarantee that a remote page will remain unchanged. Future edits must be made in the Markdown research record, followed by regeneration and validation. Never patch `data.json` by hand.

Items marked **Re-check**, **Watch**, or **Unavailable** must not be presented as confirmed. Even **Confirmed** and **Established** rows must be re-checked at the linked source before booking or travel.
