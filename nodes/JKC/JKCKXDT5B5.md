---
tag: JKCKXDT5B5
kind: concept
name: Chudnovsky algorithm
msc: [11Y60, 65D20]
sources:
  - url: https://en.wikipedia.org/wiki/Chudnovsky_algorithm
same_as:
  wikidata: Q2208385
  wikipedia: Chudnovsky algorithm
---

## Summary

The Chudnovsky algorithm computes the digits of [[pi|0C1VYVNV2N]] by summing a fast-converging series for $1/\pi$ found by David and Gregory Chudnovsky.
Each term of the series adds about fourteen correct decimal digits.
Evaluated with binary splitting and fast multiplication, it has been used for many record computations of $\pi$.
It belongs to the same family as [[Ramanujan's series for 1/pi|8PZPMF2QJD]].

## Explanations

### L1 human

To compute millions of digits of $\pi$ one needs a formula whose terms shrink very quickly.
The Chudnovsky series is such a formula: each term is about $10^{-14}$ times the previous one.
The terms are fractions of factorials and powers of the integer $640320$, so the sum can be organised as exact integer arithmetic until the final division.
The magic number $640320$ comes from the theory of elliptic curves and modular functions.
