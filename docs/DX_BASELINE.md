# Developer Experience (DX) Baseline

This document captures a quantitative baseline for the developer experience of the ISA_D repository as of the completion of Horizon 1. It measures the time and steps required for a new developer (or AI agent) to answer common questions using only the tools available in a standard command-line environment.

The goal is to identify the largest sources of friction to guide the selection of new tooling in a data-driven way.

---

## Experiment 1: Find Purpose of a Service

**Question:** What is the purpose of the `etl` service?

*   **Start Time:** `2025-09-18 08:17:11.957131`
*   **Steps Taken:**
    1.  `ls -F`
    2.  `read_file("ISA_SuperApp/etl/README.md")`
*   **End Time:** `2025-09-18 08:18:09.202886`
*   **Total Time:** ~58 seconds
*   **Friction Log:** Low friction. The `README.md` was clearly named and located in a logical place (`ISA_SuperApp/etl/`). The purpose was stated clearly in the first section of the file. No major difficulties.

---

## Experiment 2: Find Rationale for a Decision

**Question:** Why was `orjson` chosen over the standard `json` library?

*   **Start Time:** `2025-09-18 08:18:32.727352`
*   **Steps Taken:**
    1.  `ls -F docs/ADR/`
    2.  `read_file("docs/ADR/0003-canonical-json-orjson.md")`
*   **End Time:** `2025-09-18 08:19:26.347572`
*   **Total Time:** ~54 seconds
*   **Friction Log:** Low friction. The ADR directory is well-organized and the filenames are descriptive, making it easy to find the relevant document. The ADR format itself is clear and concise.

---

## Experiment 3: Find a Function Definition

**Question:** Where is the `get_development_config` function defined?

*   **Start Time:** `2025-09-18 08:19:53.843177`
*   **Steps Taken:**
    1.  `grep("def get_development_config")`
*   **End Time:** `2025-09-18 08:20:31.282628`
*   **Total Time:** ~38 seconds
*   **Friction Log:** Medium friction. The `grep` command worked, but it was slow and required knowing the exact function signature (`def ...`). A simple search for `get_development_config` would have returned many more results (imports, calls, etc.), making it harder to find the definition. A dedicated code search tool would be significantly faster and more precise.

---

## Analysis & Conclusion

*   **Summary of Findings:** The experiments show that finding high-level documentation (purpose, rationale) is a low-friction task due to the well-organized `/docs` directory. In contrast, finding a specific piece of code is a medium-friction task that relies on slow, imprecise tools like `grep`.
*   **Biggest Friction Point:** **Code Discovery & Navigation**. The current process for finding code definitions is significantly less efficient than the process for finding documentation.
*   **Proposed Next Action:** The highest-value next step is to run a time-boxed **Proof of Concept for a dedicated code search tool**, as outlined in the original improvement plan. Deploying a tool like Sourcegraph would directly address the biggest friction point identified in this baseline analysis.
