---
tag: TMNNRRRGAS
kind: concept
name: Gegenbauer transform
msc: [44A20, 33C45]
specializes: [72TSY1Z4VA]
sources:
  - url: https://en.wikipedia.org/wiki/Gegenbauer_polynomials
---

## Summary

The Gegenbauer transform is a finite [[integral transform|YCK709QB06]] on $[-1, 1]$.
It sends a function to its integrals against the [[Gegenbauer polynomials|5TRFA6F79B]] $C_n^{\lambda}$ with the weight $(1 - x^2)^{\lambda - 1/2}$.
It is the symmetric case $\alpha = \beta$ of the [[Jacobi transform|72TSY1Z4VA]], up to constant factors.
It turns the Gegenbauer differential operator into multiplication by $-n(n + 2\lambda)$.
For $\lambda = 1/2$ it is the [[Legendre transform|51PH7Z03TJ]].

## Explanations

### L1 human

Gegenbauer polynomials are orthogonal polynomials on $[-1, 1]$ for a weight that is symmetric about $0$.
They appear naturally for functions on spheres that only depend on one angle.
The Gegenbauer transform lists how much of each polynomial a function contains.
For example, with $\lambda = 1$ the polynomials are the Chebyshev polynomials of the second kind, and the weight is $\sqrt{1 - x^2}$.
