---
tag: HVSRB4QXKA
kind: example
name: Burgers vortex
msc: [76D17, 76D05]
illustrates: [18KXZHVF4M, W5RHJENGWS]
sources:
  - url: https://en.wikipedia.org/wiki/Burgers_vortex
same_as:
  wikidata: Q16000060
  wikipedia: Burgers vortex
---

## Example

Fix a strain rate $\alpha > 0$, a circulation $\Gamma > 0$ and a kinematic viscosity $\nu > 0$.
In cylindrical coordinates $(r, \theta, z)$, the *Burgers vortex* is the steady flow with
$$u_r = -\alpha r, \qquad u_z = 2 \alpha z, \qquad u_\theta = \frac{\Gamma}{2 \pi r} \Big( 1 - e^{-\alpha r^2 / (2 \nu)} \Big).$$
It is incompressible: $\frac{1}{r} \partial_r (r u_r) + \partial_z u_z = -2\alpha + 2\alpha = 0$.
Its vorticity is axial, $\omega = (0, 0, \zeta(r))$ with
$$\zeta(r) = \frac{1}{r} \frac{d}{dr}(r u_\theta) = \frac{\Gamma \alpha}{2 \pi \nu} \, e^{-\alpha r^2 / (2 \nu)}.$$
The steady [[vorticity equation|W5RHJENGWS]] reads $u_r \zeta' = 2 \alpha \zeta + \nu (\zeta'' + \zeta'/r)$, since the stretching term is $\zeta \, \partial_z u_z = 2 \alpha \zeta$.
With $\zeta = C e^{-k r^2}$ and $k = \alpha / (2\nu)$, the left side is $2 \alpha k r^2 \zeta$, and the right side is $2\alpha \zeta + \nu(4 k^2 r^2 - 4k) \zeta = 2 \alpha k r^2 \zeta$, so the equation holds.
With a suitable pressure, the flow is an exact steady solution of the incompressible [[Navier–Stokes equations|18KXZHVF4M]].

## Remarks

The radial inflow and axial stretching concentrate vorticity, while viscosity spreads it out.
The Burgers vortex is the steady balance of these two effects, with core radius of order $\sqrt{\nu / \alpha}$.
It is used as a model of the thin intense vortex tubes seen in turbulence.

## Explanations

### L1 human

Pulling a vortex along its axis makes it thinner and spin faster, like a skater pulling in the arms.
Friction does the opposite and spreads the spin out.
In the Burgers vortex the two effects balance exactly, so the vortex keeps a fixed shape forever while fluid streams in from the sides and out along the axis.
