---
tag: KTP37HF2RZ
kind: concept
name: Lamé function
msc: ["33E10", 34B30]
sources:
  - url: https://en.wikipedia.org/wiki/Lam%C3%A9_function
same_as:
  wikidata: Q3127537
  wikipedia: Lamé function
---

## Summary

A Lamé function is a solution of Lamé's equation $w'' + \left( h - \nu(\nu + 1) k^2 \operatorname{sn}^2(z, k) \right) w = 0$, where $\operatorname{sn}$ is a Jacobi [[elliptic function|FF9ZPCZ59K]].
The equation arises when [[Laplace's equation|S8RG6N1PRT]] is separated in ellipsoidal coordinates, and its solutions are also called ellipsoidal harmonics.
When $\nu = n$ is a nonnegative integer, special values of $h$ give Lamé polynomials, which play for ellipsoids the role that Legendre polynomials play for spheres.
The equation is a special case of Heun's equation and a periodic Schrödinger equation with an elliptic potential.

## Explanations

### L1 human

Lamé's equation is like the equation $w'' + h w = 0$ of a vibrating string, but with an extra term that oscillates periodically along $z$.
The oscillating term is a square of an elliptic sine, which is periodic like the sine but has a shape controlled by a modulus $k$.
For degree $\nu = 1$ the three functions $\operatorname{sn} z$, $\operatorname{cn} z$ and $\operatorname{dn} z$ are solutions, for $h = 1 + k^2$, $h = 1$ and $h = k^2$ respectively.
These are the simplest Lamé polynomials.
