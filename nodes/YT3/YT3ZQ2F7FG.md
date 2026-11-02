---
tag: YT3ZQ2F7FG
kind: concept
name: Zeta-regularized determinant
msc: [58J52, 11M41]
specializes: [VJCJYXGTDY]
sources:
  - url: https://en.wikipedia.org/wiki/Functional_determinant
---

## Summary

The zeta-regularized determinant of a positive elliptic operator is the regularized product of its eigenvalues, $\exp(-\zeta'(0))$, where $\zeta(s) = \sum \lambda^{-s}$ is its spectral zeta function.
Ray and Singer introduced it for Laplacians in order to define [[analytic torsion|MZT9D34B0A]].
It is an instance of [[zeta function regularization|VJCJYXGTDY]] and appears in string theory, quantum field theory and the geometry of [[determinant line bundles|5DST3VKEMX]].

## Explanations

### L1 human

The determinant of a matrix is the product of its eigenvalues.
A differential operator has infinitely many eigenvalues that grow to infinity, so the product diverges.
The zeta function trick replaces the logarithm of the product, $\sum \log \lambda$, by $-\zeta'(0)$, which is finite.
For the Laplacian on the circle of length $2\pi$, with the zero eigenvalue removed, this gives the value $4\pi^2$.
