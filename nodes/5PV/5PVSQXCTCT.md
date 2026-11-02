---
tag: 5PVSQXCTCT
kind: concept
name: Fourier transform of tempered distributions
msc: [46F12, 42B10]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_transform
---

## Summary

The Fourier transform of a tempered distribution $T$ is again a tempered distribution.
It acts on a Schwartz function $\varphi$ as $T$ acts on the Fourier transform of $\varphi$.
It extends the Fourier transform from integrable and square-integrable functions to all tempered distributions.
It is a linear bijection of the space of tempered distributions onto itself.
It turns derivatives into multiplication by polynomials, which makes it a main tool for linear partial differential equations.

## Explanations

### L1 human

Many useful objects, such as constant functions, polynomials and the Dirac delta, have no Fourier transform as an integral.
The trick is to move the transform onto smooth, fast-decaying test functions, where the integral always makes sense.
In this way the delta at $0$ has Fourier transform the constant function $1$, and the constant $1$ has Fourier transform the delta.
This matches the idea that a spike contains all frequencies equally.
