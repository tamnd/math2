---
tag: 1ZA98AGKGK
kind: concept
name: Regular chain
msc: [13P15, 13P10, 68W30]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_chain
same_as:
  wikidata: Q7309593
  wikipedia: Regular chain
---

## Summary

A regular chain is a triangular set of polynomials, with one polynomial for each of some of the variables.
In it, the leading coefficient of each polynomial is not a zero divisor modulo the ideal described by the earlier polynomials.
Regular chains describe the solution sets of polynomial systems in a triangular form that can be solved one variable at a time.
Every polynomial system can be decomposed into finitely many regular chains, and this gives an alternative to [[Gröbner bases|C83KPT47R0]] in computer algebra.

## Explanations

### L1 human

A triangular system first constrains $x$, then $y$ in terms of $x$, then $z$ in terms of $x$ and $y$, and so on.
To solve it, one solves for $x$, substitutes, solves for $y$, and continues.
This fails if the coefficient of the highest power of $y$ vanishes for some allowed values of $x$.
A regular chain is a triangular system in which this never happens in a harmful way.
Each leading coefficient is invertible, or at least not a zero divisor, given the earlier equations.
For example, $x^2 - 1 = 0$, $xy - 1 = 0$ is a regular chain, because $x$ is nonzero whenever $x^2 = 1$.
