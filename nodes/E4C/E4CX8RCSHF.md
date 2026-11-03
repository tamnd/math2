---
tag: E4CX8RCSHF
kind: statement
role: proposition
name: Adams–Williamson equation
msc: [86A15, 86A04]
uses: [EEPJJHC5JZ, GZ7E9GHQYB, PPXM3HCN6Y, 29WRN5J730]
about: [PPXM3HCN6Y]
sources:
  - url: https://en.wikipedia.org/wiki/Adams%E2%80%93Williamson_equation
same_as:
  wikidata: Q4680537
  wikipedia: Adams–Williamson equation
---

## Statement

Let a spherically symmetric planet be in hydrostatic equilibrium, with density $\rho(r)$ and pressure $P(r)$ at radius $r$.
Let $m(r)$ be the mass inside radius $r$, $G$ the gravitational constant, and $g(r) = G m(r)/r^2$ the gravity.
Let $\alpha(r)$ and $\beta(r)$ be the [[P-wave|EEPJJHC5JZ]] and [[S-wave|GZ7E9GHQYB]] speeds, and let
$$\Phi = \alpha^2 - \tfrac43 \beta^2 = \frac{K_S}{\rho}$$
be the seismic parameter, where $K_S$ is the adiabatic [[bulk modulus|PPXM3HCN6Y]].
Assume that, in a shell $r_1 < r < r_2$, the composition and phase do not change and the temperature follows an adiabat.
Then in this shell
$$\frac{d\rho}{dr} = -\frac{\rho(r)\, g(r)}{\Phi(r)}.$$

## Remarks

Hydrostatic equilibrium gives $dP/dr = -\rho g$.
Under the assumptions, density changes only by adiabatic compression, so $d\rho/dP = \rho/K_S = 1/\Phi$.
The chain rule $d\rho/dr = (d\rho/dP)(dP/dr)$ gives the equation.
Example: $\Phi$ is known from seismology, and $g = Gm/r^2$ by [[Newton's law of gravitation|29WRN5J730]].
So the equation and $dm/dr = 4\pi r^2 \rho$ form a closed system of ordinary differential equations for $\rho$ and $m$.
It is integrated inward from a starting density and the total mass.
The mantle and core masses must also match the total mass and the moment of inertia of the Earth.
The adiabatic and uniform-composition hypotheses are necessary: across a phase change, such as near $660$ km depth, or in a thermal boundary layer, the density does not follow the equation.
The Bullen parameter measures this departure.

## Explanations

### L1 human

Deep rock is squeezed by the weight of the rock above it, so it is denser.
How much denser depends on how hard the rock is to squeeze, and seismic waves measure exactly this stiffness.
The Adams–Williamson equation turns this into a formula for how density grows with depth.
It was the first way to estimate the density inside the Earth from seismic speeds.

### L2 human

The key identity is $\alpha^2 - \frac43\beta^2 = K_S/\rho$, which follows from $\alpha^2 = (K + \frac43\mu)/\rho$ and $\beta^2 = \mu/\rho$.
So seismology gives $K_S/\rho$ but not $\rho$ itself, and hydrostatics supplies the missing relation.
In Earth models the equation is used piecewise within each region, with jumps in density placed at seismic discontinuities.
These jumps are then fixed by the mass and the moment of inertia, and today also by the frequencies of the normal modes.
