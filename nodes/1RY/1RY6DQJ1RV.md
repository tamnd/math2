---
tag: 1RY6DQJ1RV
kind: concept
name: Symmetric spectrum
msc: [55P42, 55P43, 55U35]
specializes: [1GHF4EKBXS]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetric_spectrum
same_as:
  wikidata: Q17090831
  wikipedia: Symmetric spectrum
---

## Summary

A symmetric spectrum is a [[spectrum|1GHF4EKBXS]] in which the $n$-th space carries an action of the symmetric group on $n$ letters.
These actions are compatible with the structure maps.
This extra symmetry gives a smash product of spectra that is associative, commutative and unital on the nose, not only up to homotopy.
Symmetric spectra form a model for the [[stable homotopy category|26GTNMAF7B]] in which ring spectra with fully coherent multiplications are simply monoids.

## Explanations

### L1 human

The smash product $S^n \wedge S^m = S^{n+m}$ hides a choice: the coordinates of the first factor come before those of the second.
Swapping the factors permutes coordinates, which is a nontrivial map.
A symmetric spectrum keeps track of these permutations by letting the symmetric group act on each space.
With this bookkeeping the smash product of two symmetric spectra is defined directly, and it is strictly commutative.
The sphere spectrum, with the symmetric group acting on $S^n = S^1 \wedge \cdots \wedge S^1$ by permuting the factors, is the basic example.
