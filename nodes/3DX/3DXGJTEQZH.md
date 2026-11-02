---
tag: 3DXGJTEQZH
kind: concept
name: Dirac operator
msc: [58J60, 47F05, 15A66]
specializes: [XY8GEQSWPR]
sources:
  - url: https://en.wikipedia.org/wiki/Dirac_operator
same_as:
  wikidata: Q907439
  wikipedia: Dirac operator
---

## Summary

A Dirac operator is a first-order differential operator $D$ whose square $D^2$ is a Laplace-type operator.
It is a formal square root of the [[Laplacian|0E0B6RA8K0]], made possible by coefficients in a [[Clifford algebra|A38B1QFK20]].
Dirac introduced such an operator to write a first-order relativistic equation for the electron, the [[Dirac equation|XNZX7VXXR2]].
In geometry, Dirac operators on [[spinor bundles|PYYQQKAZ0C]] are elliptic, and their indices are computed by the Atiyah–Singer index theorem.

## Explanations

### L1 human

The Laplacian $\partial_1^2 + \cdots + \partial_n^2$ is a sum of squares, and one may ask for a first-order operator whose square is it.
With ordinary numbers this is impossible beyond one variable, because the cross terms $2\partial_j\partial_k$ do not cancel.
Dirac's idea was to use matrices $\gamma_j$ whose products anticommute, so the cross terms cancel.
In one variable it is easy: $D = -i\, d/dx$ satisfies $D^2 = -d^2/dx^2$.
In the plane, the Cauchy–Riemann operators of complex analysis assemble into a Dirac operator.
