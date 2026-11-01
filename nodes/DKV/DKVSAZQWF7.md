---
tag: DKVSAZQWF7
kind: concept
name: Clifford analysis
msc: [30G35, 15A66]
sources:
  - url: https://en.wikipedia.org/wiki/Clifford_analysis
same_as:
  wikidata: Q5133083
  wikipedia: Clifford analysis
---

## Summary

Clifford analysis extends complex analysis to $\R^n$ by letting functions take values in a [[Clifford algebra|A38B1QFK20]].
Its central objects are the [[monogenic functions|646PNPT1R6]], the functions annihilated by a Dirac operator.
The square of the Dirac operator is the Laplacian up to sign.
So the theory refines harmonic analysis, as holomorphic functions refine harmonic functions in the plane.
It has a Cauchy integral formula, Taylor and Laurent series, and links to singular integrals, spin geometry and representation theory.
It grew out of [[quaternionic analysis|SAT7ST5WP7]], which is closely related to its low-dimensional cases.

## Explanations

### L1 human

In the plane, holomorphic functions are the solutions of the Cauchy–Riemann equations, a first-order system whose "square" is the Laplace equation.
In higher dimensions there is no such system with complex numbers alone.
A Clifford algebra supplies anticommuting units $e_1, \ldots, e_n$ with $e_j^2 = -1$, and with them the operator $\sum_j e_j \partial_{x_j}$ squares to minus the Laplacian.
Functions killed by this operator behave much like holomorphic functions: they have an integral formula, power series, and a maximum principle.
