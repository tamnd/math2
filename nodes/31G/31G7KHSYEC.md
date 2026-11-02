---
tag: 31G7KHSYEC
kind: concept
name: Lanczos sigma factor
msc: [42A24, 42A10, 65T40]
sources:
  - url: https://en.wikipedia.org/wiki/Sigma_approximation
---

## Summary

The Lanczos sigma factors are the weights $\sigma_k = \frac{\sin(\pi k/m)}{\pi k/m}$ by which one multiplies the terms of a truncated [[Fourier series|G12KXDHPPS]] of order $m$.
The weighted sum, called the sigma approximation, equals the average of the partial sum over a window of length $2\pi/m$ around each point.
This local averaging greatly reduces the overshoot near jumps known as the [[Gibbs phenomenon|VMF169AT67]].
The factors are named after Cornelius Lanczos.

## Explanations

### L1 human

A truncated Fourier series of a function with a jump overshoots near the jump and ripples around it.
Averaging the truncated series over a short window, exactly one period of the first frequency that was cut off, removes most of the ripple.
In terms of the coefficients, this averaging multiplies the term of frequency $k$ by $\frac{\sin(\pi k/m)}{\pi k/m}$.
For $m = 2$ the term of frequency $1$ is multiplied by $2/\pi \approx 0.64$.
