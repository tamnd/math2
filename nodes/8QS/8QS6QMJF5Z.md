---
tag: 8QS6QMJF5Z
kind: concept
name: Strain tensor
msc: [74A05]
sources:
  - url: https://en.wikipedia.org/wiki/Strain_(mechanics)
---

## Summary

A strain tensor measures how a [[deformation|E51Y1CMF1Q]] changes lengths and angles near each point, ignoring rigid motion.
In the theory of small deformations it is the symmetric part of the displacement gradient, $\varepsilon = \tfrac12 (\nabla u + (\nabla u)^T)$.
Its diagonal entries are relative changes of length along the axes, and its off-diagonal entries are half the changes of right angles.

## Explanations

### L1 human

Strain is the relative amount of stretching.
A rod of length $1$ m that becomes $1.001$ m long has strain $0.001$ along its axis.
In three dimensions one needs a whole matrix of such numbers: stretches along each axis and shears between pairs of axes.
That symmetric $3 \times 3$ matrix, varying from point to point, is the strain tensor.
