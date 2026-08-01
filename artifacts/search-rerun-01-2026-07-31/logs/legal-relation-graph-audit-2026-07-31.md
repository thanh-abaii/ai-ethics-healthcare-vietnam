# Legal relationship graph audit — rerun 01

| Field | Value |
| --- | --- |
| Run state | `FAIL_CLOSED_INCOMPLETE_LEGAL_RELATION_GRAPH` |
| Scope | Three raw GOV-VB seed documents only; no screening, eligibility, legal-effect coding, extraction, deduplication, citation chasing, or PRISMA count. |
| Graph rule | The frozen strategy requires traversal through `căn cứ/dẫn chiếu/sửa đổi/thay thế/bãi bỏ/hướng dẫn` to depth 3, stopping only when no new document ID is found or 50 linked documents are reached. |
| Result | One direct, evidence-backed edge was verified. One additional linked document ID was discovered but is not harvested. The required traversal is therefore incomplete. |
| Immutable inputs | `protocol.md` and `artifacts/protocol-registration-lock-2026-07-31/` were read only and were not changed. |

## Raw-source inventory and provenance check

The file identities, stable locators, retrieval timestamps and hashes below are copied from `official-sources/retrieval-log.csv`; SHA-256 was recomputed locally on 31/07/2026 and matched that manifest.

| Graph node | Raw full text | PDF pages | SHA-256 | Raw metadata page | Stable locator |
| --- | --- | ---: | --- | --- | --- |
| `GOV-VB-134-2025-QH15` | `official-sources/gov-vb-134-2025-qh15-fulltext.pdf` | 20 | `53be2f9993e5060cc0ce723fc506d6535c9358978dbbeff11324c8d6236cae69` | `official-sources/gov-vb-134-2025-qh15-metadata.html` (`128c73c287197e242adfaf164fe4b4039bc1dc9575a27f424b24f84f41d0d2d3`) | `https://vanban.chinhphu.vn/?docid=216334&orggroupid=1&pageid=27160` |
| `GOV-VB-142-2026-ND-CP` | `official-sources/gov-vb-142-2026-nd-cp-fulltext.pdf` | 97 | `988fa7091b9f70615b8ae984e7e43b15293eb31398a113c86cc34f26666d5e40` | `official-sources/gov-vb-142-2026-nd-cp-metadata.html` (`c0182f97bede2ed0e434716e099a982469d71e4e7fb757ac4ec0f57ff2e1eab8`) | `https://vanban.chinhphu.vn/?docid=218029&orggroupid=2&pageid=27160` |
| `GOV-VB-05-2026-TT-BKHCN` | `official-sources/gov-vb-05-2026-tt-bkhcn-fulltext.pdf` | 9 | `45616232b7023fef199cce2d52d5896d1db59b990a74fd40648b262d11490220` | `official-sources/gov-vb-05-2026-tt-bkhcn-metadata.html` (`327893867142a8cbb0562fc1254077720a476a251cc044435ee7b4c7da8be728`) | `https://vanban.chinhphu.vn/?docid=217165&orggroupid=4&pageid=27160` |

The metadata HTML establishes the three seed identifiers and portal locators; it does not supply a complete legal-relation field. The direct relation below is therefore located in the raw PDF, not inferred from metadata or document titles.

## Edge register

| Edge ID | Source node | Relation | Target node | Evidence locator in raw source | Finding state |
| --- | --- | --- | --- | --- | --- |
| `LRE-001` | `GOV-VB-05-2026-TT-BKHCN` | `CĂN_CỨ` | `GOV-VB-134-2025-QH15` | `gov-vb-05-2026-tt-bkhcn-fulltext.pdf`, p. 1, opening recital: “Căn cứ Luật Trí tuệ nhân tạo số 134/2025/QH15 ngày 10 tháng 12 năm 2025” | `VERIFIED_DIRECT` |
| `LRE-002` | `GOV-VB-05-2026-TT-BKHCN` | `CĂN_CỨ` | `UNHARVESTED-55-2025-ND-CP` | `gov-vb-05-2026-tt-bkhcn-fulltext.pdf`, p. 1, opening recital: “Căn cứ Nghị định số 55/2025/NĐ-CP ngày 02 tháng 3 năm 2025” | `DISCOVERED_UNHARVESTED` |

`LRE-002` is a discovered target identifier, not a verified legal record: no raw official document, metadata, portal document ID, status, stable locator or checksum for `55/2025/NĐ-CP` is present in this run. It counts as a new linked document for traversal and must be harvested before the graph can advance to depth 2.

## Non-edges and limitations

- The provisions in the 05 seed about issuing future administrative guidance (p. 4) and the appendices headed “Hướng dẫn” (pp. 5–7) name no separate target legal document. They are deliberately not converted into `HƯỚNG_DẪN` edges.
- The extracted text layer of `GOV-VB-134-2025-QH15` was empty on all 20 PDF pages and that of `GOV-VB-142-2026-ND-CP` was empty on all 97 PDF pages. No relation, including a claim of “none found”, is recorded for either document. This audit did not use OCR or infer relations from their filenames, publication dates, search snippets, or the protocol narrative.
- No official legal-database pagination was captured for GOV-VB, GAZ or VBPL, and `vbpl.vn` was inaccessible in the existing client. Thus neither the required per-query stopping rule nor the graph stopping rule has been met.
- No assertion is made that the observed relation set is exhaustive, that any document is effective/repealed/amended/replaced, or that a named legal mechanism exists or operates.

## Required continuation from this audit

1. Harvest and hash the official record and full text for `55/2025/NĐ-CP`, then inspect its relations as depth 2.
2. Obtain reviewable text or page-image locators for every page of the 134 and 142 seeds before asserting their relations.
3. Run the frozen GOV-VB/GAZ/VBPL relation queries with page-level provenance; then traverse every newly discovered document to depth 3, observing the 50-linked-document cap.
4. Leave the overall official-search status fail-closed until these items and the other required search branches are independently complete.
