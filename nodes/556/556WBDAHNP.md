---
tag: 556WBDAHNP
kind: concept
name: Measure-preserving transformation
msc: [28D05, 37A05]
sources:
  - url: https://en.wikipedia.org/wiki/Measure-preserving_dynamical_system
---

## Summary

A measure-preserving transformation is a measurable map between [[measure spaces|P15VQS5DJ9]] under which the preimage of every measurable set has the same measure as the set.
Equivalently, the [[pushforward|3N66TM3TSQ]] of the first measure is the second one.
A measure-preserving map of a space to itself is the basic object of ergodic theory.
It models a system that evolves in time without creating or destroying mass, as in Hamiltonian mechanics.

## Explanations

### L1 human

Think of a fluid in a container that is stirred, where no fluid is added or lost.
After one step of stirring, the fluid that ends up in a region came from a region of the same volume.
A rotation of a circle preserves length, so it is measure-preserving.
The doubling map $x \mapsto 2x \bmod 1$ on $[0,1)$ is also measure-preserving, although it stretches: each interval has two preimage intervals of half the length.
