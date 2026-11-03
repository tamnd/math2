---
tag: N5G8WNQFC3
kind: concept
name: Cauchy–Green deformation tensor
msc: [74A05]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_strain_theory
    locator: Deformation tensors
---

## Summary

The right Cauchy–Green deformation tensor is $C = F^T F$ and the left one is $b = F F^T$, where $F$ is the [[deformation gradient|HTYRR2WDQ6]].
They remove the rotation part of $F$ and keep only the stretching.
The tensor $C$ gives the squared length of a deformed line element in terms of the undeformed one.
They are symmetric and positive definite, and they equal the identity exactly when the deformation is locally rigid.

## Explanations

### L1 human

The deformation gradient mixes two effects: turning and stretching.
Squaring away the turning, as in $F^T F$, leaves a tensor that only sees changes of length and angle.
If a tiny arrow $dX$ becomes $F\, dX$, its new squared length is $dX \cdot C\, dX$.
For a pure rotation $F = Q$ this gives $C = Q^T Q = I$: nothing is stretched.
