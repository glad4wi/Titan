"""
===============================================================================

TITAN Trading Operating System

File:
    core/shared/logger.py

Description:
    Centralized logging service for TITAN.

    All engines must use TitanLogger.

===============================================================================
"""

from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Any


class TitanLogger:
    """
    Central logging service.

    This class wraps Python's logging module behind
    TITAN's own API.
    """

    _instance: "TitanLogger | None" = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            cls._instance._configure()

        return cls._instance

    def _configure(self):

        log_directory = Path("logs")

        log_directory.mkdir(exist_ok=True)

        formatter = logging.Formatter(

            "%(asctime)s | %(levelname)-8s | %(name)-20s | %(message)s",

            "%Y-%m-%d %H:%M:%S",

        )

        handler = RotatingFileHandler(

            log_directory / "titan.log",

            maxBytes=10 * 1024 * 1024,

            backupCount=10,

            encoding="utf-8",

        )

        handler.setFormatter(formatter)

        console = logging.StreamHandler()

        console.setFormatter(formatter)

        self.logger = logging.getLogger("TITAN")

        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:

            self.logger.addHandler(handler)

            self.logger.addHandler(console)

    def _log(self, level: int, category: str, message: str, **metadata: Any):

        if metadata:

            message += f" | {metadata}"

        self.logger.log(level, f"[{category}] {message}")

    # -----------------------------------------------------

    def structure(self, message: str, **metadata):

        self._log(logging.INFO, "STRUCTURE", message, **metadata)

    def liquidity(self, message: str, **metadata):

        self._log(logging.INFO, "LIQUIDITY", message, **metadata)

    def session(self, message: str, **metadata):

        self._log(logging.INFO, "SESSION", message, **metadata)

    def news(self, message: str, **metadata):

        self._log(logging.INFO, "NEWS", message, **metadata)

    def validation(self, message: str, **metadata):

        self._log(logging.INFO, "VALIDATION", message, **metadata)

    def trade(self, message: str, **metadata):

        self._log(logging.INFO, "TRADE", message, **metadata)

    def risk(self, message: str, **metadata):

        self._log(logging.INFO, "RISK", message, **metadata)

    def execution(self, message: str, **metadata):

        self._log(logging.INFO, "EXECUTION", message, **metadata)

    def ai(self, message: str, **metadata):

        self._log(logging.INFO, "AI", message, **metadata)

    def replay(self, message: str, **metadata):

        self._log(logging.INFO, "REPLAY", message, **metadata)

    def warning(self, message: str, **metadata):

        self._log(logging.WARNING, "WARNING", message, **metadata)

    def error(self, message: str, **metadata):

        self._log(logging.ERROR, "ERROR", message, **metadata)

    def critical(self, message: str, **metadata):

        self._log(logging.CRITICAL, "CRITICAL", message, **metadata)

    def exception(self, exception: Exception):

        self.logger.exception(exception)