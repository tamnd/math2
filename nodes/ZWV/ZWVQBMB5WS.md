---
tag: ZWVQBMB5WS
kind: definition
name: Péclet number
msc: [76M55, 76R50, 76R05]
defines: 961839PHN6
uses: [T3R5FWV91P, DG49VBBT91, JH9EJ0HA0R, C4KSBMR413]
sources:
  - url: https://en.wikipedia.org/wiki/P%C3%A9clet_number
---

## Definition

Consider a flow with characteristic speed $U$ and characteristic length $L$ that transports a scalar with diffusivity $D > 0$, as in the [[advection–diffusion equation|DG49VBBT91]].
The *Péclet number* of the flow is
$$\mathrm{Pe} = \frac{U L}{D}.$$
For heat transport $D$ is the thermal diffusivity $\alpha$, and for mass transport it is the molecular diffusivity of the solute.

## Remarks

With $x = L \hat x$, $t = (L / U) \hat t$ and $u = U \hat u$, the equation $c_t + u \cdot \nabla c = D \Delta c$ becomes $c_{\hat t} + \hat u \cdot \hat\nabla c = \mathrm{Pe}^{-1} \hat\Delta c$.
So $\mathrm{Pe}$ is the only parameter of the dimensionless equation.

For heat, $\mathrm{Pe} = \mathrm{Re} \cdot \mathrm{Pr}$, the product of the [[Reynolds number|JH9EJ0HA0R]] $U L / \nu$ and the [[Prandtl number|C4KSBMR413]] $\nu / \alpha$; for mass, $\mathrm{Pe} = \mathrm{Re} \cdot \mathrm{Sc}$ with the Schmidt number $\mathrm{Sc} = \nu / D$.

Example: water flowing at $U = 1$ cm/s in a channel of width $L = 1$ cm carrying a solute with $D = 10^{-5}$ cm$^2$/s has $\mathrm{Pe} = 10^{5}$, so advection dominates.

Non-example: $U L / \nu$, with the kinematic viscosity $\nu$ in place of $D$, is the Reynolds number, not the Péclet number; it compares advection with diffusion of momentum, not of the scalar.
