---
tag: XYCD53PB5K
kind: statement
role: theorem
name: Classification of regular polytopes
msc: [51M20, 52B15]
uses: [F60PD912D5, MAE6BF4DFK, 01KJJ9A400, 017E5PRS1Q]
about: [F60PD912D5]
sources:
  - url: https://en.wikipedia.org/wiki/List_of_regular_polytopes
---

## Statement

Up to similarity, the convex [[regular polytopes|F60PD912D5]] of dimension $d$ are exactly the following, listed by their [[Schläfli symbols|MAE6BF4DFK]].

1. For $d = 2$: the [[regular polygon|01KJJ9A400]] $\set{p}$ for each integer $p \ge 3$.
2. For $d = 3$: the five [[Platonic solids|017E5PRS1Q]] $\set{3,3}$, $\set{4,3}$, $\set{3,4}$, $\set{5,3}$ and $\set{3,5}$.
3. For $d = 4$: six polytopes, the $5$-cell $\set{3,3,3}$, the tesseract $\set{4,3,3}$, the $16$-cell $\set{3,3,4}$, the [[24-cell|SH9NBM8JRR]] $\set{3,4,3}$, the [[120-cell|3RQEK50CP0]] $\set{5,3,3}$ and the [[600-cell|8MNQDK5X5W]] $\set{3,3,5}$.
4. For $d \ge 5$: three polytopes, the regular simplex $\set{3, \dots, 3}$, the [[hypercube|P9PYM71GMM]] $\set{4, 3, \dots, 3}$ and the [[cross-polytope|5DYYRZWER6]] $\set{3, \dots, 3, 4}$, each symbol having $d-1$ entries.

## Remarks

The facets and the vertex figures of a regular polytope are regular, so the possible symbols are built from shorter ones that are already known.
The new condition at each step is an angle condition: the facets around a face of dimension $d-3$ must have dihedral angles that add up to less than $2\pi$.
In dimension $3$ this gives $(p-2)(q-2) < 4$, which leaves the five Platonic symbols, as in the [[classification of the Platonic solids|0M4TCS0RRG]].
Each surviving symbol is then realised by an explicit construction, and the symbol determines the polytope up to similarity.

Example: the regular dodecahedron $\set{5,3}$ has dihedral angle $\arccos(-1/\sqrt5) \approx 116.57^\circ$.
Three dodecahedra around an edge use about $349.7^\circ < 360^\circ$, so $\set{5,3,3}$ is allowed, and it is the $120$-cell.
Four would use more than $360^\circ$, so there is no $\set{5,3,4}$.
For the cube, four around an edge use exactly $360^\circ$, so $\set{4,3,4}$ gives the cubic [[honeycomb|HTJ03RFKFH]] of space and not a polytope.

Convexity is needed for the list: allowing star polytopes adds the four [[Kepler–Poinsot polyhedra|CKQRZVBGTS]] in dimension $3$ and ten regular star polytopes in dimension $4$.

## Explanations

### L1 human

There are infinitely many regular polygons, one for each number of sides.
In three dimensions there are only five regular solids, and in four dimensions there are six.
From dimension five on, only three remain: the higher versions of the tetrahedron, the cube and the octahedron.
So the most symmetric shapes become rarer, not more common, as the dimension grows.

### L2 human

The theorem is proved by combining the [[Schläfli symbol|MAE6BF4DFK]] with an angle count, and dimension four is special because the dodecahedron and icosahedron still fit in.
The six four-dimensional polytopes include three without analogues elsewhere: the $24$-cell, which is self-dual, and the dual pair of the $120$-cell and the $600$-cell.
The symmetry groups of the regular polytopes are finite reflection groups: the dihedral groups and the types $A_d$, $B_d$, $F_4$, $H_3$ and $H_4$.
So the classification is tied to the classification of finite [[Coxeter groups|G6FND7X69J]].
