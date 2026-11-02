---
tag: FTM4W0VBC8
kind: definition
name: Hermitian manifold
msc: [53C55, 53B35]
defines: CK1DCPC3D3
uses: [9SYWRGVTRS, VCT848WV1T, Q61VFHCH2J, 0E3G0GRPZ6, 004FRCXH6M, 48P4A1CX85]
sources:
  - url: https://en.wikipedia.org/wiki/Hermitian_manifold
---

## Definition

Let $M$ be a complex manifold, and let $J$ be the integrable [[almost complex structure|9SYWRGVTRS]] given by multiplication by $i$ in holomorphic charts.
A *Hermitian metric* on $M$ is a [[Riemannian metric|Q61VFHCH2J]] $g$ on $M$ such that $g(JX, JY) = g(X, Y)$ for all tangent vectors $X, Y$ at the same point.
A *Hermitian manifold* is a complex manifold with a Hermitian metric.

The *fundamental form* of $g$ is the [[differential $2$-form|0E3G0GRPZ6]] $\omega(X, Y) = g(JX, Y)$.
The metric $g$ is *Kähler* if $d\omega = 0$, where $d$ is the [[exterior derivative|004FRCXH6M]], and then $(M, g)$ is a *Kähler manifold*.

## Remarks

Example: $\C^n = \R^{2n}$ with the Euclidean metric $g_0$ and $J$ the multiplication by $i$.
Multiplication by $i$ is an orthogonal map of $\R^{2n}$, so $g_0(JX, JY) = g_0(X, Y)$.
Its fundamental form is $\omega = \sum_k dx_k \wedge dy_k$, which has constant coefficients, so $d\omega = 0$ and $\C^n$ is Kähler.

Non-example: on $\C = \R^2$ the metric $g = dx^2 + 4\, dy^2$ is Riemannian but not Hermitian.
Here $J\partial_x = \partial_y$, so $g(J\partial_x, J\partial_x) = 4 \ne 1 = g(\partial_x, \partial_x)$.

The form $h = g - i\omega$ is a [[Hermitian form|48P4A1CX85]] on each tangent space viewed as a complex vector space.
Every complex manifold has Hermitian metrics: given any Riemannian metric $g$, the metric $g(X, Y) + g(JX, JY)$ is Hermitian.
The same definition with an almost complex structure that need not be integrable gives *almost Hermitian manifolds*; by the [[Newlander–Nirenberg theorem|VCT848WV1T]] the integrable case is the complex case.
Every complex submanifold of a Kähler manifold is Kähler with the induced metric.
