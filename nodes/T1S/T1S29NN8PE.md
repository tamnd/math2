---
tag: T1S29NN8PE
kind: concept
name: Compositum of fields
msc: [12F05, 12F99]
sources:
  - url: https://en.wikipedia.org/wiki/Tensor_product_of_fields
---

## Summary

The compositum of two subfields $E$ and $F$ of a field $\Omega$ is the smallest subfield of $\Omega$ that contains both, written $EF$.
It is the field [[generated|05NAS7AGMZ]] by $E \cup F$, and when $E = K(\alpha_1, \ldots, \alpha_n)$ it equals $F(\alpha_1, \ldots, \alpha_n)$.
Composita appear throughout Galois theory: the compositum of two Galois extensions is Galois, and its degree is controlled by [[linear disjointness|N6YZFG66YP]].
Without a common field $\Omega$ the compositum is not defined, and the [[tensor product of fields|ANH16GQJZQ]] describes all possible ways to form one.

## Explanations

### L1 human

Put two fields side by side inside one big field.
Their union is usually not a field, because sums like $\sqrt{2} + \sqrt{3}$ are missing.
The compositum is what you get by allowing all sums, products and quotients of elements from both.
For $\Q(\sqrt{2})$ and $\Q(\sqrt{3})$ inside $\C$, the compositum is $\Q(\sqrt{2}, \sqrt{3})$, a field of degree $4$ over $\Q$.
