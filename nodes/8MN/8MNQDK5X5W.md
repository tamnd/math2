---
tag: 8MNQDK5X5W
kind: object
name: 600-cell
msc: [51M20, 52B15, 52B11]
instance_of: [F60PD912D5]
uses: [MAE6BF4DFK, 0SC8T7548D]
sources:
  - url: https://en.wikipedia.org/wiki/600-cell
same_as:
  wikidata: Q2610844
  wikipedia: 600-cell
---

## Description

The *600-cell* is the convex [[regular polytope|F60PD912D5]] in $\R^4$ with [[Schläfli symbol|MAE6BF4DFK]] $\set{3, 3, 5}$.
Its cells are $600$ regular tetrahedra, five around each edge, and its vertex figure is a regular icosahedron.
It has $120$ vertices, $720$ edges, $1200$ triangular faces and $600$ cells.

A model: let $\varphi = (1 + \sqrt5)/2$ be the [[golden ratio|0SC8T7548D]].
Take the $8$ points obtained from $(\pm1, 0, 0, 0)$ by permuting coordinates, and the $16$ points $\frac12(\pm1, \pm1, \pm1, \pm1)$.
Add the $96$ points obtained from $\frac12(\pm\varphi, \pm1, \pm\varphi^{-1}, 0)$ by even permutations of the coordinates.
These $8 + 16 + 96 = 120$ points lie on the unit sphere, and their convex hull is a 600-cell with edge length $\varphi^{-1}$.

Check of the counts: the icosahedral vertex figure has $12$ vertices, so each vertex lies on $12$ edges and there are $120 \cdot 12 / 2 = 720$ edges.
Each tetrahedron has $4$ triangles, each lying in $2$ cells, so $600 \cdot 4 / 2 = 1200$ faces.
Then $120 - 720 + 1200 - 600 = 0$.

## Remarks

The 600-cell is the dual of the [[120-cell|3RQEK50CP0]], and its symmetry group is the reflection group $H_4$ of order $14400$.
Read as unit quaternions, the $120$ vertices of the model above form a group under multiplication, the binary icosahedral group.
It is the four-dimensional analogue of the icosahedron $\set{3, 5}$.

## Explanations

### L1 human

The 600-cell is a four-dimensional solid made of $600$ regular tetrahedra, with $120$ corners.
Around each corner the tetrahedra are arranged like the triangles of an icosahedron.
It is the four-dimensional cousin of the icosahedron, and its corners have coordinates built from the golden ratio.
