---
tag: JYEV0Q7T4Z
kind: concept
name: Fourier series method
msc: [35C10, 35K05, 42A16]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_series
---

## Summary

The Fourier series method solves linear partial differential equations on bounded intervals or boxes by expanding the unknown in a [[Fourier series|G12KXDHPPS]].
Each term of the series is a sine or cosine mode, and the equation acts on each mode separately.
The partial differential equation then becomes a family of ordinary differential equations for the coefficients.
Fourier introduced the method to solve the [[heat equation|VP2HN86VAG]], and it led to the theory of Fourier series.
See the [[definition|J0MHS4ZCKR]].

## Explanations

### L1 human

A vibrating string or a heated rod can be described as a sum of simple waves, each with its own frequency.
Under the heat equation or the wave equation, each simple wave evolves on its own, in a way that is easy to compute.
So one splits the initial state into simple waves, lets each of them evolve, and adds them up again.
For the heat equation on $(0, \pi)$ with zero boundary values, the mode $\sin(kx)$ just decays like $e^{-k^2 t}$.
High frequencies decay fastest, which is why heat smooths out sharp temperature differences.
