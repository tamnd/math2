---
tag: 9QNBFERMHD
kind: concept
name: Iterated kernel
msc: [45B05, 45P05]
specializes: [GSMBXT7FPK]
sources:
  - url: https://en.wikipedia.org/wiki/Liouville%E2%80%93Neumann_series
---

## Summary

The iterated kernels of a [[kernel|GSMBXT7FPK]] $K$ are the kernels $K_1 = K$, $K_2$, $K_3$, ... of the powers of its integral operator.
They are defined by $K_{n}(x, s) = \int_a^b K(x, t) K_{n-1}(t, s) \, dt$, the continuous analogue of matrix powers.
They are the terms of the [[Liouville–Neumann series|H1HWSWME6B]] and of the [[resolvent kernel|ARTJV1XCRX]].
Their growth in $n$ decides for which $\lambda$ these series converge.

## Explanations

### L1 human

Applying the integral operator twice is again an integral operator, and its kernel is $K_2$.
To compute $K_2(x, s)$, sum over all intermediate points $t$ the product of the influence of $t$ on $x$ and of $s$ on $t$.
It works like multiplying a matrix by itself, with the sum over the middle index replaced by an integral.
For example, for $K(x, s) = x s$ on $[0, 1]$ one gets $K_2(x, s) = \int_0^1 x t \cdot t s \, dt = x s / 3$.
