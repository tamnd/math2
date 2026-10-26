---
tag: 0RKG5YW66Y
kind: concept
name: LU decomposition
aliases: [lu-factorization]
msc: [15A23, 65F05]
sources:
  - url: https://en.wikipedia.org/wiki/LU_decomposition
    locator: lead section
same_as:
  wikidata: Q833089
  wikipedia: LU decomposition
---

## Summary

An *LU decomposition* of a square matrix $A$ is a factorization $A = LU$.
Here $L$ is a [[lower triangular matrix|00J3KZP8Y0]] and $U$ is an [[upper triangular matrix|0N4XY7Z3NN]].
[[Gaussian elimination|0JVJ2WCXZH]] without row exchanges produces such a factorization: $U$ is the row echelon form, and $L$ stores the multipliers of the row operations.
With row exchanges, one gets $PA = LU$ for a [[permutation matrix|08SP3DF8NB]] $P$, and each square matrix over a field has such a factorization.

## Remarks

An invertible matrix has an LU decomposition with $L$ unit lower triangular if and only if all its leading principal minors are nonzero.
This decomposition is then unique.
The matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ has no LU decomposition, but it has one after a row exchange.
To solve $Ax = b$, solve $Ly = b$ by forward substitution and $Ux = y$ by [[back substitution|0ATFVE08MW]].
The decomposition also gives $\det A = \det L \det U$.

## Explanations

### L1 human

An LU decomposition writes a matrix as a product of two triangular matrices.
Triangular systems are easy to solve, so we solve $Ax = b$ in two easy steps.
It is useful when we solve many systems with the same $A$ and different right sides.
