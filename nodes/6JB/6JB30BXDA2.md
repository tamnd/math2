---
tag: 6JB30BXDA2
kind: concept
name: Local cohomology
msc: [13D45, 14B15]
sources:
  - url: https://en.wikipedia.org/wiki/Local_cohomology
same_as:
  wikidata: Q6664297
  wikipedia: Local cohomology
---

## Summary

Let $M$ be a module over a commutative Noetherian ring and let $I$ be an ideal.
The local cohomology modules $H^i_I(M)$ are the right derived functors of the functor of sections supported on $I$.
It was introduced by Grothendieck.
Over a Noetherian local ring, local cohomology at the maximal ideal detects the [[depth|M2RADBFW99]] and the [[Krull dimension|MVGBS3J1P7]] of a finitely generated module.
It is the subject of [[Grothendieck's local duality|VA3DY2YX83]].

## Explanations

### L1 human

Take the elements of a module that are killed by some power of an ideal $I$.
Geometrically, these are the sections that live only near the closed set cut out by $I$.
Taking these elements is not an exact operation, and local cohomology records the correction terms.
For $R = K[x]$ and $I = (x)$, no nonzero polynomial is killed by a power of $x$, so $H^0_I(R) = 0$.
The first local cohomology is $H^1_I(R) = K[x, x^{-1}]/K[x]$, spanned by the classes of $x^{-1}, x^{-2}, \ldots$.
