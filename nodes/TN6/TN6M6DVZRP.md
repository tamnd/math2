---
tag: TN6M6DVZRP
kind: concept
name: Laplacian matrix
msc: [05C50]
sources:
  - url: https://en.wikipedia.org/wiki/Laplacian_matrix
same_as:
  wikidata: Q772067
  wikipedia: Laplacian matrix
---

## Summary

The Laplacian matrix of a finite graph is the degree matrix minus the [[adjacency matrix|08B9CX109G]].
It is symmetric and positive semidefinite, and its eigenvalues carry information about connectivity: the number of connected components is the multiplicity of the eigenvalue $0$.
Through [[Kirchhoff's matrix tree theorem|S1PG1N2VEX]] it counts spanning trees, and its second smallest eigenvalue controls how well the graph is connected.
It is the discrete analogue of the Laplace operator of analysis.

## Explanations

### L1 human

Put a number on each vertex of a graph.
The Laplacian compares each number with the numbers at the neighbouring vertices: it adds up the differences.
If the numbers are all equal on a connected graph, the Laplacian gives zero everywhere, just as a constant function has zero second derivative.
For the path with three vertices, the Laplacian is a $3 \times 3$ matrix with the degrees $1, 2, 1$ on the diagonal and $-1$ for each edge.
