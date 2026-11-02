---
tag: GP98BJP4JH
kind: concept
name: Chebyshev series
msc: [41A10, 42A10, 33C45]
sources:
  - url: https://en.wikipedia.org/wiki/Chebyshev_polynomials
---

## Summary

A Chebyshev series expands a function on $[-1, 1]$ as a sum $\sum a_k T_k(x)$ of [[Chebyshev polynomials|M6EAR1JHPP]].
Under the substitution $x = \cos \theta$ it becomes the Fourier cosine series of $f(\cos \theta)$.
Truncated Chebyshev series are cheap to compute and are close to minimax approximations, within a factor that grows like $\log n$.
So they are central in numerical analysis.

## Explanations

### L1 human

A Fourier series writes a periodic function as a sum of cosines and sines.
A Chebyshev series does the same for a function on $[-1, 1]$, using the polynomials $T_k$, which are cosines in disguise.
For example, $x^2 = \frac{1}{2} T_0(x) + \frac{1}{2} T_2(x)$, since $T_0 = 1$ and $T_2 = 2x^2 - 1$.
For smooth functions the coefficients shrink very fast, so a few terms already give a very accurate polynomial.
