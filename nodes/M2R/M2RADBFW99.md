---
tag: M2RADBFW99
kind: concept
name: Depth
msc: [13C15, 13D07]
sources:
  - url: https://en.wikipedia.org/wiki/Depth_(ring_theory)
same_as:
  wikidata: Q3406905
  wikipedia: Depth (ring theory)
---

## Summary

The depth of a module $M$ along an ideal $I$ is the common length of the maximal [[regular sequences|69R5R2FCS5]] on $M$ inside $I$.
For a Noetherian local ring it is bounded by the [[Krull dimension|MVGBS3J1P7]], and the rings where equality holds are the [[Cohen–Macaulay rings|N1QJQEGBFC]].
Depth can be computed with the [[Ext functor|4P7GBWJ4RR]], with [[Koszul complexes|YZY11W08SD]] or with [[local cohomology|6JB30BXDA2]].

## Explanations

### L1 human

Depth counts how many independent equations one can impose, one after the other, without any of them being a zero divisor.
Dimension counts how many independent directions a space has.
For nice rings, like polynomial rings, the two numbers agree.
For the ring $K[x,y]/(x^2, xy)$ near the origin, the dimension is $1$ but the depth is $0$, because every element vanishing at the origin is killed by $x$.
