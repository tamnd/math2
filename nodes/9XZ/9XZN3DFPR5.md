---
tag: 9XZN3DFPR5
kind: definition
name: Cavitation
msc: [76B10, 76T10]
defines: K544PYSW2A
uses: [A3Q9SNF86Q]
sources:
  - url: https://en.wikipedia.org/wiki/Cavitation
---

## Definition

Consider a liquid in motion, with pressure $p(x, t)$, at a temperature at which its vapour pressure is $p_v$.
*Cavitation* is the formation of cavities filled with vapour, or with vapour and gas, in the regions where $p$ falls below $p_v$.
The term includes the growth of these cavities and their collapse when they reach regions where $p > p_v$.
The flow is then a [[multiphase flow|A3Q9SNF86Q]] of liquid and vapour.
For a flow with reference pressure $p_\infty$, reference speed $U$ and liquid density $\rho$, the *cavitation number* is
$$\sigma = \frac{p_\infty - p_v}{\frac{1}{2} \rho U^2}.$$

## Remarks

Cavitation starts roughly when $\sigma$ drops below $-C_{p,\min}$, where $C_{p,\min}$ is the minimum pressure coefficient of the flow.
In practice nuclei such as small gas bubbles and impurities shift the onset.

Example: water at $20$ °C has $p_v \approx 2.3$ kPa; at a point of a propeller blade where the local pressure falls to $1$ kPa, vapour cavities form.

Non-example: boiling in a kettle is not cavitation; there the vapour forms because the temperature rises at constant pressure, not because the pressure drops.

The collapse of a cavity can produce local pressures large enough to damage solid surfaces, which is called cavitation erosion.
