---
tag: NY5AK617TR
kind: concept
name: Chebyshev system
msc: [41A50, 41A52, 41A05]
sources:
  - url: https://en.wikipedia.org/wiki/Equioscillation_theorem
---

## Summary

A Chebyshev system, or Haar system, is a family of $n$ continuous functions whose nonzero linear combinations have at most $n - 1$ zeros.
Polynomials of degree less than $n$ are the model case.
Their span is called a Haar subspace.
For Chebyshev systems, interpolation at any $n$ distinct points is uniquely solvable.
By Haar's theorem, they are also the families for which best uniform approximation is always unique.

## Explanations

### L1 human

A polynomial of degree at most $n - 1$ that is not zero crosses the axis at most $n - 1$ times.
A Chebyshev system is any family of functions that shares this zero-counting property.
Because of it, you can always find exactly one combination that passes through $n$ prescribed points with different abscissas.
Examples are $1, x, \dots, x^{n-1}$ on an interval, and the functions $1, \cos x, \sin x, \dots, \cos mx, \sin mx$ on the circle, with $x$ taken modulo $2\pi$.
