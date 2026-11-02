---
tag: AT1W4MMTYR
kind: concept
name: Irregular singularity
msc: [34M03, 34M30, 34M35]
specializes: [QK2J038VB4]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_singular_point
---

## Summary

An irregular singularity of a linear differential equation is a [[singular point|QK2J038VB4]] that is not a [[regular singular point|H96HXG6CA0]].
Near it, solutions can grow or decay faster than any power, typically like $e^{c / (z - z_0)^k}$ or $e^{c z^k}$ near $\infty$.
The Frobenius method fails there, and the solutions are described by asymptotic expansions valid only in sectors.
This leads to the [[Stokes phenomenon|TTGF8KCA8C]].
See the [[definition|A6EXFAP5EQ]].

## Explanations

### L1 human

At a regular singular point solutions behave like powers of the distance to the point.
At an irregular one they can behave like exponentials of a negative power, which is much wilder.
For $y' = \frac{y}{z^2}$, the solution is $y = e^{-1/z}$, which has an essential singularity at $0$.
The Bessel and Airy equations have an irregular singular point at $\infty$, where their solutions oscillate or grow exponentially.
