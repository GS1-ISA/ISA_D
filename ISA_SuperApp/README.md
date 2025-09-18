# ISA SuperApp - Core Backend

## Purpose

This directory contains the core backend application for the **ISA_D Project**. It includes the main FastAPI application, the agentic system components (Planner, Orchestrator, etc.), the data models, and the core business logic.

This is the primary application that serves the "Domain Project" goal of acting as an Intelligent Standards Architect for GS1.

## How to Run

The application is run as part of the larger project ecosystem, typically via Docker Compose or Kubernetes. Refer to the root `README.md` for instructions on how to run the full system.

The main entry point for the application is `ISA_SuperApp/main.py`.

## How to Test

The tests for this application are located in the root `tests/` directory. To run the tests for this specific component, you can use `pytest` with a path argument:

```bash
pytest tests/
```

Refer to the root `pyproject.toml` for a full list of testing and quality dependencies.

## Key Sub-directories

-   `agents/`: Contains the definitions for the different types of specialized agents.
-   `core/`: Holds the central application logic, including the main app, API server, and core data structures.
-   `etl/`: Contains the Extract, Transform, Load pipelines for various data sources.
-   `llm/`: Provides abstractions for interacting with different Large Language Models.
-   `orchestrator/`: Manages the collaboration and execution of different agents.
-   `vector_store/`: Manages the interaction with vector databases like ChromaDB.

## Further Information

For a complete understanding of the project's architecture, vision, and operational principles, please refer to the canonical documentation:

-   **`docs/ISA_D_SYNTHESIZED_VISION.md`**
-   **`docs/adr/`**
-   **`docs/agents/`**
