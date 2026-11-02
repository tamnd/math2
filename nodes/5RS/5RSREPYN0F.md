---
tag: 5RSREPYN0F
kind: concept
name: Homogenization
msc: [35B27, 74Q05, 35J15]
sources:
  - url: https://en.wikipedia.org/wiki/Asymptotic_homogenization
---

## Summary

Homogenization is the study of partial differential equations whose coefficients oscillate on a small scale $\varepsilon$, in the limit $\varepsilon \to 0$.
The solutions converge to the solution of a *homogenized* equation with effective, slowly varying or constant coefficients.
For periodic media the effective coefficients are computed from a cell problem on one period.
It explains, for example, the effective conductivity of a composite material made of a fine mixture of two materials.

## Explanations

### L1 human

Look at a material made of many thin alternating layers of copper and plastic.
At the scale of the whole piece, heat flows as if through one uniform material with some average conductivity.
Homogenization computes this average, which is in general not the plain arithmetic mean.
Across the layers, heat must cross both materials in series, and the effective conductivity is the harmonic mean, as for resistors in series.
Along the layers, heat flows through both in parallel, and the effective conductivity is the arithmetic mean.
