---
tag: 0HYC2RHD3M
kind: statement
role: theorem
name: Eigenvalues of a positive definite matrix are positive
msc: [15B57, 15A18]
uses: [0QQCG3JWJ4, 0ZND7NQ970]
sources:
  - url: https://en.wikipedia.org/wiki/Definite_matrix
    locator: Eigenvalues
---

## Statement

Let $A$ be a [[positive definite|0KX66CZMBB]] $n \times n$ complex Hermitian matrix.
Then each [[eigenvalue|0BQAA2BK3Q]] of $A$ is a positive real number.

## Remarks

If $Ax = \lambda x$ with $x \ne 0$, then $0 < x^* A x = \lambda\, x^* x$, and $x^* x > 0$.
The converse holds: a Hermitian matrix with only positive eigenvalues is positive definite, by the spectral theorem.
So $\det A > 0$ and $\tr A > 0$ for a positive definite $A$.

## Explanations

### L1 human

A positive definite matrix stretches each of its eigenvector directions by a positive factor.
It never flips or crushes a direction.
So its eigenvalues, its determinant and its trace are all positive.
