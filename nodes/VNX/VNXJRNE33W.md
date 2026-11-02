---
tag: VNXJRNE33W
kind: definition
name: Conjugate points
msc: [53C22]
defines: ZPXE5VSZ35
uses: [7CBT4SM83Y, NSYMQMHPDN, 9AHMM41PJ3]
sources:
  - url: https://en.wikipedia.org/wiki/Conjugate_points
---

## Definition

Let $(M, g)$ be a [[Riemannian manifold|7CBT4SM83Y]], let $\gamma \colon [a, b] \to M$ be a [[geodesic|NSYMQMHPDN]], and let $t_1 < t_2$ in $[a, b]$.
The points $\gamma(t_1)$ and $\gamma(t_2)$ are *conjugate along* $\gamma$ if there is a [[Jacobi field|9AHMM41PJ3]] $J$ along $\gamma$, not identically zero, with $J(t_1) = 0$ and $J(t_2) = 0$.
The *multiplicity* of the pair is the dimension of the space of such Jacobi fields.

## Remarks

Example: on the unit sphere $S^n$, let $\gamma(t)$ be a unit-speed great circle and $E$ a parallel unit field normal to $\gamma'$.
The Jacobi field $J = \sin(t) E$ vanishes at $t = 0$ and $t = \pi$, so $\gamma(0)$ and $\gamma(\pi)$, which are antipodal, are conjugate; there are $n - 1$ independent choices of $E$, so the multiplicity is $n - 1$.

Non-example: in $\R^n$ with the Euclidean metric, the Jacobi fields along $\gamma(t) = p + tv$ are $J(t) = A + tB$ with constant vectors $A, B$.
Such a field vanishing at two times is zero, so no two points are conjugate.

Equivalently, with $p = \gamma(0)$ and $\gamma(t) = \exp_p(tv)$, the point $\gamma(t_2)$ is conjugate to $p$ along $\gamma$ if and only if the differential of the [[exponential map|Y7Z0AGY1A7]] $\exp_p$ is singular at $t_2 v$.
The multiplicity is at most $n - 1$, where $n = \dim M$.
