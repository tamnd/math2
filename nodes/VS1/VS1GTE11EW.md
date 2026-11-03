---
tag: VS1GTE11EW
kind: definition
name: Biot consolidation theory
msc: [74F10, 74L10, 76S05]
defines: AX26BVMSXQ
uses: [987R9XR8KH, 80737NDZ4V, VP2HN86VAG]
sources:
  - url: https://en.wikipedia.org/wiki/Poroelasticity
---

## Definition

Consider a homogeneous isotropic linear [[poroelastic|987R9XR8KH]] medium with no body force.
Let $\lambda, \mu$ be its drained [[Lamé parameters|80737NDZ4V]], $\alpha$ its Biot coefficient and $M$ its Biot modulus.
Let $k$ be its permeability and $\eta_f$ the fluid viscosity.
*Biot consolidation theory* is the following system for the displacement $u(x, t)$ and pore pressure $p(x, t)$.
$$\mu \Delta u + (\lambda + \mu) \nabla (\nabla \cdot u) = \alpha \nabla p,$$
$$\frac{\partial}{\partial t} \left( \alpha \nabla \cdot u + \frac{p}{M} \right) = \frac{k}{\eta_f} \Delta p$$
It is completed by boundary conditions on displacement or traction and on pressure or flux, and by an initial condition.

## Remarks

The first equation is equilibrium with the poroelastic stress law, and the second is fluid mass balance with Darcy's law.
Inertia is neglected.
Example: one-dimensional (oedometric) consolidation of a layer with $u = (0, 0, w(z, t))$ under a constant applied vertical load.
Integrating the first equation in $z$ shows that $(\lambda + 2\mu) \partial_z w - \alpha p$ equals the applied vertical total stress, so it is constant in time.
So $\alpha \partial_t \partial_z w = \frac{\alpha^2}{\lambda + 2\mu} \partial_t p$, and the second equation becomes the [[diffusion equation|VP2HN86VAG]] below.
$$\partial_t p = c \, \partial_z^2 p, \qquad c = \frac{k / \eta_f}{1/M + \alpha^2/(\lambda + 2\mu)}$$
This is Terzaghi's consolidation equation with consolidation coefficient $c$.
Non-example: if the first equation is replaced by the wave equation with an inertia term $\rho \ddot u$, the system is Biot's dynamic theory of wave propagation, not the consolidation theory.
