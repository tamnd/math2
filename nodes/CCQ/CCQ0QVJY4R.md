---
tag: CCQ0QVJY4R
kind: definition
name: Facet
msc: [52B05, 52B11]
defines: DPDXN2FJC4
uses: [300K6CB1KH, KY7SB854VH, 0YMB1676R1]
sources:
  - url: https://en.wikipedia.org/wiki/Facet_(geometry)
---

## Definition

Let $P$ be a [[convex polytope|300K6CB1KH]] of dimension $d \ge 1$, where the dimension of a set is the dimension of its [[affine span|0YMB1676R1]].
A *facet* of $P$ is a [[face|KY7SB854VH]] $F$ of $P$ with $\dim F = d - 1$.

## Remarks

Example: the cube $[0,1]^3$ has dimension $3$.
The square $\set{x \in [0,1]^3 : x_3 = 1}$ is the intersection of the cube with the supporting plane $x_3 = 1$, and its affine span is a plane, so it is a facet.
The cube has six facets, one for each equation $x_i = 0$ or $x_i = 1$.

Non-example: the edge $\set{(t, 0, 0) : 0 \le t \le 1}$ of the same cube is a face, but its dimension is $1 \ne 2$, so it is not a facet.

Equivalently, when $P \subset \R^d$ is full-dimensional, $F$ is a facet if and only if $F = P \cap H$ for a supporting hyperplane $H$ such that $F$ spans $H$ affinely.
A full-dimensional polytope has an irredundant description by linear inequalities, unique up to positive scaling of each inequality.
Its inequalities correspond one to one to its facets.
The faces of dimension $0$ and $1$ are the vertices and edges; for $d = 3$ the facets are the usual two-dimensional faces.
