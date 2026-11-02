---
tag: 5SB8EKSQRN
kind: concept
name: Hyperelliptic curve
msc: [14H45, 14H55]
specializes: [XJM2MT4S3Y]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperelliptic_curve
same_as:
  wikidata: Q850110
  wikipedia: Hyperelliptic curve
---

## Summary

A hyperelliptic curve is a smooth projective [[algebraic curve|XJM2MT4S3Y]] of genus at least $2$ that is a double cover of the projective line.
Away from characteristic $2$, it has an affine model $y^2 = f(x)$ with $f$ a squarefree polynomial.
Hyperelliptic curves are the simplest curves of higher genus.
They are the exceptions in many results, such as [[Clifford's theorem|RSW29AVKGM]] and the embedding by the canonical divisor.

## Explanations

### L1 human

Take a polynomial $f(x)$ with distinct roots and look at all solutions of $y^2 = f(x)$.
For most values of $x$ there are two values of $y$, one the negative of the other, and they come together where $f(x) = 0$.
So the curve is two copies of the line glued along cuts between the roots.
For $y^2 = x^5 - x$ there are six branch points, counting the point at infinity, and the curve has genus $2$.
