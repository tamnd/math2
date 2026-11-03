---
tag: CC2HWX9X2Y
kind: concept
name: Étale K-theory
msc: [19F27, 14F20, "19E08"]
sources:
  - url: https://en.wikipedia.org/wiki/Quillen–Lichtenbaum_conjecture
---

## Summary

Étale K-theory is a version of algebraic K-theory with finite coefficients that is built to satisfy descent for the étale topology.
It is obtained by gluing the mod $\ell$ K-theory of the étale neighbourhoods of a scheme.
So it is computed by [[étale cohomology|7YX76G0838]] through a descent spectral sequence.
Algebraic K-theory maps to it, and the Quillen–Lichtenbaum conjecture, now a theorem, says this map is an isomorphism in high degrees.
It goes back to Friedlander and to Dwyer and Friedlander, and Thomason related it to algebraic K-theory with the Bott element inverted.

## Explanations

### L1 human

Algebraic K-theory is hard to compute because it does not glue well from small pieces in the étale topology.
Étale K-theory forces this gluing, and the price is that it is a different theory.
Its advantage is that it can be computed from étale cohomology, which is much better understood.
The deep question is how close the two theories are, and the answer is that they agree in high enough degrees.
