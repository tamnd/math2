---
tag: 1TKXSKDNJ6
kind: definition
name: Magnetic scalar potential
msc: [78A30]
defines: WYK6FSAF2Y
uses: [XRED3C547P, A2WZA4QA3V, 0ABK9V9Y64, 0NF6GQNXMY, 0PKG97PX9Y]
sources:
  - url: https://en.wikipedia.org/wiki/Magnetic_scalar_potential
---

## Definition

Let $U \subseteq \R^3$ be an open set, and let $H \colon U \to \R^3$ be a continuous magnetizing field.
So $H = B / \mu_0 - M$ for the [[magnetic field|XRED3C547P]] $B$, the [[magnetization|A2WZA4QA3V]] $M$ and the vacuum permeability $\mu_0 > 0$.
A *magnetic scalar potential* for $H$ on $U$ is a $C^1$ function $\psi \colon U \to \R$ such that
$$H = - \nabla \psi \quad \text{on } U,$$
where $\nabla \psi$ is the [[gradient|0ABK9V9Y64]] of $\psi$.

## Remarks

In vacuum $M = 0$, and the condition reads $B = -\mu_0 \nabla \psi$.
A potential can exist only if $H$ is a [[conservative vector field|0PKG97PX9Y]].
For a $C^1$ field this forces $\nabla \times H = 0$, which in magnetostatics means that no free current flows in $U$.
If $U$ is simply connected and $\nabla \times H = 0$ on $U$, a potential exists, and it is unique up to an additive constant when $U$ is connected.

Example: a uniform field $H = (0, 0, H_0)$ on $\R^3$ has the potential $\psi(x, y, z) = -H_0 z$, since $-\nabla \psi = (0, 0, H_0)$.

Non-example: a straight wire along the $z$-axis carrying a steady current $I \neq 0$ produces, on $U = \R^3 \setminus \set{x = y = 0}$, the field $H = \frac{I}{2 \pi (x^2 + y^2)} (-y, x, 0)$.
This field has zero [[curl|0NF6GQNXMY]] on $U$, but its line integral around the unit circle in the $xy$-plane equals $I \neq 0$.
So $H$ is not a gradient on $U$, and no single-valued potential exists there.
On $U$ minus a half-plane bounded by the wire, the angle $\theta$ around the wire is single-valued, and $\psi = -I \theta / (2 \pi)$ is a potential.

Where $\nabla \cdot B = 0$ and the medium is linear with constant permeability, $\psi$ satisfies the Laplace equation $\Delta \psi = 0$.
