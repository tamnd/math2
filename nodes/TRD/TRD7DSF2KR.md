---
tag: TRD7DSF2KR
kind: concept
name: Jacobi polynomials
msc: [33C45, 42C05]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobi_polynomials
same_as:
  wikidata: Q371631
  wikipedia: Jacobi polynomials
---

## Summary

The Jacobi polynomials $P_n^{(\alpha, \beta)}$ are the [[classical orthogonal polynomials|47WJ34NC9K]] on $[-1, 1]$ for the weight $(1 - x)^\alpha (1 + x)^\beta$, with $\alpha, \beta > -1$.
They include the [[Gegenbauer polynomials|5TRFA6F79B]], the [[Legendre polynomials|QFYGJVA996]] and both kinds of Chebyshev polynomials as special cases, up to constant factors.
They are terminating [[hypergeometric functions|463X5V31D9]], and they appear in harmonic analysis on spheres and on compact symmetric spaces.

## Explanations

### L1 human

The weight $(1 - x)^\alpha (1 + x)^\beta$ on the interval $[-1, 1]$ can favour one end, the other end, or both, depending on the two exponents.
For each choice there is one family of polynomials, perpendicular to each other for this weight: the Jacobi polynomials.
With $\alpha = \beta = 0$ the weight is constant and the family is the Legendre polynomials.
For example, $P_1^{(0,0)}(x) = x$ is perpendicular to the constant $1$ because $\int_{-1}^1 x \, dx = 0$.
