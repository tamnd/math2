---
tag: MB509A4TAG
kind: definition
name: Thermal diffusivity
msc: [80A19, 35K05]
defines: CS4ZZX092Z
uses: [XBQBT9E7JT, SYYGZ18FF5, VP2HN86VAG]
sources:
  - url: https://en.wikipedia.org/wiki/Thermal_diffusivity
---

## Definition

Let a homogeneous material have [[thermal conductivity|XBQBT9E7JT]] $k > 0$, density $\rho > 0$ and specific [[heat capacity|SYYGZ18FF5]] at constant pressure $c_p > 0$.
Its *thermal diffusivity* is
$$\alpha = \frac{k}{\rho \, c_p}.$$
Its unit is $\mathrm{m^2 \, s^{-1}}$.

## Remarks

With constant $\alpha$, conduction without heat sources obeys the [[heat equation|VP2HN86VAG]] $\partial_t T = \alpha \Delta T$.

Example: for copper, $k \approx 400$, $\rho \approx 8900$ and $c_p \approx 385$ in SI units.
So $\alpha \approx 400 / (8900 \cdot 385) \approx 1.2 \cdot 10^{-4}$ square metres per second.

Non-example: the conductivity $k$ alone is not the diffusivity.
Two materials with the same $k$ but different heat capacities warm at different rates.

The ratio $\nu / \alpha$, where $\nu$ is the kinematic viscosity of a fluid, is the [[Prandtl number|C4KSBMR413]].
