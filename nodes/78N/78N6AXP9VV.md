---
tag: 78N6AXP9VV
kind: concept
name: Calderón–Zygmund kernel
msc: [42B20]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_integral_operators_of_convolution_type
---

## Summary

A Calderón–Zygmund kernel is a function $K(x, y)$ on $\R^n \times \R^n$ off the diagonal.
It is at most of size $\abs{x - y}^{-n}$, and it is smooth in a quantitative way away from the diagonal.
These are the kernels of the [[singular integral operators|HTMCEARGDD]] of Calderón–Zygmund theory, such as the Hilbert and [[Riesz transforms|FRNDFJ9WQ5]].
The size and smoothness conditions are what turn an $L^2$ bound into $L^p$ bounds for $1 < p < \infty$.

## Explanations

### L1 human

Many important operators act by integrating a function against a kernel $K(x, y)$ that blows up when $y$ comes close to $x$.
The blow-up is of the borderline size $\abs{x - y}^{-n}$, just too big to integrate.
A Calderón–Zygmund kernel has this size and, in addition, changes slowly when $x$ or $y$ moves by a small amount compared to their distance.
The model example on the line is $K(x, y) = \frac{1}{\pi(x - y)}$, the kernel of the Hilbert transform.
