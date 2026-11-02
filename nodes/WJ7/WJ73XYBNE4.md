---
tag: WJ73XYBNE4
kind: concept
name: Direct product of algebras
msc: [08B25]
sources:
  - url: https://en.wikipedia.org/wiki/Direct_product
---

## Summary

The direct product of a family of [[algebras|QJGPT2W0FT]] of the same signature is the [[Cartesian product|09CEDJYBKP]] of their universes with the operations computed coordinatewise.
It generalizes the [[direct product of groups|00HF4RJ5QN]], of rings and of vector spaces.
Products are one of the three basic constructions of universal algebra, with subalgebras and homomorphic images, and varieties are the classes closed under all three.

## Explanations

### L1 human

To multiply two algebras, take pairs, one element from each, and do every operation separately in each coordinate.
For example, in $\Z/2\Z \times \Z/3\Z$ one adds $(1, 2) + (1, 2) = (0, 1)$, computing modulo $2$ in the first place and modulo $3$ in the second.
Any identity that holds in every factor, such as commutativity, still holds in the product.
Properties that are not identities can fail: a product of two fields is not a field, since $(1, 0) \cdot (0, 1) = (0, 0)$.
