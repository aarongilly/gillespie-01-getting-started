"""
pipeline_case.py - Project script (example).

Author: Denise Case
Date: 2026-03-07

Purpose:
  Confirm your project environment is set up correctly.
  Run this script to see a log message in the terminal.

Run as a Module:
  uv run python -m cintel.pipeline_case
"""

# === DECLARE IMPORTS ===

# First from the Python standard library (no installation needed)
import json
import logging
from pathlib import Path

# Then, external dependencies (must be listed in pyproject.toml)
from datafun_toolkit.logger import get_logger, log_header, log_path

# === CONFIGURE LOGGER ===

LOG: logging.Logger = get_logger("P1", level="DEBUG")

# === DECLARE GLOBAL CONSTANTS FOR FOLDER PATHS (directories) ===

ROOT_DIR: Path = Path.cwd()
DOCS_DIR: Path = ROOT_DIR / "docs"

# === DEFINE THE MAIN FUNCTION ===


def main() -> None:
    """Run the pipeline.

    log_header() logs a standard run header.
    log_path() logs repo-relative paths (privacy-safe).
    """
    log_header(LOG, "CINTEL")

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("========================")

    log_path(LOG, "ROOT_DIR", ROOT_DIR)
    log_path(LOG, "DOCS_DIR", DOCS_DIR)

    json_path = ROOT_DIR / "data" / "simple_mod.json"

    if json_path.exists():
        with Path.open(json_path, encoding="utf-8") as f:
            data = json.load(f)
        LOG.info(f"Loaded JSON file: {json_path}")
        for key, value in data.items():
            LOG.info(f"{key}: {value}")
    else:
        LOG.warning(f"JSON file not found: {json_path}")

    LOG.info("========================")
    LOG.info("Pipeline executed successfully!")
    LOG.info("========================")
    LOG.info("END main()")


# === CONDITIONAL EXECUTION GUARD ===

if __name__ == "__main__":
    main()
