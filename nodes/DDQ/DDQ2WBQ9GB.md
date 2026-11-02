---
tag: DDQ2WBQ9GB
kind: concept
name: Weyl's unitary trick
msc: ["22E46", 17B10]
sources:
  - url: https://en.wikipedia.org/wiki/Unitarian_trick
same_as:
  wikidata: Q7887223
  wikipedia: Unitarian trick
---

## Summary

Weyl's unitary trick proves facts about finite-dimensional representations of complex semisimple Lie groups and Lie algebras.
It does so by passing to a compact real form.
Representations of the compact form can be averaged over the group, and this gives results such as complete reducibility.
The trick then carries the results back, because the complex Lie algebra and its compact real form have the same finite-dimensional complex representations.

## Explanations

### L1 human

The group $SL(2, \C)$ is not compact, so one cannot average over it.
But it contains the compact group $SU(2)$, and the Lie algebra of $SL(2, \C)$ is the complexification of the Lie algebra of $SU(2)$.
A subspace is invariant under $SL(2,\C)$ exactly when it is invariant under $SU(2)$, at least for holomorphic representations.
So one can prove that representations of $SL(2,\C)$ split into irreducible pieces by averaging over $SU(2)$, where the proof is easy.
