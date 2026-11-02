---
tag: CRPZ1RVNKQ
kind: concept
name: Modulus of smoothness
msc: [41A25, 26A15, 41A17]
sources:
  - url: https://en.wikipedia.org/wiki/Modulus_of_smoothness
same_as:
  wikidata: Q25109621
  wikipedia: Modulus of smoothness
---

## Summary

The modulus of smoothness of order $k$ of a function measures the size of its $k$-th finite differences with small step.
For $k = 1$ in the uniform norm it is the [[modulus of continuity|AXCJBSQZWF]].
Higher orders detect smoothness beyond Lipschitz, and they give the sharp form of the direct and inverse theorems of approximation by polynomials.

## Explanations

### L1 human

The first difference $f(x + h) - f(x)$ is small when $f$ changes little over a step $h$.
The second difference $f(x + 2h) - 2 f(x + h) + f(x)$ is small when $f$ is nearly a straight line over two steps; it vanishes for every linear function.
The modulus of smoothness records the largest such difference over all steps up to $t$.
For $f(x) = x$ the first-order modulus is $t$ and the second-order modulus is $0$.
