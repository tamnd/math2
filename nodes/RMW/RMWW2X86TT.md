---
tag: RMWW2X86TT
kind: concept
name: Bartle–Dunford–Schwartz integral
msc: [46G10, 28B05]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_measure
---

## Summary

The Bartle–Dunford–Schwartz integral integrates a scalar function against a countably additive [[vector measure|PS28BSAJKJ]] with values in a [[Banach space|06GZ956657]].
The integral of a function is then a vector of the Banach space.
It is built from simple functions, as the Lebesgue integral is.
It is a standard tool for spectral measures and for operators on spaces of continuous functions.

## Explanations

### L1 human

An ordinary measure gives each set a number, and the integral of a function is a weighted sum of these numbers.
A vector measure gives each set a vector, so the weighted sum is a vector.
For a step function that takes the value $a_i$ on the set $E_i$, the integral is $\sum_i a_i \, \mu(E_i)$.
For general functions one approximates them by step functions and takes the limit of the vectors.
