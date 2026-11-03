---
tag: FMF327F0MV
kind: definition
name: Maxwell–Bloch equations
msc: [78A60, 81V80]
defines: H8Z49EWR5Q
uses: [9BWWD4QK8Y, ASQAH710WN, 07VX34QXAV, ZMRAWA0HE2]
sources:
  - url: https://en.wikipedia.org/wiki/Maxwell%E2%80%93Bloch_equations
---

## Definition

Consider a single-mode laser cavity filled with identical two-level atoms whose transition is resonant with the mode.
Let $E(t)$ be the real amplitude of the field, $P(t)$ the real amplitude of the atomic [[polarization|ASQAH710WN]], and $D(t)$ the population inversion, in suitable units.
Let $\kappa > 0$, $\gamma_\perp > 0$ and $\gamma_\parallel > 0$ be the decay rates of the field, the polarization and the inversion.
Let $D_0$ be the inversion set by the pump, and $g > 0$ the coupling constant.
In one common normalization, the *Maxwell–Bloch equations* for this laser are the system of [[ordinary differential equations|07VX34QXAV]]
$$\frac{dE}{dt} = -\kappa E + g P, \qquad \frac{dP}{dt} = -\gamma_\perp P + g E D, \qquad \frac{dD}{dt} = -\gamma_\parallel (D - D_0) - 4 g E P.$$

## Remarks

The first equation comes from [[Maxwell's equations|9BWWD4QK8Y]] in the cavity, with the polarization as source.
The other two are the optical Bloch equations of the atoms driven by the field.
Without damping and pumping, the quantity $P^2 + D^2/4$ is conserved, which is the conservation of the length of the Bloch vector.
In travelling-wave problems, the field equation is a partial differential equation in space and time instead.

Example: $E = P = 0$, $D = D_0$ is always a steady state, the laser off.
For $D_0 > \kappa \gamma_\perp / g^2$ there are also steady states with $E \ne 0$ and $D = \kappa \gamma_\perp / g^2$, the laser on.

Non-example: the [[laser rate equations|ZMRAWA0HE2]] are not Maxwell–Bloch equations, since they contain no equation for the polarization $P$.
They follow from the Maxwell–Bloch equations when $\gamma_\perp$ is much larger than the other rates and $P$ is eliminated.
