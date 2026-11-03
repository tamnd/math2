---
tag: CRNK6NQ60W
kind: definition
name: Thermal boundary layer
msc: [80A19, 76D10, 76R05]
defines: 4VAN0ZE1PB
uses: [YCFPD0GE5G, KK46Q2YV1D, C4KSBMR413, JH9EJ0HA0R]
sources:
  - url: https://en.wikipedia.org/wiki/Thermal_boundary_layer_thickness_and_shape
---

## Definition

Consider a steady flow of a fluid along a wall $y = 0$.
Here $x \ge 0$ is the distance along the wall from its leading edge and $y \ge 0$ is the distance from the wall.
Let $T(x, y)$ be the [[temperature|KK46Q2YV1D]] of the fluid and $T_w$ the wall temperature.
Let $T_\infty \ne T_w$ be the temperature of the fluid far from the wall.
Let $\theta(x, y) = (T(x, y) - T_w)/(T_\infty - T_w)$ be the dimensionless temperature, so that $\theta = 0$ at the wall and $\theta \to 1$ as $y \to \infty$.
The *thermal boundary layer thickness* $\delta_T(x)$ is the smallest $y \ge 0$ with $\theta(x, y) = 0.99$.
The *thermal boundary layer* is the region $0 \le y < \delta_T(x)$ next to the wall.

## Remarks

Example: laminar flow at speed $U$ over a flat plate at uniform temperature, with [[Prandtl number|C4KSBMR413]] $\Pr = 1$ and negligible viscous heating.
Then $u/U$ and $\theta$ solve the same boundary layer equation with the same boundary values, so $\theta = u/U$.
Hence $\delta_T$ equals the velocity [[boundary layer|YCFPD0GE5G]] thickness, about $5x / \sqrt{\mathrm{Re}_x}$, where $\mathrm{Re}_x = Ux/\nu$ is the local [[Reynolds number|JH9EJ0HA0R]] and $\nu$ the kinematic viscosity.
For other laminar flat-plate flows with $\Pr \gtrsim 0.6$, the ratio $\delta_T / \delta$ is close to $\Pr^{-1/3}$.

Non-example: if $T_\infty = T_w$, then $\theta$ is not defined and there is no thermal boundary layer, although a velocity boundary layer still forms.

Other measures of the thickness, such as the thermal displacement thickness $\int_0^\infty (1 - \theta) \, dy$, are also used.
