---
tag: 9GVQ7JXC25
kind: definition
name: Cahn–Hilliard equation
msc: [35K55, 35K25]
defines: DKN15NVKSB
uses: [1CCTH8X2FT, 0E0B6RA8K0, 7S813PEV69]
sources:
  - url: https://en.wikipedia.org/wiki/Cahn%E2%80%93Hilliard_equation
---

## Definition

Let $\Omega \subseteq \R^n$ be open and let $\gamma > 0$.
The *Cahn–Hilliard equation* is the [[parabolic equation|1CCTH8X2FT]] of fourth order for $c \colon \Omega \times (0, T) \to \R$:
$$c_t = \Delta \mu, \qquad \mu = c^3 - c - \gamma\, \Delta c,$$
where $\Delta$ is the [[Laplacian|0E0B6RA8K0]] in $x$.
The function $\mu$ is the chemical potential.
On a bounded $\Omega$ one usually imposes $\partial_\nu c = \partial_\nu \mu = 0$ on $\partial \Omega$, where $\nu$ is the outer normal.

## Remarks

Example: every constant $c \equiv c_0$ is a solution, since then $\mu$ is constant and $\Delta \mu = 0$.
Non-example: the [[Allen–Cahn equation|7S813PEV69]] $c_t = \gamma \Delta c - (c^3 - c)$ is of second order and does not conserve mass, so it is not of this form.
With the boundary conditions above, $\frac{d}{dt}\int_\Omega c\, dx = \int_{\partial\Omega} \partial_\nu \mu \, dS = 0$, so the mass is conserved.
The energy $E(c) = \int_\Omega \big(\frac{\gamma}{2}\abs{\nabla c}^2 + \frac{1}{4}(1 - c^2)^2\big)\, dx$ does not increase along smooth solutions.
