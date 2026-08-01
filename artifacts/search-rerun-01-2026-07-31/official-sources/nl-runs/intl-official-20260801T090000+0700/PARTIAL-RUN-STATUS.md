# Partial-run status

**Status:** `TECHNICAL_FAILURE_NOT_A_SEARCH_RESULT`  
**Stopped:** 2026-08-01 (local execution)  

The run stopped after saving the first UNESCO-RAM response body and headers but before saving its paired error file. The cause was an unguarded text write while the synchronized workspace transiently removed the `raw/` directory. This run is not complete, must not be appended to, and must not be used for source, candidate, PRISMA, screening, or absence claims. A separate run identifier will be used after the per-file directory guard is repaired.
