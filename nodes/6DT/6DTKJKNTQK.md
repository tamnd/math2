---
tag: 6DTKJKNTQK
kind: definition
name: Reynolds-averaged Navier–Stokes equations
msc: [76F55, 76D05]
defines: 4EYAHQDA7Q
uses: [18KXZHVF4M, V47TX9AFKF, FDQE4PF63G]
sources:
  - url: https://en.wikipedia.org/wiki/Reynolds-averaged_Navier–Stokes_equations
---

## Definition

Consider an incompressible fluid with constant density $\rho$ and kinematic viscosity $\nu$, whose velocity $u_i$ and pressure $p$ satisfy the [[Navier–Stokes equations|18KXZHVF4M]] without body forces.
Let $u_i = \bar u_i + u_i'$ and $p = \bar p + p'$ be [[Reynolds decompositions|V47TX9AFKF]].
Sum over the repeated index $j$.
The *Reynolds-averaged Navier–Stokes equations* are the averaged equations for $\bar u_i$ and $\bar p$:
$$\frac{\partial \bar u_i}{\partial t} + \bar u_j \frac{\partial \bar u_i}{\partial x_j} = -\frac{1}{\rho} \frac{\partial \bar p}{\partial x_i} + \nu \Delta \bar u_i - \frac{\partial \overline{u_i' u_j'}}{\partial x_j}, \qquad \frac{\partial \bar u_i}{\partial x_i} = 0,$$
for $i = 1, 2, 3$.

## Remarks

The derivation writes the convective term as $\partial_j (u_i u_j)$, which is allowed because $\partial_j u_j = 0$, and uses $\overline{u_i u_j} = \bar u_i \bar u_j + \overline{u_i' u_j'}$.
The extra term is the divergence of the [[Reynolds stress|FDQE4PF63G]] $-\rho \overline{u_i' u_j'}$ divided by $\rho$.
There are four equations for the ten unknowns $\bar u_i$, $\bar p$ and the six independent components of $\overline{u_i' u_j'}$, so the system is not closed.

Example: for statistically steady, fully developed flow in a channel $0 < x_2 < 2h$ with mean velocity $\bar u_1(x_2)$, the equations reduce to
$$0 = -\frac{1}{\rho} \frac{d \bar p}{d x_1} + \frac{d}{d x_2} \left( \nu \frac{d \bar u_1}{d x_2} - \overline{u_1' u_2'} \right),$$
so the total shear stress varies linearly across the channel.
Non-example: replacing $\overline{u_i u_j}$ by $\bar u_i \bar u_j$, that is, dropping the Reynolds stress, gives the Navier–Stokes equations for $\bar u$, which are not the averaged equations of a turbulent flow.
