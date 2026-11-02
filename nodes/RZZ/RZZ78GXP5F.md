---
tag: RZZ78GXP5F
kind: concept
name: Abel–Poisson summation of Fourier series
msc: ["42A24", "40G10", "31A05"]
specializes: [EZXPY4A19C]
sources:
  - url: https://en.wikipedia.org/wiki/Poisson_kernel
---

## Summary

Abel–Poisson summation applies [[Abel summation|EZXPY4A19C]] to the [[Fourier series|G12KXDHPPS]] of a periodic function.
The $k$-th term is damped by the factor $r^{\abs{k}}$, and $r$ tends to $1$ from below.
The damped series equals the convolution of the function with the [[Poisson kernel|TCYSWCTYYM]].
As a function of the point $r e^{ix}$ of the unit disc, the damped sum is a [[harmonic function|0DEB0JMN0W]].
Its boundary values, in the limit $r \to 1^-$, are the given function.
For a continuous function the Abel–Poisson means converge uniformly to it.

## Explanations

### L1 human

Write a periodic function as a sum of waves $e^{ikx}$.
Multiply the wave of frequency $k$ by $r^{\abs{k}}$ for some $r < 1$, which tames the high frequencies.
The result is a smooth function, and it is the steady temperature at radius $r$ in a round plate whose rim is held at the given function.
As $r$ goes to $1$, the smoothed function approaches the original one.
