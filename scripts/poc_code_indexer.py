#!/usr/bin/env python3
"""
Proof-of-Concept: Codebase Indexer for Neo4j

This script provides a proof-of-concept for an agent-centric code search solution.
It scans the `ISA_SuperApp` directory, parses the Python source files using the
Abstract Syntax Tree (AST) module, and ingests the code structure (files, classes,
functions) into the Neo4j graph database.

This creates a queryable knowledge graph of the codebase, which can be used by
AI agents to understand code structure and find definitions.
"""

import ast
import os
import sys
from pathlib import Path

# Add project root to path to allow importing from src
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from src.neo4j_gds_client import get_gds_client, Neo4jGDSClient
except ImportError:
    print("ERROR: Could not import Neo4jGDSClient.")
    print("Please ensure that the project is installed correctly and PYTHONPATH is set.")
    sys.exit(1)


class CodeParser(ast.NodeVisitor):
    """
    An AST NodeVisitor that extracts information about classes and functions.
    """
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.items = []

    def visit_ClassDef(self, node: ast.ClassDef):
        self.items.append({
            "type": "Class",
            "name": node.name,
            "file": self.file_path,
            "line": node.lineno,
        })
        self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef):
        self.items.append({
            "type": "Function",
            "name": node.name,
            "file": self.file_path,
            "line": node.lineno,
        })
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        self.items.append({
            "type": "Function",
            "name": node.name,
            "file": self.file_path,
            "line": node.lineno,
        })
        self.generic_visit(node)


def parse_python_file(file_path: Path) -> list[dict]:
    """Parses a Python file and returns a list of classes and functions."""
    print(f"  Parsing: {file_path}")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        tree = ast.parse(content)
        parser = CodeParser(str(file_path))
        parser.visit(tree)
        return parser.items
    except Exception as e:
        print(f"    WARNING: Could not parse {file_path}: {e}")
        return []


def ingest_code_structure(gds_client: Neo4jGDSClient, code_items: list[dict]):
    """Ingests the extracted code structure into Neo4j."""
    print(f"\n--- Ingesting {len(code_items)} code items into Neo4j ---")

    # Ensure constraints for uniqueness
    gds_client.execute_query("CREATE CONSTRAINT IF NOT EXISTS FOR (f:File) REQUIRE f.path IS UNIQUE")
    gds_client.execute_query("CREATE CONSTRAINT IF NOT EXISTS FOR (c:Class) REQUIRE c.fqn IS UNIQUE")
    gds_client.execute_query("CREATE CONSTRAINT IF NOT EXISTS FOR (f:Function) REQUIRE f.fqn IS UNIQUE")

    # Ingest using Cypher queries
    # This is a simplified POC and could be heavily optimized with UNWIND.
    for item in code_items:
        file_path = item['file']
        item_name = item['name']
        item_type = item['type']
        line_number = item['line']

        # Create a fully qualified name for uniqueness
        fqn = f"{file_path}::{item_name}"

        # Create File node and relationship
        gds_client.execute_query(
            "MERGE (f:File {path: $path})",
            {"path": file_path}
        )

        # Create Code item node and relationship
        query = f"""
        MATCH (f:File {{path: $path}})
        MERGE (c:{item_type} {{fqn: $fqn}})
        ON CREATE SET c.name = $name, c.line = $line
        MERGE (f)<-[:DEFINED_IN]-(c)
        """
        params = {
            "path": file_path,
            "fqn": fqn,
            "name": item_name,
            "line": line_number
        }
        gds_client.execute_query(query, params)

    print("--- Ingestion complete ---")


def main():
    """Main function to run the code indexer POC."""
    print("--- Starting POC Code Indexer ---")

    # 1. Connect to Neo4j
    print("\n--- Connecting to Neo4j GDS Client ---")
    try:
        gds_client = get_gds_client()
        if not gds_client.is_healthy():
            print("ERROR: Neo4j client is not healthy. Please check connection.")
            sys.exit(1)
        print("Successfully connected to Neo4j.")
    except Exception as e:
        print(f"ERROR: Failed to connect to Neo4j: {e}")
        print("Please ensure Neo4j is running and configured in .env or config files.")
        sys.exit(1)

    # 2. Find all Python files in the target directory
    target_dir = Path(__file__).parent.parent / "ISA_SuperApp"
    print(f"\n--- Scanning for Python files in {target_dir} ---")
    python_files = list(target_dir.rglob("*.py"))
    print(f"Found {len(python_files)} Python files.")

    # 3. Parse files and extract structure
    all_code_items = []
    for file_path in python_files:
        all_code_items.extend(parse_python_file(file_path))

    print(f"\nExtracted {len(all_code_items)} total classes and functions.")

    # 4. Ingest structure into Neo4j
    ingest_code_structure(gds_client, all_code_items)

    # 5. Close connection
    gds_client.close()
    print("\n--- POC Code Indexer Finished ---")


if __name__ == "__main__":
    main()
