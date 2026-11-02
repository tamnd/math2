---
tag: ZM5G144PZG
kind: concept
name: Continuous kernel
msc: [45P05, 45B05]
specializes: [GSMBXT7FPK]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_equation
---

## Summary

A continuous kernel is a [[kernel|GSMBXT7FPK]] $K(x, s)$ that is a continuous function of both variables on a closed bounded square $[a, b] \times [a, b]$.
It is the setting of the classical theory of Fredholm and Volterra.
The integral operator with a continuous kernel maps continuous functions to continuous functions and is a [[compact operator|M2NEP1K5AE]] on the space of continuous functions.
Iteration methods, the Liouville–Neumann series and the Fredholm determinant are first developed for such kernels.

## Explanations

### L1 human

A continuous kernel has no jumps and no infinite values.
Since the square is closed and bounded, the kernel is bounded by some number $M$, which makes many estimates easy.
For example, $K(x, s) = e^{x s}$ and $K(x, s) = \min(x, s)$ are continuous kernels on $[0, 1] \times [0, 1]$.
The kernel $1/\abs{x - s}$ is not, because it is infinite on the diagonal.
