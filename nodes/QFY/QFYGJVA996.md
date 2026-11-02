---
tag: QFYGJVA996
kind: concept
name: Legendre polynomials
msc: [33C45, 42C05]
specializes: [47WJ34NC9K]
sources:
  - url: https://en.wikipedia.org/wiki/Legendre_polynomials
same_as:
  wikidata: Q215405
  wikipedia: Legendre polynomials
---

## Summary

The Legendre polynomials $P_0, P_1, P_2, \dots$ are the polynomials obtained by making $1, x, x^2, \dots$ orthogonal on $[-1, 1]$ with the constant weight, normalised by $P_n(1) = 1$.
They are the simplest [[classical orthogonal polynomials|47WJ34NC9K]], the Jacobi case $\alpha = \beta = 0$.
They solve [[Legendre's equation|W6VE30V10Y]] and appear in the Laplace equation in spherical coordinates, in multipole expansions, and in Gauss–Legendre quadrature.

## Explanations

### L1 human

On the interval from $-1$ to $1$, two functions are called orthogonal when the integral of their product is zero.
Start with $1$, $x$, $x^2$, and so on, and adjust each one so that it is orthogonal to all the earlier ones.
The results, scaled to equal $1$ at $x = 1$, are $P_0 = 1$, $P_1 = x$, $P_2 = \frac{3x^2 - 1}{2}$, and so on.
They play the role on $[-1, 1]$ that sines and cosines play on a circle.
