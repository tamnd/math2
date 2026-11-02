---
tag: 6WVTB9Y3XD
kind: definition
name: Kähler–Einstein metric
msc: [32Q20, 53C55, 53C25]
defines: 6ETEBA8827
uses: [CK1DCPC3D3, 4GTNM0WHDH, 41S2EZ0KR3]
sources:
  - url: https://en.wikipedia.org/wiki/K%C3%A4hler%E2%80%93Einstein_metric
---

## Definition

Let $(M, J)$ be a complex manifold and let $g$ be a Kähler metric on $M$.
Thus $g$ is a [[Hermitian metric|CK1DCPC3D3]] whose fundamental form $\omega$ is closed.
Let $\operatorname{Ric}$ be the [[Ricci curvature|4GTNM0WHDH]] of $g$, and let $\rho(X, Y) = \operatorname{Ric}(JX, Y)$ be its Ricci form.
The metric $g$ is *Kähler–Einstein* if there is a real constant $\lambda$ such that $\operatorname{Ric} = \lambda g$, or equivalently $\rho = \lambda \omega$.

## Remarks

Example: the flat metric on a complex torus $\C^n / \Lambda$, for a lattice $\Lambda$ of rank $2n$.
It is Kähler with constant coefficients, its curvature vanishes, and so $\operatorname{Ric} = 0 = 0 \cdot g$.
The Fubini–Study metric on $\C P^n$ is Kähler–Einstein with $\lambda > 0$, and the Bergman metric on the unit ball of $\C^n$ is Kähler–Einstein with $\lambda < 0$.

Non-example: on $\C P^1 \times \Sigma$, with $\Sigma$ a compact Riemann surface of genus $2$, take the product of a round metric of curvature $1$ and a metric of curvature $-1$.
It is Kähler, but $\operatorname{Ric}$ equals $g$ on the first factor and $-g$ on the second, so no single $\lambda$ works.

On a compact Kähler manifold the Ricci form represents $2\pi c_1(M)$ in de Rham cohomology.
So a Kähler–Einstein metric with constant $\lambda$ forces $2\pi c_1(M) = \lambda [\omega]$: the first Chern class is negative, zero or positive according to the sign of $\lambda$.
A Kähler–Einstein metric is an [[Einstein metric|41S2EZ0KR3]] in the Riemannian sense.
