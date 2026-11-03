---
tag: Y631JTMMT5
kind: concept
name: Hurwitz polynomial
msc: [26C10, 93D20, 30C15]
sources:
  - url: https://en.wikipedia.org/wiki/Hurwitz_polynomial
same_as:
  wikidata: Q1414214
  wikipedia: Hurwitz polynomial
---

## Summary

A Hurwitz polynomial, or stable polynomial, is a polynomial all of whose [[roots|019MA1VTR2]] lie in the open left half-plane, that is, have negative real part.
A linear differential equation with constant coefficients has all solutions decaying to $0$ exactly when its characteristic polynomial is Hurwitz.
A real matrix is [[Hurwitz-stable|9A3TBBHRFA]] exactly when its characteristic polynomial is Hurwitz.
The [[Routh–Hurwitz stability criterion|KJF8Y19BNV]] decides whether a real polynomial is Hurwitz from its coefficients.

## Explanations

### L1 human

Each root $\lambda$ of the characteristic polynomial of a linear system gives a motion $e^{\lambda t}$.
Such a motion dies out when $\lambda$ has negative real part.
So a polynomial is Hurwitz when every motion it describes dies out.
For example, $s^2 + 3s + 2 = (s + 1)(s + 2)$ is Hurwitz, with roots $-1$ and $-2$, while $s^2 + 1$ is not, since its roots $\pm i$ give oscillations that never decay.
