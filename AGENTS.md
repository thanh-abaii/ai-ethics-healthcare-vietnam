# Agent Instructions & Immutability Rules for Research Repository

## Protection of Pre-Registered OSF Snapshot Files / Quy tắc Bảo vệ Tệp Đăng ký OSF

**MANDATORY RULE FOR ALL AI AGENTS & CONTRIBUTORS:**

1. **Do NOT modify pre-registered OSF frozen protocol files:**
   - The file `protocol.md` and all files inside `artifacts/protocol-registration-lock-2026-07-31/` represent the frozen snapshot pre-registered on OSF under DOI [10.17605/OSF.IO/62B8W](https://doi.org/10.17605/OSF.IO/62B8W) (OSF ID [`62b8w`](https://osf.io/62b8w/)).
   - **AI Agents are strictly prohibited from modifying, editing, or overwriting `protocol.md` or any frozen snapshot files.**

2. **Document post-registration execution in independent log files only:**
   - All post-registration progress, feasibility pilot outcomes (e.g. `G4-G5 PASS`), search logs, screening decisions, and data extraction outputs **must be logged exclusively in independent post-registration log files** (such as `g4-g5-feasibility-pilot-2026-07-31.md`, `search-log.csv`, or dedicated `protocol-amendment-pr-*.md` files).

3. **Ensure 100% byte-for-byte fidelity:**
   - `protocol.md` in the working directory must remain 100% identical to the OSF registration snapshot to maintain complete scientific integrity for peer review.
