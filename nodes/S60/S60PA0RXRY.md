---
tag: S60PA0RXRY
kind: concept
name: Fox H-function transforms
msc: [44A20, 33C60]
specializes: [YCK709QB06]
sources:
  - url: https://en.wikipedia.org/wiki/Fox_H-function
---

## Summary

A Fox H-function transform, or H-transform, is an [[integral transform|YCK709QB06]] on $(0, \infty)$ whose kernel is a [[Fox H-function|EAZMKENA4N]] of the product $xy$.
The H-function generalizes the Meijer G-function by allowing positive scaling factors in front of the variable in each gamma factor of its Mellin–Barnes integral.
So the H-transforms contain the [[Meijer G-function transforms|C0BCHX106R]] and, through them, the Laplace, Stieltjes and Hankel-type transforms.
They are a common framework for fractional calculus and for transforms with kernels of Mittag-Leffler or Wright type.

## Explanations

### L1 human

The Fox H-function is an even larger family of special functions than the Meijer G-function.
Its definition is a contour integral of a ratio of gamma functions, and each gamma factor may carry its own scale.
An H-transform integrates a function against such a kernel.
If every scale equals $1$, the H-function is a G-function and the H-transform is a G-transform, for example the Laplace transform with kernel $e^{-xy}$.
