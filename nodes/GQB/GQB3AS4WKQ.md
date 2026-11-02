---
tag: GQB3AS4WKQ
kind: definition
name: Honeycomb
msc: [52C22, 51M20, 05B45]
defines: HTJ03RFKFH
uses: [GKJK293DXS, 300K6CB1KH, 0325SGSJAR]
sources:
  - url: https://en.wikipedia.org/wiki/Honeycomb_(geometry)
---

## Definition

Let $n \ge 3$.
A *honeycomb* in $\R^n$ is a [[tiling|GKJK293DXS]] of $\R^n$ whose tiles, called *cells*, are $n$-dimensional [[convex polytopes|300K6CB1KH]].
In dimension $3$ the cells are convex [[polyhedra|0325SGSJAR]].

## Remarks

Example: the cubes $[a, a+1] \times [b, b+1] \times [c, c+1]$ with $a, b, c \in \Z$ form the *cubic honeycomb* in $\R^3$.
The cubes are convex polyhedra, every point $(x, y, z)$ lies in the cube with $(a, b, c) = (\floor{x}, \floor{y}, \floor{z})$, and distinct cubes have disjoint interiors.

Non-example: copies of a regular tetrahedron cannot form a honeycomb in $\R^3$.
Take a generic point $p$ on an edge of one cell.
The cells through $p$ each fill either a wedge with the dihedral angle $\alpha = \arccos(1/3)$ or a half-space, and these angles add up to $2\pi$.
So $k \alpha = 2\pi$ or $k \alpha = \pi$ for some integer $k \ge 1$.
Both fail, since $\alpha \approx 70.53^\circ$ and neither $360^\circ$ nor $180^\circ$ is an integer multiple of it.

Many authors also require the honeycomb to be face-to-face, so that two cells meet in a common face of both or not at all.
The term is also used for tilings of hyperbolic space and of spheres by polytopes.
