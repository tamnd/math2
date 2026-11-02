---
tag: XAARVNKXF1
kind: concept
name: Uniform approximation
msc: [41A65, 41A50, 41A10]
specializes: [VNWH2KADN7]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_norm
---

## Summary

Uniform approximation is [[function approximation|VNWH2KADN7]] in which the error is the largest pointwise difference, the supremum norm $\sup_x \abs{f(x) - g(x)}$.
A function is uniformly approximable by a class when it is a [[uniform limit|08FPABDQ4C]] of functions from that class.
It is the most demanding common way to measure an approximation, because it controls the error at every point at once.

## Explanations

### L1 human

Draw a thin band of width $\varepsilon$ around the graph of $f$.
A uniform approximation within $\varepsilon$ is a function whose whole graph stays inside the band.
For example, on $[0, 1]$ the polynomial $x - 1/8$ approximates $x^2$ uniformly within $1/8$.
Being close on average is not enough: a function can be close to $f$ in mean but have a tall narrow spike, and then it is far from $f$ uniformly.
