---
tag: VRSHSEFH3Q
kind: definition
name: Geothermal gradient
msc: [86A04, 80A19]
defines: N9RFPKXE2Z
uses: [0ABK9V9Y64]
sources:
  - url: https://en.wikipedia.org/wiki/Geothermal_gradient
---

## Definition

Let $T(z)$ be the temperature in the Earth at depth $z \geq 0$ below a point of the surface, a differentiable function of $z$.
The *geothermal gradient* at depth $z$ is the derivative
$$\frac{dT}{dz}(z).$$
More generally, it is the vertical component of the [[gradient|0ABK9V9Y64]] $\nabla T$ of the temperature field, taken positive downward.

## Remarks

It is measured in kelvin per kilometre, or equivalently degrees Celsius per kilometre.
If heat moves only by vertical conduction with thermal conductivity $k$, the upward surface heat flow is $q = k \, \frac{dT}{dz}(0)$ by Fourier's law.
Example: in a borehole where $T(z) = 10 + 0.028 z$ in degrees Celsius, with $z$ in metres, the gradient is $28$ K/km, and with $k = 2.5$ W/(m K) the heat flow is $0.07$ W/m².
Non-example: the temperature contrast between the surface and the centre of the Earth, divided by the radius, is not a geothermal gradient.
It is an average, and the temperature does not increase linearly with depth.
