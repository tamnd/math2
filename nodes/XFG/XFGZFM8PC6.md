---
tag: XFGZFM8PC6
kind: concept
name: Plus construction
msc: [19D06, 55R35]
sources:
  - url: https://en.wikipedia.org/wiki/Plus_construction
same_as:
  wikidata: Q7205616
  wikipedia: Plus construction
---

## Summary

The plus construction changes a connected CW complex so that a chosen perfect normal subgroup of its [[fundamental group|S1XK3HXHFX]] dies.
The homology stays the same.
The result $X^+$ is unique up to homotopy equivalence.
Daniel Quillen used it to define the higher algebraic K-groups of a ring $R$ as the homotopy groups of $BGL(R)^+$.
Here $BGL(R)$ is the [[classifying space|BK3091CPGF]] of the infinite general linear group.
This made [[algebraic K-theory|5GVFZWMWC8]] a part of homotopy theory.

## Explanations

### L1 human

Sometimes a space has a fundamental group that is too large, but its homology is exactly right.
The plus construction glues in new cells of dimension $2$ and $3$.
The $2$-cells kill the unwanted loops, and the $3$-cells cancel the extra homology that the $2$-cells created.
This works only for a perfect subgroup, one that equals its own commutator subgroup, because homology in degree $1$ sees the fundamental group only up to commutators.
For the classifying space of $GL(R)$, the plus construction kills the elementary matrices, and the new space has $\pi_1 = K_1(R)$.
