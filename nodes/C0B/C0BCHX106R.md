---
tag: C0BCHX106R
kind: concept
name: Meijer G-function transforms
msc: [44A20, 33C60]
specializes: [YCK709QB06]
sources:
  - url: https://en.wikipedia.org/wiki/Meijer_G-function
---

## Summary

A Meijer G-function transform, or G-transform, is an [[integral transform|YCK709QB06]] on $(0, \infty)$ whose kernel is a [[Meijer G-function|19JNNN5KV7]] of the product $xy$.
Many classical transforms are special cases, among them the [[Laplace transform|0V49JEZW06]], the [[Stieltjes transform|RG1HFAYD98]] and transforms with Bessel function kernels.
The [[Mellin transform|N5PVGRJE1T]] of a G-function is a ratio of products of gamma functions.
So the whole family can be studied at once through the Mellin transform.

## Explanations

### L1 human

The Meijer G-function is one very flexible special function that contains the exponential, the Bessel functions, the hypergeometric functions and many others.
Using it as the kernel of a transform gives one formula that covers a whole zoo of transforms.
For example, one choice of parameters makes the kernel $e^{-xy}$, and the G-transform becomes the Laplace transform.
Results proved once for G-transforms, such as inversion and composition rules, then hold for all these transforms.
