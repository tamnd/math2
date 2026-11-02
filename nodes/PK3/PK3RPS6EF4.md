---
tag: PK3RPS6EF4
kind: definition
name: Uniform polytope
msc: [51M20, 52B15]
defines: BZXHGNGQAX
uses: [300K6CB1KH, 01KJJ9A400, DPDXN2FJC4, 0ZG3Z5JZ85, 02GK6HZYBT, R7V3S9V891]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_polytope
---

## Definition

Convex *uniform polytopes* of dimension $d \ge 2$ are defined by induction on $d$.

1. A convex polygon is uniform if it is a [[regular polygon|01KJJ9A400]].
2. For $d \ge 3$, a [[convex polytope|300K6CB1KH]] $P \subseteq \R^d$ of dimension $d$ is uniform if both of the following hold:
   - the [[symmetry group|0ZG3Z5JZ85]] of $P$ acts [[transitively|02GK6HZYBT]] on the set of [[vertices|R7V3S9V891]] of $P$;
   - every [[facet|DPDXN2FJC4]] of $P$ is a uniform polytope of dimension $d-1$.

## Remarks

Example: the triangular prism whose bases are equilateral triangles of side $1$ and whose sides are unit squares is uniform.
Its facets are regular polygons, hence uniform.
The symmetries of the prism, namely rotations about its axis, the swap of the two bases, and reflections, carry any vertex to any other.

Non-example: the square pyramid with equilateral triangles and a unit square base has regular facets, but it is not uniform.
Its apex lies on $4$ edges and each base vertex on $3$, so no symmetry maps the apex to a base vertex, and the first condition fails.
Second non-example: a box $[0,1] \times [0,1] \times [0,2]$ is vertex-transitive, but its rectangular facets are not regular polygons, so the second condition fails.

Every [[regular polytope|F60PD912D5]] is uniform.
In dimension $3$ the convex uniform polytopes are the five Platonic solids, the thirteen Archimedean solids, and the prisms and antiprisms over regular polygons.
The definition extends to non-convex star polytopes and to uniform tilings, by allowing star polygon faces or unbounded arrangements.
