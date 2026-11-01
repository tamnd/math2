---
tag: Y76T2DQJPQ
kind: concept
name: Castelnuovo–Mumford regularity
msc: [13D02, 13D45]
sources:
  - url: https://en.wikipedia.org/wiki/Castelnuovo–Mumford_regularity
same_as:
  wikidata: Q5049716
  wikipedia: Castelnuovo–Mumford regularity
---

## Summary

The Castelnuovo–Mumford regularity is an integer that bounds the degrees in the minimal free resolution of a finitely generated graded module over a polynomial ring.
It measures how complicated the module is from the point of view of syzygies.
It bounds the degree from which the Hilbert function agrees with the [[Hilbert polynomial|RMH4FBCFDA]].
It also bounds the complexity of [[Gröbner basis|C83KPT47R0]] computations.

## Explanations

### L1 human

A module over a polynomial ring is described by generators, relations among the generators, relations among the relations, and so on.
Each of these comes in certain degrees.
The regularity records how far the degrees drift upward as one goes down this chain, after a shift of one degree for each step.
For the quotient $k[x]/(x^d)$, the generator has degree $0$ and the single relation has degree $d$, so the regularity is $d - 1$.
A small regularity means the module is simple in this sense.
