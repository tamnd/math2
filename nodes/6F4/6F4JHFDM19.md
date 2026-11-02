---
tag: 6F4JHFDM19
kind: definition
name: Simplicial polytope
msc: [52B05, 52B11, 52B12]
defines: YVJ15PGKDM
uses: [300K6CB1KH, DPDXN2FJC4, 0FQSDC2EQ2]
sources:
  - url: https://en.wikipedia.org/wiki/Simplicial_polytope
---

## Definition

A $k$-simplex is the [[convex hull|0FQSDC2EQ2]] of $k + 1$ affinely independent points.
Let $P$ be a [[convex polytope|300K6CB1KH]] of dimension $d \ge 1$.
$P$ is *simplicial* if every [[facet|DPDXN2FJC4]] of $P$ is a $(d-1)$-simplex.

## Remarks

Equivalently, every proper face of $P$ is a simplex, since each face of a simplex is a simplex.
Equivalently again, every facet of $P$ has exactly $d$ vertices.

Example: the octahedron $\operatorname{conv}\set{\pm e_1, \pm e_2, \pm e_3}$ in $\R^3$ is simplicial.
Its facets are the eight triangles $\operatorname{conv}\set{\epsilon_1 e_1, \epsilon_2 e_2, \epsilon_3 e_3}$ with $\epsilon_i \in \set{1, -1}$, and each is the hull of $3$ affinely independent points.

Non-example: the cube $[0,1]^3$ is not simplicial, because its facets are squares with $4 > 3$ vertices.

Every polygon is simplicial, since its facets are segments.
The convex hull of finitely many points in general position in $\R^d$, with at least $d+1$ of them, is simplicial.
