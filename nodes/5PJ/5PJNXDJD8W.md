---
tag: 5PJNXDJD8W
kind: definition
name: Pseudoholomorphic curve
msc: [32Q65, 53D35]
defines: N469E47V75
uses: [9SYWRGVTRS, 5K0N8QMV6Q]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudoholomorphic_curve
---

## Definition

Let $(M, J)$ be an [[almost complex manifold|9SYWRGVTRS]], so $J$ is a smooth endomorphism of $TM$ with $J^2 = -\id$.
Let $(\Sigma, j)$ be a [[Riemann surface|5K0N8QMV6Q]], with $j$ its complex structure on $T\Sigma$.
A *pseudoholomorphic curve* (or *$J$-holomorphic curve*) is a smooth map $u \colon \Sigma \to M$ such that
$$du \circ j = J \circ du.$$

## Remarks

In a local coordinate $z = s + it$ on $\Sigma$, the condition reads $\partial_s u + J(u) \, \partial_t u = 0$, a nonlinear Cauchy–Riemann equation.

Example: let $M = \C^n$ with $J$ the multiplication by $i$, and $\Sigma$ an open subset of $\C$.
Then $u$ is pseudoholomorphic exactly when each component is a holomorphic function, by the Cauchy–Riemann equations.
So $u(z) = (z, z^2)$ is a pseudoholomorphic curve in $\C^2$.

Non-example: $u(z) = \bar z$ from $\C$ to $\C$.
With $z = s + it$ and target coordinate $x + iy$, one has $du(j \partial_s) = du(\partial_t) = -\partial_y$, while $J\,du(\partial_s) = J \partial_x = \partial_y$.
So $du \circ j = -J \circ du \ne J \circ du$; the map is antiholomorphic.

If $J$ is tamed by a symplectic form $\omega$, meaning $\omega(v, Jv) > 0$ for $v \ne 0$, then the energy $\int_\Sigma u^* \omega$ of a nonconstant pseudoholomorphic curve is positive.
When $\Sigma$ is closed and $\omega$ is closed, this energy depends only on the homology class of $u$.
