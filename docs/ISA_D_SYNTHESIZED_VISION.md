# The ISA_D Project: A Synthesized Vision

*This document is the canonical source of truth for the ISA_D project's vision, principles, and roadmap. It supersedes and harmonizes all previous planning and vision documents.*

## 1. Core Vision: A Self-Developing System for a Specific Purpose

The ISA_D project has a unique dual nature:

*   **The Meta-Project:** We are building a **self-developing agentic system**. This system is designed to be maintained and evolved primarily by autonomous AI agents, not humans. It has a sophisticated architecture of collaborating agents (Planner, Builder, Verifier, Critic) and a robust "immune system" of automated quality and safety gates.
*   **The Domain Project:** The purpose of this meta-system is to create and operate an **Intelligent Standards Architect for GS1**. This expert system will focus on the GS1 domain, helping to anticipate regulatory changes, map them to GS1 standards (like GDSN), and automate compliance and data validation tasks.

In essence, **we are building an AI to build another AI.** The success of the meta-project is measured by its ability to autonomously and effectively achieve the goals of the domain project.

## 2. Core Principles for Agentic Development

Any developer, human or AI, working on this project must adhere to the following core principles:

1.  **Safety First:** All actions are constrained by strict, machine-enforced safety policies. Destructive actions are forbidden without explicit human waiver, and the system is designed to fail safe via kill-switches and automated rollbacks.
2.  **Determinism & Quality:** The system must be reproducible. Deterministic outputs are a non-negotiable requirement, enforced by cross-platform snapshot tests. All changes must meet a high bar for quality, enforced by a suite of automated gates for testing, coverage, and security.
3.  **Evidence-Based Decisions:** Changes are not made on opinion. All significant technical decisions must be supported by data and benchmarks, and the reasoning must be documented in an Architecture Decision Record (ADR).
4.  **Gradual Autonomy:** Agent autonomy is earned, not given. Increased levels of autonomy (e.g., auto-merging pull requests) are only granted after demonstrating sustained, measurable success against the project's KPIs (e.g., >85% task win-rate, <1% revert rate).
5.  **Research-First, Act-Second:** Agents must be resourceful. Before requesting human clarification, an agent is required to exhaust all available internal knowledge sources, including the documentation, the codebase, and the various generated knowledge artifacts (code index, etc.).
6.  **Docs & Tests as Part of the Work:** Documentation and tests are not afterthoughts; they are an integral part of every change. Any modification to code or behavior must be accompanied by corresponding updates to documentation and tests in the same atomic commit.

## 3. Unified Project Roadmap

To provide a single, clear timeline, all previous planning documents are now mapped to the following four-horizon roadmap:

*   **Horizon 0: Deep Analysis & Harmonization** (Current Phase)
    *   **Goal:** Analyze all existing documentation to create this synthesized vision.
    *   *Maps to: Initial parts of "30/60/90 day plan".*

*   **Horizon 1: Foundational Quick Wins (0-1 Month)**
    *   **Goal:** Establish core documentation habits (ADRs, READMEs) and developer experience tools (CodeTour) with minimal new infrastructure.
    *   *Maps to: Roadmap Phase A, Agentic Goals "Foundations", 30-day plan.*

*   **Horizon 2: Build the Knowledge Hub (1-3 Months)**
    *   **Goal:** Implement tooling for a centralized, automated documentation site (MkDocs) and advanced code search (Sourcegraph).
    *   *Maps to: Roadmap Phase B, Agentic Goals "Hardening", 60-day plan.*

*   **Horizon 3: Scale and Automate (3-6+ Months)**
    *   **Goal:** Tackle monorepo scalability with a build tool (Pants/Nx), deploy a developer portal (Backstage), and begin systematic refactoring.
    *   *Maps to: Roadmap Phases C & D, Agentic Goals "T2 Autonomy" & "Scale & Optimize", 90-day plan.*

## 4. Key Operational Protocols for Agents

To ensure consistency, all agents must follow these specific, machine-parsable protocols:

*   **Planning Format:** All iterative work must be proposed using the format defined in `docs/agents/PLANNING_PREFERENCES.md` (Action, Why, Plan, Confidence).
*   **Refactoring:** All refactoring tasks must be performed using the dedicated `scripts/refactor_guard.py` tool, which enforces a safe, step-by-step process.
*   **Boot Sequence:** When starting a new session, agents should use the "Context Pack" defined in `docs/agents/AGENTS.md` to build an accurate mental model of the repository state.
*   **Non-Goals:** Agents must explicitly adhere to the non-goals defined in `docs/ISA_VISION_OUTCOMES.md` (e.g., do not provide legal advice, do not make production changes without a waiver).

## 5. Current State: Code & Feature Audit

This section provides a high-level mapping of documented features to the current state of the codebase.

| Feature / Component         | Status & Location                                                                                                                              | Notes                                                                                                                                                                                            |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Agentic Core**            | **Implemented** (`ISA_SuperApp/agents/`, `ISA_SuperApp/orchestrator/`)                                                                           | The core roles (Planner, Researcher, etc.) and the orchestration logic exist.                                                                                                                    |
| **Memory System (RAG)**     | **Implemented** (`ISA_SuperApp/vector_store/`, `ISA_SuperApp/retrieval/`)                                                                        | ChromaDB is the primary vector store. RAG retrieval logic is in place.                                                                                                                           |
| **ETL Pipeline**            | **Implemented** (`ISA_SuperApp/etl/`)                                                                                                            | Connectors for ESMA and Eurostat data sources are present.                                                                                                                                       |
| **Frontend UI**             | **Implemented** (`frontend/`)                                                                                                                    | A Next.js/React application exists and appears to be structured by feature.                                                                                                                      |
| **Observability**           | **Partially Implemented**                                                                                                                      | The project has dependencies for structured logging and Prometheus metrics, and the API server code has been updated to support them, but they are not yet fully integrated end-to-end.            |
| **Refactor Guard Tool**     | **Not Implemented**                                                                                                                            | The `docs/agents/REFACTOR_GUARD.md` describes a `scripts/refactor_guard.py` tool, but this script does not exist. This is a documentation/implementation gap that should be addressed.            |
| **Benchmark & Audit Scripts** | **Implemented** (`scripts/`)                                                                                                                   | A strong culture of scripted audits and benchmarks is evident from the numerous scripts available.                                                                                               |
