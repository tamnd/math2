---
tag: ZQFBEX62D0
kind: concept
name: Hardy–Littlewood circle method
msc: [11P55, 11P05, 11P32]
sources:
  - url: https://en.wikipedia.org/wiki/Hardy–Ramanujan–Littlewood_circle_method
same_as:
  wikidata: Q2543359
  wikipedia: Hardy–Ramanujan–Littlewood circle method
---

## Summary

The circle method is an analytic technique for counting the solutions of additive equations.
Examples are writing $N$ as a sum of $s$ $k$-th powers, or as a sum of three primes.
It writes the number of solutions as an integral over the unit circle of a power of an [[exponential sum|97PBMQCPPM]].
The integral is split into major arcs near rationals with small denominators, which give the main term.
The rest, the minor arcs, are shown to contribute less.
It goes back to Hardy and Ramanujan's work on the partition function and was developed by Hardy and Littlewood for [[Waring's problem|7VWGA444K3]].

## Explanations

### L1 human

Say you want to count the ways of writing $N$ as a sum of three cubes.
One builds a sum of waves, one wave for each cube, and raises it to the third power.
Integrating against a wave of frequency $N$ picks out exactly the combinations that add up to $N$.
Near simple fractions such as $0$, $1/2$ or $1/3$ the waves line up and the integrand is large; this gives the main term.
Everywhere else the waves mostly cancel, and the hard work is to prove that this cancellation is strong enough.
For example, this is how Vinogradov proved that every large odd number is a sum of three primes.
