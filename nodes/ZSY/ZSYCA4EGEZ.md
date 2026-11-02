---
tag: ZSYCA4EGEZ
kind: concept
name: Lefschetz number
msc: [55M20]
sources:
  - url: https://en.wikipedia.org/wiki/Lefschetz_fixed-point_theorem
---

## Summary

Let $f$ be a self-map of a finite CW complex or compact polyhedron.
Its Lefschetz number is the alternating sum of the traces of the maps that $f$ induces on rational homology.
It depends only on the homotopy class of $f$, and for the identity map it is the Euler characteristic.
The [[Lefschetz fixed-point theorem|G44NQXCWT9]] says that if it is not zero, then $f$ has a fixed point.

## Explanations

### L1 human

A map from a space to itself moves the holes of the space around.
For each dimension, the trace measures how much of the homology the map sends back onto itself.
The Lefschetz number adds these traces with alternating signs.
For a constant map on a connected space, only dimension $0$ counts and the Lefschetz number is $1$, which matches the single fixed point.
