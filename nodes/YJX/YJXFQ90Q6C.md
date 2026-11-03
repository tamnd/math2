---
tag: YJXFQ90Q6C
kind: definition
name: Inhomogeneous electromagnetic wave equation
msc: [78A25, 35Q61, 35L05]
defines: 1AE7YGNX2R
uses: [9BWWD4QK8Y, 5EHD2XBQDG, 0E0B6RA8K0, YZ7Q9DP8RT, XRED3C547P, SAEDXNM3Y1, 8PEMR2J7EF, YBHAVTWF82]
sources:
  - url: https://en.wikipedia.org/wiki/Inhomogeneous_electromagnetic_wave_equation
---

## Definition

Let $\varepsilon_0, \mu_0 > 0$ be the vacuum permittivity and permeability, and let $c = 1/\sqrt{\varepsilon_0 \mu_0}$.
Let $\rho \colon \R^3 \times \R \to \R$ be a charge density and $J \colon \R^3 \times \R \to \R^3$ a current density.
Write $\square = \frac{1}{c^2} \partial_t^2 - \Delta$, where $\Delta$ is the [[Laplacian|0E0B6RA8K0]] in the space variable, acting componentwise on vector fields.
The *inhomogeneous electromagnetic wave equations* for the [[electric field|YZ7Q9DP8RT]] $E$ and the [[magnetic field|XRED3C547P]] $B$ are
$$\square E = -\frac{1}{\varepsilon_0} \nabla \rho - \mu_0 \, \partial_t J, \qquad \square B = \mu_0 \, \nabla \times J.$$
In terms of an [[electric potential|SAEDXNM3Y1]] $\varphi$ and a [[magnetic vector potential|8PEMR2J7EF]] $A$ that satisfy the [[Lorenz gauge condition|YBHAVTWF82]] $\nabla \cdot A + \frac{1}{c^2} \partial_t \varphi = 0$, they are
$$\square \varphi = \frac{\rho}{\varepsilon_0}, \qquad \square A = \mu_0 J.$$

## Remarks

Every twice differentiable solution of [[Maxwell's equations|9BWWD4QK8Y]] in vacuum satisfies the equations for $E$ and $B$.
For example, the identity $\nabla \times (\nabla \times E) = \nabla (\nabla \cdot E) - \Delta E$ with $\nabla \times E = -\partial_t B$ and $\nabla \cdot E = \rho / \varepsilon_0$ gives the equation for $E$.
The converse needs care.
A solution of the wave equations solves Maxwell's equations only together with the first-order equations, or with the gauge condition in the potential form.

Example: let $\rho = \rho_0$ be constant, $J = 0$, $\varphi(x, t) = -\rho_0 \abs{x}^2 / (6 \varepsilon_0)$ and $A = 0$.
Then $\partial_t \varphi = 0$ and $\Delta \varphi = -\rho_0 / \varepsilon_0$, so $\square \varphi = \rho_0 / \varepsilon_0$; also $\square A = 0 = \mu_0 J$, and the Lorenz condition holds.

Non-example: let $\rho = 0$, $J = 0$, $\varphi(x, t) = t$ and $A = 0$.
Both wave equations hold, since $\square \varphi = 0$ and $\square A = 0$.
The Lorenz condition fails, since $\nabla \cdot A + \frac{1}{c^2} \partial_t \varphi = 1/c^2 \neq 0$, so this pair is not of the form required in the definition.

In the static case, $\partial_t = 0$, the equation for $\varphi$ is Poisson's equation $-\Delta \varphi = \rho / \varepsilon_0$.

## Explanations

### L1 human

These are the equations that tell how charges and currents produce electromagnetic waves.
Each one has the form "wave operator applied to a field equals a source term".
In the Lorenz gauge the potentials obey the simplest form: the charge density drives the scalar potential and the current drives the vector potential.
