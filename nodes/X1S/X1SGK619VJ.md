---
tag: X1SGK619VJ
kind: concept
name: Biharmonic plate equation
msc: [74K20, 35J30, 74G05]
sources:
  - url: https://en.wikipedia.org/wiki/Kirchhoff–Love_plate_theory
---

## Summary

The biharmonic plate equation $D \Delta^2 w = q$ gives the deflection $w$ of a thin elastic plate under a transverse load $q$.
It is the main equation of linear [[Kirchhoff–Love plate theory|9E6E0SCEYA]], with bending stiffness $D = Eh^3/(12(1 - \nu^2))$.
It is a fourth-order elliptic equation built from the [[biharmonic|AS8A9F5SKE]] operator, and a clamped or simply supported edge supplies two boundary conditions.
It is the two-dimensional analogue of the [[Euler–Bernoulli beam equation|13FGKM7NQ0]] $EI w'''' = q$.

## Explanations

### L1 human

A thin plate bends under a load in a way that depends on its stiffness and on how its edges are held.
The equation says that applying the Laplace operator twice to the deflection gives the load divided by the stiffness.
Applying the Laplacian twice measures how the curvature of the surface changes from point to point.
For a round plate of radius $a$ clamped at its rim and loaded evenly by $q$, the centre sinks by $qa^4/(64D)$.
