---
tag: SNJC87TBHD
kind: concept
name: Generalized Fourier series
msc: [42C15, 42C10, 46C05]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_Fourier_series
same_as:
  wikidata: Q5532436
  wikipedia: Generalized Fourier series
---

## Summary

A generalized Fourier series expands a vector of an [[inner product space|0QVNCJXRY3]] along an orthogonal family, with coefficients computed by inner products.
The classical [[Fourier series|G12KXDHPPS]] is the case of the exponentials $e^{inx}$ in $L^2$ of the circle.
Other cases are expansions in Legendre polynomials, Bessel functions or eigenfunctions of a Sturm–Liouville problem.
The partial sums are the best approximations from the span of the first terms, and the series recovers the vector when the family is complete.

## Explanations

### L1 human

In the plane, the coordinates of a vector along two perpendicular directions are found by dot products.
A generalized Fourier series does the same in a space of functions, with infinitely many perpendicular directions.
For example, on $[-1, 1]$ the function $x^2$ equals $\frac13 \cdot 1 + \frac23 \cdot \frac{3x^2 - 1}{2}$, a sum along the first and third Legendre polynomials.
Each coefficient tells how much of one basic shape is present in the function.
