---
tag: 7F386TSFRW
kind: concept
name: Separable state
msc: [81P42, 81P40]
sources:
  - url: https://en.wikipedia.org/wiki/Separable_state
same_as:
  wikidata: Q614178
  wikipedia: Separable state
---

## Summary

A separable state of a two-part quantum system is a mixture of product states.
Two parties can prepare it with local operations and shared classical randomness.
The separable states form a closed [[convex set|02AS45T3H9]] inside the set of all [[density matrices|V1JTB52E8C]].
A state that is not separable is [[entangled|CHNXT8CCK7]].
Deciding whether a given state is separable is a central problem; the [[Peres–Horodecki criterion|HRMX4R3C1B]] solves it in small dimensions.

## Explanations

### L1 human

Imagine two labs that each prepare a particle, and before that they agree on which recipe to use by rolling a shared die.
The joint states they can produce this way are exactly the separable states.
Their particles may be correlated, but only through the die, a classical source of shared chance.
For example, a die that says "both prepare $|0\rangle$" or "both prepare $|1\rangle$" with equal chance gives the separable state $\tfrac12(|00\rangle\langle 00| + |11\rangle\langle 11|)$.
Anything that cannot be produced this way carries genuine quantum correlation.
