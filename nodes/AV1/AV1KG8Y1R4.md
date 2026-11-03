---
tag: AV1KG8Y1R4
kind: definition
name: Accretion disk
msc: [85A30, 76U05, "76E07"]
defines: 6ADKW56QGV
uses: [7147M98XNR, NM5Q4845Z4, M1A7XV292M]
sources:
  - url: https://en.wikipedia.org/wiki/Accretion_disk
---

## Definition

Let a central body of mass $M$ be surrounded by gas, and let $G$ be the gravitational constant.
An *accretion disk* is a configuration of the gas with the following properties:

1. The gas is concentrated near a plane through the central body, with a thickness $H(r)$ much smaller than the distance $r$ from the centre.
2. The gas rotates around the centre on nearly circular orbits with angular velocity close to the Keplerian value $\Omega_K(r) = \sqrt{G M / r^3}$, as given by [[Kepler's laws|M1A7XV292M]].
3. Internal stresses, such as [[viscosity|NM5Q4845Z4]] or turbulence, transport [[angular momentum|7147M98XNR]] outward.
   As a result the gas drifts inward with radial speed much smaller than the orbital speed.

## Remarks

Example: take a steady, thin, optically thick disk with accretion rate $\dot M$ and inner edge $r_{\text{in}}$, where the stress vanishes.
If the energy released locally is radiated from both faces, the surface temperature satisfies $\sigma T^4(r) = \frac{3 G M \dot M}{8\pi r^3} \left( 1 - \sqrt{r_{\text{in}} / r} \right)$.
Here $\sigma$ is the Stefan–Boltzmann constant.
Non-example: gas without angular momentum falling radially onto the central body, as in [[Bondi accretion|BB23EKZ2QS]], is accreted but forms no disk.
It is not an accretion disk, because it neither rotates nor is concentrated near a plane, so clauses 1 and 2 fail.
Molecular viscosity is far too small to explain observed inflow rates, so the stress is attributed to turbulence.
The [[Shakura–Sunyaev alpha disk model|E5GR4K48B5]] models it, and the [[magnetorotational instability|FBBJFNC7RC]] is thought to cause it.
