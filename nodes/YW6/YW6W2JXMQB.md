---
tag: YW6W2JXMQB
kind: definition
name: Jacobi field
msc: [53C22, 53C20]
defines: 9AHMM41PJ3
uses: [7CBT4SM83Y, NSYMQMHPDN, 5FZDQQHQKM, JA29ETCM02]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobi_field
---

## Definition

Let $(M, g)$ be a [[Riemannian manifold|7CBT4SM83Y]] with Levi-Civita connection $\nabla$ and curvature $R(X, Y)Z = \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z - \nabla_{[X, Y]} Z$, see [[Riemann curvature tensor|JA29ETCM02]].
Let $\gamma \colon I \to M$ be a [[geodesic|NSYMQMHPDN]], and let $D_t$ be the [[covariant derivative|5FZDQQHQKM]] along $\gamma$.
A smooth vector field $J$ along $\gamma$ is a *Jacobi field* if
$$D_t^2 J + R(J, \gamma')\gamma' = 0 \quad \text{on } I.$$

## Remarks

Example: on the unit sphere $S^2$, let $\gamma$ be a unit-speed geodesic and $E$ a parallel unit field along $\gamma$ orthogonal to $\gamma'$.
For $J = \sin(t) E$, one has $D_t^2 J = -\sin(t) E$ and, since the curvature is $1$, $R(J, \gamma')\gamma' = \sin(t) E$; the sum is $0$, so $J$ is a Jacobi field.

Non-example: on the same sphere, $J = tE$ has $D_t^2 J = 0$ but $R(J, \gamma')\gamma' = tE \ne 0$ for $t \ne 0$, so $J$ is not a Jacobi field, although it is one in the flat plane.

If $\Gamma(s, t)$ is a smooth family of geodesics $t \mapsto \Gamma(s, t)$, then $J(t) = \partial_s \Gamma(0, t)$ is a Jacobi field, and every Jacobi field along a geodesic on a compact interval arises in this way.
A Jacobi field is determined by $J(t_0)$ and $D_t J(t_0)$ at one time, so the Jacobi fields along $\gamma$ form a vector space of dimension $2n$, where $n = \dim M$.
The fields $\gamma'$ and $t \gamma'$ are always Jacobi fields; the interesting ones are normal to $\gamma$.
With the opposite sign convention for $R$, the equation reads $D_t^2 J + R(\gamma', J)\gamma' = 0$.
