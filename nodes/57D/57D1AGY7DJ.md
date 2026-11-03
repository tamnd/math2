---
tag: 57D1AGY7DJ
kind: concept
name: Kasparov product
msc: [19K35, 46L80]
sources:
  - url: https://en.wikipedia.org/wiki/KK-theory
---

## Summary

The Kasparov product is a bilinear, associative pairing $KK(A, D) \times KK(D, B) \to KK(A, B)$ in [[KK-theory|1W9Q7W378J]].
It composes generalized morphisms, so that separable C*-algebras with the groups $KK(A, B)$ as morphisms form an additive category.
It contains as special cases the pairing of K-theory with K-homology, the index of elliptic operators twisted by bundles, and the composition of $*$-homomorphisms.
Its existence is the main technical result of Kasparov's theory.

## Explanations

### L1 human

Kasparov modules are like morphisms from one algebra to another, and the product composes them.
If one module goes from $A$ to $D$ and another from $D$ to $B$, the product goes from $A$ to $B$.
On the Hilbert module level, one takes the tensor product of the two modules over $D$, and then one has to glue the two operators into one.
For $*$-homomorphisms $A \to D \to B$, the product is the class of the composite homomorphism.
With $A = \C$ and $B = \C$, the product of a K-theory class of $D$ with a K-homology class of $D$ is an integer, an index.
