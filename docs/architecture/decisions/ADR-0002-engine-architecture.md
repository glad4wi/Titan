# ADR 0002: Engine Architecture

## Status
Accepted

## Context
The core execution pipeline needs to coordinate data fetching, module analysis, validation, risk calculation, and order execution without tight coupling.

## Decision
We decouple the engine into distinct core components:
- **Coordinator**: Manages life cycle, initialization, and component lifecycle.
- **Pipeline**: Sequentially or concurrently processes incoming ticks/candles through registered modules.
- **Event Bus**: Handles async communication for market data, news, session transitions, and execution signals.
- **Module Manager**: Dynamically registers, enables, or disables feature modules.

## Consequences
- Modular execution allows independent testing of market state analysis vs. risk execution.
- Enables seamless switching between live market processing, backtesting, and replay simulation.
