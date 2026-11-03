---
tag: GPRRR97BYG
kind: definition
name: Hadley cell and Held–Hou model
msc: [86A10, 76U60]
defines: D7RF8J0HWK
uses: [73GW90ST91, 6HZRX3WSQD]
sources:
  - url: https://en.wikipedia.org/wiki/Hadley_cell
---

## Definition

Consider an atmosphere on a planet of radius $a$ rotating with angular speed $\Omega$, with gravitational acceleration $g$ and latitude $\varphi$.
A *Hadley cell* is a thermally direct meridional overturning circulation of the zonally averaged flow.
It has rising motion near the equator, poleward flow aloft, sinking in the subtropics and equatorward flow near the surface.

The *Held–Hou model* is the steady, axisymmetric model of such a cell in a Boussinesq atmosphere of depth $H$ with the following assumptions.

1. Without the circulation the atmosphere would be in radiative equilibrium. Its potential temperature would decrease from equator to pole by the fraction $\Delta_H$ of a reference value $\theta_0$.
2. The upper, poleward branch conserves angular momentum and starts from rest at the equator, so its zonal wind is $u_M(\varphi) = \Omega a \sin^2 \varphi / \cos \varphi$.
3. The temperature in the cell is in [[thermal wind|73GW90ST91]] balance with $u_M$.
4. The temperature is continuous at the poleward edge $\varphi_H$ of the cell. The cell neither gains nor loses heat in total, so its mean temperature equals the mean radiative equilibrium temperature.

## Remarks

In the small-angle approximation these assumptions determine the edge of the cell,
$$\varphi_H = \left( \frac{5}{3} \frac{g H \Delta_H}{\Omega^2 a^2} \right)^{1/2}.$$
Example: for the Earth, $g = 9.81$ m/s$^2$, $H = 10^4$ m, $\Delta_H = 1/3$, $\Omega = 7.29 \times 10^{-5}$ s$^{-1}$ and $a = 6.37 \times 10^6$ m give $\varphi_H \approx 0.5$ rad, about $29^\circ$, close to the observed edge of the Hadley cell.
The model predicts a strong westerly jet at $\varphi_H$ and, by [[Coriolis|6HZRX3WSQD]] deflection of the return flow, easterly winds near the surface in the tropics.

Non-example: the observed winds in the upper branch are weaker than $u_M$, because eddies carry momentum.
A flow with such eddy fluxes does not satisfy assumption 2, and the model overestimates the subtropical jet.

The model also predicts that the cell widens as $\Omega$ decreases, a trend seen in simulations of slowly rotating planets.
