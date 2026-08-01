"""Bounded PR07 public-source retrieval primitives.

This module defines only the frozen slot/query plan. Network retrieval is kept
separate so the plan can be tested without contacting any external service.
"""
from __future__ import annotations

from dataclasses import dataclass


SENTINEL_QUERIES = (
    "DQ-IMPL-01", "DQ-IMPL-04", "DQ-IMPL-05", "DQ-TOOL-01", "DQ-TOOL-02",
    "DQ-EVID-01", "DQ-EVID-02", "DQ-EVID-03", "DQ-EVID-04", "DQ-EVID-05",
)


@dataclass(frozen=True)
class SlotPlan:
    slot_id: str
    slot_class: str
    domains: tuple[str, ...]
    query_ids: tuple[str, ...]


def build_slot_plan() -> tuple[SlotPlan, ...]:
    """Return the 12 non-legal PR07 slots in their published order."""
    return (
        SlotPlan("MINISTRY-01", "MINISTRY", ("moh.gov.vn", "asttmoh.vn", "kcb.vn"),
                 ("DQ-IMPL-02", "DQ-IMPL-01", "DQ-IMPL-04")),
        SlotPlan("MINISTRY-02", "MINISTRY", ("moh.gov.vn", "imda.moh.gov.vn", "ttyqg.vn", "kcb.vn"),
                 ("DQ-IMPL-04", "DQ-IMPL-05", "DQ-EVID-03")),
        SlotPlan("MINISTRY-03", "MINISTRY", ("most.gov.vn",),
                 ("DQ-IMPL-03", "DQ-TOOL-01", "DQ-TOOL-02")),
        SlotPlan("MINISTRY-04", "MINISTRY", ("moh.gov.vn", "most.gov.vn"),
                 ("DQ-TOOL-01", "DQ-TOOL-02", "DQ-EVID-01", "DQ-EVID-05")),
        SlotPlan("INTL-01", "INTL", ("www.who.int/vietnam",),
                 ("DQ-IMPL-03", "DQ-EVID-04")),
        SlotPlan("INTL-02", "INTL", ("www.unesco.org",),
                 ("DQ-IMPL-03", "DQ-TOOL-01")),
        SlotPlan("INTL-03", "INTL", ("www.who.int/vietnam", "www.unesco.org"),
                 ("DQ-EVID-04", "DQ-EVID-05")),
        SlotPlan("SENTINEL-01", "SENTINEL", ("soyte.hanoi.gov.vn",), SENTINEL_QUERIES),
        SlotPlan("SENTINEL-02", "SENTINEL", ("soyte.danang.gov.vn",), SENTINEL_QUERIES),
        SlotPlan("SENTINEL-03", "SENTINEL", ("medinet.gov.vn",), SENTINEL_QUERIES),
        SlotPlan("SENTINEL-04", "SENTINEL", ("bachmai.gov.vn", "bvtwhue.com.vn", "choray.vn"), SENTINEL_QUERIES),
        SlotPlan("SENTINEL-05", "SENTINEL", ("vinmec.com", "tamanhhospital.vn", "umc.edu.vn"), SENTINEL_QUERIES),
    )
