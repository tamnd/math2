---
tag: 3YM9EK6VMB
kind: topic
name: Adjoints, normal operators and the spectral theorems
msc: ["15A18", "15A21", "15B57"]
topics: [GN8GYSDZFX]
---

## Summary

An inner product lets a linear map act on either side of the pairing, and the map that acts on the other side is the adjoint $T^*$.
For matrices in orthonormal coordinates the adjoint is the conjugate transpose, but it exists without coordinates, so it works on spaces of polynomials and functions as well.
The theory of operators on inner product spaces, a part of [[linear algebra|GN8GYSDZFX]], asks which operators get along well with their adjoints.
The self-adjoint operators, with $T^* = T$, have real eigenvalues and orthogonal eigenspaces.
The normal operators, with $T T^* = T^* T$, are over $\mathbb{C}$ exactly the operators that are diagonal in some orthonormal basis.
That last fact is the spectral theorem, and the name covers three versions: one for real symmetric matrices, one for Hermitian matrices and one for normal operators.
Watch out for the words: the real version needs a self-adjoint operator, the complex version needs only a normal one, and some books call self-adjoint matrices "symmetric" even over $\mathbb{C}$.
The route goes through Schur's theorem, which puts every complex operator in upper triangular form in an orthonormal basis.
It ends with the spectral decomposition into orthogonal projections, the block form of real normal operators, simultaneous diagonalization of commuting families, and the Rayleigh quotient, which finds the extreme eigenvalues by maximizing and minimizing.
Positive operators and the singular value decomposition come next, and they rest on the spectral theorem.

## Remarks

### Reading order

1. [[Adjoint of a linear map|0R9NMSM1ZP]]: the identity $\ip{Tv}{w} = \ip{v}{T^* w}$, first examples, and the algebra rules.
2. [[Matrix of the adjoint|0DBTE6HVBD]]: the conjugate transpose in orthonormal bases, and the fix for other bases.
3. [[Kernel and image of the adjoint|YPP8XT6B7Y]]: how $T^*$ swaps kernels and images, and a test for solving $Tv = w$.
4. [[Self-adjoint operator|0NEGN5CRSC]]: symmetric and Hermitian matrices as operators, and the real form $\ip{Tv}{v}$.
5. [[Eigenvalues of a self-adjoint operator are real|0C4NT4GT3X]]: a one-line proof by $\ip{Tv}{v}$.
6. [[Orthogonality of eigenspaces|0JHGAV9H25]]: for a normal operator, eigenvectors for different eigenvalues meet at right angles.
7. [[Schur decomposition|V1JG4C7R7B]]: every complex operator is upper triangular in some orthonormal basis.
8. [[Normal operator|0C8BR8XRTR]]: the condition $T T^* = T^* T$ and the equal norms $\norm{Tv} = \norm{T^* v}$.
9. [[Complex spectral theorem|04CW1P44VD]]: over $\mathbb{C}$, normal is the same as having an orthonormal basis of eigenvectors, so $A = U D U^*$.
10. [[Spectral theorem for Hermitian matrices|0DGZBQWZWN]]: the case $A = U D U^*$ with a real diagonal $D$.
11. [[Real spectral theorem|06J4PXRG22]]: over $\mathbb{R}$, self-adjoint is the same as orthonormally diagonalizable.
12. [[Spectral decomposition of a normal operator|D5KVBA1K9R]]: $T = \sum_j \lambda_j P_j$ with orthogonal projections, and functions $f(T)$ of an operator.
13. [[Normal form of a real normal operator|G6T1FNE3JC]]: over $\mathbb{R}$, $2 \times 2$ rotation and scaling blocks replace the eigenvalues that are not real.
14. [[Simultaneous unitary diagonalization of commuting normal operators|BFQQDA489F]]: one orthonormal eigenbasis for a whole commuting family.
15. [[Rayleigh quotient|06WHP8SE98]]: the extreme eigenvalues as the extreme values of $\ip{Av}{v} / \ip{v}{v}$.

### Prerequisites

- [[Inner product spaces|1D4JTZ9VS3]]: inner products, norms and orthonormal bases.
- [[Orthogonal complements, projections and least squares|8GQVME4SZZ]]: orthogonal complements and orthogonal projections.
- [[Diagonalization, triangularization and invariant subspaces|Z6S6PWMJPH]]: invariant subspaces and diagonalizable operators.
- [[Eigenvalues, the characteristic polynomial and the minimal polynomial|6R1D6QPY3S]]: eigenvalues, eigenvectors and the characteristic polynomial.
