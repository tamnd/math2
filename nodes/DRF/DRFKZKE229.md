---
tag: DRFKZKE229
kind: definition
name: Regular surface
msc: [53A05]
defines: 6080X3FAD4
uses: [05788J51WZ, 0BE3QDH73A, 05GZ11PWRY, 01ZQQDCERP, 0YF0VXKXGB]
sources:
  - url: https://en.wikipedia.org/wiki/Differential_geometry_of_surfaces
---

## Definition

Let $S \subseteq \R^3$ be a subset.
The set $S$ is a *regular surface* if each $p \in S$ has the following property.
There are an [[open set|01ZQQDCERP]] $V \subseteq \R^3$ containing $p$, an open set $U \subseteq \R^2$, and a map $x \colon U \to V \cap S$ such that:

1. The map $x$ is [[smooth|0BE3QDH73A]] as a map from $U$ to $\R^3$.
2. The map $x$ is a [[homeomorphism|05GZ11PWRY]] from $U$ onto $V \cap S$, with the subspace topology on $V \cap S$.
3. For each $q \in U$, the [[Jacobian matrix|0YF0VXKXGB]] of $x$ at $q$ has rank $2$, that is, $x_u(q)$ and $x_v(q)$ are linearly independent.

Such a map $x$ is a *local parametrisation* of $S$ at $p$.

## Remarks

Example: the unit sphere is a regular surface.
At points with $z > 0$, the map $x(u, v) = (u, v, \sqrt{1 - u^2 - v^2})$ on the open unit disc satisfies the three clauses, and five similar maps cover the rest.
More generally, if $f \colon \R^3 \to \R$ is smooth and $\nabla f \ne 0$ on $f^{-1}(c)$, then the level set $f^{-1}(c)$, when nonempty, is a regular surface.
Non-example: the double cone $x^2 + y^2 = z^2$ fails clause 2 at the origin.
Indeed, removing the origin from a small neighbourhood of it in the cone leaves two pieces, while a punctured disc is connected.
Each local parametrisation is a regular [[parametrised surface|05788J51WZ]] in the sense of a map, but a regular surface is a set, covered by such maps.
