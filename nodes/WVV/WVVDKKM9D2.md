---
tag: WVVDKKM9D2
kind: definition
name: Vorticity equation
msc: [76B47, 76D17, 76D05]
defines: W5RHJENGWS
uses: [B3SXT9TWFA, CJW50K5HZB, 18KXZHVF4M, 0NF6GQNXMY]
sources:
  - url: https://en.wikipedia.org/wiki/Vorticity_equation
---

## Definition

Let $u$ be a smooth velocity field on an open set of $\R^3$.
Assume it solves the incompressible [[Navier–Stokes equations|18KXZHVF4M]]
$$\frac{\partial u}{\partial t} + (u \cdot \nabla) u = -\nabla p + \nu \Delta u - \nabla \Phi, \qquad \nabla \cdot u = 0,$$
with kinematic viscosity $\nu \ge 0$, pressure $p$ (divided by the constant density) and body force potential $\Phi$.
Let $\omega = \nabla \times u$ be the [[vorticity|B3SXT9TWFA]], the [[curl|0NF6GQNXMY]] of $u$.
The *vorticity equation* is the equation
$$\frac{D\omega}{Dt} = (\omega \cdot \nabla) u + \nu \Delta \omega,$$
where $D\omega/Dt = \partial_t \omega + (u \cdot \nabla) \omega$ is the [[material derivative|CJW50K5HZB]].
It holds for every such solution, as one sees by taking the curl of the momentum equation.

## Remarks

The term $(\omega \cdot \nabla) u$ describes stretching and tilting of vortex lines; $\nu \Delta \omega$ describes viscous diffusion.
For $\nu = 0$ it is the vorticity equation of the [[Euler equations|RW0JK9VDZE]].

Example: for a planar flow $u = (u_1(x, y, t), u_2(x, y, t), 0)$, the vorticity is $\omega = (0, 0, \zeta)$ and $(\omega \cdot \nabla) u = \zeta \, \partial_z u = 0$.
So the equation reduces to the scalar equation $D\zeta/Dt = \nu \Delta \zeta$.

Non-example: for a compressible fluid whose density is not a function of the pressure, the equation above is not satisfied in general.
The general equation has the extra terms $-\omega (\nabla \cdot u)$ and the baroclinic term $\nabla \rho \times \nabla p / \rho^2$, plus terms from viscous stresses.
