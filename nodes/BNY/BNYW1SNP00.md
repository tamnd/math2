---
tag: BNYW1SNP00
kind: definition
name: Hyperbolic 3-manifold
msc: [57K32]
defines: GHVW1Z35BS
uses: [R20TB2KEQQ, 7CBT4SM83Y, 1X42JAA349]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperbolic_3-manifold
---

## Definition

A *hyperbolic $3$-manifold* is a connected [[3-manifold|R20TB2KEQQ]] $M$ with a [[Riemannian metric|7CBT4SM83Y]] $g$ such that:

1. $(M, g)$ is complete as a metric space, and
2. every [[sectional curvature|1X42JAA349]] of $g$ is equal to $-1$.

## Remarks

Example: hyperbolic $3$-space $\mathbb{H}^3 = \set{(x, y, t) \in \R^3 : t > 0}$ with the metric $(dx^2 + dy^2 + dt^2)/t^2$ is complete and has constant sectional curvature $-1$.
More generally, if $\Gamma$ is a discrete group of isometries of $\mathbb{H}^3$ acting freely, then $\mathbb{H}^3 / \Gamma$ with the quotient metric is a hyperbolic $3$-manifold.

Non-example: the open subset $\mathbb{H}^3 \setminus \set{p}$, for a point $p$, has curvature $-1$, but it is not complete, since a geodesic heading to $p$ stops after finite length.

By the Killing–Hopf theorem, every hyperbolic $3$-manifold is isometric to some $\mathbb{H}^3 / \Gamma$ as above.
It is orientable exactly when $\Gamma$ lies in the group of orientation-preserving isometries, which is isomorphic to $PSL(2, \C)$.
