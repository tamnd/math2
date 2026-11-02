---
tag: 3GV2E2YTZX
kind: concept
name: Minimal surface equation
msc: [35J93, 53A10]
specializes: [7X9N9H3RK6]
sources:
  - url: https://en.wikipedia.org/wiki/Minimal_surface
---

## Summary

The minimal surface equation for a function $u$ of $n$ variables says that its graph is a [[minimal surface|41X0YW2R9N]].
That is, the graph has zero mean curvature.
It reads $\operatorname{div}\big(\nabla u / \sqrt{1 + \abs{\nabla u}^2}\big) = 0$.
It is the Euler–Lagrange equation of the area of the graph, $\int \sqrt{1 + \abs{\nabla u}^2} \, dx$.
It is a model [[quasilinear|7X9N9H3RK6]] elliptic equation, and its study led to Bernstein's problem and to deep results on regularity.

## Explanations

### L1 human

Imagine a soap film over a wire frame, seen as the graph of a height function $u(x, y)$.
The film settles where its area cannot be lowered by small changes, and this condition is a differential equation for the height.
For gentle slopes, the equation is close to Laplace's equation $u_{xx} + u_{yy} = 0$.
Planes are the simplest solutions, and Scherk's surface $u(x, y) = \log(\cos y / \cos x)$ is a famous curved one.
