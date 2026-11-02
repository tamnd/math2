---
tag: H8P36XFV8K
kind: concept
name: Integral operator
msc: [47G10, 45P05]
specializes: [0NRYHJPQG2]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_operator
---

## Summary

An integral operator is a [[linear map|0NRYHJPQG2]] between spaces of functions that acts by integration against a kernel: $(Tf)(x) = \int K(x, y) f(y)\, dy$.
Integral operators are the infinite-dimensional analogue of matrices.
They appear as [[integral transforms|YCK709QB06]], as solution operators of differential equations, and in [[Volterra integral equations|DND8CBEVXT]] and Fredholm integral equations.
With a square-integrable kernel they are [[compact operators|M2NEP1K5AE]], which gives them a spectral theory close to that of matrices.

## Explanations

### L1 human

A matrix turns a vector $y$ into the vector with entries $\sum_j K_{ij} y_j$.
An integral operator does the same with functions, and the sum becomes an integral.
The simplest example is $(Vf)(x) = \int_0^x f(y)\, dy$ on $[0, 1]$, which takes a function to its running total.
Its kernel is $1$ when $y < x$ and $0$ otherwise, a "triangular matrix" with infinitely many entries.
