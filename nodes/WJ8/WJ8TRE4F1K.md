---
tag: WJ8TRE4F1K
kind: concept
name: Nakano positivity
msc: [32L05, 32L20, 53C55]
specializes: [FVCDGMNSAN]
sources:
  - url: https://en.wikipedia.org/wiki/Kodaira_vanishing_theorem
---

## Summary

Nakano positivity is a notion of positive curvature for a holomorphic Hermitian vector bundle, stronger than [[Griffiths positivity|FVCDGMNSAN]].
It views the curvature of the [[Chern connection|7RC9CN2Q49]] as a Hermitian form on the tensor product of the tangent space and the fibre.
Then it asks that this form be positive definite.
It is the hypothesis under which the Bochner–Kodaira–Nakano identity gives vanishing of cohomology, as in Nakano's vanishing theorem $H^q(X, K_X \otimes E) = 0$ for $q \ge 1$ on compact Kähler $X$.
For line bundles it agrees with Griffiths positivity.

## Explanations

### L1 human

The curvature of a vector bundle eats a tangent direction and a fibre vector.
Griffiths positivity only tests "pure" pairs, one tangent vector together with one fibre vector.
Nakano positivity tests all combinations, that is, all elements of the tensor product of the two spaces, including sums of such pairs.
So it is a stronger requirement, and in return it gives stronger vanishing theorems.
