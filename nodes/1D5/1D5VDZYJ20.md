---
tag: 1D5VDZYJ20
kind: concept
name: Function having a given Mellin transform
msc: [44A15]
sources:
  - url: https://en.wikipedia.org/wiki/Mellin_transform
---

## Summary

A function $f$ on $(0, \infty)$ has Mellin transform $m$ at a point $s$ when the integral $\int_0^\infty x^{s-1} f(x) \, dx$ converges absolutely and its value is $m$.
The notion bundles the [[Mellin convergence|SGZZ4Y0D36]] of $f$ at $s$ with the value of the [[Mellin transform|N5PVGRJE1T]].
It is convenient in proofs, because a formula such as $\mathcal{M}f(s) = \Gamma(s)$ then carries its convergence claim with it.

## Explanations

### L1 human

Writing $\mathcal{M}f(s) = m$ quietly assumes that the integral makes sense.
Saying that $f$ has Mellin transform $m$ at $s$ makes this explicit: the integral converges absolutely, and it equals $m$.
For example, $e^{-x}$ has Mellin transform $\Gamma(2) = 1$ at $s = 2$, since $\int_0^\infty x e^{-x} \, dx = 1$.
The constant function $1$ has no Mellin transform at any $s$, so it has Mellin transform $m$ for no pair $(s, m)$.
