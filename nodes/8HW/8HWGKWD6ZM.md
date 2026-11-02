---
tag: 8HWGKWD6ZM
kind: concept
name: Fredholm operator
msc: [47A53]
sources:
  - url: https://en.wikipedia.org/wiki/Fredholm_operator
same_as:
  wikidata: Q573631
  wikipedia: Fredholm operator
---

## Summary

A Fredholm operator is a bounded linear map between Banach spaces whose kernel and cokernel are both finite-dimensional.
Such an operator is invertible up to finite-dimensional errors, so linear equations with it behave almost like square linear systems.
Fredholm operators carry an integer invariant, the index, which is stable under small and compact perturbations and links operator theory with topology.

## Explanations

### L1 human

For a square matrix, the equation $Ax = b$ either has a unique solution for every $b$, or it fails in a finite number of directions.
A Fredholm operator has the same kind of behaviour on infinite-dimensional spaces.
Only finitely many independent vectors are sent to zero, and only finitely many independent directions are missed by the image.
For example, the shift $(x_1, x_2, \ldots) \mapsto (0, x_1, x_2, \ldots)$ on square-summable sequences sends no nonzero vector to zero and misses only the direction of the first coordinate.
