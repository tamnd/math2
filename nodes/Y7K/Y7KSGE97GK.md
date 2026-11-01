---
tag: Y7KSGE97GK
kind: concept
name: Lagrange polynomial
msc: [41A05, 65D05, 26C05]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange_polynomial
same_as:
  wikidata: Q861606
  wikipedia: Lagrange polynomial
---

## Summary

Take $n + 1$ points in the plane with distinct first coordinates.
Their Lagrange polynomial is the unique [[polynomial function|1G0B73WPX8]] of degree at most $n$ whose graph passes through all of them.
It is written as a sum of basis polynomials, each equal to $1$ at one node and $0$ at the others.
It gives an explicit solution of [[polynomial interpolation|SS1YMS2NPC]] and is the starting point of numerical differentiation and quadrature rules.
The [[definition|TEQNAME853]] gives the formula.

## Explanations

### L1 human

Through two points there is one line, and through three points with different $x$-values there is one parabola or line.
The Lagrange formula writes this curve down directly.
For each point it builds a small polynomial that is $1$ at that point and $0$ at all the other points.
Then it adds these pieces, each multiplied by the height it must reach.
For the points $(0, 1)$, $(1, 3)$, $(2, 7)$ the result is $x^2 + x + 1$.
