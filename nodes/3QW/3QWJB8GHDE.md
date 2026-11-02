---
tag: 3QWJB8GHDE
kind: concept
name: Saturation of approximation methods
msc: [41A40, 41A35, 41A36]
sources:
  - url: https://en.wikipedia.org/wiki/Approximation_theory
---

## Summary

Many linear approximation methods cannot converge faster than a certain rate, except for a small class of trivial functions.
This phenomenon is called saturation, and that rate is the saturation order of the method.
The functions approximated with exactly this rate form the saturation class.
Saturation explains why smoothness beyond a certain level does not improve methods such as Bernstein polynomials or Fejér means.

## Explanations

### L1 human

Some approximation methods hit a speed limit.
Bernstein polynomials of a function with a nonzero second derivative have error of order $1/n$ and not smaller, however smooth the function is.
Only the straight lines, which the method reproduces exactly, do better.
Knowing the speed limit of a method tells when it is worth switching to a better one.
