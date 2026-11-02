---
tag: QYYCFQ8E5D
kind: concept
name: Incomplete Cholesky factorization
msc: [65F08, 65F50, 65F10]
sources:
  - url: https://en.wikipedia.org/wiki/Incomplete_Cholesky_factorization
same_as:
  wikidata: Q6015160
  wikipedia: Incomplete Cholesky factorization
---

## Summary

An incomplete Cholesky factorization of a sparse symmetric positive definite matrix $A$ is a sparse lower triangular matrix $L$ with $L L^T \approx A$.
It is computed like the [[Cholesky decomposition|0WKG8CYY6A]], but every entry outside a prescribed sparsity pattern is dropped.
Its main use is as a [[preconditioner|KE98SW3SBD]] for the conjugate gradient method.

## Explanations

### L1 human

The exact Cholesky factor of a sparse matrix is often much denser than the matrix itself.
The incomplete factor keeps only the entries in allowed positions, for example the positions where $A$ itself is nonzero.
The result is cheap to store and to use, and $L L^T$ is close to $A$, though not equal.
Solving with $L L^T$ then serves as a fast rough inverse of $A$ inside an iterative method.
