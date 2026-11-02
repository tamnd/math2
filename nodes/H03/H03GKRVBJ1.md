---
tag: H03GKRVBJ1
kind: concept
name: Arithmetic genus
msc: [14H99, 14C40]
sources:
  - url: https://en.wikipedia.org/wiki/Arithmetic_genus
same_as:
  wikidata: Q4791125
  wikipedia: Arithmetic genus
---

## Summary

The arithmetic genus of a projective variety is an integer computed from the Euler characteristic of its structure sheaf.
For a connected reduced projective curve over an algebraically closed field, it is the dimension of the first cohomology of the structure sheaf.
It is constant in flat families, so it behaves well under degeneration, unlike the geometric genus.
For smooth projective curves it agrees with the usual [[genus|6W8TDV9VVN]].

## Explanations

### L1 human

The ordinary genus of a curve counts holes, but it can jump when a smooth curve degenerates to a singular one.
The arithmetic genus is a version of the genus that does not jump.
A smooth plane cubic has genus $1$; when it degenerates to the nodal cubic $y^2 = x^2(x + 1)$, the geometric genus drops to $0$, but the arithmetic genus stays $1$.
In a sense, the node keeps track of the lost hole.
