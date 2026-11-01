---
tag: BEW48TA9WZ
kind: concept
name: Brauer group
msc: [16K50, 12G05]
sources:
  - url: https://en.wikipedia.org/wiki/Brauer_group
same_as:
  wikidata: Q900456
  wikipedia: Brauer group
---

## Summary

The Brauer group of a field $K$ is the group of classes of central simple algebras over $K$ up to matrix algebras, see the [[definition|EX34J8PP61]].
Its product is given by the tensor product.
Each class contains exactly one central [[division ring|0EA5BTA0CX]] up to isomorphism, so the group classifies the division algebras with center $K$ and finite dimension.
It is isomorphic to the Galois cohomology group $H^2(K, (K^s)^\times)$, see [[Galois cohomology|9MPCZ3EAJM]].
Its computation for local and global fields is a main part of class field theory.

## Explanations

### L1 human

Over the real numbers there are exactly two finite-dimensional division algebras with center $\R$: $\R$ itself and the quaternions.
The Brauer group packs this kind of information into a group.
Each division algebra with center $K$ gives an element, and the product of two elements comes from the tensor product of the algebras.
For $\R$ the group has two elements, and the quaternions square to the trivial class, because $\mathbb{H} \otimes_\R \mathbb{H}$ is the algebra of $4 \times 4$ real matrices.
