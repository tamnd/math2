---
tag: 94TNBAAJYX
kind: concept
name: Weakly singular kernel
msc: [45P05, 45H05]
specializes: [GSMBXT7FPK]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_equation
---

## Summary

A weakly singular kernel is a [[kernel|GSMBXT7FPK]] that may become infinite on the diagonal $x = s$.
It may grow there only like a power $\abs{x - s}^{-\alpha}$ with exponent $\alpha$ below the dimension.
Such a singularity is integrable, so the integral operator still makes sense on continuous functions and is compact there.
So the Fredholm theory for continuous kernels carries over.
Kernels of this type arise in potential theory and in Abel's integral equation.

## Explanations

### L1 human

The kernel blows up where the two points meet, but slowly enough that the area under it stays finite.
On an interval this means a blow-up like $1/\abs{x - s}^{\alpha}$ with $\alpha < 1$.
For example, $1/\sqrt{\abs{x - s}}$ and $\log \abs{x - s}$ are weakly singular on $[0, 1]$.
The kernel $1/(x - s)$ is not, because $\int_0^1 ds / \abs{x - s}$ is infinite.
