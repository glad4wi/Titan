"""
===============================================================================

TITAN Trading Operating System
Core Shared Constants

File:
    core/shared.constants

Description:
    Global immutable constants used across the TITAN engine.

    IMPORTANT

    This file MUST NEVER contain:

    - Broker credentials
    - Risk settings
    - Strategy parameters
    - Symbol configuration
    - User configuration

    Those belong inside /config.

===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass


# =============================================================================
# ENGINE INFORMATION
# =============================================================================

@dataclass(frozen=True)
class EngineInfo:
    NAME: str = "TITAN"

    VERSION: str = "1.0.0"

    CODENAME: str = "Genesis"

    AUTHOR: str = "Titan Core"


# =============================================================================
# FILESYSTEM
# =============================================================================

@dataclass(frozen=True)
class FileNames:

    LOG_FILE = "titan.log"

    ERROR_LOG = "errors.log"

    BACKTEST_RESULTS = "backtest.json"

    TRADE_HISTORY = "trade_history.json"


# =============================================================================
# PRECISION
# =============================================================================

@dataclass(frozen=True)
class Precision:

    PRICE_DECIMALS = 5

    LOT_DECIMALS = 2

    PERCENT_DECIMALS = 2

    CONFIDENCE_DECIMALS = 4


# =============================================================================
# VALIDATION
# =============================================================================

@dataclass(frozen=True)
class Validation:

    MIN_CONFIDENCE = 0.60

    MAX_CONFIDENCE = 1.00

    MIN_SCORE = 0.00

    MAX_SCORE = 100.00


# =============================================================================
# TIME
# =============================================================================

@dataclass(frozen=True)
class Time:

    SECONDS_PER_MINUTE = 60

    MINUTES_PER_HOUR = 60

    HOURS_PER_DAY = 24

    DAYS_PER_WEEK = 7


# =============================================================================
# MATHEMATICS
# =============================================================================

@dataclass(frozen=True)
class Math:

    EPSILON = 1e-9

    ZERO = 0.0

    ONE = 1.0


# =============================================================================
# ENGINE LIMITS
# =============================================================================

@dataclass(frozen=True)
class Limits:

    MAX_ANALYSIS_MESSAGES = 1000

    MAX_WARNINGS = 100

    MAX_ERRORS = 100

    MAX_SIGNALS = 1000


# =============================================================================
# DEFAULTS
# =============================================================================

@dataclass(frozen=True)
class Defaults:

    UNKNOWN = "UNKNOWN"

    EMPTY = ""

    NONE = "NONE"

    NOT_AVAILABLE = "N/A"


# =============================================================================
# MODULE NAMES
# =============================================================================

@dataclass(frozen=True)
class ModuleNames:

    MARKET = "Market Engine"

    STRUCTURE = "Structure Engine"

    LIQUIDITY = "Liquidity Engine"

    ORDERBLOCK = "Order Block Engine"

    FVG = "Fair Value Gap Engine"

    SESSION = "Session Engine"

    NEWS = "News Engine"

    VALIDATION = "Validation Engine"

    DECISION = "Decision Engine"

    EXECUTION = "Execution Engine"

    ANALYTICS = "Analytics Engine"