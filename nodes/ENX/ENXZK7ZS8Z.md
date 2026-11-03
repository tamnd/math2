---
tag: ENXZK7ZS8Z
kind: definition
name: Drag coefficient
msc: [76D05, 76G25]
defines: NZ4E3K1J59
uses: [JH9EJ0HA0R]
sources:
  - url: https://en.wikipedia.org/wiki/Drag_coefficient
---

## Definition

Let a body move with constant speed $U > 0$ relative to a fluid of density $\rho > 0$.
Let $A > 0$ be a chosen reference area of the body, such as its frontal area.
Let $F_D$ be the component, along the direction of the relative flow, of the force that the fluid exerts on the body.
The *drag coefficient* of the body is
$$C_D = \frac{2 F_D}{\rho U^2 A}.$$
The quantity $\frac12 \rho U^2$ is the dynamic pressure.

## Remarks

Example: for a sphere of radius $a$ at small [[Reynolds number|JH9EJ0HA0R]], Stokes' law gives $F_D = 6 \pi \mu a U$.
With $A = \pi a^2$ this gives $C_D = \frac{12 \mu}{\rho U a} = \frac{24}{\mathrm{Re}}$, where $\mathrm{Re} = 2 \rho U a / \mu$.

Non-example: the force component perpendicular to the flow does not enter $C_D$; divided in the same way it gives the lift coefficient $C_L$.

The value of $C_D$ depends on the choice of $A$, so the reference area must always be stated; for wings one usually takes the wing area.
