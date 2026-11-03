---
tag: BWS2PMSA3N
kind: definition
name: Robin boundary condition for convective cooling
msc: [80A19, 35Q79]
defines: XE02D2KD21
uses: [581AGFCCRX, 9YJZ1PP2Y8, J821AD6YTE, XBQBT9E7JT, 0WQJJCCTC8]
sources:
  - url: https://en.wikipedia.org/wiki/Robin_boundary_condition
---

## Definition

Let a body occupy a bounded open set $\Omega \subseteq \R^3$ with $C^1$ boundary $\partial \Omega$ and outward unit [[normal|0WQJJCCTC8]] $\nu$.
Let $k > 0$ be its [[thermal conductivity|XBQBT9E7JT]], and let $T$ be its temperature, continuously differentiable up to $\partial \Omega$.
Let the body be surrounded by a fluid at temperature $T_\infty$, with [[heat transfer coefficient|J821AD6YTE]] $h > 0$.
The *convective boundary condition* is the [[Robin condition|581AGFCCRX]]
$$-k \, \frac{\partial T}{\partial \nu} = h \left(T - T_\infty\right) \quad \text{on } \partial \Omega.$$

## Remarks

The left side is the outward normal component of the conductive flux from [[Fourier's law|9YJZ1PP2Y8]].
The right side is the flux carried away by the fluid.

Example: a slab $0 < x < L$ with $T(0) = T_0$ and the convective condition at $x = L$, in steady state.
Then $T(x) = T_0 - q x / k$ with $q = (T_0 - T_\infty) / (L / k + 1 / h)$.
Check: $-k T'(L) = q$, and $h (T(L) - T_\infty) = h (T_0 - T_\infty - q L / k) = q$, since $T_0 - T_\infty = q (L / k + 1 / h)$.

Non-example: the condition $T = T_\infty$ on $\partial \Omega$ is not of this type.
It is the Dirichlet condition, which is the limit $h \to \infty$.
The limit $h \to 0$ gives the insulated Neumann condition $\partial T / \partial \nu = 0$.
