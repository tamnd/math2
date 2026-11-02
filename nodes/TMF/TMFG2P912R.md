---
tag: TMFG2P912R
kind: concept
name: Degree of a continuous map
msc: [55M25]
sources:
  - url: https://en.wikipedia.org/wiki/Degree_of_a_continuous_mapping
same_as:
  wikidata: Q306564
  wikipedia: Degree of a continuous mapping
---

## Summary

Let $f$ be a continuous map between closed connected oriented manifolds of the same dimension.
Its degree is an integer that counts, with signs, how many times the source wraps around the target.
For maps from the $n$-sphere to itself it is defined by the action on the top homology group $H_n(S^n; \Z) \cong \Z$.
The degree is a homotopy invariant, and for maps to a sphere it is a complete invariant by the [[Hopf degree theorem|902X7EHFSC]].
It underlies the proofs of the Brouwer fixed point theorem, the hairy ball theorem and the fundamental theorem of algebra.

## Explanations

### L1 human

Think of a rubber band wrapped around a circular post.
The degree counts how many times it goes around, counting clockwise turns as negative.
The map $z \mapsto z^3$ on the unit circle in $\C$ wraps the circle three times around itself, so it has degree $3$.
Sliding the band around without cutting it never changes this count.
