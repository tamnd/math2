---
tag: SGZZ4Y0D36
kind: concept
name: Mellin convergence
msc: [44A15]
sources:
  - url: https://en.wikipedia.org/wiki/Mellin_transform
---

## Summary

A function $f$ on $(0, \infty)$ is Mellin convergent at a complex number $s$ when $x^{s-1} f(x)$ is integrable on $(0, \infty)$.
This is exactly the condition under which the [[Mellin transform|N5PVGRJE1T]] $\mathcal{M}f(s)$ is defined as an absolutely convergent integral.
It depends only on $\operatorname{Re} s$, and the set of real parts where it holds is an interval.
Its interior gives the vertical strip on which the Mellin transform is holomorphic.

## Explanations

### L1 human

The power $x^{s-1}$ is large near $0$ when $\operatorname{Re} s < 1$ and large near $\infty$ when $\operatorname{Re} s > 1$.
So Mellin convergence is a balance: $f$ must be small enough near $0$ to tame one end and small enough near $\infty$ to tame the other.
For example, $f(x) = 1/(1 + x)$ behaves like $1$ near $0$ and like $1/x$ near $\infty$.
It is Mellin convergent exactly when $0 < \operatorname{Re} s < 1$.
