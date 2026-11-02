---
tag: X11Q0G8PNA
kind: concept
name: Schur stable polynomial
msc: [39A30, 93D20, 26C10]
sources:
  - url: https://en.wikipedia.org/wiki/Stable_polynomial
---

## Summary

A Schur stable polynomial is a polynomial whose [[roots|019MA1VTR2]] all lie strictly inside the unit circle of the complex plane.
It is the discrete-time partner of a Hurwitz stable polynomial, whose roots lie in the open left half-plane.
A linear recurrence with constant coefficients has all its solutions tending to zero exactly when its [[characteristic polynomial|0YA7X86K05]] is Schur stable.
So the notion is the basic test for stability of discrete-time linear systems and of numerical schemes.

## Explanations

### L1 human

Look at all the complex roots of a polynomial and draw them in the plane.
The polynomial is Schur stable when every root lies inside the circle of radius $1$ around the origin, and none lies on the circle.
For example, $z^2 - \tfrac{1}{4}$ has roots $\pm \tfrac{1}{2}$, so it is Schur stable.
The polynomial $z - 2$ is not, because its root $2$ lies outside the circle.
Powers $\lambda^n$ of a root with $\abs{\lambda} < 1$ shrink to zero, which is why these polynomials describe systems that settle down.
