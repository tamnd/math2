---
tag: RRZGEFJS7H
kind: concept
name: Symmetric and self-reciprocal kernels
msc: [44A05, 44A15]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_transform
---

## Summary

A [[kernel|9M0NNNFJGM]] $K(x, y)$ of an [[integral transform|YCK709QB06]] is symmetric when it does not change if $x$ and $y$ are swapped.
It is self-reciprocal (a Fourier kernel) when the transform is its own inverse: applying it twice gives back the original function.
The Fourier cosine and sine kernels and the [[Hankel transform|2P9YWDGKC4]] kernel $\sqrt{xy}\, J_\nu(xy)$ are both symmetric and self-reciprocal.
For such kernels the transform and its [[inverse transform|GC96MQC0PP]] are given by the same formula, which makes the theory and the tables symmetric.

## Explanations

### L1 human

A symmetric kernel is like a symmetric matrix.
A self-reciprocal kernel is like a matrix whose square is the identity, such as a reflection.
For the cosine kernel $\sqrt{2/\pi}\cos(xy)$ on $(0, \infty)$, if $g$ is the transform of $f$, then $f$ is the transform of $g$.
So a table of cosine transforms can be read from left to right or from right to left.
