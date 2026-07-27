# ADR 0005: Event-Driven Engine & Pub-Sub Mechanism

## Status
Accepted

## Context
High-frequency market ticks, scheduled economic news announcements, session changes, and order executions occur asynchronously.

## Decision
We implement an event-driven event bus in `core/engine/event_bus.py` with typed event definitions under `core/events/`:
- `MarketEvent`
- `NewsEvent`
- `SessionEvent`
- `ExecutionEvent`

Subscribers register handlers for specific event types.

## Consequences
- Clean separation between incoming data streams, strategy processing, and output services (broker execution / notification / dashboard updates).
- Simplified testing via mock event publishing.
