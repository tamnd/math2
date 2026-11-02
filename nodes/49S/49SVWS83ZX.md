---
tag: 49SVWS83ZX
kind: definition
name: Sectional curvature
msc: [53B20, 53C20]
defines: 1X42JAA349
uses: [7CBT4SM83Y, JA29ETCM02]
sources:
  - url: https://en.wikipedia.org/wiki/Sectional_curvature
---

## Definition

Let $(M, g)$ be a [[Riemannian manifold|7CBT4SM83Y]] with curvature $R(X, Y)Z = \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z - \nabla_{[X, Y]} Z$ (see [[Riemann curvature tensor|JA29ETCM02]]).
Let $p \in M$ and let $\sigma \subseteq T_pM$ be a $2$-dimensional linear subspace, spanned by $u, v$.
The *sectional curvature* of $\sigma$ is
$$K(\sigma) = K(u, v) = \frac{g\bigl(R(u, v)v, u\bigr)}{g(u, u) \, g(v, v) - g(u, v)^2}.$$

## Remarks

The value does not depend on the choice of basis $u, v$ of $\sigma$, because numerator and denominator both change by the square of the determinant of the change of basis.

Example: on the unit sphere $S^n$, $R(X, Y)Z = g(Y, Z)X - g(X, Z)Y$, so for orthonormal $u, v$ the numerator is $g(g(v, v)u - g(u, v)v, u) = 1$ and $K(\sigma) = 1$ for every plane.

Non-example: $K(u, v)$ is not defined when $u$ and $v$ are linearly dependent, since then they span no plane and the denominator is $0$.

For a surface, the only plane at $p$ is $T_pM$, and $K$ is the [[Gaussian curvature|SQVQ5DQT6W]].
A manifold has constant sectional curvature $k$ if and only if $R(X, Y)Z = k\bigl(g(Y, Z)X - g(X, Z)Y\bigr)$.
With the opposite sign convention for $R$, the numerator is written $g(R(u, v)u, v)$.
