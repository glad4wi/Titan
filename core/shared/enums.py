"""
===========================================================
Titan Trading Engine

Module:
Shared Enums

Purpose:
Defines every global enumeration used across TITAN.

These enums establish a common language between
all engines, analyzers, validators and services.

No module should use raw strings for internal
decision making.

Author:
Titan Core - Gladwin W G

===========================================================
"""

from __future__ import annotations

from enum import Enum, IntEnum, auto


# =========================================================
# General Status
# =========================================================

class ModuleStatus(Enum):
    """Execution status of a module."""

    IDLE = auto()
    RUNNING = auto()
    SUCCESS = auto()
    FAILED = auto()
    SKIPPED = auto()


# =========================================================
# Trend
# =========================================================

class TrendDirection(Enum):
    """Market trend."""

    BULLISH = auto()
    BEARISH = auto()
    RANGING = auto()
    UNKNOWN = auto()


# =========================================================
# Market Structure
# =========================================================

class StructureType(Enum):

    HH = auto()
    HL = auto()
    LH = auto()
    LL = auto()

    BOS = auto()
    CHOCH = auto()

    INTERNAL = auto()
    EXTERNAL = auto()

    NONE = auto()


# =========================================================
# Market Phase
# =========================================================

class MarketPhase(Enum):

    TREND = auto()

    RANGE = auto()

    ACCUMULATION = auto()

    DISTRIBUTION = auto()

    REACCUMULATION = auto()

    REDISTRIBUTION = auto()

    UNKNOWN = auto()


# =========================================================
# Liquidity
# =========================================================

class LiquiditySide(Enum):

    BUY_SIDE = auto()

    SELL_SIDE = auto()

    BOTH = auto()

    NONE = auto()


class LiquidityStatus(Enum):

    UNSWEPT = auto()

    SWEPT = auto()

    RAIDED = auto()

    UNKNOWN = auto()


# =========================================================
# Order Blocks
# =========================================================

class OrderBlockType(Enum):

    BULLISH = auto()

    BEARISH = auto()

    BREAKER = auto()

    MITIGATED = auto()

    INVALID = auto()


# =========================================================
# Fair Value Gap
# =========================================================

class FVGType(Enum):

    BULLISH = auto()

    BEARISH = auto()

    INVERSE = auto()

    NONE = auto()


# =========================================================
# Premium Discount
# =========================================================

class PremiumDiscountZone(Enum):

    PREMIUM = auto()

    EQUILIBRIUM = auto()

    DISCOUNT = auto()


# =========================================================
# Sessions
# =========================================================

class TradingSession(Enum):

    ASIAN = auto()

    LONDON = auto()

    NEW_YORK = auto()

    SYDNEY = auto()

    OVERLAP = auto()

    CLOSED = auto()


# =========================================================
# News
# =========================================================

class NewsImpact(Enum):

    LOW = auto()

    MEDIUM = auto()

    HIGH = auto()

    HOLIDAY = auto()

    NONE = auto()


# =========================================================
# Trade Direction
# =========================================================

class TradeDirection(Enum):

    BUY = auto()

    SELL = auto()

    NONE = auto()


# =========================================================
# Decision
# =========================================================

class DecisionType(Enum):

    WAIT = auto()

    WATCH = auto()

    BUY = auto()

    SELL = auto()

    EXIT = auto()

    HOLD = auto()


# =========================================================
# Risk
# =========================================================

class RiskLevel(Enum):

    VERY_LOW = auto()

    LOW = auto()

    MEDIUM = auto()

    HIGH = auto()

    EXTREME = auto()


# =========================================================
# Confidence
# =========================================================

class ConfidenceLevel(IntEnum):

    VERY_LOW = 20

    LOW = 40

    MEDIUM = 60

    HIGH = 80

    VERY_HIGH = 100


# =========================================================
# Signal Strength
# =========================================================

class SignalStrength(IntEnum):

    WEAK = 25

    MODERATE = 50

    STRONG = 75

    VERY_STRONG = 100


# =========================================================
# Validation
# =========================================================

class ValidationResult(Enum):

    PASS = auto()

    WARNING = auto()

    FAIL = auto()


# =========================================================
# Timeframes
# =========================================================

class TimeFrame(Enum):

    M1 = "1m"

    M3 = "3m"

    M5 = "5m"

    M15 = "15m"

    M30 = "30m"

    H1 = "1h"

    H4 = "4h"

    D1 = "1d"

    W1 = "1w"

    MN1 = "1M"