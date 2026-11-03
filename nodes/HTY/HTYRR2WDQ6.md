---
tag: HTYRR2WDQ6
kind: concept
name: Deformation gradient
msc: [74A05]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_strain_theory
    locator: Deformation gradient tensor
---

## Summary

The deformation gradient is the derivative $F = \nabla \varphi$ of a [[deformation|E51Y1CMF1Q]] $\varphi$.
It maps a small material line element in the reference configuration to its image in the deformed configuration.
It carries all local information on stretching and rotation, and its determinant gives the local change of volume.
All finite strain measures, such as the [[Cauchy–Green deformation tensor|N5G8WNQFC3]], are built from it.

## Explanations

### L1 human

Zoom in on a tiny square drawn on a rubber sheet before stretching.
After the deformation the square has become, to first order, a parallelogram.
The deformation gradient is the linear map that turns the small square into that parallelogram.
For the shear $\varphi(X) = (X_1 + \gamma X_2, X_2, X_3)$ it is the matrix with rows $(1, \gamma, 0)$, $(0, 1, 0)$, $(0, 0, 1)$, which slants squares but keeps their area.
