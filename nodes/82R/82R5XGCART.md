---
tag: 82R5XGCART
kind: concept
name: Følner condition
msc: [43A07, 20F65]
sources:
  - url: https://en.wikipedia.org/wiki/Følner_sequence
---

## Summary

A group satisfies the Følner condition when it has finite subsets that are almost invariant under translation.
Moving such a set by a given element changes only a small fraction of it.
A sequence of such sets is a Følner sequence.
By Følner's theorem, a discrete group satisfies the condition exactly when it is [[amenable|CEAT9BESKK]].
Følner sequences are the natural sets over which to take averages in ergodic theorems for group actions.

## Explanations

### L1 human

In the integers, the block $\set{0, 1, \ldots, n-1}$ is almost unchanged when it is shifted by $1$: only one point leaves and one point enters.
As $n$ grows, the fraction of points that change goes to $0$.
Groups with such almost invariant finite sets are said to satisfy the Følner condition.
In the grid $\Z^2$, large squares work, since their boundary is small compared with their area.
In a free group, every finite set has a boundary comparable to its size, so the condition fails.
