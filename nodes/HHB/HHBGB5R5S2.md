---
tag: HHBGB5R5S2
kind: concept
name: Absolutely convergent Fourier series
msc: [42A20, 42A16]
specializes: [G12KXDHPPS]
sources:
  - url: https://en.wikipedia.org/wiki/Wiener_algebra
---

## Summary

A [[Fourier series|G12KXDHPPS]] converges absolutely when the sum of the absolute values of its coefficients is finite.
Then the series converges uniformly to a continuous function, which agrees with the original function almost everywhere.
If the function is continuous, it equals the sum of its Fourier series at every point.
The functions with this property form the [[Wiener algebra|5H8XESYCHQ]].
Criteria such as [[Bernstein's theorem|NQC6CRDWFW]] tell which smoothness forces absolute convergence.

## Explanations

### L1 human

A Fourier series writes a periodic function as a sum of waves with amplitudes $c_n$.
If the amplitudes are so small that $\sum \abs{c_n}$ is finite, the waves can never add up to anything wild.
The partial sums then approach the function uniformly, with no Gibbs overshoot.
For example, the triangle wave $\abs{x}$ on $[-\pi, \pi]$ has coefficients of size about $1/n^2$, so its Fourier series converges absolutely.
