---
tag: KFWQ24D9M6
kind: concept
name: Finitely additive measure
msc: [28A12, 28A10]
sources:
  - url: https://en.wikipedia.org/wiki/Content_(measure_theory)
---

## Summary

A finitely additive measure is a function on an algebra of sets with values in $[0, \infty]$.
It is $0$ on the empty set and adds over finite disjoint unions.
It is weaker than a measure, which must add over countable disjoint unions.
Finitely additive measures appear in the construction of measures, in densities on the integers and in the duals of spaces of bounded functions.

## Explanations

### L1 human

A finitely additive measure gives sizes to sets so that the size of two separate pieces together is the sum of their sizes.
Nothing is required for infinitely many pieces.
For example, on the natural numbers, give size $0$ to finite sets and size $1$ to sets with finite complement.
Two disjoint pieces cannot both have finite complement, so sizes add.
But $\N$ is the union of the singletons $\set{n}$, each of size $0$, so the rule fails for infinitely many pieces.
