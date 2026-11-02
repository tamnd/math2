---
tag: NVH3F8FTYS
kind: concept
name: Numerical differentiation
msc: [65D25]
sources:
  - url: https://en.wikipedia.org/wiki/Numerical_differentiation
same_as:
  wikidata: Q1683292
  wikipedia: Numerical differentiation
---

## Summary

Numerical differentiation approximates the [[derivative|0V1EJCT8G6]] of a function from its values at finitely many points.
The basic tools are difference quotients such as $\frac{f(x+h) - f(x-h)}{2h}$, whose error is controlled by [[Taylor's theorem|03QHBVW4TT]].
A small step $h$ reduces the truncation error but magnifies the [[round-off error|CPN6SD3BTV]], so the step must be chosen with care.
Systematic formulas are given by [[finite difference coefficients|752Z7DRT7P]], and [[automatic differentiation|BW7FEZ8WM1]] is an alternative that avoids truncation error altogether.

## Explanations

### L1 human

The derivative is the slope of a graph at a point.
Without a formula, one can still estimate it by taking two nearby points on the graph and computing the slope of the line through them.
For $f(x) = x^2$ at $x = 1$ with points $0.9$ and $1.1$, the slope is $\frac{1.21 - 0.81}{0.2} = 2$, which here is exact.
Moving the points closer usually helps, but on a computer, points that are too close cause rounding errors to dominate.
