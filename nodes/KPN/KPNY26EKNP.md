---
tag: KPNY26EKNP
kind: example
name: Associahedron
msc: [52B12, 52B05, 05A15]
instance_of: [7E6FXTGH2Y]
uses: [300K6CB1KH, R7V3S9V891, DPDXN2FJC4, 0YWZJEABB2, Q6KKBP3RRP]
sources:
  - url: https://en.wikipedia.org/wiki/Associahedron
same_as:
  wikidata: Q4809117
  wikipedia: Associahedron
---

## Example

Let $n \ge 1$ and let $Q$ be a convex polygon with $n + 3$ vertices.
A diagonal of $Q$ joins two non-adjacent vertices.
The *associahedron* $K$ of dimension $n$ is a [[convex polytope|300K6CB1KH]] whose face lattice is described as follows.

1. The nonempty faces of $K$ correspond to the sets of pairwise non-crossing diagonals of $Q$, ordered by reverse inclusion. A $k$-face corresponds to $n - k$ diagonals.
2. The [[vertices|R7V3S9V891]] correspond to the [[triangulations|Q6KKBP3RRP]] of $Q$, the maximal sets of $n$ non-crossing diagonals.
3. The [[facets|DPDXN2FJC4]] correspond to the single diagonals of $Q$.
4. Two vertices are joined by an edge when the triangulations differ by a flip. A flip removes one diagonal and inserts the other diagonal of the quadrilateral that appears.

Each triangulation has $n$ diagonals and each can be flipped, so every vertex lies in exactly $n$ edges, and $K$ is a [[simple polytope|7E6FXTGH2Y]].
The number of vertices is the [[Catalan number|0YWZJEABB2]] $C_{n+1}$, the number of triangulations of an $(n+3)$-gon.

## Remarks

For $n = 2$, $Q$ is a pentagon with $5$ triangulations and $5$ diagonals, and $K$ is a pentagon.
For $n = 3$, $Q$ is a hexagon with $14$ triangulations and $9$ diagonals, and $K$ is a three-dimensional polytope with $14$ vertices and $9$ facets ($3$ squares and $6$ pentagons).
The same lattice also describes the ways to put brackets in a product of $n + 2$ factors, which is where the name comes from.
Several explicit realizations by coordinates are known.

## Explanations

### L1 human

Draw a hexagon and cut it into triangles with straight cuts between corners.
There are $14$ ways to do it.
Changing one cut at a time moves you between them, and these moves form the edges of a solid with $14$ corners.
That solid is the associahedron; in general its corners count the triangulations of a polygon.
