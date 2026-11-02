---
tag: 5S7ER95XAC
kind: concept
name: Symmetric monoidal category
msc: [18M05]
specializes: [VT8SFWT0XW]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetric_monoidal_category
same_as:
  wikidata: Q17103860
  wikipedia: Symmetric monoidal category
---

## Summary

A symmetric monoidal category is a [[braided monoidal category|VT8SFWT0XW]] whose braiding, applied twice, gives the identity.
It is the categorical form of a commutative operation: $A \otimes B$ and $B \otimes A$ are identified by a swap that undoes itself.
Sets with the Cartesian product, vector spaces with the [[tensor product|0BF2DE2SYK]], and modules over a commutative ring are symmetric monoidal.
Symmetric monoidal categories are the setting of commutative monoid objects, of topological quantum field theories and of linear logic.

## Explanations

### L1 human

In a symmetric monoidal category, swapping two objects placed side by side and then swapping them back changes nothing.
So only the order of the objects matters, not how they were moved past each other.
For finite sets with the product, the swap $(a, b) \mapsto (b, a)$ is the symmetry, and doing it twice gives back $(a, b)$.
This is the familiar commutativity, made into a structure rather than an equation.
