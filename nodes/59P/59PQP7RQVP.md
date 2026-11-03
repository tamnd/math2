---
tag: 59PQP7RQVP
kind: definition
name: Postglacial rebound
msc: [86A04, 86A40, 76D07]
defines: A4YSEXMJ4P
uses: [7CJTGB6M0V, 13CB7V2YM4, NM5Q4845Z4, GCX1B3DAJN]
sources:
  - url: https://en.wikipedia.org/wiki/Post-glacial_rebound
---

## Definition

Let an ice load be removed at time $t = 0$ from a region of the Earth's surface that was in [[isostatic|7CJTGB6M0V]] equilibrium under the load.
Let $w(x, t)$ be the remaining depression of the surface below its equilibrium height without the load, at position $x$ and time $t > 0$.
*Postglacial rebound* is the uplift $-\partial_t w$ of the surface for $t > 0$.
It is driven by the flow of the [[viscous|NM5Q4845Z4]] or [[viscoelastic|GCX1B3DAJN]] mantle back under the former load.

## Remarks

For a Newtonian viscous half-space of viscosity $\mu$ and density $\rho$ under gravity $g$, a depression of the form $w = w_0 \cos(2\pi x/\lambda)$ decays, by [[Stokes flow|13CB7V2YM4]], as
$$w(x, t) = w_0 \cos(2\pi x/\lambda) \, e^{-t/\tau}, \qquad \tau = \frac{4\pi \mu}{\rho g \lambda}.$$
Example: $\mu = 10^{21}$ Pa s, $\rho = 3300$ kg/m³, $g = 10$ m/s² and $\lambda = 3000$ km give $\tau \approx 1.3 \times 10^{11}$ s, about $4000$ years.
Non-example: the immediate elastic uplift when the load is removed is not rebound in this sense; it happens at once and does not involve mantle flow.
Wider loads relax faster in this model, since $\tau$ decreases with $\lambda$.
