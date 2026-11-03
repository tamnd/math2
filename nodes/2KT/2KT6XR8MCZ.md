---
tag: 2KT6XR8MCZ
kind: concept
name: Assembly map
msc: [19D50, 19B28, 55N20]
sources:
  - url: https://en.wikipedia.org/wiki/Assembly_map
same_as:
  wikidata: Q4808684
  wikipedia: Assembly map
---

## Summary

An assembly map compares a homology theory of the classifying space of a group with K-theory or L-theory of its [[group ring|4NMTSX0XDS]].
In the Baum–Connes setting, the target is K-theory of the group C*-algebra.
The source is computable by standard methods of algebraic topology, while the target is hard to compute.
The isomorphism conjectures of Farrell–Jones and Baum–Connes predict that suitable assembly maps are isomorphisms.
Assembly maps are central in the topology of high-dimensional manifolds.

## Explanations

### L1 human

The K-theory of a group ring $R[G]$ is hard to compute directly.
The assembly map builds elements of it from two simpler pieces: the K-theory of the coefficient ring $R$, and the homology of the [[classifying space|WSZ40H5E4T]] $BG$.
Think of gluing local information, spread over the space $BG$, into one global invariant.
For the trivial group the assembly map is the identity of $K(R)$.
For $G = \Z$ and $R$ regular, it is an isomorphism, and it recovers the formula $K_n(R[t, t^{-1}]) \cong K_n(R) \oplus K_{n-1}(R)$.
