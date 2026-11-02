---
tag: T782PJYVEZ
kind: concept
name: Lattice congruence
msc: [06B10, 08A30]
sources:
  - url: https://en.wikipedia.org/wiki/Congruence_relation
---

## Summary

A lattice congruence is an [[equivalence relation|0G8VEZ3WTK]] on a [[lattice|WH4SFAACAS]] that is compatible with [[join and meet|J2T75ATRV5]].
Its classes can be joined and met by taking representatives, so they form a quotient lattice.
The congruences of a lattice are exactly the kernels of the [[lattice homomorphisms|BNVRR925X8]] defined on it.
This mirrors the role of normal subgroups for groups and of ideals for rings.
The congruences of a lattice form a distributive lattice themselves.

## Explanations

### L1 human

A congruence groups the elements of a lattice into blocks so that the lattice operations do not see the difference inside a block.
If two elements lie in the same block, joining each with a third element gives two results that again lie in a common block.
For example, in the chain $0 < 1 < 2$, merge $1$ and $2$ into one block and keep $0$ alone.
The quotient is the two-element chain, and the map $0 \mapsto 0$, $1 \mapsto 1$, $2 \mapsto 1$ collapses each block to one point.
