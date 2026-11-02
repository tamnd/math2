---
tag: PP11DV3ZMQ
kind: concept
name: Krull dimension of a noncommutative ring
msc: [16P40, 16P70]
sources:
  - url: https://en.wikipedia.org/wiki/Krull_dimension
    locator: For non-commutative rings
---

## Summary

The Krull dimension of a module over a possibly noncommutative ring, in the sense of Gabriel and Rentschler, is an ordinal.
It measures how far the lattice of submodules is from satisfying the descending chain condition.
It is defined by transfinite recursion: dimension $0$ means nonzero [[Artinian|YQNZTQGP1X]].
Dimension at most $\alpha$ means that every descending chain of submodules has, from some point on, factors of dimension less than $\alpha$.
The right Krull dimension of a ring is the Krull dimension of the ring as a right module over itself.
For commutative [[Noetherian rings|0670T59HGE]] it agrees with the classical [[Krull dimension|MVGBS3J1P7]] defined by chains of prime ideals.

## Explanations

### L1 human

In a commutative ring, dimension counts the longest chain of prime ideals, but in noncommutative rings prime ideals can be scarce.
The Gabriel–Rentschler dimension looks instead at descending chains of submodules.
Artinian modules, where every descending chain stops, get dimension $0$.
The integers get dimension $1$: a descending chain of ideals $\Z \supseteq a_1\Z \supseteq a_2\Z \supseteq \cdots$ can go on forever, but its factors are finite groups, which have dimension $0$.
A polynomial ring in two variables gets dimension $2$, and so on, matching the usual dimension.
