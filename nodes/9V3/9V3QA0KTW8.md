---
tag: 9V3QA0KTW8
kind: concept
name: Shifted Legendre polynomials
msc: [33C45, 42C05]
sources:
  - url: https://en.wikipedia.org/wiki/Legendre_polynomials
---

## Summary

The shifted Legendre polynomials are the [[Legendre polynomials|QFYGJVA996]] moved from the interval $[-1, 1]$ to the interval $[0, 1]$.
They are given by $\tilde{P}_n(x) = P_n(2x - 1)$.
They are orthogonal on $[0, 1]$ for the constant weight.
So they are the natural polynomial basis for least squares and Gaussian quadrature on the unit interval.

## Explanations

### L1 human

Legendre polynomials live on the interval from $-1$ to $1$.
Many problems live on the interval from $0$ to $1$ instead, for example in probability.
The substitution $x \mapsto 2x - 1$ stretches and moves $[0, 1]$ onto $[-1, 1]$, and composing with it gives the shifted polynomials.
For example, $P_1(x) = x$ becomes $\tilde{P}_1(x) = 2x - 1$, which has average zero on $[0, 1]$.
