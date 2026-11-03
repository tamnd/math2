---
tag: YF5RQH30XH
kind: definition
name: Weber number
msc: [76M55, 76D45, 76T10]
defines: ZKGDMA1WZG
uses: [T3R5FWV91P]
sources:
  - url: https://en.wikipedia.org/wiki/Weber_number
---

## Definition

Consider a flow with an interface between two fluids, with surface tension $\sigma$ on the interface.
Let $\rho$ be the density of the relevant fluid, $U$ a characteristic speed and $L$ a characteristic length, such as the diameter of a drop.
The *Weber number* is
$$\mathrm{We} = \frac{\rho U^2 L}{\sigma}.$$

## Remarks

It is a [[dimensionless number|T3R5FWV91P]]: surface tension has dimension $\mathsf{M} \mathsf{T}^{-2}$, the same as $\rho U^2 L$.
Example: a water drop of diameter $L = 1\ \mathrm{mm}$ moving at $U = 1\ \mathrm{m/s}$, with $\rho = 1000\ \mathrm{kg/m^3}$ and $\sigma \approx 0.072\ \mathrm{N/m}$, has $\mathrm{We} \approx 14$.
Non-example: $\rho U L / \sigma$ is not a Weber number; it has dimension $\mathsf{T}/\mathsf{L}$, since one factor of the speed is missing.
The Weber number is the ratio of the dynamic pressure $\rho U^2$ to the capillary pressure scale $\sigma / L$.
