---
tag: PG3ECG5D0G
kind: concept
name: Antipode
msc: [16T05]
sources:
  - url: https://en.wikipedia.org/wiki/Hopf_algebra
---

## Summary

The antipode of a [[bialgebra|Q9HHVN606G]] is a linear map $S$ that is a two-sided inverse of the identity map for the convolution product.
A bialgebra with an antipode is a [[Hopf algebra|7XFYP0N84H]].
The antipode generalizes the inverse map $g \mapsto g^{-1}$ of a group, and it is used to define dual representations.
When it exists it is unique, and it reverses the order of products and of coproducts.

## Explanations

### L1 human

In a group, multiplying an element by its inverse gives the identity.
In a bialgebra one first splits an element into pairs, applies $S$ to the left part of each pair, and multiplies the parts back together.
The antipode is the map for which this always gives the counit of the element times $1$.
For a group algebra, the antipode sends $g$ to $g^{-1}$.
For polynomials $K[x]$ with $x$ split as $x \otimes 1 + 1 \otimes x$, the antipode sends $x$ to $-x$.
