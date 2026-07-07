"""Frontend build orchestration — npm install + npm run build on startup."""

from __future__ import annotations

import logging
import subprocess
import sys
from pathlib import Path

logger = logging.getLogger(__name__)

_FRONTEND_DIR = Path(__file__).resolve().parent / "frontend"
_STATIC_DIR = Path(__file__).resolve().parent / "static"


def ensure_frontend_built() -> None:
    """Check if the frontend is built; if not, run npm install + build.

    Raises ``SystemExit`` if Node.js is not available or the build fails.
    """
    # Check if static files already exist
    if _STATIC_DIR.exists() and any(_STATIC_DIR.glob("index.html")):
        return

    if not _FRONTEND_DIR.exists():
        logger.warning("Frontend directory not found at %s — skipping build.", _FRONTEND_DIR)
        return

    print("Frontend not built — running npm install + build…")

    # Check for Node.js
    try:
        subprocess.run(["node", "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        sys.exit(
            "Error: Node.js is required to build the web frontend.\n"
            "  Install it from https://nodejs.org and try again."
        )

    # npm install
    print("  → npm install…")
    result = subprocess.run(
        ["npm", "install"],
        cwd=str(_FRONTEND_DIR),
        capture_output=False,
    )
    if result.returncode != 0:
        sys.exit("Error: npm install failed. See output above.")

    # npm run build
    print("  → npm run build…")
    result = subprocess.run(
        ["npm", "run", "build"],
        cwd=str(_FRONTEND_DIR),
        capture_output=False,
    )
    if result.returncode != 0:
        sys.exit("Error: npm run build failed. See output above.")

    print("Frontend build complete.")
