"""Regression tests for PR07 locator integrity in the master registry compiler."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from compile_master_input_registry import ARTIFACT_ROOT, find_pr07_body_by_checksum, relative_artifact_locator


class Pr07LocatorTests(unittest.TestCase):
    def test_resolves_ministry_artifact_by_manifest_checksum_not_glob_order(self) -> None:
        root = Path(__file__).resolve().parents[1]
        raw_dir = root / "artifacts" / "pr07-12slot-provenance-compliance-run-20260801T230707" / "raw-artifacts"
        expected = "d69fdc367abf482e569fc7ab4a234c8468ffd2e3e8f8a0c5efabf319d69967bf"
        resolved = find_pr07_body_by_checksum(raw_dir, expected)
        self.assertIsNotNone(resolved)
        self.assertEqual("doc-MINISTRY-01-moh.gov.vn-DQ-IMPL-01-pos3.body", resolved.name)

    def test_pr07_locator_is_relative_to_the_registry_artifact_root(self) -> None:
        root = Path(__file__).resolve().parents[1]
        raw_file = root / "artifacts" / "pr07-12slot-provenance-compliance-run-20260801T230707" / "raw-artifacts" / "doc-MINISTRY-01-moh.gov.vn-DQ-IMPL-01-pos3.body"
        locator = relative_artifact_locator(raw_file)
        self.assertEqual(
            "../pr07-12slot-provenance-compliance-run-20260801T230707/raw-artifacts/doc-MINISTRY-01-moh.gov.vn-DQ-IMPL-01-pos3.body",
            locator,
        )
        self.assertTrue((ARTIFACT_ROOT / locator).resolve().is_file())


if __name__ == "__main__":
    unittest.main()
