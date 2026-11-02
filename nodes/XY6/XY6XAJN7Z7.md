---
tag: XY6XAJN7Z7
kind: definition
name: Cospherical points
msc: [51M04, 51M05]
defines: HYVFPWS9ER
uses: [P9CM4GQ2T0, 0VKD1TP7F3]
sources:
  - url: https://en.wikipedia.org/wiki/Concyclic_points
---

## Definition

Let $(X, d)$ be a [[metric space|0VKD1TP7F3]] and let $S \subseteq X$ be a set of points.
The set $S$ is *cospherical* if there are a point $c \in X$ and a real number $r$ such that $d(x, c) = r$ for every $x \in S$.
That is, $S$ is contained in the [[sphere|P9CM4GQ2T0]] with centre $c$ and radius $r$.

## Remarks

This is the form of Mathlib's `EuclideanGeometry.Cospherical`.
In the Euclidean plane, cospherical points are the same as [[concyclic points|049DCJZ448]].
In $\R^n$, any $n + 1$ affinely independent points are cospherical, and their sphere is the [[circumsphere|MRC4WMVTAH]] of the simplex they span.

Example: the eight vertices $(\pm 1, \pm 1, \pm 1)$ of a cube in $\R^3$ are cospherical.
Each lies at distance $\sqrt 3$ from $c = (0, 0, 0)$.

Non-example: the points $(0, 0)$, $(1, 0)$, $(2, 0)$ of $\R^2$ are not cospherical.
A point equidistant from the first two has $x$-coordinate $1/2$, and a point equidistant from the last two has $x$-coordinate $3/2$, so no centre exists.
