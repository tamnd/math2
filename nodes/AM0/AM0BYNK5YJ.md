---
tag: AM0BYNK5YJ
kind: concept
name: Sum-of-squares optimization
msc: [90C23, 90C22]
sources:
  - url: https://en.wikipedia.org/wiki/Sum-of-squares_optimization
same_as:
  wikidata: Q7636875
  wikipedia: Sum-of-squares optimization
---

## Summary

Sum-of-squares optimization is optimization over polynomials constrained to be sums of squares of polynomials.
Since a polynomial is a sum of squares exactly when a related matrix of coefficients is [[positive semidefinite|01MMVW8CKC]], these problems are [[semidefinite programs|2RTN2X4R2N]].
Every sum of squares is nonnegative, so the method gives computable certificates of nonnegativity and lower bounds for polynomial minimisation.
The gap between nonnegative polynomials and sums of squares is the subject of [[Hilbert's seventeenth problem|J45F4F13VB]], and the [[Positivstellensatz|FN734RQYM6]] gives certificates on semialgebraic sets.

## Explanations

### L1 human

Proving that a polynomial is never negative is hard in general.
An easy sufficient reason is that it can be written as a sum of squares, like $x^2 - 2xy + 2y^2 = (x - y)^2 + y^2$.
Finding such a decomposition is a convex problem that a computer can solve.
To bound the minimum of $p$ from below, one looks for the largest $\gamma$ such that $p - \gamma$ is a sum of squares.
