# ADR 0004: Standardized Module Contracts

## Status
Accepted

## Context
Modules in `modules/` perform domain-specific analysis (e.g. liquidity detection, FVG identification, risk scoring). To ensure interchangeability, all modules must abide by fixed contracts.

## Decision
All modules must implement abstract interfaces defined in `core/interfaces/` (e.g., `Analyzer`, `Validator`).
Every module must accept a standardized input (`MarketState` / `Candle`) and return a standardized output (`AnalysisResult` / `Signal`).

## Consequences
- New strategy modules or alternative models can be plugged in without modifying core engine logic.
- Enables automated validation and scoring across modules.
