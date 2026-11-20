---
tag: 8GQVME4SZZ
kind: topic
name: Orthogonal complements, projections and least squares
msc: ["15A63", "15A23", "65F20"]
topics: [GN8GYSDZFX]
---

## Summary

This topic is a part of [[linear algebra|GN8GYSDZFX]].
It covers orthogonal complements and decompositions, orthogonal projections and best approximation, least squares, and the QR decomposition.

## Remarks

### Reading order

1. [[Orthogonal complement|0XJXTBCB2T]]: the vectors orthogonal to a subspace, computed as a null space.
2. [[Orthogonal decomposition|0SP7P0G7KQ]]: $V = U \oplus U^\perp$ and $\dim U^\perp = \dim V - \dim U$ in finite dimension.
3. [[Double orthogonal complement|0PXN9G4MX1]]: $(U^\perp)^\perp = U$ in finite dimension.
4. [[Orthogonality of the fundamental subspaces|GQF2KG1R1N]]: the null space and the row space are orthogonal complements, and so are the column space and the left null space.
5. [[Orthogonal projection|0B8KZRT28M]]: the projection along $U^\perp$, its formulas and its matrix $A (A^{\mathsf{T}} A)^{-1} A^{\mathsf{T}}$.
6. [[Best approximation theorem|0MCDDSCB9Z]]: the projection is the unique closest point of the subspace.
7. [[Least squares|0BYTQ4X1HC]]: minimize $\norm{Ax - b}$ by projecting $b$ onto the column space.
8. [[Normal equations|4D7MRG4D91]]: $A^{\mathsf{T}} A x = A^{\mathsf{T}} b$, and why they square the condition number.
9. [[QR decomposition|0ERWG4NXQ9]]: Gram-Schmidt in matrix form, and least squares by $R x = Q^{\mathsf{T}} b$.
10. [[Minimum-norm solution|QM2Y84VDX8]]: the shortest solution of an underdetermined system lies in the row space.
11. [[Principal angles between subspaces|YHVD3773AW]]: angles between two subspaces from the singular values of $Q_1^{\mathsf{T}} Q_2$.
12. [[Best mean-square approximation|899D63WW04]]: Legendre polynomials and Fourier coefficients as projections in spaces of functions.

### Prerequisites

- [[Inner product spaces|1D4JTZ9VS3]]: inner products, norms, orthonormal bases and the Gram-Schmidt process.
- [[Matrices of linear maps, rank and change of basis|S6559D61BP]]: column space, null space, rank and the rank-nullity theorem.
- [[Direct sums, complements and quotient spaces|QHKTJ89V6S]]: direct sums and complements of subspaces.
- [[Vectors in the plane and in space|VKVAJ94SKZ]]: the dot product and angles in $\R^2$ and $\R^3$.
