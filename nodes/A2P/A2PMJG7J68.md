---
tag: A2PMJG7J68
kind: concept
name: Mellin convolution
msc: [44A35, 44A15]
specializes: [2Z29JN3VES]
sources:
  - url: https://en.wikipedia.org/wiki/Mellin_transform
---

## Summary

The Mellin convolution of two functions $f$ and $g$ on $(0, \infty)$ is $(f \star g)(x) = \int_0^\infty f(x/y) g(y) \, \frac{dy}{y}$.
It is the [[convolution|2Z29JN3VES]] of the multiplicative group $(0, \infty)$ with its invariant measure $dy/y$.
The [[Mellin transform|N5PVGRJE1T]] turns it into a product: $\mathcal{M}(f \star g) = \mathcal{M}f \cdot \mathcal{M}g$ where both transforms converge absolutely.
It describes, for example, the law of a product of independent positive random variables and many integral operators with homogeneous kernels.

## Explanations

### L1 human

Ordinary convolution averages $f(x - y)$ against $g(y)$, mixing shifts.
Mellin convolution averages $f(x/y)$ against $g(y)$, mixing rescalings instead.
The weight $dy/y$ treats the intervals $[1, 2]$ and $[10, 20]$ as equally large, as a logarithmic scale does.
For example, the indicator function of $(0, 1]$ convolved with itself gives $-\log x$ on $(0, 1]$ and $0$ beyond.
