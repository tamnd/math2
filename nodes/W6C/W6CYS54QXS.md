---
tag: W6CYS54QXS
kind: concept
name: Homogeneous integral equation
msc: [45A05, 45C05]
specializes: [AYZCKG34QK]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_equation
---

## Summary

A homogeneous integral equation is a [[linear integral equation|AYZCKG34QK]] whose free term $f$ is zero, such as $\varphi(x) = \lambda \int_a^b K(x, s) \varphi(s) \, ds$.
It always has the zero solution, and its solutions form a vector space.
The values of $\lambda$ for which it has a nonzero solution are the characteristic values of the kernel.
By the Fredholm alternative, these values decide whether the inhomogeneous equation is uniquely solvable.

## Explanations

### L1 human

Homogeneous means that the equation has no term without the unknown.
It is the integral version of a system $A x = 0$ of linear equations.
Zero is always a solution; the interesting question is whether there are others.
For example, $\varphi(x) = \lambda \int_0^1 \varphi(s) \, ds$ has the nonzero solution $\varphi = 1$ exactly when $\lambda = 1$.
