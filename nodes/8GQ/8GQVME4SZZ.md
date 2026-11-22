---
tag: 8GQVME4SZZ
kind: topic
name: Orthogonal complements, projections and least squares
msc: ["15A63", "15A23", "65F20"]
topics: [GN8GYSDZFX]
---

## Summary

Once a vector space has an inner product, every subspace has a partner: the set of vectors at a right angle to all of it.
This part of [[linear algebra|GN8GYSDZFX]] starts from that orthogonal complement.
In finite dimension a subspace and its complement split the space, so every vector is a part inside the subspace plus a part orthogonal to it.
For a matrix, the same splitting pairs the null space with the row space and the left null space with the column space.
The part inside the subspace is the orthogonal projection, and the best approximation theorem shows that it is the closest point of the subspace.
That one fact turns an unsolvable system $Ax = b$ into the least-squares problem, solved by the normal equations $A^{\mathsf{T}} A x = A^{\mathsf{T}} b$ or, more stably, by the QR decomposition.
Three uses of the same geometry close the story.
They are the shortest solution of an underdetermined system, the angles between two subspaces, and the approximation of functions by Legendre polynomials and Fourier sums.

## Remarks

### Reading order

1. [[Orthogonal complement|0XJXTBCB2T]]: how to find all vectors orthogonal to a subspace, by solving a null space problem.
2. [[Orthogonal decomposition|0SP7P0G7KQ]]: why each vector splits uniquely into a part in $U$ and a part in $U^\perp$, and why the dimensions add up.
3. [[Double orthogonal complement|0PXN9G4MX1]]: the rule $(U^\perp)^\perp = U$, and why it needs finite dimension or closedness.
4. [[Orthogonality of the fundamental subspaces|GQF2KG1R1N]]: the picture of $Ax = b$, and a one-line test for whether it has a solution.
5. [[Orthogonal projection|0B8KZRT28M]]: the map that keeps the part in $U$, its formulas, its matrix $A (A^{\mathsf{T}} A)^{-1} A^{\mathsf{T}}$, and its algebraic description.
6. [[Best approximation theorem|0MCDDSCB9Z]]: why the projection is the unique closest point, and how to compute the distance to a subspace.
7. [[Least squares|0BYTQ4X1HC]]: how to fit a model to data by projecting $b$ onto the column space.
8. [[Normal equations|4D7MRG4D91]]: the linear system that every least-squares solution satisfies, and why it can lose accuracy.
9. [[QR decomposition|0ERWG4NXQ9]]: Gram-Schmidt written as a matrix factorization, and the stable way to solve least squares.
10. [[Minimum-norm solution|QM2Y84VDX8]]: how to choose the shortest of many solutions, and why it lies in the row space.
11. [[Principal angles between subspaces|YHVD3773AW]]: how to measure the angles between two subspaces with singular values.
12. [[Best mean-square approximation|899D63WW04]]: Legendre polynomials and Fourier coefficients as projections in spaces of functions.

### Prerequisites

- [[Inner product spaces|1D4JTZ9VS3]]: inner products, norms, orthonormal bases and the Gram-Schmidt process.
- [[Matrices of linear maps, rank and change of basis|S6559D61BP]]: column space, null space, rank and the rank-nullity theorem.
- [[Direct sums, complements and quotient spaces|QHKTJ89V6S]]: direct sums and complements of subspaces.
- [[Vectors in the plane and in space|VKVAJ94SKZ]]: the dot product and angles in $\R^2$ and $\R^3$.
