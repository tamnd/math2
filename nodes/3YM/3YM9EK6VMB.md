---
tag: 3YM9EK6VMB
kind: topic
name: Adjoints, normal operators and the spectral theorems
msc: ["15A18", "15A21", "15B57"]
topics: [GN8GYSDZFX]
---

## Summary

This topic is a part of [[linear algebra|GN8GYSDZFX]].
It covers the adjoint of a linear map, self-adjoint and normal operators, Schur's unitary triangularization, and the spectral theorems in finite dimension.
The adjoint $T^*$ moves an operator from one side of the inner product to the other.
Self-adjoint operators have real eigenvalues and orthogonal eigenspaces.
Normal operators are exactly the operators with an orthonormal basis of eigenvectors over $\mathbb{C}$.
The name "spectral theorem" is used for three versions: for real symmetric matrices, for Hermitian matrices and for normal operators.
Some books call self-adjoint operators "symmetric".
The last pages give the spectral decomposition, the normal form of a real normal operator, simultaneous diagonalization and the Rayleigh quotient.

## Remarks

### Reading order

1. [[Adjoint of a linear map|0R9NMSM1ZP]]: the operator $T^*$ with $\ip{Tv}{w} = \ip{v}{T^* w}$.
2. [[Matrix of the adjoint|0DBTE6HVBD]]: the conjugate transpose in an orthonormal basis.
3. [[Kernel and image of the adjoint|~09be9c75]]: $\ker T^*$ is the orthogonal complement of the image of $T$.
4. [[Self-adjoint operator|0NEGN5CRSC]]: operators with $T^* = T$, and the skew-adjoint operators with $T^* = -T$.
5. [[Eigenvalues of a self-adjoint operator are real|0C4NT4GT3X]]: real eigenvalues, and an eigenvector from the maximum of the quadratic form.
6. [[Orthogonality of eigenspaces|0JHGAV9H25]]: eigenvectors for distinct eigenvalues are orthogonal.
7. [[Schur decomposition|V1JG4C7R7B]]: each complex operator is upper triangular in some orthonormal basis.
8. [[Normal operator|0C8BR8XRTR]]: operators that commute with their adjoint.
9. [[Complex spectral theorem|04CW1P44VD]]: over $\mathbb{C}$, normal means orthonormal eigenbasis.
10. [[Spectral theorem for Hermitian matrices|0DGZBQWZWN]]: $A = U D U^*$ with $U$ unitary and $D$ real.
11. [[Real spectral theorem|06J4PXRG22]]: over $\mathbb{R}$, self-adjoint means orthonormal eigenbasis, by induction or by maximization.
12. [[Spectral decomposition of a normal operator|~e55cbc04]]: $T = \sum_j \lambda_j P_j$ with orthogonal projections.
13. [[Normal form of a real normal operator|~abc653f3]]: blocks $\begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ in place of the non-real eigenvalues.
14. [[Simultaneous unitary diagonalization of commuting normal operators|~60326533]]: one orthonormal eigenbasis for a commuting family.
15. [[Rayleigh quotient|06WHP8SE98]]: the extreme eigenvalues as extreme values, and the way to the Courant-Fischer theorem.

### Prerequisites

- [[Inner product spaces|1D4JTZ9VS3]]: inner products, norms and orthonormal bases.
- [[Orthogonal complements, projections and least squares|8GQVME4SZZ]]: orthogonal complements and orthogonal projections.
- [[Diagonalization, triangularization and invariant subspaces|Z6S6PWMJPH]]: invariant subspaces and diagonalizable operators.
- [[Eigenvalues, the characteristic polynomial and the minimal polynomial|6R1D6QPY3S]]: eigenvalues, eigenvectors and the characteristic polynomial.
