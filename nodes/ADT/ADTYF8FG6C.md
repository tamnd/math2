---
tag: ADTYF8FG6C
kind: concept
name: Symmetric kernel
msc: [45C05, 45P05]
specializes: [2ZB3NFZ94T]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%E2%80%93Schmidt_integral_operator
---

## Summary

A symmetric kernel is a real-valued [[kernel|GSMBXT7FPK]] with $K(x, s) = K(s, x)$ for all $x$ and $s$.
It is the continuous analogue of a [[symmetric matrix|0VR671PHE5]], and the real case of a [[Hermitian kernel|2ZB3NFZ94T]].
A nonzero square-integrable symmetric kernel has real characteristic values and an orthonormal system of eigenfunctions, as the Hilbert–Schmidt theory shows.
Green's functions of self-adjoint boundary value problems are symmetric kernels.

## Explanations

### L1 human

The influence of the point $s$ on the point $x$ is the same as the influence of $x$ on $s$.
If one draws the kernel as a surface over the square, the surface is mirror symmetric across the diagonal $x = s$.
For example, $K(x, s) = \min(x, s)$ and $K(x, s) = e^{-\abs{x - s}}$ are symmetric.
The kernel $K(x, s) = x$ is not, because $K(1, 0) = 1$ but $K(0, 1) = 0$.
