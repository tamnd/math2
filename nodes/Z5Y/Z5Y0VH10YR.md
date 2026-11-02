---
tag: Z5Y0VH10YR
kind: concept
name: Bernstein–Bézier form
msc: [41A10, 65D17, 41A15]
sources:
  - url: https://en.wikipedia.org/wiki/Bernstein_polynomial
---

## Summary

The Bernstein–Bézier form writes a polynomial in the [[Bernstein basis|0JT92VK307]] adapted to an interval, or to a simplex in several variables.
Its coefficients, the Bézier coefficients, behave like control points.
The polynomial lies between their minimum and maximum, and it agrees with the end coefficients at the endpoints.
This form is numerically stable and is the standard way to store and manipulate polynomial pieces of splines and Bézier curves.

## Explanations

### L1 human

The usual way to write a polynomial uses powers $1, x, x^2, \dots$.
The Bernstein–Bézier form instead uses the blending weights $\binom{n}{k}(1-u)^{n-k}u^k$, where $u$ measures the position in the interval.
Then each coefficient has a geometric meaning, a height that the graph is pulled toward.
For example, on $[0, 1]$ the polynomial $x$ of degree $2$ has Bézier coefficients $0, 1/2, 1$, equally spaced heights along the line.
