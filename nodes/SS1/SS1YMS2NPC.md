---
tag: SS1YMS2NPC
kind: concept
name: Polynomial interpolation
msc: [41A05, 65D05]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial_interpolation
same_as:
  wikidata: Q637347
  wikipedia: Polynomial interpolation
---

## Summary

Polynomial interpolation finds a polynomial whose graph passes through finitely many given points.
Through $n + 1$ points with distinct first coordinates there is exactly one polynomial of degree at most $n$.
[[Lagrange interpolation|237KR6FRCK]] gives an explicit formula for it.
It is a basic tool to approximate functions, to derive numerical integration rules and to reconstruct polynomials from their values.

## Explanations

### L1 human

Through two points there is one line, and through three points with distinct $x$-values there is one parabola or line.
In general, $n + 1$ points fix a polynomial of degree at most $n$.
For the points $(0, 1)$, $(1, 3)$ and $(2, 7)$ the polynomial is $x^2 + x + 1$.
The [[definition|EKDSDN89FR]] states the conditions.
