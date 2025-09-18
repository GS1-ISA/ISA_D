# ADR 0005 — Code Search Strategy

**Date:** 2025-09-18

**Status:** Proposed

## Context

The "Developer Experience Baseline" analysis (`docs/DX_BASELINE.md`) identified that code discovery and navigation is a medium-friction task for new developers (human or AI). The existing method relies on `grep`, which is slow and imprecise. To address this, a Proof of Concept was conducted to compare two potential solutions: a human-centric UI tool (Sourcegraph) and an agent-centric, queryable database (Neo4j Code Index).

## Decision

We will adopt the **Agent-Centric Neo4j Code Index** as the primary, officially supported code search solution for the ISA_D project.

The `scripts/poc_code_indexer.py` script will be productized and integrated into a nightly CI workflow to ensure the code index is kept up-to-date. This provides a structured, queryable API of the codebase, which is ideal for programmatic use by AI agents.

The setup guide for Sourcegraph (`docs/poc/sourcegraph_setup.md`) will be maintained as a recommended resource for human developers who prefer a UI-based tool for local development, but it will not be a required or officially supported part of the core infrastructure at this time.

## Consequences

*   **Positive:**
    *   Provides a powerful, structured, and machine-readable way for AI agents to query and understand the codebase, directly supporting the project's "agent-first" core principle.
    *   Reuses and builds upon the existing Neo4j infrastructure, which is more efficient than introducing and maintaining a completely new tool like Sourcegraph.
    *   The nightly CI job will ensure that the code knowledge graph is always current.
*   **Negative:**
    *   Human developers who want a UI for code search will need to run Sourcegraph locally themselves, following the provided documentation. This is a slightly higher barrier to entry than a centrally hosted instance.
    *   We will need to maintain the `code_indexer.py` script as the codebase evolves.

## Rationale

This decision prioritizes the needs of our primary future developers: AI agents. A queryable graph of the codebase is a fundamentally more powerful and flexible tool for an agent than a UI. It allows agents to perform complex queries about code structure (e.g., "Find all functions that call function X") that are difficult or impossible in a standard search tool. By making this the primary solution, we are making a strategic investment in the agentic capabilities of the system.

Given that the friction for human developers to run Sourcegraph locally is relatively low, this approach provides a good balance of capabilities for both audiences while staying true to the project's core vision.
