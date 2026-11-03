---
tag: 6XRTXBPASW
kind: concept
name: Chern character
msc: ["19L10", "57R20", "14C17"]
sources:
  - url: https://en.wikipedia.org/wiki/Chern_class
    locator: Chern character
---

## Summary

The Chern character is a ring homomorphism from K-theory to rational cohomology, or to the rational Chow ring in algebraic geometry.
It is built from the [[Chern classes|PAD37GKDPD]] so that a line bundle $L$ goes to $e^{c_1(L)}$.
Unlike the total Chern class, it turns direct sums into sums and tensor products into products.
It appears in the [[Grothendieck–Riemann–Roch theorem|3HKREN3Y3F]] and the Atiyah–Singer index theorem.

## Explanations

### L1 human

Chern classes measure how a complex vector bundle twists, but they combine awkwardly: the total Chern class of a direct sum is the product of the total Chern classes.
The Chern character repackages them so that it adds over direct sums and multiplies over tensor products.
The trick is the exponential, which turns sums into products: a line bundle with first Chern class $c$ gets the character $e^{c} = 1 + c + c^2/2 + \cdots$.
For a bundle that splits into line bundles with classes $x_1, \ldots, x_r$, the character is $e^{x_1} + \cdots + e^{x_r}$.
Its degree-zero part is the rank, so it is a refined version of the dimension.
