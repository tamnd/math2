---
tag: YNFT400EV9
kind: definition
name: Incidence matrix
msc: [05C50]
defines: 9DNFN8M83X
uses: [0JD5C82QMB, 0R5HTV7REV, 0NZ8MDBN6Q, TN6M6DVZRP]
sources:
  - url: https://en.wikipedia.org/wiki/Incidence_matrix
---

## Definition

Let $G$ be a finite [[graph|0JD5C82QMB]] with vertices $v_1, \dots, v_n$ and edges $e_1, \dots, e_m$.
The incidence matrix of $G$ is the $n \times m$ matrix $B$ with $B_{ij} = 1$ if $v_i$ is an end of $e_j$, and $B_{ij} = 0$ otherwise.
Suppose that each edge $e_j$ is given an orientation, from a tail to a head.
The oriented incidence matrix is the $n \times m$ matrix $N$ with $N_{ij} = 1$ if $v_i$ is the head of $e_j$.
Also $N_{ij} = -1$ if $v_i$ is the tail of $e_j$, and $N_{ij} = 0$ otherwise.

## Remarks

Example: for the triangle with edges $e_1 = v_1 v_2$, $e_2 = v_2 v_3$, $e_3 = v_1 v_3$,
$$B = \begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix},$$
and each column has exactly two entries $1$, at the ends of its edge.
Non-example: a $0$–$1$ matrix with a column containing three entries $1$ is not the incidence matrix of a graph, since an edge has exactly two ends; such matrices describe hypergraphs.
Let $D$ be the diagonal matrix of degrees and $A$ the [[adjacency matrix|0NZ8MDBN6Q]] of a simple graph.
Then $B B^{T} = D + A$, and $N N^{T} = D - A$ is the [[Laplacian matrix|TN6M6DVZRP]] for every orientation.
Some authors use the transpose, with rows indexed by edges, or the opposite sign convention for $N$.
Mathlib defines the unoriented incidence matrix as `SimpleGraph.incMatrix`.
