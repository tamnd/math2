---
tag: EPND9BNW82
kind: definition
name: Prandtl number
msc: [76M55, 76R05, 80A19]
defines: C4KSBMR413
uses: [T3R5FWV91P, NM5Q4845Z4]
sources:
  - url: https://en.wikipedia.org/wiki/Prandtl_number
---

## Definition

Consider a fluid with density $\rho$, dynamic [[viscosity|NM5Q4845Z4]] $\mu$, specific heat capacity at constant pressure $c_p$ and thermal conductivity $k$.
Let $\nu = \mu / \rho$ be its kinematic viscosity and $\alpha = k / (\rho c_p)$ its thermal diffusivity.
The *Prandtl number* of the fluid is
$$\mathrm{Pr} = \frac{\nu}{\alpha} = \frac{c_p \mu}{k}.$$

## Remarks

It is a [[dimensionless number|T3R5FWV91P]]: $\nu$ and $\alpha$ both have dimension $\mathsf{L}^2 \mathsf{T}^{-1}$.
Example: air at room temperature has $\mathrm{Pr} \approx 0.7$, and water has $\mathrm{Pr} \approx 7$.
Non-example: the ratio $\mu / k$ is not the Prandtl number; it is not dimensionless, since the factor $c_p$ is missing.
For $\mathrm{Pr} \gg 1$ the thermal boundary layer is thinner than the velocity boundary layer, and for $\mathrm{Pr} \ll 1$ (as in liquid metals) it is thicker.
