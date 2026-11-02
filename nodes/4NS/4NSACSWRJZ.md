---
tag: 4NSACSWRJZ
kind: concept
name: Eigenfunction of an integral operator
msc: [45C05, 47A75, 47G10]
specializes: [0N6960W0BV]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenfunction
---

## Summary

An eigenfunction of an integral operator $T_K$ is a nonzero function $\varphi$ with $T_K \varphi = \mu \varphi$ for some number $\mu$.
It is an [[eigenvector|0N6960W0BV]] of $T_K$ in a space of functions.
For symmetric kernels the eigenfunctions can be chosen to form an orthonormal system, and expanding in them diagonalizes the operator, as in the [[Hilbert–Schmidt theorem|A1G25R99PY]].

## Explanations

### L1 human

Applying the integral operator to an eigenfunction does not change its shape; it only multiplies it by a number.
So eigenfunctions are the natural modes of the operator, like the pure tones of a vibrating string.
For the kernel $K(x, y) = \min(x, y)$ on $[0, 1]$, the function $\sin(\pi x / 2)$ is an eigenfunction with eigenvalue $4 / \pi^2$.
