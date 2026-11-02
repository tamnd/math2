---
tag: Y1M03JQKKR
kind: concept
name: Monotone operator
msc: [47H05, 47J20]
sources:
  - url: https://en.wikipedia.org/wiki/Monotonic_function
    locator: Monotonicity in functional analysis
---

## Summary

A monotone operator is a map $T$ from a Banach space $X$ to its dual $X^*$ with $\ip{T(u) - T(v)}{u - v} \ge 0$ for all $u, v$.
It generalises the increasing functions of one real variable, the [[monotone functions|0A7KV2WB7A]], to infinite dimensions.
Gradients of convex functionals and many nonlinear elliptic operators are monotone.
Monotone operator theory, with results such as the [[Browder–Minty theorem|NWK9Z80BT2]], solves nonlinear equations $T(u) = f$ without compactness.

## Explanations

### L1 human

A function $f$ on the real line is increasing when $(f(u) - f(v))(u - v) \ge 0$: larger inputs never give smaller outputs.
A monotone operator asks the same thing in many dimensions, with the product replaced by a pairing.
For example, the gradient of a convex function on $\R^n$ is monotone, because a convex function bends upwards in every direction.
The map $T(u) = -u$ is not monotone, since it reverses order.
