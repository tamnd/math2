---
tag: 9M0NNNFJGM
kind: concept
name: Kernel of an integral transform
msc: [44A05]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_transform
---

## Summary

The kernel of an [[integral transform|YCK709QB06]] is the function $K(t, u)$ of two variables that is integrated against the input function.
It determines the transform completely: different transforms differ only in their kernels and in their domains of integration.
Properties of the kernel, such as symmetry or decay, decide which functions can be transformed and whether the transform can be inverted.

## Explanations

### L1 human

The kernel plays the role of a matrix with continuously many rows and columns.
A matrix acts on a vector by $y_u = \sum_t K_{t u} x_t$, and a kernel acts on a function by $(Tf)(u) = \int f(t) K(t, u)\, dt$.
The Laplace transform has kernel $e^{-ut}$ and the Fourier transform has kernel $e^{-2\pi i t u}$.
The word "kernel" here has nothing to do with the kernel of a linear map, which is the set of vectors sent to zero.
