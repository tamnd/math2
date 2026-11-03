---
tag: 2VRV90Z4GZ
kind: definition
name: Nusselt number
msc: [80A19, 76R05, 76R10]
defines: THH3V9AHDN
uses: [T3R5FWV91P, J821AD6YTE, XBQBT9E7JT, RK24AYNG4Z]
sources:
  - url: https://en.wikipedia.org/wiki/Nusselt_number
---

## Definition

Let a surface exchange heat by [[convection|RK24AYNG4Z]] with a fluid of [[thermal conductivity|XBQBT9E7JT]] $k_f > 0$.
Let $h$ be the [[heat transfer coefficient|J821AD6YTE]] and $L > 0$ a characteristic length of the flow.
The *Nusselt number* is the [[dimensionless number|T3R5FWV91P]]
$$\mathrm{Nu} = \frac{h L}{k_f}.$$

## Remarks

The length is, for example, the diameter of a pipe or the length of a plate along the flow.

Example: in a fluid layer of thickness $L$ at rest between plates at temperatures $T_1$ and $T_2$, the flux is $k_f (T_1 - T_2) / L$.
So $h = k_f / L$ and $\mathrm{Nu} = 1$.

Non-example: the number $h L / k_s$ with the conductivity $k_s$ of the solid wall is not the Nusselt number.
It is the Biot number, which compares resistances inside and at the surface of the solid.
