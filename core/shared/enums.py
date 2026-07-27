"""
===============================================================================

TITAN Trading Operating System
Core Shared Enums

File:
    core/shared/enums.py

Description:
    Defines the global language used across the TITAN ecosystem.

    Every engine, analyzer, validator, service, broker,
    AI model and execution component MUST use these enums.

    No raw strings should ever be used for decisions.

Author:
    TITAN Core

===============================================================================
"""

from __future__ import annotations

from enum import Enum


# =============================================================================
# BASE ENUM
# =============================================================================

class TitanEnum(str, Enum):
    """
    Base enumeration for TITAN.

    Benefits:
        - JSON serializable
        - Database friendly
        - Human readable
        - FastAPI compatible
        - Logging friendly
    """

    def __str__(self) -> str:
        return self.value


# =============================================================================
# ENGINE
# =============================================================================

class ModuleStatus(TitanEnum):

    IDLE = "IDLE"
    INITIALIZING = "INITIALIZING"
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    WARNING = "WARNING"
    FAILED = "FAILED"
    SHUTDOWN = "SHUTDOWN"


# =============================================================================
# MARKET TREND
# =============================================================================

class TrendDirection(TitanEnum):

    BULLISH = "BULLISH"
    BEARISH = "BEARISH"
    RANGING = "RANGING"
    TRANSITION = "TRANSITION"
    UNKNOWN = "UNKNOWN"


# =============================================================================
# MARKET STRUCTURE
# =============================================================================

class StructureType(TitanEnum):

    HH = "HH"
    HL = "HL"
    LH = "LH"
    LL = "LL"

    BOS = "BOS"
    CHOCH = "CHOCH"

    INTERNAL = "INTERNAL"
    EXTERNAL = "EXTERNAL"

    NONE = "NONE"


# =============================================================================
# MARKET PHASE
# =============================================================================

class MarketPhase(TitanEnum):

    TREND = "TREND"

    RANGE = "RANGE"

    ACCUMULATION = "ACCUMULATION"

    DISTRIBUTION = "DISTRIBUTION"

    REACCUMULATION = "REACCUMULATION"

    REDISTRIBUTION = "REDISTRIBUTION"

    UNKNOWN = "UNKNOWN"


# =============================================================================
# LIQUIDITY
# =============================================================================

class LiquiditySide(TitanEnum):

    BUY_SIDE = "BUY_SIDE"
    SELL_SIDE = "SELL_SIDE"
    BOTH = "BOTH"
    NONE = "NONE"


class LiquidityStatus(TitanEnum):

    UNSWEPT = "UNSWEPT"
    SWEPT = "SWEPT"
    RAIDED = "RAIDED"
    UNKNOWN = "UNKNOWN"


# =============================================================================
# ORDER BLOCK
# =============================================================================

class OrderBlockType(TitanEnum):

    BULLISH = "BULLISH"
    BEARISH = "BEARISH"
    BREAKER = "BREAKER"
    MITIGATED = "MITIGATED"
    INVALID = "INVALID"


# =============================================================================
# FAIR VALUE GAP
# =============================================================================

class FairValueGapType(TitanEnum):

    BULLISH = "BULLISH"
    BEARISH = "BEARISH"
    INVERSE = "INVERSE"
    NONE = "NONE"


# =============================================================================
# PREMIUM / DISCOUNT
# =============================================================================

class PremiumDiscountZone(TitanEnum):

    PREMIUM = "PREMIUM"
    EQUILIBRIUM = "EQUILIBRIUM"
    DISCOUNT = "DISCOUNT"


# =============================================================================
# SESSION
# =============================================================================

class TradingSession(TitanEnum):

    SYDNEY = "SYDNEY"
    TOKYO = "TOKYO"
    LONDON = "LONDON"
    NEW_YORK = "NEW_YORK"

    LONDON_NEWYORK_OVERLAP = "LONDON_NEWYORK_OVERLAP"

    CLOSED = "CLOSED"


# =============================================================================
# NEWS
# =============================================================================

class NewsImpact(TitanEnum):

    NONE = "NONE"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    HOLIDAY = "HOLIDAY"


# =============================================================================
# TRADE
# =============================================================================

class TradeDirection(TitanEnum):

    BUY = "BUY"
    SELL = "SELL"
    NONE = "NONE"


class PositionStatus(TitanEnum):

    OPEN = "OPEN"
    CLOSED = "CLOSED"
    PARTIAL = "PARTIAL"
    CANCELLED = "CANCELLED"


# =============================================================================
# DECISION
# =============================================================================

class DecisionType(TitanEnum):

    WAIT = "WAIT"

    WATCH = "WATCH"

    BUY = "BUY"

    SELL = "SELL"

    HOLD = "HOLD"

    EXIT = "EXIT"


# =============================================================================
# VALIDATION
# =============================================================================

class ValidationResult(TitanEnum):

    PASS = "PASS"
    WARNING = "WARNING"
    FAIL = "FAIL"


# =============================================================================
# SIGNAL
# =============================================================================

class SignalStrength(TitanEnum):

    VERY_WEAK = "VERY_WEAK"
    WEAK = "WEAK"
    MODERATE = "MODERATE"
    STRONG = "STRONG"
    VERY_STRONG = "VERY_STRONG"


# =============================================================================
# RISK
# =============================================================================

class RiskLevel(TitanEnum):

    VERY_LOW = "VERY_LOW"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    EXTREME = "EXTREME"


# =============================================================================
# CONFIDENCE
# =============================================================================

class ConfidenceLevel(TitanEnum):

    VERY_LOW = "VERY_LOW"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    VERY_HIGH = "VERY_HIGH"


# =============================================================================
# TIMEFRAME
# =============================================================================

class TimeFrame(TitanEnum):

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