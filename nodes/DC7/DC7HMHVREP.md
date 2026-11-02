---
tag: DC7HMHVREP
kind: concept
name: Characteristic value of a kernel
msc: [45C05, 47A75]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
---

## Summary

A characteristic value of a kernel $K$ is a number $\lambda$ for which the homogeneous integral equation $\varphi(x) = \lambda \int K(x, y) \varphi(y) \, dy$ has a nonzero solution.
It is the reciprocal of a nonzero [[eigenvalue|0BQAA2BK3Q]] of the integral operator with kernel $K$.
Characteristic values are the exceptional parameters of the [[Fredholm equation of the second kind|DEYYNVCV9J]].
Away from them, the equation has exactly one solution for each right-hand side.

## Explanations

### L1 human

An integral equation of the second kind contains a parameter $\lambda$ in front of the integral.
For most values of $\lambda$ the equation is well behaved, but for some special values the homogeneous equation has a nonzero solution, and uniqueness fails.
These special values are the characteristic values.
For $K(x, y) = xy$ on $[0, 1]$, the only one is $\lambda = 3$, with solution $\varphi(x) = x$, because $\int_0^1 x y \cdot y \, dy = x/3$.
