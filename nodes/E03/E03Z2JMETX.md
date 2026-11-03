---
tag: E03Z2JMETX
kind: definition
name: Lorenz gauge condition
msc: [78A25, 35Q61]
defines: YBHAVTWF82
uses: [TXD7MTYQYS, BQFCNWFV9Q, 5EHD2XBQDG, 0MWV6ZTK6S]
sources:
  - url: https://en.wikipedia.org/wiki/Lorenz_gauge_condition
---

## Definition

Let $(\phi, A)$ be $C^1$ potentials of an electromagnetic field on an open set of $\R^3 \times \R$, and let $c$ be the speed of light.
The potentials satisfy the *Lorenz gauge condition* if
$$\nabla \cdot A + \frac{1}{c^2} \frac{\partial \phi}{\partial t} = 0,$$
where $\nabla \cdot$ is the [[divergence|0MWV6ZTK6S]].
In terms of the [[four-potential|BQFCNWFV9Q]] $A^\mu = (\phi / c, A)$, the condition is $\partial_\mu A^\mu = 0$.

## Remarks

It is a [[gauge condition|TXD7MTYQYS]]: if $L = \nabla \cdot A + c^{-2} \partial_t \phi$ for given potentials, a gauge transformation with a function $\chi$ that solves $\frac{1}{c^2} \partial_t^2 \chi - \Delta \chi = L$ yields potentials that satisfy it.
Solutions $\chi$ of the homogeneous [[wave equation|5EHD2XBQDG]] leave the condition unchanged, so the gauge is not complete.

In the Lorenz gauge, Maxwell's equations in vacuum with charge density $\rho$ and current density $J$ become the decoupled wave equations
$$\frac{1}{c^2} \frac{\partial^2 \phi}{\partial t^2} - \Delta \phi = \frac{\rho}{\varepsilon_0}, \qquad \frac{1}{c^2} \frac{\partial^2 A}{\partial t^2} - \Delta A = \mu_0 J.$$
Their retarded solutions give the retarded potentials.

Example: the static Coulomb potentials $\phi = q / (4 \pi \varepsilon_0 \abs{x})$, $A = 0$ satisfy the condition, since $\nabla \cdot A = 0$ and $\partial_t \phi = 0$.

Non-example: the potentials $\phi = 0$, $A = (x, 0, 0)$ describe the zero field, but $\nabla \cdot A + c^{-2} \partial_t \phi = 1 \neq 0$, so they are not in the Lorenz gauge.
