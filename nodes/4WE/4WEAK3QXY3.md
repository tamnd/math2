---
tag: 4WEAK3QXY3
kind: definition
name: Thermal conduction
msc: [80A19, 35K05]
defines: SW8X60GYZT
uses: [CY4GJQGF06, KK46Q2YV1D, 1Y36434YTE]
sources:
  - url: https://en.wikipedia.org/wiki/Thermal_conduction
---

## Definition

Let a body occupy an open set $\Omega \subseteq \R^3$, with [[temperature|KK46Q2YV1D]] field $T(x, t)$.
*Thermal conduction* is the transport of [[heat|CY4GJQGF06]] through $\Omega$ that is caused by the spatial variation of $T$.
It is not carried by a bulk motion of the material.
In the continuum model it is described by a [[heat flux|1Y36434YTE]] $\mathbf{q}$ that is determined by the temperature field.

## Remarks

Example: hold one end of a solid copper bar at $100$ degrees Celsius and the other at $0$ degrees Celsius.
The heat that flows along the bar is conducted, since the copper does not move.

Non-example: in water heated from below in a pan, warm water rises and carries heat with it.
That transport is by bulk motion, so it is convection, not conduction.

The usual constitutive law for conduction is Fourier's law $\mathbf{q} = -k \nabla T$, where $k$ is the thermal conductivity.
