# Legal/official portal run — rerun 01

| Field | Value |
| --- | --- |
| Run scope | Legal-framework, legal-relation and national-AI-ethics-council query IDs in frozen search strategy §§6–8. |
| Run date | 31/07/2026 (UTC retrieval timestamps are in the CSV manifest). |
| Status | `FAIL_CLOSED_INCOMPLETE_OFFICIAL_PORTAL_SEARCH` |
| Boundary | Raw retrieval only; no screening, eligibility, legal-effect coding, implementation inference, citation chasing, deduplication, or PRISMA count. |
| Immutable inputs | `protocol.md` and `artifacts/protocol-registration-lock-2026-07-31/` were read only and not changed. |

## Evidence captured

- The prior seed harvest remains intact: three direct `vanban.chinhphu.vn` seed identifiers, each with HTML metadata, PDF full text, retrieval time and SHA-256 in `official-sources/retrieval-log.csv`.
- Live portal access check: `vanban.chinhphu.vn`, `congbao.chinhphu.vn`, and `mst.gov.vn` returned HTTP 200; `vbpl.vn` failed TLS negotiation in this client. The raw homepage captures are under `official-sources/portal-*-home-2026-07-31.html`.
- `mst.gov.vn` accepts `GET /tim-kiem.htm?keywords=...`. The raw results and manifest `official-sources/mst-query-run-2026-07-31.csv` cover DQ-LAW-02, DQ-FRAME-02, DQ-REL-01, DQ-COUNCIL-NAME-01 through `-06`, DQ-COUNCIL-EST-01 and DQ-COUNCIL-ACT-01 through `-02`, together with the query-group subqueries required because the portal lacks Boolean controls.
- The exact national-council name queries and the unsplit Boolean-like parent queries reported zero MST results. This is an observation limited to the captured first results page; it is not evidence that a council, a legal instrument, or an activity does not exist.

## Why this branch remains fail-closed

The frozen protocol requires every GOV/GAZ/GOV-VB/VBPL query to reach its own stopping rule (up to 100 results/10 pages) and the legal document graph to be traversed to depth three until no new document ID, subject to a 50-linked-document cap. This run has not met those requirements because:

1. The MST endpoint is a news search, not the GOV/GAZ/GOV-VB/VBPL legal-document search required for legal relationships.
2. The captured MST pages are first-page evidence only. Several decomposed terms exceed the 50-result cap, so they are explicitly unsaturated.
3. The client could not access `vbpl.vn`; no replacement source is asserted.
4. No document-relation graph (legal basis, citation, amendment, replacement, repeal, implementation guidance) has been constructed from the three seed full texts.
5. The MOH units, UNESCO-RAM, WHO-VNM and the fixed implementation-case frame are intentionally outside this narrowly bounded legal/council run and remain unrun.

## Required next action

Use a client that can query the official legal databases with pagination and capture response provenance. Run each frozen query ID separately, retain raw page-level results, traverse the three seed documents' legal relation graph, and only then update the overall search status. No status may be promoted on the basis of this log.
