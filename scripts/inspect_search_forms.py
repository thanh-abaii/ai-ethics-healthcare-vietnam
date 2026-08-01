#!/usr/bin/env python3
"""Inspect form inputs, JavaScript AJAX calls, and ASP.NET parameters in vanban.chinhphu.vn and congbao.chinhphu.vn."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "artifacts/search-rerun-01-2026-07-31/official-sources/legal-portals-20260801T092029/raw"


def main() -> int:
    gov_file = RAW_DIR / "gov-vb-q01-p01.html"
    gaz_file = RAW_DIR / "gaz-q01-p01.html"

    if gov_file.exists():
        text_gov = gov_file.read_text(encoding="utf-8", errors="replace")
        print(f"=== GOV-VB HTML Size: {len(text_gov)} bytes ===")
        forms = re.findall(r'<form[^>]*>', text_gov, re.IGNORECASE)
        print("Forms found:", forms)
        inputs = re.findall(r'<input[^>]*name=["\']([^"\']+)["\'][^>]*>', text_gov, re.IGNORECASE)
        print("Input names found:", inputs[:15])
        scripts = re.findall(r'fetch\(|jQuery\.ajax|\$\.ajax|\$\.post|\$\.get|location\.href', text_gov, re.IGNORECASE)
        print("Script keywords found:", len(scripts))

    if gaz_file.exists():
        text_gaz = gaz_file.read_text(encoding="utf-8", errors="replace")
        print(f"\n=== GAZ HTML Size: {len(text_gaz)} bytes ===")
        forms_gaz = re.findall(r'<form[^>]*>', text_gaz, re.IGNORECASE)
        print("GAZ Forms found:", forms_gaz)
        inputs_gaz = re.findall(r'<input[^>]*name=["\']([^"\']+)["\'][^>]*>', text_gaz, re.IGNORECASE)
        print("GAZ Input names found:", inputs_gaz[:15])

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
