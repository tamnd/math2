---
tag: YES06WTNRZ
kind: definition
name: Schläfli symbol
msc: [51M20, 52B15]
defines: MAE6BF4DFK
uses: [F60PD912D5, 01KJJ9A400, DPDXN2FJC4, KY7SB854VH]
sources:
  - url: https://en.wikipedia.org/wiki/Schl%C3%A4fli_symbol
---

## Definition

The *Schläfli symbol* of a convex [[regular polytope|F60PD912D5]] $P$ of dimension $d \ge 2$ is defined by induction on $d$.

1. If $d = 2$, then $P$ is a [[regular polygon|01KJJ9A400]] with $p$ sides for some $p \ge 3$, and its symbol is $\set{p}$.
2. If $d \ge 3$, then all [[facets|DPDXN2FJC4]] of $P$ are congruent regular polytopes of dimension $d-1$, with a common symbol $\set{p_1, \dots, p_{d-2}}$.
Let $p_{d-1}$ be the number of facets of $P$ that contain a given [[face|KY7SB854VH]] of dimension $d-3$.
By regularity it does not depend on the face.
The symbol of $P$ is $\set{p_1, \dots, p_{d-2}, p_{d-1}}$.

## Remarks

Example: the cube has square facets, with symbol $\set{4}$, and exactly $3$ facets contain each vertex, so its symbol is $\set{4, 3}$.
The tesseract has cubes as facets and $3$ cubes around each edge, so its symbol is $\set{4, 3, 3}$.
The regular $d$-simplex has symbol $\set{3, 3, \dots, 3}$ with $d-1$ entries.

Non-example: the string $\set{6, 3}$ is not the symbol of a convex polyhedron.
Three regular hexagons at a vertex have angles summing to $3 \cdot 120^\circ = 360^\circ$, so they lie flat, and the pattern gives the hexagonal tiling of the plane instead of a polytope.

If $P$ has symbol $\set{p_1, \dots, p_{d-1}}$, its vertex figure has symbol $\set{p_2, \dots, p_{d-1}}$, and its dual polytope has symbol $\set{p_{d-1}, \dots, p_1}$.
The same notation is used for regular tilings, such as $\set{4, 4}$ for the square tiling, and for star polytopes with fractional entries, such as $\set{5/2}$ for the pentagram.
