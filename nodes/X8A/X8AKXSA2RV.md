---
tag: X8AKXSA2RV
kind: concept
name: Stress deviator tensor
msc: [74A10, 74C05]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy_stress_tensor
    locator: Stress deviator tensor
---

## Summary

The stress deviator tensor is what remains of the [[Cauchy stress tensor|KG2XWEMJ30]] after its mean, hydrostatic part is removed: $s = \sigma - \tfrac13 (\operatorname{tr} \sigma) I$.
The hydrostatic part tends to change volume, while the deviator tends to change shape.
Because metals yield by changes of shape, plasticity theory, for example the von Mises criterion, is written in terms of the deviator.

## Explanations

### L1 human

Deep under water a small object is squeezed equally from all sides; this changes its size but not its shape.
Stress in general is such an equal squeeze plus something else, and that something else is the deviator.
The deviator is the part that distorts shapes, for example turning a cube into a slanted box.
For water at rest the deviator is zero.
