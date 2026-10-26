---
tag: 0JWCX0TW2S
kind: definition
name: Concyclic points
msc: [51M04]
defines: 049DCJZ448
uses: [060W5CBZP6, 0V3XAMF3C1, 0NPPGHQNXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Concyclic_points
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Concyclic_points
    locator: Perpendicular bisectors
---

## Definition

Let $S$ be a set of points of the Euclidean space $\mathbb{R}^n$, and let $d$ be the [[Euclidean distance|0NPPGHQNXQ]].
The points of $S$ are concyclic if they lie on one [[circle|060W5CBZP6]]. That is, there are a [[plane|0V3XAMF3C1]] $P$ that contains $S$, a point $c \in P$ and a real number $r \geq 0$ with $d(x, c) = r$ for each $x \in S$.

## Remarks

Three points that are not collinear are always concyclic. Thus each triangle has a circumcircle.
Four or more points of the plane are not concyclic in general. Four concyclic points are the vertices of a cyclic quadrilateral.
The centre $c$ is on the perpendicular bisector of each two distinct points of $S$.
Mathlib's `EuclideanGeometry.Concyclic` asks for points that are cospherical and coplanar. This is the same condition.

## Explanations

### L1 human

Concyclic points are points on one common circle. The four corners of a rectangle are concyclic: the circle has its centre at the crossing of the diagonals. The four points $(0, 0)$, $(1, 0)$, $(2, 0)$ and $(0, 1)$ are not concyclic, because a circle meets a line in at most two points.
