---
tag: N6YZFG66YP
kind: concept
name: Linearly disjoint extensions
msc: [12F05, 12F99]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_disjointness
same_as:
  wikidata: Q3062530
  wikipedia: Linear disjointness
---

## Summary

Let $E$ and $F$ be extensions of a field $K$ inside a common field.
They are linearly disjoint over $K$ when elements of $E$ that are [[linearly independent|0CRMGPAH83]] over $K$ stay independent over $F$.
Equivalently, the natural map from the [[tensor product|ANH16GQJZQ]] $E \otimes_K F$ to the common field is injective.
For finite extensions this means that the degree of the [[compositum|T1S29NN8PE]] is as large as possible: $[EF:F] = [E:K]$.
The notion is the field version of independence, and it is used to compute degrees and Galois groups of composita.

## Explanations

### L1 human

Two extensions are linearly disjoint when they do not overlap in a hidden way.
A basis of one stays a basis after you extend the scalars by the other.
For example, $\Q(\sqrt{2})$ and $\Q(\sqrt{3})$ are linearly disjoint over $\Q$: together they generate a field of degree $2 \cdot 2 = 4$.
Having only $\Q$ in common is not enough in general.
The fields $\Q(\sqrt[3]{2})$ and $\Q(\omega\sqrt[3]{2})$, with $\omega = e^{2\pi i/3}$, meet only in $\Q$, but together they generate a field of degree $6$, not $9$.
