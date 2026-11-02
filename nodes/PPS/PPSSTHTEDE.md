---
tag: PPSSTHTEDE
kind: concept
name: Cauchy–Riemann operator
msc: [32W05, 35J46, 30A99]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy%E2%80%93Riemann_equations
---

## Summary

The Cauchy–Riemann operator is the first-order differential operator $\partial / \partial \bar z = \tfrac12 (\partial_x + i \partial_y)$ on complex-valued functions of $z = x + iy$.
A continuously differentiable function $f$ is [[holomorphic|0NAHXR1FRH]] exactly when $\partial f / \partial \bar z = 0$, which is a compact form of the [[Cauchy–Riemann equations|0T71SSYZ39]].
It is the simplest elliptic operator, with fundamental solution $1/(\pi z)$.
Its several-variable version, the $\bar\partial$ operator, is a main tool of complex analysis and complex geometry.

## Explanations

### L1 human

A function of $z = x + iy$ can depend on $x$ and $y$ in any way, for example through $\bar z = x - iy$.
The Cauchy–Riemann operator measures how much a function depends on $\bar z$.
Holomorphic functions, such as polynomials in $z$, do not depend on $\bar z$ at all, so the operator gives zero on them.
For example, it gives $0$ on $z^2$ and $1$ on $\bar z$.
