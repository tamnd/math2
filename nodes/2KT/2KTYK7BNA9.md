---
tag: 2KTYK7BNA9
kind: concept
name: Y transform
msc: [44A20, 33C10]
specializes: [YCK709QB06]
sources:
  - url: https://en.wikipedia.org/wiki/Bessel_function
---

## Summary

The Y transform of order $\nu$ is an [[integral transform|YCK709QB06]] on $(0, \infty)$ with kernel $\sqrt{xy}\, Y_\nu(xy)$.
Here $Y_\nu$ is the [[Bessel function of the second kind|GRSNDJG363]].
It is the companion of the [[Hankel transform|2P9YWDGKC4]], which uses the Bessel function of the first kind $J_\nu$ in the same way.
Unlike the Hankel transform, it is not its own inverse.
It appears when boundary value problems in cylindrical coordinates need solutions that are singular on the axis.

## Explanations

### L1 human

Bessel functions come in two kinds: $J_\nu$ is finite at the origin, and $Y_\nu$ blows up there.
The Hankel transform uses $J_\nu$ as its family of test waves, and the Y transform uses $Y_\nu$.
For the order $\nu = 1/2$ the kernel is a cosine, so the Y transform is, up to a sign and a constant, the Fourier cosine transform.
For other orders it is a genuinely new transform with its own inversion theory.
