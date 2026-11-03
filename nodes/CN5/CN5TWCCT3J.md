---
tag: CN5TWCCT3J
kind: definition
name: Coulomb gauge
msc: [78A25, 35Q61]
defines: JWGVKWD7TA
uses: [TXD7MTYQYS, 8PEMR2J7EF, DWK5N5SKTK, 0MWV6ZTK6S]
sources:
  - url: https://en.wikipedia.org/wiki/Gauge_fixing
    locator: Coulomb gauge
---

## Definition

Let $(\phi, A)$ be $C^1$ potentials of an electromagnetic field on an open set of $\R^3 \times \R$, with $A$ the [[vector potential|8PEMR2J7EF]].
The potentials are in the *Coulomb gauge* if
$$\nabla \cdot A = 0$$
at every point and time, where $\nabla \cdot$ is the [[divergence|0MWV6ZTK6S]] in the space variables.

## Remarks

It is a [[gauge condition|TXD7MTYQYS]]: on $\R^3$, for $\nabla \cdot A$ smooth and decaying fast enough, a gauge transformation with $\chi$ solving $\Delta \chi = -\nabla \cdot A$ yields potentials that satisfy it.
The residual freedom consists of functions $\chi$ with $\Delta \chi = 0$; requiring decay at infinity removes it up to functions of $t$ alone.

In the Coulomb gauge, Gauss's law becomes [[Poisson's equation|DWK5N5SKTK]] $\Delta \phi = -\rho / \varepsilon_0$.
For a charge density decaying at infinity, the decaying solution is
$$\phi(x, t) = \frac{1}{4 \pi \varepsilon_0} \int_{\R^3} \frac{\rho(y, t)}{\abs{x - y}} \, dy,$$
the Coulomb potential at the same time $t$.
The Ampère–Maxwell law becomes $\frac{1}{c^2} \partial_t^2 A - \Delta A = \mu_0 J - \frac{1}{c^2} \nabla \partial_t \phi$.
The instantaneous $\phi$ does not violate causality, since the fields $E$ and $B$ remain retarded.

Example: for a uniform magnetic field $B = (0, 0, B_0)$, the potential $A = \frac{B_0}{2} (-y, x, 0)$ has $\nabla \cdot A = 0$ and $\nabla \times A = B$.

Non-example: $A = (0, B_0 x, 0) + (x, 0, 0)$ gives the same magnetic field, but $\nabla \cdot A = 1$, so it is not in the Coulomb gauge.
