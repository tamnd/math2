---
tag: H17SE6HQFV
kind: definition
name: Boiling heat transfer
msc: [80A19, 80A22, 76T10]
defines: 7DHX367Z44
uses: [RK24AYNG4Z, FN6Z9QKAH5, J821AD6YTE, 1Y36434YTE, KK46Q2YV1D]
sources:
  - url: https://en.wikipedia.org/wiki/Nucleate_boiling
---

## Definition

Consider a solid surface at [[temperature|KK46Q2YV1D]] $T_w$ in contact with a liquid.
Let $T_{\mathrm{sat}}$ be the saturation temperature of the liquid at the local pressure.
*Boiling heat transfer* is [[convective heat transfer|RK24AYNG4Z]] from the surface to the liquid with $T_w > T_{\mathrm{sat}}$.
In it, vapour is generated at the surface, as bubbles or as a vapour film.
The difference $\Delta T_e = T_w - T_{\mathrm{sat}}$ is the *excess temperature* (or wall superheat), and the [[heat flux|1Y36434YTE]] is written $q'' = h \, \Delta T_e$ with a [[heat transfer coefficient|J821AD6YTE]] $h$.

## Remarks

Example: water at atmospheric pressure, $T_{\mathrm{sat}} = 100$ °C, on a plate at $110$ °C.
Here $\Delta T_e = 10$ K, vapour bubbles form at the plate, and the regime is nucleate boiling.

Non-example: evaporation of a pond in the sun.
Vapour leaves the free surface, but no surface in contact with the water is above $T_{\mathrm{sat}}$ and no vapour forms at a wall, so this is not boiling.

As $\Delta T_e$ grows, the regimes are: natural convection without bubbles, nucleate boiling, transition boiling, and film boiling.
The heat flux has a maximum, the critical heat flux, at the end of nucleate boiling.
For water at atmospheric pressure it is of order $10^6$ W/m$^2$.
It is reached at $\Delta T_e$ around $30$ K.
The vapour carries the [[latent heat|FN6Z9QKAH5]] of vaporisation, which is why $h$ is large.
If the bulk liquid is below $T_{\mathrm{sat}}$ the boiling is called subcooled, and if it is at $T_{\mathrm{sat}}$ it is called saturated.
