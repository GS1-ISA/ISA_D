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
*   **Proposed Next Action:** The original recommendation was to run a POC for a code search tool. This analysis has been completed below.

---

## POC Comparison: Agent-Centric vs. Human-Centric Code Search

Based on the analysis, two POCs were prepared to address the Code Discovery friction point.

### Approach A: Agent-Centric (Neo4j Code Index)

*   **Implementation:** A script (`scripts/poc_code_indexer.py`) was created to parse the codebase and ingest its structure into the existing Neo4j database.
*   **Simulated Search Task:** To find the `get_development_config` function, an agent would execute the following Cypher query:
    ```cypher
    MATCH (f:Function {name: 'get_development_config'})-[:DEFINED_IN]->(file:File)
    RETURN file.path, f.line
    ```
*   **Friction Analysis:** **Very Low (for an agent)**. This approach is ideal for AI developers. It is programmatic, structured, and returns precise data that can be directly used in an agent's workflow without screen scraping or parsing a UI. The main prerequisite is a running Neo4j instance.

### Approach B: Human-Centric (Sourcegraph)

*   **Implementation:** A setup guide (`docs/poc/sourcegraph_setup.md`) was created for a human developer to run Sourcegraph locally via Docker.
*   **Simulated Search Task:** To find the `get_development_config` function, a human would:
    1.  Open a web browser to `http://localhost:7080`.
    2.  Type `def get_development_config` into the search bar.
    3.  Click on the top result to navigate directly to the definition.
*   **Friction Analysis:** **Very Low (for a human)**. This approach is ideal for human developers. The UI is intuitive, provides rich context (like blame and references), and requires no knowledge of a query language.

### Conclusion & Recommendation

Both approaches are excellent and solve the identified problem. They are not mutually exclusive. Given the project's core "agent-first" principle, the Neo4j-based approach is more strategically aligned.

*   **Recommendation:** The **Agent-Centric Neo4j Code Index** should be fully implemented and maintained as a core piece of the project's infrastructure. Its data should be refreshed in a nightly CI job. The `poc_code_indexer.py` script should be productized.
*   **Secondary Recommendation:** The `sourcegraph_setup.md` document should be kept as a valuable resource for human developers who prefer a UI-based tool for local development.
