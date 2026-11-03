---
tag: MRANPXATRD
kind: concept
name: Green–Lagrange strain tensor
msc: [74A05]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_strain_theory
    locator: Finite strain tensors
---

## Summary

The Green–Lagrange strain tensor is $E = \tfrac12 (F^T F - I)$, where $F$ is the [[deformation gradient|HTYRR2WDQ6]].
It is a finite measure of strain: it vanishes exactly for locally rigid motions, whatever the size of the rotation.
Its linear part in the displacement gradient is the infinitesimal [[strain tensor|8QS6QMJF5Z]].

## Explanations

### L1 human

Strain should be zero when a body is only moved and turned, not stretched.
The Green–Lagrange tensor has this property for rotations of any size, which the small-strain formula lacks.
If a tiny arrow of length $\ell$ becomes an arrow of length $\ell'$, then $(\ell'^2 - \ell^2)/2$ is read off from $E$.
For a uniform stretch by a factor $2$ along one axis, the corresponding entry of $E$ is $(4 - 1)/2 = 3/2$.
