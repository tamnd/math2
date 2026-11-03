---
tag: 9XCA2BB7KW
kind: definition
name: Knudsen number
msc: [76P05, 82C40]
defines: 22V2W7KB1D
uses: [HHTG8JVGKQ, GFHJ858AN1, JH9EJ0HA0R]
sources:
  - url: https://en.wikipedia.org/wiki/Knudsen_number
---

## Definition

Consider a flow of a gas with a characteristic length $L > 0$, such as the size of a body or the width of a channel.
Let $\lambda > 0$ be the mean free path of the gas molecules, the mean distance travelled between two successive collisions.
The *Knudsen number* is the dimensionless number
$$\mathrm{Kn} = \frac{\lambda}{L}.$$

## Remarks

For a gas of hard spheres of diameter $d$ at pressure $p$ and temperature $T$, the mean free path is $\lambda = \dfrac{kT}{\sqrt{2}\, \pi d^2 p}$, where $k$ is the Boltzmann constant.
For an ideal gas with adiabatic exponent $\gamma$, it is related to the [[Mach number|GFHJ858AN1]] $\mathrm{Ma}$ and the [[Reynolds number|JH9EJ0HA0R]] $\mathrm{Re}$ by $\mathrm{Kn} = \dfrac{\mathrm{Ma}}{\mathrm{Re}} \sqrt{\dfrac{\gamma \pi}{2}}$.
Commonly quoted regimes are continuum flow for $\mathrm{Kn} < 0.01$, slip flow for $0.01 < \mathrm{Kn} < 0.1$, transitional flow for $0.1 < \mathrm{Kn} < 10$ and free molecular flow for $\mathrm{Kn} > 10$; the limits are conventions.
In the scaled Boltzmann equation the Knudsen number multiplies the transport term relative to the collision term.

Example: air at sea level has $\lambda \approx 68$ nm, so a flow past a body of size $L = 1$ m has $\mathrm{Kn} \approx 7 \times 10^{-8}$, deep in the continuum regime.

Non-example: the ratio of the molecular diameter to $L$ is not the Knudsen number.
It does not involve the density, while the mean free path grows as the gas becomes thinner.
