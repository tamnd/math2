---
tag: 13FGKM7NQ0
kind: concept
name: Euler–Bernoulli beam equation
msc: [74K10, 74B05, 34B60]
specializes: [GDM0J9ZCBT]
sources:
  - url: https://en.wikipedia.org/wiki/Euler–Bernoulli_beam_theory
same_as:
  wikidata: Q805099
  wikipedia: Euler–Bernoulli beam theory
---

## Summary

The Euler–Bernoulli beam equation $(EI w'')'' = q$ gives the deflection $w$ of a slender elastic beam under a transverse load $q$.
It is the simplest and most used [[beam theory|GDM0J9ZCBT]], and it assumes that cross-sections stay plane and perpendicular to the bent axis.
The bending stiffness $EI$ is the product of [[Young's modulus|T8ENJX1905]] and the [[second moment of area|1QCSARFXQ0]] of the cross-section.
It underlies the design of beams, shafts and frames, and its dynamic form describes the vibrations of rods.

## Explanations

### L1 human

A beam bends more where the bending moment is large and where the beam is soft or thin.
The equation says that the curvature of the beam equals the bending moment divided by the stiffness $EI$.
Since the moment itself comes from the loads, two more derivatives link the curvature to the load, which gives a fourth-order equation.
A cantilever of length $L$ with a weight $P$ at its tip bends down by $PL^3/(3EI)$ at the tip.
So doubling the length makes the tip drop eight times as far.
