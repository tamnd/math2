---
tag: X2FXX4Z4F8
kind: statement
role: fact
name: Kozeny–Carman equation
msc: [76S05]
uses: [DX8RV2XG6H, NM5Q4845Z4]
about: [DX8RV2XG6H]
sources:
  - url: https://en.wikipedia.org/wiki/Kozeny%E2%80%93Carman_equation
same_as:
  wikidata: Q1043489
  wikipedia: Kozeny–Carman equation
---

## Statement

Consider slow, steady, laminar flow of a fluid with dynamic [[viscosity|NM5Q4845Z4]] $\mu$ through a packed bed of solid particles of length $L$.
Let $\varepsilon \in (0, 1)$ be the porosity of the bed, $D_p$ the particle diameter and $\Phi_s \in (0, 1]$ the sphericity of the particles.
Let $u_s$ be the superficial velocity, the volume flow rate per unit cross-sectional area of the bed.
The Kozeny–Carman equation states that the pressure drop $\Delta p$ across the bed is
$$\frac{\Delta p}{L} = \frac{180 \, \mu}{\Phi_s^2 D_p^2} \, \frac{(1 - \varepsilon)^2}{\varepsilon^3} \, u_s.$$
Equivalently, the bed obeys [[Darcy's law|DX8RV2XG6H]] $u_s = (k / \mu)(\Delta p / L)$ with permeability
$$k = \frac{\Phi_s^2 D_p^2 \, \varepsilon^3}{180 \, (1 - \varepsilon)^2}.$$

## Remarks

The relation is semi-empirical.
Its form comes from modelling the pore space as a bundle of tortuous capillary tubes whose hydraulic diameter is proportional to $\varepsilon D_p / (1 - \varepsilon)$, and applying the Hagen–Poiseuille law in each tube.
The constant $180$ is fitted to experiments on beds of near-spherical particles.

Example: for a bed of spheres ($\Phi_s = 1$) with $D_p = 1$ mm and $\varepsilon = 0.4$, the permeability is $k = 10^{-6} \cdot 0.064 / (180 \cdot 0.36) \approx 9.9 \times 10^{-10}$ m$^2$.

The equation needs laminar flow through the pores.
At larger pore Reynolds numbers inertial losses grow like $u_s^2$, and the Ergun equation adds such a term.

## Explanations

### L1 human

Water seeping through sand meets more resistance when the grains are finer and when they are packed more tightly.
The Kozeny–Carman equation turns this into a formula: the resistance grows like one over the square of the grain size, and very fast as the empty space between grains shrinks.
It lets engineers estimate how easily fluid passes through a filter or a soil from the grain size and the porosity alone.

### L2 human

Darcy's law says that flow through a porous medium is proportional to the pressure gradient, but it does not say what the permeability is.
The Kozeny–Carman relation supplies the permeability of a packed bed from its geometry.
The factor $\varepsilon^3 / (1 - \varepsilon)^2$ shows the strong dependence on porosity: halving the porosity from $0.4$ to $0.2$ lowers the permeability by a factor of about $14$.
It is used in filtration, chemical reactors, soil mechanics and models of compaction.
