---
tag: MTZCFEV37Y
kind: concept
name: Complex powers of elliptic operators
msc: [58J40, 58J52, 35S05]
sources:
  - url: https://en.wikipedia.org/wiki/Zeta_function_regularization
---

## Summary

Complex powers $A^s$, $s \in \C$, of a positive [[elliptic operator|MT9P2X85V8]] $A$ on a closed manifold generalise the powers $\lambda^s$ of a positive number.
Seeley showed that they are [[pseudo-differential operators|FF27N0BWTP]] of order $ms$, where $m$ is the order of $A$, depending holomorphically on $s$.
Their traces define the spectral zeta function $\zeta_A(s) = \operatorname{tr} A^{-s}$, which extends meromorphically to $\C$ and is regular at $s = 0$.
This is the basis of [[zeta function regularization|VJCJYXGTDY]] of determinants of Laplacians and of analytic torsion.

## Explanations

### L1 human

For a positive matrix with eigenvalues $\lambda_j$, the power $A^s$ is the matrix with the same eigenvectors and eigenvalues $\lambda_j^s$.
An elliptic operator such as a Laplacian on a closed manifold has infinitely many eigenvalues tending to infinity, and one can define $A^s$ in the same way.
For example, on the circle the operator $1 - d^2/dx^2$ multiplies $e^{inx}$ by $1 + n^2$, and $A^s$ multiplies it by $(1 + n^2)^s$.
When the real part of $s$ is negative enough, these powers are trace class, and their traces, continued to all $s$, give a zeta function attached to the operator.
Its derivative at $0$ defines a regularised determinant, a finite substitute for the infinite product of the eigenvalues.
