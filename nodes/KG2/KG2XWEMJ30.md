---
tag: KG2XWEMJ30
kind: concept
name: Cauchy stress tensor
msc: [74A10]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy_stress_tensor
same_as:
  wikidata: Q13409892
  wikipedia: Cauchy stress tensor
---

## Summary

The Cauchy stress tensor $\sigma$ at a point of a deformed body is a linear map.
It sends the unit normal $n$ of a surface element to the traction $\sigma n$ across that element.
Its nine components in a basis give the [[stress|HXGCGHS070]] on the three coordinate planes and determine the stress on every other plane.
It is symmetric, by balance of angular momentum, and it is the true stress, measured per unit area of the deformed body.

## Explanations

### L1 human

At a point inside a loaded body there are infinitely many ways to cut, one for each direction.
Remarkably, the forces on all those cuts are encoded in one $3 \times 3$ matrix.
Its first column is the force per area on a cut facing the $x$-direction, and similarly for the other columns.
For water at pressure $p$, the matrix is $-p$ times the identity: every cut feels the same push, straight inward.
