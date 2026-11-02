---
tag: RK2G9HN63E
kind: concept
name: Fourier–Legendre series
msc: [42C10, 33C45]
specializes: [SNJC87TBHD]
sources:
  - url: https://en.wikipedia.org/wiki/Legendre_polynomials
---

## Summary

A Fourier–Legendre series expands a function on $[-1, 1]$ as a sum of [[Legendre polynomials|QFYGJVA996]].
It is the [[generalized Fourier series|SNJC87TBHD]] for the orthogonal system of Legendre polynomials in $L^2([-1, 1])$.
Since this system is complete, the series of every square-integrable function converges to it in the mean-square sense.
Such series appear when one solves the Laplace equation in spherical coordinates.

## Explanations

### L1 human

The Legendre polynomials $P_0, P_1, P_2, \dots$ play on the interval $[-1, 1]$ the role that sines and cosines play on a circle.
Each one is orthogonal to all the others, so one can read off how much of each $P_n$ a function contains by one integral.
Summing these pieces rebuilds the function.
For example, $x^2 = \tfrac13 P_0(x) + \tfrac23 P_2(x)$, where $P_0(x) = 1$ and $P_2(x) = (3x^2 - 1)/2$.
