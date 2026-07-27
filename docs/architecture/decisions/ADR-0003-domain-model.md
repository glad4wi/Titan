# ADR 0003: Core Domain Model Design

## Status
Accepted

## Context
Market concepts such as Order Blocks, Fair Value Gaps, Liquidity Pools, and Market Structures are central to Titan's strategy engine. We need standardized data representations across modules.

## Decision
All domain entities will be defined in `core/domain/` as strongly typed models (e.g. using Pydantic or Dataclasses).
Entities include:
- `Candle`, `MarketState`, `Structure`
- `OrderBlock`, `FairValueGap`, `Mitigation`
- `Trade`, `Signal`, `Decision`, `Position`

## Consequences
- Guarantees type safety and validation across all modular pipelines.
- Immutability where possible prevents race conditions in multi-threaded analysis.
