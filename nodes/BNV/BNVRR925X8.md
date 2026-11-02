---
tag: BNVRR925X8
kind: concept
name: Lattice homomorphism
msc: [06B05]
sources:
  - url: https://en.wikipedia.org/wiki/Lattice_(order)
---

## Summary

A lattice homomorphism is a map between two [[lattices|WH4SFAACAS]] that preserves [[join and meet|J2T75ATRV5]].
Every lattice homomorphism is [[monotone|0A7KV2WB7A]], but a monotone map need not preserve joins or meets.
Lattice homomorphisms are the morphisms of the category of lattices; their kernels are the lattice congruences, and the bijective ones are the lattice isomorphisms.

## Explanations

### L1 human

A lattice homomorphism carries one lattice into another and keeps best common bounds.
The best common upper bound of two elements goes to the best common upper bound of their images, and the same for lower bounds.
For example, fix a subset $A$ of a set $X$ and send each subset $S$ of $X$ to $S \cap A$.
Then $(S \cup T) \cap A = (S \cap A) \cup (T \cap A)$ and $(S \cap T) \cap A = (S \cap A) \cap (T \cap A)$.
So this map from the subsets of $X$ to the subsets of $A$ is a lattice homomorphism.
