---
tag: KZ00AZ2HFM
kind: definition
name: CAT(k) space
msc: [53C23, 51F99]
defines: 1FAF2VNA4G
uses: [0VKD1TP7F3, 0CTNFGYMM2, 0XPR1E85W0]
sources:
  - url: https://en.wikipedia.org/wiki/CAT(k)_space
---

## Definition

Let $k$ be a real number.
Let $M_k$ be the complete simply connected surface of constant curvature $k$.
It is the round sphere of radius $1/\sqrt{k}$ if $k > 0$, the [[Euclidean plane|0XPR1E85W0]] if $k = 0$, and the hyperbolic plane of curvature $k$ if $k < 0$.
Let $D_k = \pi/\sqrt{k}$ if $k > 0$ and $D_k = \infty$ if $k \le 0$.

Let $(X, d)$ be a [[metric space|0VKD1TP7F3]].
A *geodesic segment* in $X$ is a map $c \colon [0, \ell] \to X$ with $d(c(s), c(t)) = \abs{s - t}$ for all $s, t$.
A *geodesic triangle* consists of three points of $X$ and a geodesic segment between each pair of them.
A *comparison triangle* for it is a [[triangle|0CTNFGYMM2]] in $M_k$ with the same three side lengths.
Each point $p$ on a side has a comparison point $\bar p$ on the matching side, at the same distances from the ends.

The space $X$ is a *CAT($k$) space* if:

1. any two points of $X$ at distance less than $D_k$ are joined by a geodesic segment, and
2. for every geodesic triangle of perimeter less than $2 D_k$ and all points $p, q$ on its sides, $d(p, q) \le d_{M_k}(\bar p, \bar q)$.

## Remarks

Example: $\R^n$ with the Euclidean distance is CAT(0).
Its geodesic triangles are flat triangles, and a comparison triangle in $M_0$ is congruent to it, so equality holds in clause 2.

Non-example: the unit round sphere $S^2$ is not CAT(0).
Take the triangle with vertices on the equator at longitudes $0$, $\pi/2$ and the north pole; its sides have length $\pi/2$.
The midpoints of the two sides through the pole are at spherical distance $\pi/3$.
The comparison triangle in $M_0$ is equilateral with side $\pi/2$, so the comparison points are at distance $\pi/4 < \pi/3$.
So clause 2 fails; the sphere is CAT(1).

A CAT($k$) space is also CAT($k'$) for every $k' \ge k$.
A complete simply connected Riemannian manifold is CAT($k$) for some $k \le 0$ exactly when its [[sectional curvature|1X42JAA349]] is at most $k$.
Metric trees are CAT($k$) for every $k$.
