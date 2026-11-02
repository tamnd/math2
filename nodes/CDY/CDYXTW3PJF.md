---
tag: CDYXTW3PJF
kind: concept
name: Approximate identity
msc: [46H05, 43A20]
sources:
  - url: https://en.wikipedia.org/wiki/Approximate_identity
same_as:
  wikidata: Q621743
  wikipedia: Approximate identity
---

## Summary

An approximate identity in a Banach algebra is a [[net|4DVJQJV0DG]] of elements that behaves more and more like a unit.
Multiplying by it changes each element less and less.
Many important algebras have no unit, such as the convolution algebra $L^1(\R)$ and the algebra of continuous functions vanishing at infinity.
In these algebras an approximate identity often replaces the unit in proofs.
Every C*-algebra has one, and a bounded approximate identity is the hypothesis of the Cohen factorization theorem.

## Explanations

### L1 human

Think of a sequence of bumps that equal $1$ on larger and larger intervals.
Multiplying a function that dies out at infinity by such a bump changes it only far away, where it is already small.
So the bumps act almost like the constant function $1$, which itself is not in the algebra.
In $L^1(\R)$ with convolution, taller and thinner spikes of area $1$ play the same role: convolving with them averages over tiny windows and changes a function very little.
