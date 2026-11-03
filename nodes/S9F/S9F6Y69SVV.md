---
tag: S9F6Y69SVV
kind: definition
name: Boussinesq eddy viscosity hypothesis
msc: [76F55]
defines: 4K9W1VP58R
uses: [FDQE4PF63G, V47TX9AFKF, P1KWMQG4NZ, NM5Q4845Z4, A2X0FXC6HK]
sources:
  - url: https://en.wikipedia.org/wiki/Eddy_diffusion
---

## Definition

Consider an incompressible turbulent flow with mean velocity $\bar u_i$ and velocity fluctuations $u_i'$ given by the [[Reynolds decomposition|V47TX9AFKF]].
Let $\bar S_{ij} = \frac12 (\partial \bar u_i / \partial x_j + \partial \bar u_j / \partial x_i)$ be the mean [[strain rate tensor|P1KWMQG4NZ]] and $k = \frac12 \overline{u_l' u_l'}$ the turbulent kinetic energy.
Let $\delta_{ij}$ be the Kronecker delta.
The *Boussinesq eddy viscosity hypothesis* is the assumption that some scalar field $\nu_t \ge 0$, the eddy viscosity, satisfies
$$-\overline{u_i' u_j'} = 2 \nu_t \bar S_{ij} - \frac{2}{3} k \, \delta_{ij}, \qquad i, j = 1, 2, 3.$$

## Remarks

The isotropic term $\frac23 k \delta_{ij}$ makes the traces of both sides agree, since $\bar S_{ii} = 0$ by incompressibility; it can be absorbed into a modified mean pressure.
With this hypothesis the [[Reynolds stress|FDQE4PF63G]] term of the averaged equations becomes a viscous-type term with variable [[viscosity|NM5Q4845Z4]] $\nu + \nu_t$, and the [[closure problem|A2X0FXC6HK]] reduces to finding the single field $\nu_t$.
Mixing-length models give $\nu_t$ by an algebraic formula, and the $k$–$\varepsilon$ model gives it from two transport equations.

Example: in a mean shear flow $\bar u_1(x_2)$, the hypothesis gives $-\overline{u_1' u_2'} = \nu_t \, d\bar u_1 / dx_2$.
So momentum flows down the mean velocity gradient, as observed in channel and boundary layer flows away from the wall.
Non-example: take a homogeneous flow with $\bar S_{ij} = 0$ but unequal normal stresses, for instance decaying anisotropic turbulence.
The hypothesis would force $\overline{u_i' u_j'} = \frac23 k \delta_{ij}$, so it fails there.
The anisotropy of the Reynolds stresses in such a flow is not linked to the mean strain.
