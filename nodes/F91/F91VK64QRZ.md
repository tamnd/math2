---
tag: F91VK64QRZ
kind: concept
name: Koiter shell model
msc: [74K25, 74B05, 74G65]
specializes: [DF7RPJHHY1]
sources:
  - url: https://en.wikipedia.org/wiki/Plate_theory
---

## Summary

The Koiter shell model is a two-dimensional [[shell theory|DF7RPJHHY1]] for thin linearly elastic shells, due to W. T. Koiter.
Its energy is the sum of a membrane term and a bending term.
The membrane term is proportional to the thickness and quadratic in the change of metric of the middle surface.
The bending term is proportional to the cube of the thickness and quadratic in the change of curvature.
It is the shell analogue of [[Kirchhoff–Love plate theory|9E6E0SCEYA]], and it is widely used in the mathematical analysis of shells.
It exists in a nonlinear form and in a linearised form.

## Explanations

### L1 human

A shell can deform in two ways: by stretching its surface and by changing how its surface curves.
Stretching is expensive, and its cost grows with the thickness.
Bending is cheap for a thin shell, and its cost grows with the cube of the thickness.
The Koiter model adds these two costs, and the shape the shell takes under a load is the one that minimises the total energy minus the work of the load.
