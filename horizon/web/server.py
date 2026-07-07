"""FastAPI application + ``horizon web`` CLI command.

Start with::

    horizon web [--host 127.0.0.1] [--port 8080]
"""

from __future__ import annotations

import logging
from contextlib import asynccontextmanager
from pathlib import Path

import click
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from horizon.web.builder import ensure_frontend_built
from horizon.web.routes.config import router as config_router
from horizon.web.routes.history import router as history_router
from horizon.web.routes.run import router as run_router

logger = logging.getLogger(__name__)

_STATIC_DIR = Path(__file__).resolve().parent / "static"


def create_app() -> FastAPI:
    """Build the FastAPI application."""
    app = FastAPI(
        title="Horizon Web",
        version="0.2.0",
    )

    app.include_router(run_router, prefix="/api")
    app.include_router(config_router, prefix="/api")
    app.include_router(history_router, prefix="/api")

    # Serve React SPA from static/
    if _STATIC_DIR.exists() and any(_STATIC_DIR.iterdir()):
        app.mount("/", StaticFiles(directory=str(_STATIC_DIR), html=True), name="static")

    return app


# ── CLI command ─────────────────────────────────────────────────────────────


def register_web_command(main_group: click.Group) -> None:
    """Attach ``web`` sub-command to the Horizon CLI group."""

    @main_group.command()
    @click.option("--host", default="127.0.0.1", show_default=True, help="Bind address.")
    @click.option("--port", default=8080, show_default=True, help="Bind port.")
    def web(host: str, port: int) -> None:
        """Start the Horizon web interface."""
        ensure_frontend_built()

        click.echo(f"Starting Horizon Web at http://{host}:{port}")
        uvicorn.run(
            "horizon.web.server:create_app",
            host=host,
            port=port,
            factory=True,
            log_level="info",
        )
