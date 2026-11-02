---
tag: PBYCBVG5CG
kind: definition
name: Simple polytope
msc: [52B05, 52B11, 52B12]
defines: 7E6FXTGH2Y
uses: [300K6CB1KH, R7V3S9V891, DPDXN2FJC4]
sources:
  - url: https://en.wikipedia.org/wiki/Simple_polytope
---

## Definition

Let $P$ be a [[convex polytope|300K6CB1KH]] of dimension $d \ge 1$.
An edge of $P$ is a face of dimension $1$.
$P$ is *simple* if every [[vertex|R7V3S9V891]] of $P$ lies in exactly $d$ edges of $P$.

## Remarks

Equivalently, every vertex of $P$ lies in exactly $d$ [[facets|DPDXN2FJC4]] of $P$.
Every vertex of a $d$-polytope lies in at least $d$ edges, so simple polytopes are those where this lower bound is always reached.

Example: the cube $[0,1]^3$ is simple.
At the vertex $0$ the edges are the three segments from $0$ to $e_1$, $e_2$ and $e_3$, and by symmetry every vertex lies in $3$ edges.

Non-example: the octahedron $\operatorname{conv}\set{\pm e_1, \pm e_2, \pm e_3}$ is not simple, since the vertex $e_1$ lies in the $4$ edges joining it to $\pm e_2$ and $\pm e_3$.

If $P$ contains the origin in its interior, then $P$ is simple if and only if its polar polytope is simplicial.
Every polygon is simple.
