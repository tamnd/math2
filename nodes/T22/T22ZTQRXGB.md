---
tag: T22ZTQRXGB
kind: concept
name: Associative quotient of a magma
msc: [20N02, 20M05]
sources:
  - url: https://en.wikipedia.org/wiki/Magma_(algebra)
---

## Summary

The associative quotient of a [[magma|9689SFPVE9]] is the largest quotient of the magma that is a [[semigroup|0XMEM406JM]].
It is obtained by forcing the associative law and nothing else.
Every homomorphism from the magma to a semigroup factors in exactly one way through this quotient.
So it is the universal way to make a magma associative.

## Explanations

### L1 human

In a magma, $(xy)z$ and $x(yz)$ may be different.
The associative quotient glues these two elements together, for all $x, y, z$, and glues whatever else must follow so that the operation still makes sense.
What remains is a semigroup, where brackets no longer matter.
For example, the free magma on one letter $a$ has the different elements $(aa)a$ and $a(aa)$; in its associative quotient they become the same element $a^3$.
