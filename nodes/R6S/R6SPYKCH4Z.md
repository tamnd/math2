---
tag: R6SPYKCH4Z
kind: definition
name: Convective heat transfer
msc: [80A19, 76R05, 76R10]
defines: RK24AYNG4Z
uses: [SW8X60GYZT, 1Y36434YTE, XBQBT9E7JT, 0299VCW1TH]
sources:
  - url: https://en.wikipedia.org/wiki/Convection_(heat_transfer)
---

## Definition

Let a fluid fill an open set $\Omega \subseteq \R^3$ and move with velocity [[field|0299VCW1TH]] $\mathbf{u}(x, t)$.
Let it have density $\rho$, specific heat $c_p$, [[thermal conductivity|XBQBT9E7JT]] $k$ and temperature $T(x, t)$.
*Convective heat transfer* is the transport of heat in the fluid by advection together with [[conduction|SW8X60GYZT]].
Its [[heat flux|1Y36434YTE]] is
$$\mathbf{q} = \rho \, c_p \, T \, \mathbf{u} - k \, \nabla T,$$
with $T$ measured from a reference temperature.
For an incompressible fluid with constant properties and negligible viscous heating, energy balance gives
$$\rho \, c_p \left(\partial_t T + \mathbf{u} \cdot \nabla T\right) = k \, \Delta T.$$

## Remarks

Example: a fluid moving with constant speed $U$ in the $x_1$ direction, with $T = T(x_1)$ in steady state.
Then $\rho c_p U T' = k T''$, so $T = A + B e^{U x_1 / \alpha}$ with $\alpha = k / (\rho c_p)$.
The profile is no longer linear, as it would be for conduction alone.

Non-example: in a fluid at rest, $\mathbf{u} = 0$, the first term vanishes and only conduction remains.

The flow is called forced when it is imposed from outside, and natural, or free, when buoyancy causes it.
