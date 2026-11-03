---
tag: 8XC4C5MFNQ
kind: definition
name: Stanton number
msc: [80A19, 76R05]
defines: 6T2FKXGS25
uses: [T3R5FWV91P, J821AD6YTE, THH3V9AHDN, JH9EJ0HA0R, C4KSBMR413]
sources:
  - url: https://en.wikipedia.org/wiki/Stanton_number
---

## Definition

Let a fluid of density $\rho > 0$ and specific heat $c_p > 0$ flow with characteristic speed $U > 0$ past a surface.
Let $h$ be the [[heat transfer coefficient|J821AD6YTE]] of the surface.
The *Stanton number* is the [[dimensionless number|T3R5FWV91P]]
$$\mathrm{St} = \frac{h}{\rho \, c_p \, U}.$$

## Remarks

With a length $L$, conductivity $k$, kinematic viscosity $\nu$ and diffusivity $\alpha = k / (\rho c_p)$, one has $\mathrm{St} = \mathrm{Nu} / (\mathrm{Re} \, \mathrm{Pr})$.
Check: $\mathrm{Nu} / (\mathrm{Re} \, \mathrm{Pr}) = (h L / k) \cdot \alpha / (U L) = h / (\rho c_p U)$.
This uses the [[Nusselt|THH3V9AHDN]], [[Reynolds|JH9EJ0HA0R]] and [[Prandtl|C4KSBMR413]] numbers.

Example: water with $\rho c_p \approx 4.2 \cdot 10^6$ joules per cubic metre per kelvin, at $U = 1$ metre per second, with $h = 4200$ in SI units.
Then $\mathrm{St} \approx 4200 / (4.2 \cdot 10^6) = 10^{-3}$.

Non-example: $h L / k$ is not the Stanton number; it is the Nusselt number and does not involve the flow speed.
