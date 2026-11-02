---
tag: 1HM7ZYMPD7
kind: concept
name: Monoid ring
msc: [16S36, 20M25, 16S34]
specializes: [0B1261B5ED]
sources:
  - url: https://en.wikipedia.org/wiki/Monoid_ring
same_as:
  wikidata: Q1945005
  wikipedia: Monoid ring
---

## Summary

The monoid ring $R[M]$ of a [[monoid|0N6R902FG1]] $M$ over a [[ring|0B1261B5ED]] $R$ is the ring of finite formal sums $\sum r_m m$, multiplied with the monoid law.
It contains $R$ and a copy of $M$ inside its multiplicative monoid.
Polynomial rings, Laurent polynomial rings and group rings are all monoid rings.
It is the free way to turn a monoid into a ring with coefficients in $R$.

## Explanations

### L1 human

Take the elements of a monoid as building blocks and form linear combinations of them with coefficients in a ring.
Multiply two combinations by expanding and multiplying the blocks with the monoid law.
For the monoid $\set{1, x, x^2, \dots}$ of powers of one letter, this gives the ordinary polynomials.
For example, $(1 + x)(2 + x^2) = 2 + 2x + x^2 + x^3$.
Changing the monoid changes the ring: the integers under addition give polynomials with negative exponents too.
