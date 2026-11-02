---
tag: SH9NBM8JRR
kind: object
name: 24-cell
msc: [51M20, 52B15, 52B11]
instance_of: [F60PD912D5]
uses: [MAE6BF4DFK, QHTAEPTKEB]
sources:
  - url: https://en.wikipedia.org/wiki/24-cell
same_as:
  wikidata: Q539008
  wikipedia: 24-cell
---

## Description

The *24-cell* is the convex polytope in $\R^4$ whose vertices are the $24$ points obtained from $(\pm 1, \pm 1, 0, 0)$ by permuting the coordinates.
It is a convex [[regular polytope|F60PD912D5]] with [[Schläfli symbol|MAE6BF4DFK]] $\set{3, 4, 3}$.
It has $24$ vertices, $96$ edges, $96$ triangular faces and $24$ cells, which are regular octahedra.

Check of the vertex and edge counts: there are $\binom{4}{2} = 6$ ways to place the two nonzero coordinates and $4$ choices of signs, so $24$ vertices.
All vertices lie at distance $\sqrt2$ from the origin.
The nearest neighbours of $(1,1,0,0)$ are the $8$ points $(1,0,\pm1,0)$, $(1,0,0,\pm1)$, $(0,1,\pm1,0)$, $(0,1,0,\pm1)$, at distance $\sqrt2$.
So each vertex lies on $8$ edges, and there are $24 \cdot 8 / 2 = 96$ edges.
The Euler characteristic check $24 - 96 + 96 - 24 = 0$ holds, as for every convex $4$-polytope.

## Remarks

The vertex figure is a cube, in agreement with the symbol: the last two entries $\set{4, 3}$ are the symbol of the cube.
The symbol reads the same backwards, and indeed the 24-cell is self-dual.
Apart from polygons and simplices, it is the only self-dual convex regular polytope, and it has no analogue in other dimensions.
Its symmetry group has order $1152$.
Another model: the $24$ units $\pm 1$, $\pm i$, $\pm j$, $\pm k$ and $\frac12(\pm 1 \pm i \pm j \pm k)$ of the [[Hurwitz quaternions|QHTAEPTKEB]] are the vertices of a 24-cell.

## Explanations

### L1 human

The 24-cell is a four-dimensional solid built from $24$ octahedra, glued so that each triangle is shared by two of them.
It is one of the six perfectly regular solids of four-dimensional space.
Unlike the other five, it is its own dual and it has no cousin among the regular solids of three or five dimensions.
