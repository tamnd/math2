---
tag: CT3PNBCYMX
kind: concept
name: Multivariate approximation
msc: [41A63, 41A10]
specializes: [YPJSH79SHQ]
sources:
  - url: https://en.wikipedia.org/wiki/Approximation_theory
---

## Summary

Multivariate approximation is the part of [[approximation theory|YPJSH79SHQ]] that approximates functions of several variables.
Its tools include [[polynomials in several variables|07GNX8GCYP]], tensor product methods, [[radial basis functions|XZ33P3HBB9]], box splines, [[sparse grids|84BR7X6HET]] and neural networks.
Many one-dimensional facts fail or change form here: for instance, interpolation by polynomials at arbitrary distinct points is no longer always possible.
A central question is how the error depends on the dimension, which leads to the [[curse of dimensionality|YS424FTY4E]].

## Explanations

### L1 human

A function of one variable is a curve, and a function of two variables is a surface; in many applications there are dozens or thousands of variables.
Multivariate approximation asks how to replace such a function by a simpler one, such as a polynomial, that is close to it everywhere.
The number of simple building blocks grows quickly with the number of variables.
For example, polynomials of degree at most $2$ in one variable form a space of dimension $3$, but in $10$ variables they form a space of dimension $\binom{12}{2} = 66$.
