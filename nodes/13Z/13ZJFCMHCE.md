---
tag: 13ZJFCMHCE
kind: definition
name: Convective available potential energy
msc: [86A10]
defines: 33GSXYK10W
uses: [ZPXXA62VQB]
sources:
  - url: https://en.wikipedia.org/wiki/Convective_available_potential_energy
---

## Definition

Consider a hydrostatic atmosphere with gravitational acceleration $g$.
Lift an air parcel from near the surface, dry adiabatically up to saturation and then moist adiabatically.
Let $T_{v,p}(z)$ be the virtual temperature of the parcel and $T_{v,e}(z)$ that of the environment at height $z$.
The *level of free convection* $z_f$ is the lowest height above which the parcel is warmer than the environment, $T_{v,p} > T_{v,e}$.
The *equilibrium level* $z_n > z_f$ is the height above $z_f$ at which the parcel first becomes as cold as the environment again.
The *convective available potential energy* is
$$\mathrm{CAPE} = \int_{z_f}^{z_n} g \, \frac{T_{v,p}(z) - T_{v,e}(z)}{T_{v,e}(z)} \, dz.$$
If there is no level of free convection, $\mathrm{CAPE} = 0$.

## Remarks

The integrand is the buoyancy acceleration of the parcel, so CAPE has units of J/kg.
With the hydrostatic relation and the ideal gas law, CAPE $= R_d \int_{p_n}^{p_f} (T_{v,p} - T_{v,e}) \, d \ln p$, where $R_d$ is the gas constant of dry air and $p_f$, $p_n$ are the pressures at $z_f$ and $z_n$.
The negative buoyancy below $z_f$ gives the convective inhibition.

Example: if $T_{v,e} = 300$ K and $T_{v,p} - T_{v,e} = 3$ K on the whole layer from $z_f = 1$ km to $z_n = 11$ km, then CAPE $= 9.81 \cdot 0.01 \cdot 10^4 \approx 981$ J/kg.
Parcel theory then bounds the updraught speed by $\sqrt{2 \, \mathrm{CAPE}} \approx 44$ m/s.

Non-example: suppose the environmental [[lapse rate|ZPXXA62VQB]] is smaller than the moist adiabatic lapse rate at every level.
Then a lifted parcel stays colder than its surroundings, there is no level of free convection, and CAPE is zero.
