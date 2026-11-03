---
tag: EHHS7BZ9HK
kind: definition
name: Heat transfer coefficient
msc: [80A19, 76R05]
defines: J821AD6YTE
uses: [RK24AYNG4Z, 1Y36434YTE, KK46Q2YV1D]
sources:
  - url: https://en.wikipedia.org/wiki/Heat_transfer_coefficient
---

## Definition

Let a solid surface at [[temperature|KK46Q2YV1D]] $T_s$ exchange heat by [[convection|RK24AYNG4Z]] with a fluid of reference temperature $T_\infty \ne T_s$.
Let $q_s$ be the normal [[heat flux|1Y36434YTE]] from the surface into the fluid.
The *heat transfer coefficient* is
$$h = \frac{q_s}{T_s - T_\infty}.$$
Its unit is $\mathrm{W \, m^{-2} \, K^{-1}}$.

## Remarks

The reference $T_\infty$ is the temperature far from the surface for an external flow, and a mean temperature for flow in a pipe.
The coefficient may be local, at a point, or averaged over the surface.

Example: a plate at $60$ degrees Celsius in air at $20$ degrees Celsius loses $400$ watts per square metre.
Then $h = 400 / 40 = 10$ watts per square metre per kelvin.

Non-example: the thermal conductivity of air, about $0.026$ watts per metre per kelvin, is not a heat transfer coefficient.
Its unit is different, and it is a property of the material alone.

Writing $q_s = h (T_s - T_\infty)$ with $h$ independent of $T_s$ is [[Newton's law of cooling|02HB5F40VR]].
