---
tag: 9MZFTX77CD
kind: concept
name: Jackson kernel
msc: [42A10, 41A25, 41A35]
sources:
  - url: https://en.wikipedia.org/wiki/Jackson%27s_inequality
---

## Summary

The Jackson kernel is a nonnegative trigonometric polynomial, the normalised square of the [[Fejér kernel|DCCA2T9GKH]].
Convolution with it gives trigonometric polynomials that approximate a continuous periodic function with error of order $\omega(f, 1/n)$.
It is the standard tool in the proof of Jackson's inequality.

## Explanations

### L1 human

Averaging a function against a narrow bump smooths it and keeps it close to the original.
If the bump is itself a trigonometric polynomial, the average is a trigonometric polynomial too.
The Fejér kernel is such a bump, but its tails are too heavy for the best error bounds.
Squaring it makes the tails much thinner, which is exactly what Jackson's proof needs.
