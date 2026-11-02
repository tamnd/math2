---
tag: R7RNMX78KZ
kind: concept
name: Kernel approximation in reproducing kernel Hilbert spaces
msc: ["46E22", 41A05, 41A63]
sources:
  - url: https://en.wikipedia.org/wiki/Reproducing_kernel_Hilbert_space
---

## Summary

Kernel approximation reconstructs a function from its values at finitely many points $x_j$.
It uses a combination $\sum_j c_j K(\cdot, x_j)$ of copies of a positive definite kernel $K$.
The natural setting is the [[reproducing kernel Hilbert space|4CK2GSRAGD]] $H_K$ of the kernel.
There the kernel interpolant is the element of smallest norm that matches the data.
Its pointwise error is bounded by a power function times the norm of the target.
It covers radial basis function interpolation and works in many variables and on scattered points.

## Explanations

### L1 human

Place a bump, given by the kernel, at each data point, and choose the heights of the bumps so that their sum passes through the data.
For the Gaussian kernel $K(x, y) = e^{-\abs{x - y}^2}$ and one data point $x_1 = 0$ with value $1$, the interpolant is just $e^{-x^2}$.
With more points one solves a linear system with the matrix of kernel values $K(x_i, x_j)$.
The reproducing kernel Hilbert space explains why this is a good choice.
Among all functions of the space that fit the data, this sum is the smoothest in the sense of the norm.
Adding a penalty to the fit gives kernel ridge regression and other methods of machine learning.
