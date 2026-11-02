---
tag: M665JWCEXY
kind: definition
name: Maxwell's equations
msc: [35Q61, 35Q60]
defines: 9BWWD4QK8Y
uses: [GC5BDZ6QBC, 0299VCW1TH, 0MWV6ZTK6S, 0NF6GQNXMY]
sources:
  - url: https://en.wikipedia.org/wiki/Maxwell's_equations
---

## Definition

Let $\varepsilon_0 > 0$ and $\mu_0 > 0$ be constants, the vacuum permittivity and permeability, and put $c = 1 / \sqrt{\varepsilon_0 \mu_0}$.
Let $\rho \colon \R^3 \times \R \to \R$ be a given charge density and $J \colon \R^3 \times \R \to \R^3$ a given current density.
*Maxwell's equations* in vacuum are the system
$$\nabla \cdot E = \frac{\rho}{\varepsilon_0}, \qquad \nabla \cdot B = 0, \qquad \nabla \times E = - \partial_t B, \qquad \nabla \times B = \mu_0 J + \mu_0 \varepsilon_0 \, \partial_t E,$$
for unknown [[vector fields|0299VCW1TH]] $E, B \colon \R^3 \times \R \to \R^3$, the electric and the magnetic field.
Here $\nabla \cdot$ is the [[divergence|0MWV6ZTK6S]] and $\nabla \times$ is the [[curl|0NF6GQNXMY]] in the space variable.

## Remarks

Example: with $\rho = 0$ and $J = 0$, for $E_0 \in \R$, $k > 0$ and $\omega = ck$, the plane wave
$$E = \big(0, E_0 \cos(kx - \omega t), 0\big), \qquad B = \big(0, 0, \tfrac{E_0}{c} \cos(kx - \omega t)\big)$$
is a solution.
Both fields depend only on $x$ and point across the $x$ direction, so both divergences vanish.
One has $(\nabla \times E)_z = \partial_x E_y = -k E_0 \sin(kx - \omega t) = -\partial_t B_z$, and $(\nabla \times B)_y = -\partial_x B_z = \tfrac{k E_0}{c} \sin(kx - \omega t) = \tfrac{1}{c^2} \partial_t E_y$.

Non-example: $E = (-y, x, 0)$ and $B = 0$ with $\rho = 0$ and $J = 0$ is not a solution, because $\nabla \times E = (0, 0, 2)$ while $-\partial_t B = 0$.

The first two equations are Gauss's laws, the third is Faraday's law, and the fourth is the Ampère–Maxwell law.
Taking the divergence of the fourth equation gives the continuity equation $\partial_t \rho + \nabla \cdot J = 0$ as a condition on the sources.
In matter one also uses the fields $D$ and $H$, related to $E$ and $B$ by constitutive relations.
