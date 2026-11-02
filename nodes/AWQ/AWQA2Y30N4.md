---
tag: AWQA2Y30N4
kind: concept
name: Numerical methods for linear least squares
msc: [65F20, 62J05]
sources:
  - url: https://en.wikipedia.org/wiki/Numerical_methods_for_linear_least_squares
same_as:
  wikidata: Q55627115
  wikipedia: Numerical methods for linear least squares
---

## Summary

Numerical methods for linear least squares are algorithms for the [[least squares|0BYTQ4X1HC]] problem.
They compute a vector $x$ minimizing $\norm{Ax - b}_2$ for a given matrix $A$ and vector $b$.
The main methods solve the normal equations by a [[Cholesky decomposition|0WKG8CYY6A]], use a [[QR decomposition|0ERWG4NXQ9]] of $A$, or use the [[singular value decomposition|000NPTMX6J]].
They differ in cost and in how rounding errors are amplified, which depends on the [[condition number|AB3S6MHJ8X]] of $A$.

## Explanations

### L1 human

Fitting a straight line through many measured points gives more equations than unknowns, and usually no line passes through all points.
Least squares picks the line that makes the sum of squared misses smallest.
On paper one can solve the normal equations $A^T A x = A^T b$, but on a computer this can lose twice as many digits as needed.
For example, if $A$ has condition number $10^8$, then $A^T A$ has condition number $10^{16}$.
In double precision the normal equations may then give no correct digits, while a QR-based method still gives about eight when the data are nearly consistent.
