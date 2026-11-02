---
tag: 8TXASARQN1
kind: concept
name: Orthogonal polynomials
msc: [42C05, 33C45]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_polynomials
same_as:
  wikidata: Q619458
  wikipedia: Orthogonal polynomials
---

## Summary

A sequence of orthogonal polynomials is a sequence $p_0, p_1, p_2, \dots$ with $\deg p_n = n$ that are pairwise orthogonal.
Orthogonality refers to the inner product $\int p q \, d\mu$ of a measure $\mu$ on the real line.
They arise from the monomials $1, x, x^2, \dots$ by Gram–Schmidt orthogonalization, and they are unique up to constant factors.
The classical families of Hermite, Laguerre, Jacobi, Legendre and Chebyshev polynomials are examples.
They satisfy a three-term recurrence, their zeros are real and interlace, and they are used in approximation, numerical integration, spectral theory and random matrices.

## Explanations

### L1 human

Two polynomials are orthogonal for a weight if the integral of their product against the weight is zero.
Start with $1, x, x^2, \dots$ and straighten them one at a time so that each is orthogonal to all earlier ones.
The result is a list of polynomials, one of each degree, that act like perpendicular axes in a space of functions.
For the plain weight on $[-1, 1]$ one gets the Legendre polynomials $1$, $x$, $\frac12(3x^2 - 1)$, and so on.
