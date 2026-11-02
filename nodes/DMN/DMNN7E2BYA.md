---
tag: DMNN7E2BYA
kind: concept
name: Chebyshev constant
msc: [31A15, 30C85, 41A50]
sources:
  - url: https://en.wikipedia.org/wiki/Conformal_radius
---

## Summary

The Chebyshev constant of a compact set $K$ in the plane measures how small a monic polynomial can be on $K$.
For each degree $n$ one takes the least maximum of $\abs{p}$ on $K$ over [[monic polynomials|0C3QBCR46M]] $p$ of degree $n$.
Then one takes its $n$-th root and lets $n$ tend to infinity.
The extremal polynomials generalize the classical [[Chebyshev polynomials|M6EAR1JHPP]] of an interval.
A theorem of Fekete and Szegő says that the Chebyshev constant equals the [[logarithmic capacity|DBQXRTC0VN]] of $K$.

## Explanations

### L1 human

A monic polynomial of degree $n$ has leading coefficient $1$, so it cannot be small everywhere: far from the origin it is about $\abs{z}^n$.
The question is how small it can stay on a given set $K$.
On the unit circle the best choice is $z^n$, with maximum $1$, so the Chebyshev constant is $1$.
On the interval $[-1, 1]$ the best choice is the Chebyshev polynomial divided by $2^{n-1}$, with maximum $2^{1-n}$, so the Chebyshev constant is $1/2$.
A small set lets monic polynomials stay small, and so has a small Chebyshev constant.
