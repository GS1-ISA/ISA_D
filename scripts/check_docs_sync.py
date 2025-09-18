#!/usr/bin/env python3
"""
Doc-Code Sync Checker

This script performs basic checks to ensure that the documentation is synchronized
with the state of the codebase. It is intended to be run in CI.

Checks performed:
1.  Ensures that all key top-level directories contain a README.md file.
2.  Parses ADR documents to find references to scripts and ensures those scripts exist.
"""

import sys
from pathlib import Path
import re

# --- Configuration ---

# Directories that must contain a README.md
REQUIRED_README_DIRS = [
    "./",
    "ISA_SuperApp/",
    "frontend/",
    "scripts/",
    "docs/",
]

# Directory containing Architecture Decision Records
ADR_DIR = Path("docs/ADR")

# --- Checker Logic ---

def check_readme_existence(base_path: Path) -> list[str]:
    """Checks for the existence of README.md in specified directories."""
    errors = []
    print("--- Checking for README.md files ---")
    for dir_path in REQUIRED_README_DIRS:
        readme_path = base_path / dir_path / "README.md"
        if not readme_path.is_file():
            errors.append(f"Missing README.md in directory: {dir_path}")
            print(f"❌ FAILED: Missing README.md in {dir_path}")
        else:
            print(f"✅ PASSED: Found README.md in {dir_path}")
    return errors

def find_script_references_in_adrs(adr_dir: Path) -> set[str]:
    """Finds all references to scripts within ADR files."""
    script_references = set()
    script_pattern = re.compile(r"`(scripts/[a-zA-Z0-9_./-]+\.py)`")

    if not adr_dir.is_dir():
        print(f"⚠️ WARNING: ADR directory not found at {adr_dir}, skipping script check.")
        return script_references

    print("\n--- Checking for script references in ADRs ---")
    for adr_file in adr_dir.glob("*.md"):
        print(f"Scanning {adr_file}...")
        content = adr_file.read_text(encoding="utf-8")
        matches = script_pattern.findall(content)
        for match in matches:
            script_references.add(match)

    if not script_references:
        print("No script references found in ADRs.")

    return script_references

def check_script_existence(base_path: Path, script_paths: set[str]) -> list[str]:
    """Checks if the referenced scripts exist."""
    errors = []
    if not script_paths:
        return errors

    print("\n--- Verifying existence of referenced scripts ---")
    for script_path in sorted(list(script_paths)):
        full_path = base_path / script_path
        if not full_path.is_file():
            errors.append(f"Script mentioned in ADR does not exist: {script_path}")
            print(f"❌ FAILED: Script not found at {script_path}")
        else:
            print(f"✅ PASSED: Found script {script_path}")
    return errors

def main() -> int:
    """Main function."""
    print("Running Doc-Code Sync Check...")
    base_dir = Path(__file__).parent.parent
    all_errors = []

    # Run checks
    all_errors.extend(check_readme_existence(base_dir))

    script_refs = find_script_references_in_adrs(base_dir / ADR_DIR)
    all_errors.extend(check_script_existence(base_dir, script_refs))

    # Report results
    if all_errors:
        print("\n--- ❌ Doc-Code Sync Check Failed ---")
        for error in all_errors:
            print(f"- {error}")
        return 1
    else:
        print("\n--- ✅ Doc-Code Sync Check Passed ---")
        return 0

if __name__ == "__main__":
    sys.exit(main())
