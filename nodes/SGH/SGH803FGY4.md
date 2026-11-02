---
tag: SGH803FGY4
kind: definition
name: Delaunay triangulation
msc: [52C99, 68U05]
defines: 259Y10BYJC
uses: [V0B6C6TMWD, 03VZJE6C8C, QDNEBBVZ84]
sources:
  - url: https://en.wikipedia.org/wiki/Delaunay_triangulation
---

## Definition

Let $P$ be a finite set of points in $\R^2$, not all collinear.
For a triangle $\Delta$, its *circumdisk* is the open disk bounded by the [[circumcircle|03VZJE6C8C]] of $\Delta$.
A [[triangulation|V0B6C6TMWD]] $T$ of $P$ is a *Delaunay triangulation* if no point of $P$ lies in the circumdisk of any triangle of $T$.

## Remarks

Example: let $P = \set{(0,0), (2,0), (1,2)}$, a single triangle.
Its only triangulation is the triangle itself, and the open circumdisk contains no point of $P$, since the three points lie on the circle.

Non-example: let $P = \set{(-2, 0), (2, 0), (0, 1), (0, -1)}$ and take the triangulation by the diagonal from $(-2, 0)$ to $(2, 0)$.
The circumcircle of $(-2, 0), (2, 0), (0, 1)$ has centre $(0, -3/2)$ and radius $5/2$, and $(0, -1)$ is at distance $1/2$ from the centre, so it lies inside.
The other diagonal, from $(0, 1)$ to $(0, -1)$, gives the Delaunay triangulation.

A Delaunay triangulation of $P$ always exists, and it is unique when no four points of $P$ lie on a common circle.
Among all triangulations of $P$, a Delaunay triangulation maximizes the smallest angle of its triangles.
When no four points are concyclic, two points of $P$ are joined by an edge exactly when their cells in the [[Voronoi diagram|QDNEBBVZ84]] share an edge.
