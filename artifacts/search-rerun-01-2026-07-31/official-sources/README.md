# Official/legal source harvest — rerun 01

- Run label: `OFFICIAL_LEGAL_SEED_HARVEST`
- Retrieval date (UTC): `2026-07-31T12:36:35Z`
- Scope: fresh direct retrieval of the three pre-specified legal seed identifiers only: `DQ-LAW-01`, `DQ-DEC-01`, `DQ-FRAME-01`.
- Portal: `vanban.chinhphu.vn` (metadata/stable locators) and official `datafiles.chinhphu.vn` attachments.
- Boundary: This is raw-source harvest only. It is **not** a completed official-portal search, deduplication, screening, extraction, PRISMA flow, or gate result. No eligibility decision is recorded here.
- Reproduction: use the exact URLs and document identifiers in `query-run-log.csv`; verify the files with SHA-256 in `retrieval-log.csv`.
- Header-provenance limitation: all six raw artifacts were written and SHA-256 verified. The client did not expose HTTP response headers after file output; `retrieval-headers.json` records this limitation prospectively. Do not infer an HTTP status, ETag or Last-Modified date.
- Failure rule: a missing/failed artifact causes this seed harvest to be `FAIL_CLOSED`; no substitute source is introduced.
