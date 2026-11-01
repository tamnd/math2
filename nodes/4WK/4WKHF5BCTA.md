---
tag: 4WKHF5BCTA
kind: statement
role: theorem
name: Dehn–Sommerville equations
msc: [52B05, "05E45"]
uses: [DCK64GFPD7, V8GZ0W1ZZ5, 879SBTVE7V]
about: [DCK64GFPD7]
sources:
  - url: https://en.wikipedia.org/wiki/Dehn%E2%80%93Sommerville_equations
same_as:
  wikidata: Q4027001
  wikipedia: Dehn–Sommerville equations
---

## Statement

Let $P$ be a simplicial convex polytope of dimension $d \ge 1$, that is, a polytope all of whose proper faces are simplices.
Let $(h_0, h_1, \dots, h_d)$ be the [[h-vector|DCK64GFPD7]] of the boundary complex of $P$.
Then
$$h_i = h_{d-i} \quad \text{for } 0 \le i \le d.$$

## Remarks

One proof uses a shelling of the boundary complex, an order of the facets in which each new facet meets the earlier ones in a union of its own facets.
For each facet, record the size of its smallest new face; then $h_i$ is the number of facets for which this size is $i$.
The reverse of a line shelling is again a shelling, and reversing the order turns size $i$ into size $d - i$, which gives the symmetry.

The equation $h_0 = h_d$ is equivalent to Euler's relation $f_0 - f_1 + f_2 - \dots + (-1)^{d-1} f_{d-1} = 1 - (-1)^d$ for the boundary.
For $d = 3$ the equations give $f_1 = 3 f_0 - 6$ and $f_2 = 2 f_0 - 4$, so the number of vertices determines the whole f-vector of a simplicial $3$-polytope.

Example: the octahedron has $h = (1, 3, 3, 1)$, which is symmetric.

The hypothesis that the complex is the boundary of a polytope (more generally, a sphere) is necessary.
The full triangle, viewed as a simplicial complex of dimension $2$, has $f = (1, 3, 3, 1)$ and $h = (1, 0, 0, 0)$, which is not symmetric.

## Explanations

### L1 human

The face numbers of a polytope with triangular faces are not free: they satisfy linear equations.
In the h-vector form the equations are a simple mirror symmetry.
For example, a convex polyhedron in space made of triangles with $v$ vertices always has $3v - 6$ edges and $2v - 4$ triangles.

### L2 human

The equations hold more generally for simplicial spheres and for Eulerian complexes.
They show that about half of the entries of the f-vector of a simplicial $d$-polytope determine the rest.
The remaining question, which h-vectors occur at all, is answered by the [[g-theorem|4CZMWQVC30]].
