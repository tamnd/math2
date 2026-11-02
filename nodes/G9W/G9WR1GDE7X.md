---
tag: G9WR1GDE7X
kind: concept
name: System of linear integral equations
msc: [45F05, 45F15]
specializes: [AYZCKG34QK]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_equation
---

## Summary

A system of linear integral equations has several unknown functions $\varphi_1, \ldots, \varphi_n$, and each equation involves integrals of all of them.
In vector notation it is a single [[linear integral equation|AYZCKG34QK]] whose kernel is an $n \times n$ [[matrix|0VD9ZSWWJG]] of functions.
Much of the theory for one equation, such as [[Fredholm theory|242TFD41KZ]], carries over.
The reason is that a system on an interval can be rewritten as one equation on a longer interval.
Systems arise from coupled physical fields, from boundary integral methods for vector problems, and from the factorization of matrix symbols.

## Explanations

### L1 human

Sometimes one unknown function is not enough: two populations, two components of a displacement, two layers of a medium.
Each unknown then satisfies an equation that also contains integrals of the others.
Stacking the unknowns into a vector turns the system into one equation with a matrix kernel.
For example, on $[0, 1]$ the pair $\varphi_1(x) = x + \frac{1}{2}$, $\varphi_2(x) = x$ solves $\varphi_1(x) - \int_0^1 \varphi_2(t)\, dt = x$ and $\varphi_2(x) - x \int_0^1 \varphi_1(t)\, dt = 0$.
