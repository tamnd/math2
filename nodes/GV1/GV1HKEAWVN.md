---
tag: GV1HKEAWVN
kind: concept
name: Dedekind-finite ring
msc: [16U99, 16U60]
specializes: [0B1261B5ED]
sources:
  - url: https://en.wikipedia.org/wiki/Dedekind-finite_ring
same_as:
  wikidata: Q112160790
  wikipedia: Dedekind-finite ring
---

## Summary

A ring is Dedekind-finite when every one-sided inverse is a two-sided inverse: $ab = 1$ forces $ba = 1$.
Such rings are also called directly finite.
Commutative rings, finite rings and matrix rings over fields are Dedekind-finite, while rings of operators on infinite-dimensional spaces need not be.

## Explanations

### L1 human

For square matrices over a field, if $AB = I$ then also $BA = I$.
A ring with this property is Dedekind-finite.
The name recalls Dedekind's definition of a finite set: a set is finite when it is not in bijection with a proper subset.
Consider the ring of linear maps on the space of infinite sequences.
There, "shift right" followed by "shift left" is the identity.
But "shift left" followed by "shift right" loses the first term, so that ring is not Dedekind-finite.
