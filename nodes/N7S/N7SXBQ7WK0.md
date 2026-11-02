---
tag: N7SXBQ7WK0
kind: concept
name: Cap product
msc: [55N45]
sources:
  - url: https://en.wikipedia.org/wiki/Cap_product
same_as:
  wikidata: Q5034459
  wikipedia: Cap product
---

## Summary

The cap product combines a homology class of degree $n$ and a cohomology class of degree $k \le n$ into a homology class of degree $n - k$.
It makes [[singular homology|M0Q5CFJ7ZH]] a module over the [[cohomology ring|RDT4785M4D]].
Its main use is Poincaré duality, where capping with the fundamental class of a closed oriented manifold turns cohomology into homology.

## Explanations

### L1 human

A cohomology class is a test on simplices; a homology class is built from simplices.
The cap product uses the test on the front part of each simplex and keeps the back part as a smaller simplex.
So a degree $k$ test eats $k$ dimensions of an $n$-dimensional chain and leaves an $(n - k)$-dimensional chain.
When $k = n$, nothing but a point is left, and the cap product just records the value of the test on the chain.
