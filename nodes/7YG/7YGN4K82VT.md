---
tag: 7YGN4K82VT
kind: definition
name: Grashof number
msc: [76R10, 80A19]
defines: VVCSRXKQWR
uses: [T3R5FWV91P, 2NRW3XGP3T, NM5Q4845Z4, TXQQQG9T2S]
sources:
  - url: https://en.wikipedia.org/wiki/Grashof_number
---

## Definition

Let a surface at temperature $T_s$ be in a fluid at temperature $T_\infty$ under gravity of acceleration $g > 0$.
Let the fluid have [[thermal expansion coefficient|2NRW3XGP3T]] $\beta$ and kinematic [[viscosity|NM5Q4845Z4]] $\nu > 0$.
Let $L > 0$ be a characteristic length, such as the height of a vertical plate.
The *Grashof number* is the [[dimensionless number|T3R5FWV91P]]
$$\mathrm{Gr} = \frac{g \, \beta \, (T_s - T_\infty) \, L^3}{\nu^2}.$$

## Remarks

It arises when the momentum equation with the [[Boussinesq approximation|TXQQQG9T2S]] is made dimensionless.
Some authors use $\abs{T_s - T_\infty}$ so that $\mathrm{Gr} \ge 0$.

Example: air with $\beta \approx 1/300$ per kelvin and $\nu \approx 1.5 \cdot 10^{-5}$ square metres per second, at a plate $L = 0.5$ metres high and $30$ kelvin warmer.
Then $\mathrm{Gr} \approx 9.81 \cdot 0.1 \cdot 0.125 / (2.25 \cdot 10^{-10}) \approx 5.4 \cdot 10^8$.

Non-example: $g \beta \Delta T L^3 / (\nu \alpha)$, with thermal diffusivity $\alpha$, is not the Grashof number.
It is the Rayleigh number, equal to $\mathrm{Gr} \cdot \mathrm{Pr}$.
