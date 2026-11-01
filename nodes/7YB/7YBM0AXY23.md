---
tag: 7YBM0AXY23
kind: definition
name: Laplacian matrix
msc: [05C50]
defines: TN6M6DVZRP
uses: [0JD5C82QMB, 0NZ8MDBN6Q, 0T0F6CCS9W, 0N28QN4CYA, 0880F9EQCP]
sources:
  - url: https://en.wikipedia.org/wiki/Laplacian_matrix
---

## Definition

Let $G$ be a finite simple [[graph|0JD5C82QMB]] with vertices $v_1, \dots, v_n$.
Let $D$ be the diagonal matrix with $D_{ii} = \deg(v_i)$, the [[degree|0T0F6CCS9W]] of $v_i$, and let $A$ be the [[adjacency matrix|0NZ8MDBN6Q]] of $G$.
The Laplacian matrix of $G$ is the $n \times n$ matrix $L = D - A$.
So $L_{ii} = \deg(v_i)$, $L_{ij} = -1$ if $i \ne j$ and $v_i v_j$ is an edge, and $L_{ij} = 0$ otherwise.

## Remarks

For every real vector $x$, $x^{T} L x = \sum (x_i - x_j)^2$, the sum running over the edges $v_i v_j$.
Hence $L$ is [[symmetric|0N28QN4CYA]] and [[positive semidefinite|0880F9EQCP]], the all-ones vector lies in its kernel, and the multiplicity of the eigenvalue $0$ equals the number of connected components of $G$.
Example: for the path $v_1 v_2 v_3$,
$$L = \begin{pmatrix} 1 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{pmatrix},$$
whose eigenvalues are $0$, $1$ and $3$, with eigenvectors $(1,1,1)$, $(1,0,-1)$ and $(1,-2,1)$.
Non-example: the matrix $D + A$ has the right diagonal but the wrong sign off the diagonal.
It is the signless Laplacian, and it has the same spectrum as $L$ when $G$ is bipartite, but not in general.
The normalized Laplacian $D^{-1/2} L D^{-1/2}$, defined when no vertex is isolated, is also common.
Mathlib defines the Laplacian matrix as `SimpleGraph.lapMatrix`.
