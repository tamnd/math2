---
tag: 7JCF2TE3V5
kind: concept
name: Invertible sheaf
msc: [14C20, 14F06]
specializes: [P4DZM975BV]
sources:
  - url: https://en.wikipedia.org/wiki/Invertible_sheaf
same_as:
  wikidata: Q2905137
  wikipedia: Invertible sheaf
---

## Summary

An invertible sheaf on a ringed space is a sheaf of modules that is locally isomorphic to the structure sheaf.
It is the algebraic version of a line bundle, a family of one-dimensional vector spaces over the points of the space.
The name comes from the fact that, on a scheme, such sheaves are exactly the sheaves of modules with an inverse for the tensor product.
Their isomorphism classes form the Picard group.

## Explanations

### L1 human

A line bundle attaches a line to each point of a space, and these lines vary smoothly.
Locally it looks like the space times a line, but globally it can twist, like a Möbius band over a circle.
An invertible sheaf records the sections of a line bundle: over small open sets they are just functions, but globally they can be glued with a twist.
On projective space, the twisting sheaves $\mathcal{O}(n)$ are the basic examples, and for $n \ge 0$ the global sections of $\mathcal{O}(n)$ are the homogeneous polynomials of degree $n$.
