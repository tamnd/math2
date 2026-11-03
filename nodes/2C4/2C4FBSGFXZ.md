---
tag: 2C4FBSGFXZ
kind: definition
name: Ekman layer
msc: [76U60, 76U05, 86A05]
defines: H5GNFWEW80
uses: [CZ1S1P465Y, YCFPD0GE5G, NM5Q4845Z4]
sources:
  - url: https://en.wikipedia.org/wiki/Ekman_transport
---

## Definition

Consider a fluid of constant density $\rho$ in a frame rotating with Coriolis parameter $f > 0$, near a horizontal boundary, with vertical coordinate $z$.
Let $\nu > 0$ be its constant kinematic [[viscosity|NM5Q4845Z4]], or an eddy viscosity.
Assume the flow is steady and horizontally uniform, with horizontal velocity $u_h(z)$.
Assume that far from the boundary it tends to a [[geostrophic|CZ1S1P465Y]] velocity $u_g$, or that a stress $\tau$ is applied at a free surface.
An *Ekman layer* is the [[boundary layer|YCFPD0GE5G]] in which $u_h$ solves
$$f \, e_z \times (u_h - u_g) = \nu \, \frac{d^2 u_h}{d z^2},$$
with the boundary condition of the problem.
Here $e_z$ is the upward unit vector, and $u_g = 0$ for a layer driven only by surface stress.
Its thickness scale is the *Ekman depth* $\delta = \sqrt{2 \nu / f}$.

## Remarks

Example: at a bottom wall $z = 0$ with no slip and $u_g = (U, 0)$, the solution that tends to $u_g$ is
$$u = U \big( 1 - e^{-z/\delta} \cos(z / \delta) \big), \qquad v = U e^{-z/\delta} \sin(z / \delta).$$
To check, set $w = (u - U) + i v$; the equation becomes $w'' = (i f / \nu) w = \big( (1 + i)/\delta \big)^2 w$, and $w = -U e^{-(1 + i) z / \delta}$ is the decaying solution with $w(0) = -U$.

At a free surface with stress $\tau$ and $u_g = 0$, integration over the layer gives the *Ekman transport* $M = \int u_h \, dz = \dfrac{1}{\rho f} \, \tau \times e_z$.
It is at right angles to the stress, to its right in the northern hemisphere.

Non-example: in a non-rotating fluid ($f = 0$) there is no Ekman layer, since the thickness $\sqrt{2 \nu / f}$ is infinite.
A layer driven by a surface stress then keeps deepening by diffusion and never reaches a steady state.
