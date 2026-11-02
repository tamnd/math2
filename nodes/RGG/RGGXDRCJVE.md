---
tag: RGGXDRCJVE
kind: concept
name: Gauss–Legendre quadrature
msc: [65D32, 41A55, 33C45]
specializes: [FP37BTP93K]
sources:
  - url: https://en.wikipedia.org/wiki/Gauss–Legendre_quadrature
same_as:
  wikidata: Q85762846
  wikipedia: Gauss–Legendre quadrature
---

## Summary

Gauss–Legendre quadrature is [[Gaussian quadrature|FP37BTP93K]] for the constant weight $1$ on the interval $[-1, 1]$.
Its $n$ nodes are the zeros of the [[Legendre polynomial|QFYGJVA996]] $P_n$, and it integrates every polynomial of degree at most $2n - 1$ exactly.
An integral over any bounded interval $[a, b]$ is handled by a linear change of variable.
It is the default Gaussian rule for smooth functions on a bounded interval.

## Explanations

### L1 human

To integrate a function over $[-1, 1]$, sample it at a few special points and add the samples with special weights.
The points are not equally spaced: they crowd towards the two ends of the interval.
With two points, at $\pm 1/\sqrt{3}$, and weights $1$, the rule already gives the exact integral of every cubic.
For example, for $f(x) = x^2$ it gives $1/3 + 1/3 = 2/3$, which is $\int_{-1}^{1} x^2\,dx$.
