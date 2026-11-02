---
tag: RN9D96ESWN
kind: concept
name: Kan extension
msc: [18A40]
sources:
  - url: https://en.wikipedia.org/wiki/Kan_extension
same_as:
  wikidata: Q1723418
  wikipedia: Kan extension
---

## Summary

A Kan extension extends a [[functor|28NQ0KRHD3]] $F \colon \mathcal{A} \to \mathcal{C}$ along another functor $K \colon \mathcal{A} \to \mathcal{B}$ to a functor on $\mathcal{B}$, in the best possible way.
There is a left Kan extension, which is universal among functors receiving a [[natural transformation|KYCPCC57FT]] from $F$, and a dual right Kan extension.
Limits, colimits and [[adjoint functors|TZHF6ZM92S]] are all special cases.
This is why Kan extensions are often called the most basic universal construction of category theory.

## Explanations

### L1 human

Suppose a functor is only known on a part of a category, or on a category that maps into a bigger one.
A Kan extension asks for the closest functor on the bigger category that is compatible with the given one.
The left Kan extension approximates from one side, the right Kan extension from the other side.
When the bigger category has just one object and one arrow, the left Kan extension is the colimit of $F$ and the right one is the limit.
For a subgroup $H$ of a group $G$, the left Kan extension of a representation of $H$ along the inclusion is the induced representation of $G$.
