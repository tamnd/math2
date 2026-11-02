---
tag: RNX150HS1P
kind: concept
name: Strictly singular operator
msc: [47B07, 47L20]
sources:
  - url: https://en.wikipedia.org/wiki/Strictly_singular_operator
same_as:
  wikidata: Q7623695
  wikipedia: Strictly singular operator
---

## Summary

A strictly singular operator is a bounded linear map between Banach spaces that is not an isomorphism on any infinite-dimensional closed subspace.
Every compact operator is strictly singular, but the converse fails in general Banach spaces.
Strictly singular operators share an important property with compact ones: adding one of them to a Fredholm operator does not change the Fredholm index.

## Explanations

### L1 human

An isomorphism onto its image keeps every vector at a length comparable to its original length.
A strictly singular operator cannot do that on any infinite-dimensional piece of the space: on every such piece some unit vectors are shrunk almost to zero.
For example, the inclusion of the sequence space $\ell^1$ into $\ell^2$ is strictly singular.
It is not compact, since it sends the unit vectors $e_n$ to unit vectors at distance $\sqrt{2}$ from each other.
