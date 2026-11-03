---
tag: RKTX9MN7Q3
kind: concept
name: Representation ring
msc: [19A22, 20C15]
specializes: [0310REJJY8]
sources:
  - url: https://en.wikipedia.org/wiki/Representation_ring
same_as:
  wikidata: Q7314220
  wikipedia: Representation ring
---

## Summary

The representation ring $R(G)$ of a group $G$ is a commutative ring built from finite-dimensional [[representations|WYGRXCG2RN]] of $G$.
Its addition is the direct sum and its multiplication is the tensor product.
For a finite group over $\C$, it is free abelian on the classes of the [[irreducible representations|FX3NEFYFFN]].
Taking [[characters|RMWMYBY8TC]] embeds it in the ring of class functions, so it is also called the character ring.

## Explanations

### L1 human

Representations of a group can be added, by the direct sum, and multiplied, by the tensor product.
The representation ring also allows formal differences, called virtual representations.
Over the complex numbers, every representation of a finite group splits into irreducible pieces in a unique way, so an element of the ring is a list of integer multiplicities.
For the group $\Z/2\Z$ there are two irreducible representations, the trivial one $1$ and the sign $s$, with $s \otimes s = 1$.
So its representation ring is $\Z[s]/(s^2 - 1)$.
