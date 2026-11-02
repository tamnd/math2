---
tag: GW3B4K1WA5
kind: concept
name: Index of a singular integral operator
msc: ["45E05", 47A53]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_integral_operators_on_closed_curves
---

## Summary

Consider a singular integral operator $a \varphi + b S \varphi + \int_\Gamma k \varphi$ on a closed curve $\Gamma$.
Its index is the winding number around $0$ of the function $(a - b)/(a + b)$ on $\Gamma$.
It is an integer computed from the coefficients alone, and it does not depend on the regular part $k$.
By the [[Noether theorems|FDC1BEB8FW]], it equals the number of independent solutions of the homogeneous equation minus that of the adjoint homogeneous equation.
So it is the [[Fredholm index|2V9Q4KHY1T]] of the operator.
It decides how far the classical Fredholm alternative fails for the equation.

## Explanations

### L1 human

For a matrix equation, the number of free parameters in the solutions minus the number of conditions on the data is a fixed number, the difference of the dimensions.
For a singular integral equation, both numbers are finite, and their difference is the index.
The surprise is that the index can be read off from a picture.
Follow the complex number $(a(t) - b(t))/(a(t) + b(t))$ as $t$ runs around the curve, and count how many times it turns around $0$.
For example, on the unit circle with $a(t) = (t + 1)/2$ and $b(t) = (t - 1)/2$, the quotient is $1/t$, which turns once clockwise, so the index is $-1$.
