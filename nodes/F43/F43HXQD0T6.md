---
tag: F43HXQD0T6
kind: concept
name: Quasi-ergodicity
msc: [37A40, 37A25]
sources:
  - url: https://en.wikipedia.org/wiki/Ergodicity
---

## Summary

A quasi-ergodic map is a [[quasi-measure-preserving map|F608XX51KA]] of a measure space to itself whose invariant sets are all trivial: null or of null complement.
It extends the notion of an [[ergodic transformation|AZRPHS478B]] to maps that need not preserve the measure, but only send null sets back to null sets.
This is the natural setting of nonsingular ergodic theory, where measures are only known up to equivalence.
A quasi-ergodic map cannot be split into two parts of positive measure that the map keeps apart.

## Explanations

### L1 human

Ergodicity says that a measure-preserving map cannot be split: it has no invariant pieces except null sets and sets of full measure.
Quasi-ergodicity asks for the same indivisibility, but drops the request that the map keeps the size of sets.
The map may stretch and shrink sets, as long as it never pulls a set of size zero back to a set of positive size.
For example, an irrational rotation of the circle is ergodic for length.
So it is quasi-ergodic for any measure with a positive density, even when it does not preserve that measure.
