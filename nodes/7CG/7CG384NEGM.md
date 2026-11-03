---
tag: 7CG384NEGM
kind: definition
name: Atmospheric dynamics
msc: [86A10, 76U05]
defines: 78N8TY99FB
uses: [F2JRWJNYN4, 18KXZHVF4M, 6HZRX3WSQD, QANHETP404]
sources:
  - url: https://en.wikipedia.org/wiki/Meteorology
---

## Definition

*Atmospheric dynamics* is the study of the motion of the atmosphere of a rotating planet.
The atmosphere is modelled as a compressible gas under gravity, in a frame rotating with angular velocity $\boldsymbol{\Omega}$.
Its state is given by the velocity $\mathbf{u}$, pressure $p$, density $\rho$ and temperature $T$, which satisfy:

1. the momentum equation $\dfrac{D\mathbf{u}}{Dt} + 2 \boldsymbol{\Omega} \times \mathbf{u} = -\dfrac{1}{\rho} \nabla p + \mathbf{g} + \mathbf{F}$, where $D/Dt$ is the material derivative, $2\boldsymbol{\Omega} \times \mathbf{u}$ is the [[Coriolis term|6HZRX3WSQD]], $\mathbf{g}$ is the effective gravity and $\mathbf{F}$ is friction;
2. the continuity equation $\dfrac{D\rho}{Dt} + \rho \, \nabla \cdot \mathbf{u} = 0$;
3. the thermodynamic energy equation $c_p \dfrac{DT}{Dt} - \dfrac{1}{\rho} \dfrac{Dp}{Dt} = Q$, with $c_p$ the specific heat at constant pressure and $Q$ the heating rate per unit mass;
4. the ideal gas law $p = \rho R_d T$, with $R_d$ the gas constant of dry air.

## Remarks

These are the [[Navier–Stokes equations|18KXZHVF4M]] of a compressible ideal gas in a rotating frame, with heating.
For large-scale flow the vertical momentum equation is replaced by hydrostatic balance $\partial p/\partial z = -\rho g$, which gives the [[primitive equations|QANHETP404]].
Example: in geostrophic flow, the Coriolis term balances the horizontal pressure gradient, so $2\Omega \sin\varphi \, \hat{\mathbf{z}} \times \mathbf{u} = -\rho^{-1} \nabla_h p$ at latitude $\varphi$, and the wind blows along isobars.
Non-example: sound waves in a room obey clauses 1 to 4 with $\boldsymbol{\Omega}$ negligible, but they belong to acoustics.
Atmospheric dynamics is concerned with motions shaped by rotation, stratification or the planet's scale.
It is a branch of [[fluid dynamics|F2JRWJNYN4]] and the core of dynamical meteorology.
