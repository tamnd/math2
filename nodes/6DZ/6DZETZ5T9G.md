---
tag: 6DZETZ5T9G
kind: concept
name: Linear PDE
msc: [35A99]
specializes: [RCNY89A4NY]
sources:
  - url: https://en.wikipedia.org/wiki/Partial_differential_equation
---

## Summary

A linear PDE is a [[partial differential equation|GC5BDZ6QBC]] in which the unknown and its derivatives appear only linearly.
Its coefficients depend on the variables alone.
For a linear homogeneous equation, sums and multiples of solutions are again solutions.
This superposition principle makes linear PDEs the best understood class, and it is the setting of Fourier methods, fundamental solutions and distribution theory.
See the [[definition|B54GEJWQAV]].

## Explanations

### L1 human

In a linear PDE each term is a known function times one derivative of the unknown $u$, plus possibly a known source term.
No products such as $u \cdot \partial_x u$ and no powers such as $u^2$ occur.
The [[heat equation|VP2HN86VAG]] $\partial_t u = \partial_x^2 u$ is linear: if $u$ and $v$ solve it, so does $2u + 3v$.
The equation $\partial_t u + u \, \partial_x u = 0$ is not linear, and the sum of two of its solutions is usually not a solution.
