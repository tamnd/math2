---
tag: CDXEXNJT7N
kind: definition
name: Rayleigh number
msc: [76R10, "76E06", 76M55]
defines: CEKBV27MP0
uses: [T3R5FWV91P, TXQQQG9T2S, NM5Q4845Z4, C4KSBMR413]
sources:
  - url: https://en.wikipedia.org/wiki/Rayleigh_number
---

## Definition

Consider a horizontal layer of fluid of depth $d$, described by the [[Boussinesq approximation|TXQQQG9T2S]].
Let $g$ be the gravitational acceleration, $\beta$ the thermal expansion coefficient, $\nu$ the kinematic [[viscosity|NM5Q4845Z4]] and $\kappa$ the thermal diffusivity.
Assume the bottom is held at a temperature larger by $\Delta T$ than the top.
The *Rayleigh number* of the layer is
$$\mathrm{Ra} = \frac{g \beta \, \Delta T \, d^3}{\nu \kappa}.$$

## Remarks

In dimensionless form the Boussinesq equations of the layer depend only on $\mathrm{Ra}$ and the [[Prandtl number|C4KSBMR413]] $\mathrm{Pr} = \nu / \kappa$.
Linear stability theory gives the critical value at which the conductive state becomes unstable: $\mathrm{Ra}_c \approx 1708$ for two rigid no-slip plates, and $\mathrm{Ra}_c = 27 \pi^4 / 4 \approx 657.5$ for two stress-free boundaries.

Example: a water layer with $d = 1$ cm, $\Delta T = 1$ K, $\beta \approx 2 \times 10^{-4}$ K$^{-1}$, $\nu \approx 10^{-6}$ m$^2$/s and $\kappa \approx 1.4 \times 10^{-7}$ m$^2$/s has $\mathrm{Ra} \approx 9.81 \cdot 2 \times 10^{-4} \cdot 10^{-6} / (1.4 \times 10^{-13}) \approx 1.4 \times 10^{4}$, above the critical value, so it convects.

Non-example: if the top is warmer than the bottom, $\Delta T < 0$ and $\mathrm{Ra} < 0$; the layer is stably stratified and never starts to convect, whatever the magnitude.
