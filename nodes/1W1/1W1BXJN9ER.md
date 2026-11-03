---
tag: 1W1BXJN9ER
kind: concept
name: Convex optimization
msc: [90C25, 52A41]
specializes: [W3ZXKT3DS1]
sources:
  - url: https://en.wikipedia.org/wiki/Convex_optimization
same_as:
  wikidata: Q463359
  wikipedia: Convex optimization
---

## Summary

Convex optimization is the study of minimizing a [[convex function|07Q7CNM5WF]] over a [[convex set|02AS45T3H9]].
In such problems every local minimum is a global minimum, and the first-order optimality conditions are sufficient.
Linear, quadratic, second-order cone and semidefinite programs are all convex.
Many convex problems can be solved efficiently, for example by interior-point methods.

## Explanations

### L1 human

Picture a bowl-shaped landscape: wherever you stand, walking downhill leads to the bottom.
A convex problem has this shape, so there are no false valleys where a search could get stuck.
For example, minimizing $(x - 1)^2 + (y + 2)^2$ over the disc $x^2 + y^2 \le 1$ is convex.
Its minimum is at the point of the disc closest to $(1, -2)$.
