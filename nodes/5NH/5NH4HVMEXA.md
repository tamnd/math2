---
tag: 5NH4HVMEXA
kind: definition
name: Polygon triangulation
msc: [68U05, 52C45]
defines: Q6KKBP3RRP
uses: [0CTNFGYMM2, VQ4Q2V45RP]
sources:
  - url: https://en.wikipedia.org/wiki/Polygon_triangulation
---

## Definition

Let $P \subset \R^2$ be a simple polygon, that is, a closed region bounded by a closed polygonal chain with $n \ge 3$ vertices that does not cross itself.
A *triangulation* of $P$ is a finite set $T$ of [[triangles|0CTNFGYMM2]] such that:

1. the union of the triangles of $T$ is $P$;
2. the vertices of each triangle of $T$ are vertices of $P$;
3. any two distinct triangles of $T$ meet in the empty set, in one common vertex, or in one common side.

Equivalently, a triangulation is given by a maximal set of diagonals of $P$ that pairwise meet only at endpoints.
A diagonal is a [[line segment|VQ4Q2V45RP]] joining two vertices of $P$ that lies in $P$ and meets the boundary of $P$ only at its endpoints.

## Remarks

Example: let $P$ be the square with vertices $(0,0)$, $(1,0)$, $(1,1)$, $(0,1)$.
The diagonal from $(0,0)$ to $(1,1)$ splits it into two triangles.
Their union is $P$, their vertices are vertices of $P$, and they meet in a common side, so all three clauses hold.

Non-example: split the same square into four triangles by joining the centre $(1/2, 1/2)$ to the four corners.
Clauses 1 and 3 hold, but clause 2 fails, since the centre is not a vertex of $P$.

Every simple polygon with $n$ vertices has a triangulation, and every triangulation has $n - 2$ triangles and $n - 3$ diagonals.
A convex polygon with $n$ vertices has exactly $C_{n-2}$ triangulations, where $C_m = \frac{1}{m+1}\binom{2m}{m}$ is the $m$-th Catalan number.
