---
tag: GC96MQC0PP
kind: concept
name: Inverse transform
msc: [44A05]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_transform
---

## Summary

The inverse transform of an [[integral transform|YCK709QB06]] $T$ recovers a function $f$ from its image $Tf$.
It exists when $T$ is one-to-one on the class of functions in use.
Often the inverse is itself an integral transform with its own kernel.
Examples are the Fourier inversion formula and the [[Bromwich integral|5KNAXNHRY6]] for the [[inverse Laplace transform|07WBTX1MHA]].
A typical use of a transform is: transform the problem, solve it on the transform side, then apply the inverse transform.

## Explanations

### L1 human

If a transform translates functions into another language, the inverse transform translates back.
For the [[Fourier transform|DPVM34ADZV]], the inverse looks almost like the transform itself: only the sign in the exponential changes.
For the Laplace transform, the inverse needs an integral along a vertical line in the complex plane, so in practice one uses tables of [[transform pairs|ZA1HC10WM6]].
For example, the inverse Laplace transform of $1/(s - 2)$ is $e^{2t}$.
