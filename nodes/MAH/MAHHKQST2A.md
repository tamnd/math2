---
tag: MAHHKQST2A
kind: concept
name: Uniform convergence of series
msc: [40A30]
specializes: [08VZ57PT26]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_convergence
---

## Summary

A [[series of functions|0Y3KSN2E9X]] converges uniformly on a set when its partial sums converge [[uniformly|08VZ57PT26]] on that set.
Equivalently, the tails of the series become small at the same rate at every point.
This is the mode of convergence that lets one carry continuity, integrals and, with extra hypotheses, derivatives from the terms to the sum.

## Explanations

### L1 human

A series of functions is, at each point, an ordinary series of numbers.
At each point the leftover tail after $N$ terms shrinks, but the speed may depend on the point.
Uniform convergence asks for one $N$ that makes the tail small at all points at once.
For example, $\sum_{n \ge 0} x^n$ converges uniformly on $[0, 1/2]$, because the tail after $N$ terms is at most $2 \cdot 2^{-(N+1)}$ there.
On $[0, 1)$ it converges at each point but not uniformly, since near $x = 1$ the tail stays large.
