---
tag: J2YFR1F2NG
kind: example
name: Lamb–Oseen vortex
msc: [76D17, 76D05]
illustrates: [18KXZHVF4M, B3SXT9TWFA]
sources:
  - url: https://en.wikipedia.org/wiki/Lamb–Oseen_vortex
same_as:
  wikidata: Q6481628
  wikipedia: Lamb–Oseen vortex
---

## Example

Fix a circulation $\Gamma > 0$ and a kinematic viscosity $\nu > 0$.
For $t > 0$, the *Lamb–Oseen vortex* is the planar flow with radial velocity $0$ and azimuthal velocity
$$u_\theta(r, t) = \frac{\Gamma}{2 \pi r} \Big( 1 - e^{-r^2 / (4 \nu t)} \Big).$$
Its [[vorticity|B3SXT9TWFA]] is
$$\zeta(r, t) = \frac{1}{r} \frac{\partial}{\partial r}(r u_\theta) = \frac{\Gamma}{4 \pi \nu t} \, e^{-r^2 / (4 \nu t)},$$
a Gaussian whose integral over the plane is $\Gamma$.
In a planar circular flow, the vorticity is constant along streamlines, so the transport term $(u \cdot \nabla) \zeta$ vanishes.
So the vorticity equation reduces to the heat equation $\partial_t \zeta = \nu \Delta \zeta$.
The Gaussian above is the heat kernel times $\Gamma$, so it solves this equation.
With the pressure given by $\partial p / \partial r = \rho \, u_\theta^2 / r$, the flow is an exact solution of the incompressible [[Navier–Stokes equations|18KXZHVF4M]].

## Remarks

As $t \to 0^+$ the flow tends to the point vortex $u_\theta = \Gamma / (2 \pi r)$.
For fixed $t$, it behaves like a rigid rotation near the centre and like a point vortex for $r$ much larger than $\sqrt{\nu t}$.
So it is a smooth version of the [[Rankine vortex|1JP90A94FR]].

## Explanations

### L1 human

Start with an ideal whirl concentrated at one point and let friction act.
The spin spreads out from the centre like heat from a hot spot, while the total amount of swirl stays the same.
The Lamb–Oseen vortex is the exact formula for this decay, and its core grows like the square root of time.
