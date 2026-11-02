---
tag: QBJ9R06GYE
kind: concept
name: Siciak extremal function
msc: [32U35, 32U15]
sources:
  - url: https://en.wikipedia.org/wiki/Pluripolar_set
---

## Summary

The Siciak extremal function $V_E$ of $E \subseteq \C^n$ is the supremum of all functions of the [[Lelong class|X4ZHQG9995]] that are at most $0$ on $E$.
For compact $E$ it can also be computed from polynomials.
It is the supremum of $\frac{1}{\deg p} \log\abs{p}$ over polynomials $p$ of degree at least $1$ with $\abs{p} \le 1$ on $E$.
It is the higher-dimensional version of the Green function of a planar compact set with pole at infinity.
It is also called the pluricomplex Green function of $E$ with pole at infinity.
It controls polynomial approximation and interpolation on $E$, and for compact $E$ its upper semicontinuous regularisation is identically $+\infty$ exactly when $E$ is [[pluripolar|N0MAGPW8AP]].

## Explanations

### L1 human

Suppose a polynomial is at most $1$ in size on a set $E$.
How large can it be at a point $z$ outside $E$, given its degree?
The Siciak extremal function answers this: the best bound is $\abs{p(z)} \le e^{d \, V_E(z)}$ for polynomials of degree $d$.
For the closed unit ball in $\C^n$, the answer is $V_E(z) = \log\abs{z}$ outside the ball.
So a polynomial of degree $d$ bounded by $1$ on the ball is bounded by $\abs{z}^d$ outside it.
