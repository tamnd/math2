---
tag: AWQVZ0H24T
kind: definition
name: Equivalent potential temperature
msc: [86A10, 80A10]
defines: 50GYDF3XWJ
uses: [SJTMRNXFZ3]
sources:
  - url: https://en.wikipedia.org/wiki/Equivalent_potential_temperature
---

## Definition

Consider a parcel of moist air with pressure $p$, temperature $T$ and water vapour mixing ratio $r \ge 0$ (mass of vapour per mass of dry air).
Lift the parcel adiabatically until all its water vapour has condensed and the condensate has fallen out.
Then the latent heat of condensation has been added to the air.
Then bring the dry parcel adiabatically to the reference pressure $p_0 = 1000$ hPa.
The *equivalent potential temperature* $\theta_e$ of the parcel is its temperature at the end of this process.

## Remarks

Equivalently, $\theta_e$ is the [[potential temperature|SJTMRNXFZ3]] of the parcel after the release of all its latent heat.
A common approximation is
$$\theta_e \approx \theta \exp\left( \frac{L_v r}{c_p T_L} \right).$$
Here $\theta$ is the potential temperature and $L_v$ is the latent heat of vaporisation.
Also $c_p$ is the specific heat of dry air at constant pressure and $T_L$ is the temperature at the lifting condensation level.
More accurate empirical formulas are used in practice.

Example: with $\theta = 300$ K, $r = 0.015$, $L_v = 2.5 \times 10^6$ J/kg, $c_p = 1005$ J/(kg K) and $T_L = 290$ K, the exponent is about $0.129$ and $\theta_e \approx 341$ K.
For dry air, $r = 0$ and $\theta_e = \theta$.

Non-example: if heat is added to the parcel from outside, for example by radiation or by mixing with other air, $\theta_e$ changes.
It is conserved only under dry and moist adiabatic processes, and only approximately in the second case.

A layer in which $\theta_e$ decreases with height is called potentially unstable: it becomes unstable when lifted to saturation as a whole.
