---
tag: ZWE9BFVQ37
kind: definition
name: Thermal resistance
msc: [80A19]
defines: 1CB45W4GA6
uses: [RFWGC57K4H, 1Y36434YTE, XBQBT9E7JT, KK46Q2YV1D]
sources:
  - url: https://en.wikipedia.org/wiki/Thermal_conductance_and_resistance
---

## Definition

Let an object carry heat in [[steady state|RFWGC57K4H]] between two surfaces held at uniform [[temperatures|KK46Q2YV1D]] $T_1$ and $T_2$.
Let $Q \ne 0$ be the heat rate, in watts, from the first surface to the second.
The *thermal resistance* of the object between the two surfaces is
$$R = \frac{T_1 - T_2}{Q}.$$
Its unit is $\mathrm{K \, W^{-1}}$.
The reciprocal $1/R$ is the *thermal conductance*.

## Remarks

Example: a flat wall of thickness $L$, area $A$ and [[conductivity|XBQBT9E7JT]] $k$ has $Q = k A (T_1 - T_2) / L$ by the linear steady profile.
So $R = L / (k A)$.

Non-example: the [[heat flux|1Y36434YTE]] per kelvin, $q / (T_1 - T_2)$, is not a resistance.
It is a conductance per unit area, and its unit is $\mathrm{W \, m^{-2} \, K^{-1}}$.

For layers in series that carry the same heat rate, the resistances add: $R = R_1 + R_2$.
For paths in parallel with the same end temperatures, the conductances add.
