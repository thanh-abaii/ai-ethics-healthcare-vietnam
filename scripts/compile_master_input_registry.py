from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_ROOT = ROOT / "artifacts" / "search-rerun-01-2026-07-31"
PR07_ROOT = ROOT / "artifacts" / "pr07-12slot-provenance-compliance-run-20260801T230707"
REGISTRY_DIR = ARTIFACT_ROOT / "registry"
LOGS_DIR = ARTIFACT_ROOT / "logs"

INVENTORY_FIELDS = [
    "manifestation_id", "source_channel", "source_record_id", "title", "year",
    "doi", "pmid", "openalex_id", "normalized_url", "raw_artifact_locator", "raw_artifact_checksum",
    "retrieval_run_id", "query_locator", "provenance_status",
]

CANDIDATE_FIELDS = [
    "candidate_id", "match_basis", "match_value", "member_manifestation_ids",
    "member_sources", "recommendation", "rationale",
]

EVENT_FIELDS = [
    "registry_event_id", "row_type", "record_id", "canonical_record_id", "document_id", "framework_id", "title", "year",
    "language", "doi", "pmid", "openalex_id", "official_document_number", "normalized_url", "manifestation_type",
    "provenance_event_id", "discovery_channel", "query_id", "seed_record_id", "citation_direction", "discovery_date",
    "raw_artifact_locator", "raw_artifact_checksum", "duplicate_status", "duplicate_basis", "preferred_version",
    "preferred_version_reason", "reviewer", "screening_stage", "reviewer_decision", "exclusion_reason", "decision_date",
    "final_adjudication", "adjudicator", "adjudication_date", "screening_codebook_version", "registry_version",
    "supersedes_event_id", "change_type", "change_reason", "notes",
]

MASTER_REGISTRY_FIELDS = [
    "canonical_record_id", "primary_manifestation_id", "title", "year", "source_channels",
    "doi", "pmid", "openalex_id", "official_document_number", "member_manifestation_count",
    "member_manifestation_ids", "duplicate_status", "duplicate_basis", "preferred_version_reason",
    "screening_status", "provenance_status",
]


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().lower()


def norm_doi(value: str | None) -> str:
    value = (value or "").strip().lower()
    value = re.sub(r"^https?://(dx\.)?doi\.org/", "", value)
    return value.rstrip(" .;,)")


def norm_title(value: str | None) -> str:
    val = (value or "").lower()
    val = re.sub(r"[^\w\s]", "", val)
    return re.sub(r"\s+", " ", val).strip()


def year_from(value: str | None) -> str:
    match = re.search(r"\b(19|20)\d{2}\b", value or "")
    return match.group(0) if match else "2026"


def check_file(path: Path, expected_sha: str, failures: list[str]) -> bool:
    if not path.is_file():
        failures.append(f"MISSING_RAW_ARTIFACT: {path}")
        return False
    actual = file_sha256(path)
    if actual.lower() != expected_sha.lower():
        failures.append(f"CHECKSUM_MISMATCH: {path} expected={expected_sha} actual={actual}")
        return False
    return True


def find_pr07_body_by_checksum(raw_dir: Path, expected_sha: str) -> Path | None:
    """Return the one PR07 body file whose bytes match the manifest checksum.

    Glob order is not provenance: a failed probe may precede the successful
    document probe for the same slot.  The manifest hash is the authority.
    """
    expected = expected_sha.lower()
    matches = [path for path in raw_dir.glob("doc-*.body") if file_sha256(path).lower() == expected]
    return matches[0] if len(matches) == 1 else None


def relative_artifact_locator(path: Path) -> str:
    """Return a portable locator relative to the registry artifact root."""
    return os.path.relpath(path, ARTIFACT_ROOT).replace("\\", "/")


def load_pubmed_inventory(failures: list[str]) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    for manifest_path in sorted((ARTIFACT_ROOT / "pubmed").glob("*/manifest.json")):
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if "RAW_" not in manifest.get("status", "") or "CAPTURED" not in manifest.get("status", ""):
            continue
        run_dir = manifest_path.parent
        files = {item["file"]: item["sha256"] for item in manifest.get("files", [])}
        required = ["esearch-response.raw", "esummary-batch-000000-response.raw"]
        if any(name not in files for name in required):
            failures.append(f"PUBMED_MANIFEST_INCOMPLETE: {manifest_path}")
            continue
        if not all(check_file(run_dir / name, files[name], failures) for name in required):
            continue
        summary_file = run_dir / "esummary-batch-000000-response.raw"
        try:
            payload = json.loads(summary_file.read_text(encoding="utf-8"))
            result = payload["result"]
            uids = result["uids"]
        except (json.JSONDecodeError, KeyError, TypeError) as exc:
            failures.append(f"PUBMED_PARSE_ERROR: {summary_file}: {exc}")
            continue
        for uid in uids:
            item = result.get(str(uid), {})
            ids = {entry.get("idtype", ""): entry.get("value", "") for entry in item.get("articleids", [])}
            records.append({
                "manifestation_id": f"PMID:{uid}",
                "source_channel": "PUBMED",
                "source_record_id": str(uid),
                "title": item.get("title", "").strip(),
                "year": year_from(item.get("pubdate") or item.get("epubdate")),
                "doi": norm_doi(ids.get("doi")),
                "pmid": str(uid),
                "openalex_id": "",
                "raw_artifact_locator": str(summary_file.relative_to(ARTIFACT_ROOT)).replace("\\", "/"),
                "raw_artifact_checksum": files[summary_file.name].lower(),
                "retrieval_run_id": manifest.get("run_id", "UNKNOWN"),
                "query_locator": "DQ-PUBMED-01",
                "normalized_url": f"https://pubmed.ncbi.nlm.nih.gov/{uid}/",
                "provenance_status": "VERIFIED_RAW_MANIFEST",
            })
    return records


def load_openalex_inventory(failures: list[str]) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    for manifest_path in sorted((ARTIFACT_ROOT / "openalex").glob("*/manifest.json")):
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if "RAW_" not in manifest.get("status", "") or "CAPTURED" not in manifest.get("status", ""):
            continue
        run_dir = manifest_path.parent
        pages = manifest.get("pages", [])
        if not pages or any(page.get("http_status") != 200 for page in pages):
            failures.append(f"OPENALEX_MANIFEST_NOT_COMPLETE: {manifest_path}")
            continue
        for page in pages:
            raw = run_dir / page["raw_file"]
            if not check_file(raw, page["raw_sha256"], failures):
                continue
            try:
                payload = json.loads(raw.read_text(encoding="utf-8"))
                results = payload["results"]
            except (json.JSONDecodeError, KeyError, TypeError) as exc:
                failures.append(f"OPENALEX_PARSE_ERROR: {raw}: {exc}")
                continue
            for item in results:
                work_id = item["id"].rsplit("/", 1)[-1]
                ids = item.get("ids") or {}
                pmid = (ids.get("pmid") or "").rsplit("/", 1)[-1]
                doi_val = norm_doi(item.get("doi"))
                norm_url = f"https://doi.org/{doi_val}" if doi_val else f"https://openalex.org/W{work_id}"
                records.append({
                    "manifestation_id": f"OPENALEX:{work_id}",
                    "source_channel": "OPENALEX",
                    "source_record_id": work_id,
                    "title": (item.get("display_name") or "").strip(),
                    "year": str(item.get("publication_year") or "2026"),
                    "doi": doi_val,
                    "pmid": pmid,
                    "openalex_id": work_id,
                    "raw_artifact_locator": str((run_dir / page["raw_file"]).relative_to(ARTIFACT_ROOT)).replace("\\", "/"),
                    "raw_artifact_checksum": page["raw_sha256"].lower(),
                    "retrieval_run_id": manifest.get("run_id", run_dir.name),
                    "query_locator": "DQ-OPENALEX-01",
                    "normalized_url": norm_url,
                    "provenance_status": "VERIFIED_RAW_MANIFEST",
                })
    return records


def load_verified_legal_documents(failures: list[str]) -> list[dict[str, str]]:
    nd_cp = "N\u0110-C" + "P"
    legal_docs = [
        {
            "manifestation_id": "LEGAL:134/2025/QH15",
            "source_channel": "LEGAL_OFFICIAL_PORTAL",
            "source_record_id": "134/2025/QH15",
            "title": "Luật Trí tuệ nhân tạo",
            "year": "2025",
            "doi": "", "pmid": "", "openalex_id": "",
            "raw_artifact_locator": "official-sources/legal-seed-retrieval-20260801T135648/raw/s01.signed.pdf",
            "raw_artifact_checksum": "53be2f9993e5060cc0ce723fc506d6535c9358978dbbeff11324c8d6236cae69",
            "retrieval_run_id": "legal-seed-retrieval-20260801T135648",
            "query_locator": "DQ-LEGAL-SEED-01",
            "normalized_url": "https://vanban.chinhphu.vn/?classid=1&docid=216334&pageid=27160&typegroupid=3",
            "provenance_status": "VERIFIED_RAW_MANIFEST",
        },
        {
            "manifestation_id": f"LEGAL:142/2026/{nd_cp}",
            "source_channel": "LEGAL_OFFICIAL_PORTAL",
            "source_record_id": f"142/2026/{nd_cp}",
            "title": "Quy định chi tiết một số điều và biện pháp thi hành Luật Trí tuệ nhân tạo",
            "year": "2026",
            "doi": "", "pmid": "", "openalex_id": "",
            "raw_artifact_locator": "official-sources/legal-seed-retrieval-20260801T135648/raw/s02.signed.pdf",
            "raw_artifact_checksum": "988fa7091b9f70615b8ae984e7e43b15293eb31398a113c86cc34f26666d5e40",
            "retrieval_run_id": "legal-seed-retrieval-20260801T135648",
            "query_locator": "DQ-LEGAL-SEED-02",
            "normalized_url": "https://vanban.chinhphu.vn/?docid=218029&orggroupid=2&pageid=27160",
            "provenance_status": "VERIFIED_RAW_MANIFEST",
        },
        {
            "manifestation_id": "LEGAL:05/2026/TT-BKHCN",
            "source_channel": "LEGAL_OFFICIAL_PORTAL",
            "source_record_id": "05/2026/TT-BKHCN",
            "title": "Ban hành Khung đạo đức trí tuệ nhân tạo quốc gia",
            "year": "2026",
            "doi": "", "pmid": "", "openalex_id": "",
            "raw_artifact_locator": "official-sources/legal-seed-retrieval-20260801T135648/raw/s03.signed.pdf",
            "raw_artifact_checksum": "45616232b7023fef199cce2d52d5896d1db59b990a74fd40648b262d11490220",
            "retrieval_run_id": "legal-seed-retrieval-20260801T135648",
            "query_locator": "DQ-LEGAL-SEED-03",
            "normalized_url": "https://vanban.chinhphu.vn/?classid=1&docid=217165&pageid=27160&typegroupid=6",
            "provenance_status": "VERIFIED_RAW_MANIFEST",
        },
        {
            "manifestation_id": f"LEGAL:55/2025/{nd_cp}",
            "source_channel": "LEGAL_OFFICIAL_PORTAL",
            "source_record_id": f"55/2025/{nd_cp}",
            "title": f"Nghị định 55/2025/{nd_cp} quy định chi tiết về quản lý và vận hành hệ thống thông tin y tế số",
            "year": "2025",
            "doi": "", "pmid": "", "openalex_id": "",
            "raw_artifact_locator": "official-sources/legal-relation-traversal-20260801T135720/raw/resolve-04.fulltext.pdf",
            "raw_artifact_checksum": "96558197392fc88f1d5f3b398cc294a113f976b34df034856eace3c385bff03b",
            "retrieval_run_id": "legal-relation-traversal-20260801T135720",
            "query_locator": "DQ-LEGAL-REL-01",
            "normalized_url": "https://vanban.chinhphu.vn/?pageid=27160&docid=213020",
            "provenance_status": "VERIFIED_RAW_MANIFEST",
        },
    ]
    for doc in legal_docs:
        path = ARTIFACT_ROOT / doc["raw_artifact_locator"]
        if not check_file(path, doc["raw_artifact_checksum"], failures):
            failures.append(f"LEGAL_DOC_CHECKSUM_FAILED: {doc['manifestation_id']}")
    return legal_docs


def load_pr07_inventory(failures: list[str]) -> list[dict[str, str]]:
    manifest_inv = PR07_ROOT / "manifestations-inventory.csv"
    if not manifest_inv.is_file():
        failures.append(f"MISSING_PR07_FILES: {manifest_inv}")
        return []
            
    records = []
    with manifest_inv.open("r", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            slot_id = row["slot_id"]
            expected_sha = row["raw_body_sha256"].lower()
            matched_file = find_pr07_body_by_checksum(PR07_ROOT / "raw-artifacts", expected_sha)
            
            if not matched_file:
                failures.append(f"PR07_CHECKSUM_NOT_FOUND: slot={slot_id} expected_sha={expected_sha}")
                continue
                
            locator = relative_artifact_locator(matched_file)
            if not check_file(matched_file, expected_sha, failures):
                failures.append(f"PR07_CHECKSUM_MISMATCH: slot={slot_id} file={matched_file.name}")
                continue

            records.append({
                "manifestation_id": f"PR07:{row['manifestation_id']}",
                "source_channel": "PR07_PUBLIC_SOURCE",
                "source_record_id": slot_id,
                "title": row["title"].strip(),
                "year": "2026",
                "doi": "",
                "pmid": "",
                "openalex_id": "",
                "raw_artifact_locator": locator.replace("\\", "/"),
                "raw_artifact_checksum": expected_sha,
                "retrieval_run_id": "pr07-12slot-provenance-compliance-run-20260801T230707",
                "query_locator": f"DQ-PR07-{slot_id}",
                "normalized_url": row["source_url"],
                "provenance_status": "VERIFIED_RAW_MANIFEST",
            })
    return records


def canonicalize_and_deduplicate(records: list[dict[str, str]]) -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    manifestation_by_id = {r["manifestation_id"]: r for r in records}
    
    doi_map: dict[str, list[str]] = defaultdict(list)
    pmid_map: dict[str, list[str]] = defaultdict(list)
    openalex_map: dict[str, list[str]] = defaultdict(list)
    title_year_map: dict[tuple[str, str], list[str]] = defaultdict(list)
    
    for r in records:
        mid = r["manifestation_id"]
        if r["doi"]:
            doi_map[r["doi"]].append(mid)
        if r["pmid"]:
            pmid_map[r["pmid"]].append(mid)
        if r["openalex_id"]:
            openalex_map[r["openalex_id"]].append(mid)
        norm_t = norm_title(r["title"])
        if norm_t and len(norm_t) > 15:
            title_year_map[(norm_t, r["year"])].append(mid)

    parent = {r["manifestation_id"]: r["manifestation_id"] for r in records}

    def get_root(i: str) -> str:
        if parent[i] == i:
            return i
        parent[i] = get_root(parent[i])
        return parent[i]

    def join_sets(i: str, j: str) -> None:
        root_i = get_root(i)
        root_j = get_root(j)
        if root_i != root_j:
            parent[root_i] = root_j

    match_bases: dict[tuple[str, str], set[str]] = defaultdict(set)

    for doi, mids in doi_map.items():
        for i in range(len(mids)):
            for j in range(i + 1, len(mids)):
                join_sets(mids[i], mids[j])
                match_bases[(min(mids[i], mids[j]), max(mids[i], mids[j]))].add("DOI")

    for pmid, mids in pmid_map.items():
        for i in range(len(mids)):
            for j in range(i + 1, len(mids)):
                join_sets(mids[i], mids[j])
                match_bases[(min(mids[i], mids[j]), max(mids[i], mids[j]))].add("PMID")

    for oaid, mids in openalex_map.items():
        for i in range(len(mids)):
            for j in range(i + 1, len(mids)):
                join_sets(mids[i], mids[j])
                match_bases[(min(mids[i], mids[j]), max(mids[i], mids[j]))].add("OPENALEX_ID")

    candidate_review_pairs: list[dict[str, str]] = []
    candidate_counter = 1
    for (t, y), mids in title_year_map.items():
        if len(mids) > 1:
            sources = sorted({manifestation_by_id[m]["source_channel"] for m in mids})
            candidate_review_pairs.append({
                "candidate_id": f"DUP-C{candidate_counter:05d}",
                "match_basis": "EXACT_TITLE_YEAR",
                "match_value": manifestation_by_id[mids[0]]["title"][:80],
                "member_manifestation_ids": " | ".join(sorted(mids)),
                "member_sources": " | ".join(sources),
                "recommendation": "CANONICALIZATION_REVIEW_REQUIRED",
                "rationale": "Identical title and year string without verified shared DOI/PMID/OpenAlex ID. Requires human/codebook fulltext verification before merging.",
            })
            candidate_counter += 1

    clusters: dict[str, list[str]] = defaultdict(list)
    for r in records:
        root_id = get_root(r["manifestation_id"])
        clusters[root_id].append(r["manifestation_id"])

    sorted_cluster_roots = sorted(clusters.keys(), key=lambda r: (
        manifestation_by_id[r]["doi"] or "",
        manifestation_by_id[r]["pmid"] or "",
        manifestation_by_id[r]["openalex_id"] or "",
        manifestation_by_id[r]["title"]
    ))

    master_registry: list[dict[str, str]] = []
    candidates: list[dict[str, str]] = candidate_review_pairs
    events: list[dict[str, str]] = []

    event_counter = 1
    discovered = datetime.now(timezone.utc).date().isoformat()

    for idx, root_id in enumerate(sorted_cluster_roots, 1):
        member_mids = sorted(clusters[root_id])
        canon_id = f"CANON-{idx:05d}"
        doc_id = f"DOC-{idx:05d}"

        def pref_score(m_id: str) -> tuple[int, int]:
            item = manifestation_by_id[m_id]
            ch = item["source_channel"]
            if "LEGAL" in ch or "OFFICIAL" in ch or "PR07" in ch:
                channel_rank = 0
            elif ch == "PUBMED":
                channel_rank = 1
            else:
                channel_rank = 2
            has_doi = 0 if item["doi"] else 1
            return (channel_rank, has_doi)

        primary_mid = min(member_mids, key=pref_score)
        primary_item = manifestation_by_id[primary_mid]

        is_duplicate = len(member_mids) > 1
        dup_status = "DUPLICATE_ALIAS" if is_duplicate else "UNIQUE"
        
        cluster_bases: set[str] = set()
        for i in range(len(member_mids)):
            for j in range(i + 1, len(member_mids)):
                pair = (min(member_mids[i], member_mids[j]), max(member_mids[i], member_mids[j]))
                cluster_bases.update(match_bases.get(pair, set()))
        
        dup_basis = " | ".join(sorted(cluster_bases)) if cluster_bases else "NOT_APPLICABLE"

        all_sources = sorted({manifestation_by_id[m]["source_channel"] for m in member_mids})

        master_registry.append({
            "canonical_record_id": canon_id,
            "primary_manifestation_id": primary_mid,
            "title": primary_item["title"],
            "year": primary_item["year"],
            "source_channels": " | ".join(all_sources),
            "doi": primary_item["doi"] or "NOT_REPORTED",
            "pmid": primary_item["pmid"] or "NOT_APPLICABLE",
            "openalex_id": primary_item["openalex_id"] or "NOT_APPLICABLE",
            "official_document_number": primary_item["source_record_id"] if "LEGAL" in primary_item["source_channel"] else "NOT_APPLICABLE",
            "member_manifestation_count": str(len(member_mids)),
            "member_manifestation_ids": " | ".join(member_mids),
            "duplicate_status": dup_status,
            "duplicate_basis": dup_basis,
            "preferred_version_reason": "Official legal/authority document priority." if "LEGAL" in primary_item["source_channel"] or "PR07" in primary_item["source_channel"] else ("Highest metadata completeness." if is_duplicate else "Single unique manifestation."),
            "screening_status": "PENDING_SCREENING",
            "provenance_status": "VERIFIED_RAW_MANIFEST",
        })

        if is_duplicate and dup_basis != "NOT_APPLICABLE":
            candidates.append({
                "candidate_id": f"DUP-C{candidate_counter:05d}",
                "match_basis": dup_basis,
                "match_value": primary_item["doi"] or primary_item["pmid"] or primary_item["openalex_id"],
                "member_manifestation_ids": " | ".join(member_mids),
                "member_sources": " | ".join(all_sources),
                "recommendation": "CANONICALIZATION_AUTOMATIC_VERIFIED",
                "rationale": f"Deterministic shared strong identifier ({dup_basis}). Retained all {len(member_mids)} manifestations for append-only provenance.",
            })
            candidate_counter += 1

        for mid in member_mids:
            item = manifestation_by_id[mid]
            legal = "LEGAL" in item["source_channel"]
            pref = "YES" if mid == primary_mid else "NO"
            pref_reason = "Selected as canonical representative based on channel authority and identifier completeness." if pref == "YES" else "Retained as manifestation alias within canonical cluster."
            
            events.append({
                "registry_event_id": f"REG-E{event_counter:06d}",
                "row_type": "MANIFESTATION",
                "record_id": mid,
                "canonical_record_id": canon_id,
                "document_id": doc_id,
                "framework_id": "NOT_APPLICABLE",
                "title": item["title"],
                "year": item["year"],
                "language": "VI" if "OFFICIAL" in item["source_channel"] or "PR07" in item["source_channel"] or "LEGAL" in item["source_channel"] else "EN",
                "doi": item["doi"] or "NOT_REPORTED",
                "pmid": item["pmid"] or "NOT_APPLICABLE",
                "openalex_id": item["openalex_id"] or "NOT_APPLICABLE",
                "official_document_number": item["source_record_id"] if legal else "NOT_APPLICABLE",
                "normalized_url": item["normalized_url"],
                "manifestation_type": "PDF" if legal else ("JSON" if "OPENALEX" in item["source_channel"] or "PUBMED" in item["source_channel"] else "HTML"),
                "provenance_event_id": "NOT_APPLICABLE",
                "discovery_channel": item["source_channel"],
                "query_id": "NOT_APPLICABLE",
                "seed_record_id": "NOT_APPLICABLE",
                "citation_direction": "NOT_APPLICABLE",
                "discovery_date": discovered,
                "raw_artifact_locator": item["raw_artifact_locator"],
                "raw_artifact_checksum": item["raw_artifact_checksum"],
                "duplicate_status": dup_status,
                "duplicate_basis": dup_basis,
                "preferred_version": pref,
                "preferred_version_reason": pref_reason,
                "reviewer": "NOT_APPLICABLE",
                "screening_stage": "NOT_APPLICABLE",
                "reviewer_decision": "NOT_APPLICABLE",
                "exclusion_reason": "",
                "decision_date": "NOT_APPLICABLE",
                "final_adjudication": "PENDING",
                "adjudicator": "NOT_APPLICABLE",
                "adjudication_date": "NOT_APPLICABLE",
                "screening_codebook_version": "NOT_APPLICABLE",
                "registry_version": "0.1-draft",
                "supersedes_event_id": "",
                "change_type": "CREATE",
                "change_reason": "Verified raw manifestation loaded without canonicalization.",
                "notes": item["provenance_status"],
            })
            event_counter += 1

            events.append({
                "registry_event_id": f"REG-E{event_counter:06d}",
                "row_type": "PROVENANCE",
                "record_id": mid,
                "canonical_record_id": canon_id,
                "document_id": doc_id,
                "framework_id": "NOT_APPLICABLE",
                "title": item["title"],
                "year": item["year"],
                "language": "VI" if "OFFICIAL" in item["source_channel"] or "PR07" in item["source_channel"] or "LEGAL" in item["source_channel"] else "EN",
                "doi": item["doi"] or "NOT_REPORTED",
                "pmid": item["pmid"] or "NOT_APPLICABLE",
                "openalex_id": item["openalex_id"] or "NOT_APPLICABLE",
                "official_document_number": item["source_record_id"] if legal else "NOT_APPLICABLE",
                "normalized_url": item["normalized_url"],
                "manifestation_type": "PDF" if legal else ("JSON" if "OPENALEX" in item["source_channel"] or "PUBMED" in item["source_channel"] else "HTML"),
                "provenance_event_id": f"PROV-{mid}",
                "discovery_channel": item["source_channel"],
                "query_id": item["query_locator"],
                "seed_record_id": "NOT_APPLICABLE",
                "citation_direction": "NOT_APPLICABLE",
                "discovery_date": discovered,
                "raw_artifact_locator": item["raw_artifact_locator"],
                "raw_artifact_checksum": item["raw_artifact_checksum"],
                "duplicate_status": dup_status,
                "duplicate_basis": dup_basis,
                "preferred_version": pref,
                "preferred_version_reason": pref_reason,
                "reviewer": "NOT_APPLICABLE",
                "screening_stage": "NOT_APPLICABLE",
                "reviewer_decision": "NOT_APPLICABLE",
                "exclusion_reason": "",
                "decision_date": "NOT_APPLICABLE",
                "final_adjudication": "PENDING",
                "adjudicator": "NOT_APPLICABLE",
                "adjudication_date": "NOT_APPLICABLE",
                "screening_codebook_version": "NOT_APPLICABLE",
                "registry_version": "0.1-draft",
                "supersedes_event_id": "",
                "change_type": "ADD_PROVENANCE",
                "change_reason": "Raw artifact checksum independently verified.",
                "notes": f"retrieval_run_id={item['retrieval_run_id']}",
            })
            event_counter += 1

            events.append({
                "registry_event_id": f"REG-E{event_counter:06d}",
                "row_type": "CANONICALIZATION",
                "record_id": mid,
                "canonical_record_id": canon_id,
                "document_id": doc_id,
                "framework_id": "NOT_APPLICABLE",
                "title": item["title"],
                "year": item["year"],
                "language": "VI" if "OFFICIAL" in item["source_channel"] or "PR07" in item["source_channel"] or "LEGAL" in item["source_channel"] else "EN",
                "doi": item["doi"] or "NOT_REPORTED",
                "pmid": item["pmid"] or "NOT_APPLICABLE",
                "openalex_id": item["openalex_id"] or "NOT_APPLICABLE",
                "official_document_number": item["source_record_id"] if legal else "NOT_APPLICABLE",
                "normalized_url": item["normalized_url"],
                "manifestation_type": "PDF" if legal else ("JSON" if "OPENALEX" in item["source_channel"] or "PUBMED" in item["source_channel"] else "HTML"),
                "provenance_event_id": "NOT_APPLICABLE",
                "discovery_channel": item["source_channel"],
                "query_id": "NOT_APPLICABLE",
                "seed_record_id": "NOT_APPLICABLE",
                "citation_direction": "NOT_APPLICABLE",
                "discovery_date": discovered,
                "raw_artifact_locator": item["raw_artifact_locator"],
                "raw_artifact_checksum": item["raw_artifact_checksum"],
                "duplicate_status": dup_status,
                "duplicate_basis": dup_basis,
                "preferred_version": pref,
                "preferred_version_reason": pref_reason,
                "reviewer": "NOT_APPLICABLE",
                "screening_stage": "NOT_APPLICABLE",
                "reviewer_decision": "NOT_APPLICABLE",
                "exclusion_reason": "",
                "decision_date": "NOT_APPLICABLE",
                "final_adjudication": "PENDING",
                "adjudicator": "NOT_APPLICABLE",
                "adjudication_date": "NOT_APPLICABLE",
                "screening_codebook_version": "NOT_APPLICABLE",
                "registry_version": "0.1-draft",
                "supersedes_event_id": "",
                "change_type": "CANONICALIZE",
                "change_reason": f"Canonicalized under cluster {canon_id} with match basis {dup_basis}.",
                "notes": f"primary_manifestation_id={primary_mid}",
            })
            event_counter += 1

    return master_registry, candidates, events


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    failures: list[str] = []
    
    pubmed = load_pubmed_inventory(failures)
    openalex = load_openalex_inventory(failures)
    legal = load_verified_legal_documents(failures)
    pr07 = load_pr07_inventory(failures)
    
    all_records = pubmed + openalex + legal + pr07

    if len(all_records) != 445:
        failures.append(f"INCORRECT_MANIFESTATION_COUNT: expected=445 actual={len(all_records)}")

    counts = Counter(r["manifestation_id"] for r in all_records)
    dups = [k for k, v in counts.items() if v > 1]
    if dups:
        failures.append(f"DUPLICATE_MANIFESTATION_ID: {dups}")

    if failures:
        print(f"Compilation FAILED with {len(failures)} errors:")
        for f in failures:
            print(f"  - {f}")
        return 2

    master_registry, candidates, events = canonicalize_and_deduplicate(all_records)

    raw_inv_path = REGISTRY_DIR / "raw-manifestation-inventory.csv"
    write_csv(raw_inv_path, INVENTORY_FIELDS, sorted(all_records, key=lambda r: r["manifestation_id"]))

    dedup_path = REGISTRY_DIR / "global-dedup-candidates.csv"
    write_csv(dedup_path, CANDIDATE_FIELDS, candidates)

    event_ledger_path = REGISTRY_DIR / "registry-event-ledger.csv"
    write_csv(event_ledger_path, EVENT_FIELDS, events)

    master_reg_path = REGISTRY_DIR / "master-record-registry.csv"
    write_csv(master_reg_path, MASTER_REGISTRY_FIELDS, master_registry)

    audit_path = LOGS_DIR / "provenance-dedup-audit.json"
    audit_summary = {
        "audit_type": "MASTER_INPUT_REGISTRY_COMPILATION_AND_CANONICALIZATION",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "total_raw_manifestations": len(all_records),
        "source_channel_breakdown": dict(Counter(r["source_channel"] for r in all_records)),
        "total_canonical_records": len(master_registry),
        "hard_identifier_duplicate_clusters": sum(c["match_basis"] != "EXACT_TITLE_YEAR" for c in candidates),
        "title_year_review_candidates": sum(c["match_basis"] == "EXACT_TITLE_YEAR" for c in candidates),
        "total_dedup_candidates": len(candidates),
        "total_registry_events": len(events),
        "event_type_breakdown": dict(Counter(e["row_type"] for e in events)),
        "integrity_failures": failures,
        "status": "PASS_READINESS_FOR_CANONICAL_MASTER_REGISTRY",
        "screening_phase_status": "SCREENING_NOT_OPEN",
        "search_status": "DIRECT_SEARCH_IN_PROGRESS",
        "remediation_note": "Remediated previous run: excluded 223 candidate titles; locked exact 445 verified manifestations scope; fixed authority priority order; fixed query_id & normalized_url schema fields."
    }
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    audit_path.write_text(json.dumps(audit_summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(audit_summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
