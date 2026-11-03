---
tag: 6MGFWKBDW8
kind: definition
name: Biot number
msc: [80A19]
defines: ZYJRK1RVP5
uses: [T3R5FWV91P, J821AD6YTE, XBQBT9E7JT]
sources:
  - url: https://en.wikipedia.org/wiki/Biot_number
---

## Definition

Let a solid body of [[thermal conductivity|XBQBT9E7JT]] $k > 0$ exchange heat with a fluid through its surface, with [[heat transfer coefficient|J821AD6YTE]] $h > 0$.
Let $L > 0$ be a characteristic length of the body.
The *Biot number* is the [[dimensionless number|T3R5FWV91P]]
$$\mathrm{Bi} = \frac{h L}{k}.$$

## Remarks

A common choice of length is $L = V / A$, the volume of the body divided by its surface area.

Example: a steel ball of radius $r = 0.01$ metres with $k = 50$, cooled in air with $h = 10$, in SI units.
Then $L = V / A = r / 3$, so $\mathrm{Bi} = 10 \cdot 0.01 / (3 \cdot 50) \approx 6.7 \cdot 10^{-4}$, which is far below $0.1$.

Non-example: the ratio $h L / k_f$ with the conductivity $k_f$ of the fluid instead of the solid is not the Biot number.
It is the Nusselt number.

When $\mathrm{Bi} < 0.1$, the rule of thumb in engineering is that the temperature inside the body is nearly uniform.
