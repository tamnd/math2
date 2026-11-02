---
tag: 2BBB8NY5ZA
kind: concept
name: Admissibility condition for wavelets
msc: [42C40, 42A38]
sources:
  - url: https://en.wikipedia.org/wiki/Continuous_wavelet_transform
---

## Summary

The admissibility condition asks that a function $\psi$ in $L^2(\R)$ have finite constant $C_\psi = \int \abs{\hat\psi(\xi)}^2 / \abs{\xi} \, d\xi$.
It makes the [[continuous wavelet transform|57FR21NDGV]] with respect to $\psi$ preserve energy up to the factor $C_\psi$.
So the transform can be inverted.
For integrable $\psi$ it forces $\int \psi = 0$: an admissible function must oscillate.

## Explanations

### L1 human

A wavelet transform measures a signal against stretched and shifted copies of one shape.
For this to lose no information, the shape must not contain a constant part, because very wide copies would then just measure the average of the signal again and again.
The admissibility condition makes this precise in terms of the Fourier transform near frequency zero.
The Mexican hat curve, which dips below zero on both sides, passes the test.
A plain bell curve, which is positive everywhere, fails it.
