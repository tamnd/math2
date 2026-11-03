---
tag: HNH4C6DV46
kind: concept
name: Push–relabel maximum flow algorithm
msc: [90C35, 05C21, 05C85]
sources:
  - url: https://en.wikipedia.org/wiki/Push%E2%80%93relabel_maximum_flow_algorithm
same_as:
  wikidata: Q583889
  wikipedia: Push–relabel maximum flow algorithm
---

## Summary

The push–relabel algorithm computes a maximum flow in a [[flow network|ZSNXTW5E2K]].
It does not follow augmenting paths.
Instead it keeps a preflow, which may hold extra flow at some vertices, and moves this extra flow locally along residual edges.
A height label on each vertex tells where the extra flow may go, and labels are raised when it is stuck.
It was introduced by Andrew Goldberg and Robert Tarjan, and its variants are among the fastest practical methods for the [[maximum flow problem|EXMR7RYRTP]].

## Explanations

### L1 human

Think of the vertices as water tanks placed at different heights, joined by pipes of limited capacity.
At the start the source floods all its outgoing pipes, so some tanks overflow.
An overflowing tank may pour water only into a neighbour exactly one level lower through a pipe that still has room.
If it cannot pour anywhere, the tank is lifted just high enough to pour again.
Water that cannot reach the sink is eventually lifted above the source and flows back to it.
When no tank overflows any more, the water that reached the sink is a maximum flow.
