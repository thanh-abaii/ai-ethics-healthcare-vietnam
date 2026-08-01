import csv
import datetime
import hashlib
import json
import os
import re
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_ROOT = ROOT / "artifacts" / "search-rerun-01-2026-07-31"
OFFICIAL_ROOT = ARTIFACT_ROOT / "official-sources"
OUTPUT_CSV = ARTIFACT_ROOT / "official-inventory.csv"

INVENTORY_FIELDS = [
    "manifestation_id", "source_channel", "source_record_id", "title", "year",
    "doi", "pmid", "openalex_id", "raw_artifact_locator", "raw_artifact_checksum",
    "retrieval_run_id", "query_locator", "provenance_status",
]


def sha256_file(path_obj):
    h = hashlib.sha256()
    abs_str = str(path_obj.resolve())
    long_p = "\\\\?\\" + abs_str if os.name == "nt" and not abs_str.startswith("\\\\?\\") else abs_str
    with open(long_p, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest().lower()


class HTMLTitleExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.current_href = None
        self.current_text = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "a":
            d = dict(attrs)
            href = d.get("href")
            title_attr = d.get("title", "")
            if href:
                self.current_href = href
                self.current_text = [title_attr] if title_attr else []

    def handle_data(self, data):
        if self.current_href and data.strip():
            self.current_text.append(data.strip())

    def handle_endtag(self, tag):
        if tag.lower() == "a" and self.current_href:
            txt = " ".join(self.current_text).strip()
            if len(txt) >= 15:
                self.links.append((self.current_href, txt))
            self.current_href = None
            self.current_text = []


def main():
    records = []
    seen_titles = set()
    counter = 1

    # 1. Parse Legal Portals HTML (vanban & congbao)
    legal_dir = OFFICIAL_ROOT / "legal-portals-20260801T095241" / "raw"
    if legal_dir.exists():
        for html_p in sorted(legal_dir.glob("*.html")):
            rel_loc = str(html_p.relative_to(ARTIFACT_ROOT)).replace("\\", "/")
            file_hash = sha256_file(html_p)
            
            content = html_p.read_text(encoding="utf-8", errors="replace")
            parser = HTMLTitleExtractor()
            try:
                parser.feed(content)
            except Exception:
                continue

            channel = "LEGAL_GOV" if "gov-vb" in html_p.name else "LEGAL_GAZ"
            for href, title in parser.links:
                clean_title = re.sub(r'\s+', ' ', title).strip()
                if clean_title and clean_title not in seen_titles:
                    seen_titles.add(clean_title)
                    doc_id = f"OFFICIAL-LEGAL-{counter:04d}"
                    counter += 1
                    records.append({
                        "manifestation_id": f"MANIFEST:{doc_id}",
                        "source_channel": channel,
                        "source_record_id": doc_id,
                        "title": clean_title[:200],
                        "year": "2026",
                        "doi": "",
                        "pmid": "",
                        "openalex_id": "",
                        "raw_artifact_locator": rel_loc,
                        "raw_artifact_checksum": file_hash,
                        "retrieval_run_id": "legal-portals-20260801T095241",
                        "query_locator": "official-sources/legal-portals-20260801T095241/query-ledger.csv",
                        "provenance_status": "VERIFIED_RAW_MANIFEST",
                    })

    # 2. Parse Non-legal Official Portals HTML (MOH 7 channels, MOST, UNESCO, WHO)
    nl_runs_dir = OFFICIAL_ROOT / "nl-runs"
    if nl_runs_dir.exists():
        for run_dir in sorted(nl_runs_dir.glob("*")):
            raw_sub = run_dir / "raw"
            if raw_sub.exists():
                for html_p in sorted(raw_sub.glob("*.html")):
                    rel_loc = str(html_p.relative_to(ARTIFACT_ROOT)).replace("\\", "/")
                    file_hash = sha256_file(html_p)
                    content = html_p.read_text(encoding="utf-8", errors="replace")
                    parser = HTMLTitleExtractor()
                    try:
                        parser.feed(content)
                    except Exception:
                        continue
                    
                    for href, title in parser.links:
                        clean_title = re.sub(r'\s+', ' ', title).strip()
                        if clean_title and clean_title not in seen_titles:
                            seen_titles.add(clean_title)
                            doc_id = f"OFFICIAL-MOH-{counter:04d}"
                            counter += 1
                            records.append({
                                "manifestation_id": f"MANIFEST:{doc_id}",
                                "source_channel": "OFFICIAL_MOH_POLICY",
                                "source_record_id": doc_id,
                                "title": clean_title[:200],
                                "year": "2026",
                                "doi": "",
                                "pmid": "",
                                "openalex_id": "",
                                "raw_artifact_locator": rel_loc,
                                "raw_artifact_checksum": file_hash,
                                "retrieval_run_id": run_dir.name,
                                "query_locator": str((run_dir / "query-ledger.csv").relative_to(ARTIFACT_ROOT)).replace("\\", "/"),
                                "provenance_status": "VERIFIED_RAW_MANIFEST",
                            })

    print(f"Compiled {len(records)} official candidate title manifestations.")

    with open(OUTPUT_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=INVENTORY_FIELDS)
        writer.writeheader()
        writer.writerows(records)

    print(f"Saved official inventory CSV: {OUTPUT_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
