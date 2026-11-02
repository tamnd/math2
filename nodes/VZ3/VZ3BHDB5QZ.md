---
tag: VZ3BHDB5QZ
kind: concept
name: Whittaker transform
msc: [44A20, 33C15]
specializes: [YCK709QB06]
sources:
  - url: https://en.wikipedia.org/wiki/Whittaker_function
---

## Summary

A Whittaker transform is an [[integral transform|YCK709QB06]] on $(0, \infty)$ whose kernel is built from a [[Whittaker function|7EFDMJSVDP]] $W_{\kappa, \mu}$ of the product $xy$.
Several normalizations are in use in the literature.
The form recorded here contains the [[Laplace transform|0V49JEZW06]] as the special case $\kappa = \mu + 1/2$.
Whittaker functions are confluent hypergeometric functions, so these transforms belong to the study of transforms with special function kernels.

## Explanations

### L1 human

Whittaker functions are solutions of a second order differential equation that also produces the exponential function, the error function and Laguerre polynomials as special cases.
A Whittaker transform integrates a function against such a solution instead of against $e^{-xy}$.
With two parameters $\kappa$ and $\mu$ it gives a family of transforms that bends the Laplace transform in two directions.
For one choice of the parameters the kernel becomes exactly $e^{-xy}$, and nothing new happens.
