"""Contract tests for the PR07 bounded public-source retrieval runner."""
from __future__ import annotations

import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pr07_slot_retrieval import build_slot_plan


class SlotPlanTests(unittest.TestCase):
    def test_plan_has_exactly_twelve_nonlegal_slots(self) -> None:
        plan = build_slot_plan()
        self.assertEqual(12, len(plan))
        self.assertEqual(
            {"MINISTRY-01", "MINISTRY-02", "MINISTRY-03", "MINISTRY-04",
             "INTL-01", "INTL-02", "INTL-03", "SENTINEL-01",
             "SENTINEL-02", "SENTINEL-03", "SENTINEL-04", "SENTINEL-05"},
            {slot.slot_id for slot in plan},
        )

    def test_ministry_query_priority_is_preserved(self) -> None:
        plan = {slot.slot_id: slot for slot in build_slot_plan()}
        self.assertEqual(("DQ-IMPL-02", "DQ-IMPL-01", "DQ-IMPL-04"), plan["MINISTRY-01"].query_ids)
        self.assertEqual(("DQ-IMPL-04", "DQ-IMPL-05", "DQ-EVID-03"), plan["MINISTRY-02"].query_ids)

    def test_sentinel_slots_keep_all_ten_locked_queries(self) -> None:
        plan = {slot.slot_id: slot for slot in build_slot_plan()}
        expected = (
            "DQ-IMPL-01", "DQ-IMPL-04", "DQ-IMPL-05", "DQ-TOOL-01", "DQ-TOOL-02",
            "DQ-EVID-01", "DQ-EVID-02", "DQ-EVID-03", "DQ-EVID-04", "DQ-EVID-05",
        )
        self.assertEqual(expected, plan["SENTINEL-01"].query_ids)
        self.assertEqual(expected, plan["SENTINEL-05"].query_ids)


if __name__ == "__main__":
    unittest.main()
