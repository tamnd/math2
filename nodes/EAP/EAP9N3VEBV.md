---
tag: EAP9N3VEBV
kind: concept
name: Generalized convolution of an integral transform
msc: [44A35, 44A05]
sources:
  - url: https://en.wikipedia.org/wiki/Convolution
---

## Summary

A convolution of an [[integral transform|YCK709QB06]] $T$ is a bilinear product $\circledast$ of functions that $T$ turns into the pointwise product: $T(f \circledast g) = Tf \cdot Tg$.
The usual [[convolution on the line|ERP5737VZ1]] plays this role for the Fourier transform.
The [[convolution on the half-line|FCKX8KFVGN]] plays it for the Laplace transform, and the [[Mellin convolution|A2PMJG7J68]] for the Mellin transform.
Finding such a product for a given transform gives it a convolution theorem, which is what makes it useful for solving integral and differential equations.

## Explanations

### L1 human

Many transforms are useful because they turn a hard operation into multiplication.
For each transform one can ask which operation on the original functions becomes multiplication on the transform side.
That operation is the convolution of the transform.
For the Fourier transform it is the familiar convolution; for other transforms it is a different integral, adapted to the kernel of the transform.
