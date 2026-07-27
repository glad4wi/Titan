"""
===============================================================================

TITAN Trading Operating System
Core Shared Exceptions

File:
    core/shared/exceptions.py

Description:
    Defines the global exception hierarchy used throughout TITAN.

    Every exception raised inside TITAN should inherit from TitanError.

    This allows centralized error handling, logging, monitoring,
    recovery and debugging.

===============================================================================
"""

from __future__ import annotations

from typing import Any


class TitanError(Exception):
    """
    Base exception for all TITAN errors.
    """

    def __init__(
        self,
        message: str,
        *,
        module: str | None = None,
        details: dict[str, Any] | None = None,
    ) -> None:

        self.message = message
        self.module = module
        self.details = details or {}

        super().__init__(self.__str__())

    def __str__(self) -> str:

        text = self.message

        if self.module:
            text = f"[{self.module}] {text}"

        if self.details:
            text += f" | Details: {self.details}"

        return text


# =============================================================================
# Configuration
# =============================================================================

class ConfigurationError(TitanError):
    """Raised when configuration is invalid."""


# =============================================================================
# Validation
# =============================================================================

class ValidationError(TitanError):
    """Raised when validation fails."""


# =============================================================================
# Market Data
# =============================================================================

class MarketDataError(TitanError):
    """Raised when market data is invalid or unavailable."""


# =============================================================================
# Structure
# =============================================================================

class StructureError(TitanError):
    """Raised by the Market Structure Engine."""


# =============================================================================
# Liquidity
# =============================================================================

class LiquidityError(TitanError):
    """Raised by the Liquidity Engine."""


# =============================================================================
# Order Block
# =============================================================================

class OrderBlockError(TitanError):
    """Raised by the Order Block Engine."""


# =============================================================================
# Fair Value Gap
# =============================================================================

class FairValueGapError(TitanError):
    """Raised by the Fair Value Gap Engine."""


# =============================================================================
# Session
# =============================================================================

class SessionError(TitanError):
    """Raised by the Session Engine."""


# =============================================================================
# News
# =============================================================================

class NewsEngineError(TitanError):
    """Raised by the News Engine."""


# =============================================================================
# Analysis
# =============================================================================

class AnalyzerError(TitanError):
    """Raised by analyzers."""


# =============================================================================
# Decision
# =============================================================================

class DecisionEngineError(TitanError):
    """Raised by the Decision Engine."""


# =============================================================================
# Risk
# =============================================================================

class RiskEngineError(TitanError):
    """Raised by the Risk Engine."""


# =============================================================================
# Execution
# =============================================================================

class ExecutionError(TitanError):
    """Raised by the Execution Engine."""


# =============================================================================
# Broker
# =============================================================================

class BrokerError(TitanError):
    """Raised by broker integrations."""


# =============================================================================
# Database
# =============================================================================

class DatabaseError(TitanError):
    """Raised by repositories and databases."""


# =============================================================================
# Replay
# =============================================================================

class ReplayEngineError(TitanError):
    """Raised by replay/backtesting engines."""


# =============================================================================
# AI
# =============================================================================

class AIEngineError(TitanError):
    """Raised by AI components."""