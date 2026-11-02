---
tag: 7CATGEN6KH
kind: concept
name: Chebyshev polynomials of the second kind
msc: [33C45, 42C05]
specializes: [5TRFA6F79B]
sources:
  - url: https://en.wikipedia.org/wiki/Chebyshev_polynomials
---

## Summary

The Chebyshev polynomials of the second kind $U_n$ are the polynomials with $U_n(\cos \theta) \sin \theta = \sin((n + 1)\theta)$.
They are the companions of the [[Chebyshev polynomials|M6EAR1JHPP]] of the first kind $T_n$, and satisfy the same three-term recurrence with a different start.
They are orthogonal on $[-1, 1]$ for the weight $\sqrt{1 - x^2}$, and they are the [[Gegenbauer polynomials|5TRFA6F79B]] with parameter $1$.

## Explanations

### L1 human

The ratio $\sin((n + 1)\theta) / \sin \theta$ can always be written as a polynomial in $\cos \theta$.
That polynomial is $U_n$.
For example, $\sin(3\theta) / \sin \theta = 4 \cos^2 \theta - 1$, so $U_2(x) = 4x^2 - 1$.
They show up as derivatives of the first-kind polynomials, as determinants of tridiagonal matrices, and in the semicircle law of random matrices.
