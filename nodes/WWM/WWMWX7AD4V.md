---
tag: WWMWX7AD4V
kind: concept
name: Square-integrable kernel
msc: [45P05, 47G10]
specializes: [GSMBXT7FPK]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%E2%80%93Schmidt_integral_operator
---

## Summary

A square-integrable kernel is a [[kernel|GSMBXT7FPK]] $K(x, s)$ whose squared absolute value has a finite double integral.
Such kernels are also called Hilbert–Schmidt kernels or $L^2$ kernels.
The integral operator of a square-integrable kernel is a bounded and [[compact operator|M2NEP1K5AE]] on the [[Lp space|SASP14MA1Z]] $L^2$, namely a [[Hilbert–Schmidt integral operator|CB5G212Q03]].
This class contains all continuous kernels on a square and also many unbounded ones.

## Explanations

### L1 human

The kernel may be infinite at some points, but not too badly: its square must still have a finite total integral.
This is the natural condition when one measures functions by their energy $\int \abs{\varphi}^2$.
For example, $K(x, s) = \abs{x - s}^{-1/4}$ on $[0, 1]^2$ is unbounded but square-integrable.
The kernel $\abs{x - s}^{-1/2}$ is not, because the double integral of $1/\abs{x - s}$ diverges.
