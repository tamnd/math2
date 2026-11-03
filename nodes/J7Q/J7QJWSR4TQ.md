---
tag: J7QJWSR4TQ
kind: definition
name: Natural convection
msc: [76R10, 80A19]
defines: R2KHGJ2N7V
uses: [RK24AYNG4Z, KK46Q2YV1D]
sources:
  - url: https://en.wikipedia.org/wiki/Convection
---

## Definition

Consider a fluid in a gravitational field with acceleration $g$, whose density depends on its [[temperature|KK46Q2YV1D]].
*Natural convection* (or *free convection*) is [[convective heat transfer|RK24AYNG4Z]] in which the motion of the fluid is caused only by buoyancy forces.
These forces arise from density differences due to temperature differences.
No flow is imposed from outside, by a pump, a fan, a moving body or a free stream.

## Remarks

Example: still air around a hot vertical plate.
The air near the plate is warmer and so lighter than the air far away, so it rises along the plate and carries heat away, with no outside forcing.

Non-example: the same plate in the air stream of a fan.
The flow is imposed from outside, so this is forced convection.
A fluid layer heated from above also shows no natural convection: the warm light fluid is already on top, the layering is stable, and heat moves by conduction only.

In models one often uses the Boussinesq approximation $\rho = \rho_0 \big(1 - \beta (T - T_0)\big)$ in the buoyancy term only, where $\beta$ is the thermal expansion coefficient.
The strength of the buoyant flow is measured by the Grashof number $\mathrm{Gr} = g \beta \Delta T L^3 / \nu^2$ and the Rayleigh number $\mathrm{Ra} = \mathrm{Gr} \Pr$.
Here $\Delta T$ is a temperature difference, $L$ a length and $\nu$ the kinematic viscosity.
