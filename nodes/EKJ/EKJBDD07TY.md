---
tag: EKJBDD07TY
kind: concept
name: Closed monoidal category
msc: [18D15, 18M05]
specializes: [M3MSQ3NKAE]
sources:
  - url: https://en.wikipedia.org/wiki/Closed_monoidal_category
same_as:
  wikidata: Q5135347
  wikipedia: Closed monoidal category
---

## Summary

A closed monoidal category is a [[monoidal category|M3MSQ3NKAE]] in which morphisms between two objects form again an object, the internal hom.
The internal hom $[B, C]$ is characterised by a currying bijection between morphisms $A \otimes B \to C$ and morphisms $A \to [B, C]$.
[[Cartesian closed categories|BFBNQ36QS8]] are the case where $\otimes$ is the product.
Vector spaces, abelian groups and modules over a commutative ring, with the tensor product, are closed monoidal.

## Explanations

### L1 human

In many categories, the set of maps from $B$ to $C$ carries the same kind of structure as $B$ and $C$.
For example, the linear maps between two vector spaces form a vector space.
A closed monoidal category is one where this happens in a way that matches the tensor product.
A linear map out of $A \otimes B$ is the same thing as a linear map from $A$ into the space of linear maps from $B$ to $C$.
