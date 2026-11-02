---
tag: 14AKAC0S0T
kind: concept
name: Monge–Ampère equation
msc: [35J96, 35J60]
specializes: [2D3N1ZJWBW]
sources:
  - url: https://en.wikipedia.org/wiki/Monge%E2%80%93Amp%C3%A8re_equation
same_as:
  wikidata: Q1552291
  wikipedia: Monge–Ampère equation
---

## Summary

The Monge–Ampère equation prescribes the determinant of the [[Hessian matrix|0693Y2METT]] of an unknown function: $\det D^2 u = f$.
It is the basic example of a [[fully nonlinear PDE|2D3N1ZJWBW]], since it is nonlinear in the highest derivatives.
It is elliptic when $u$ is convex and $f > 0$.
It appears in the problem of prescribing the Gauss curvature of a convex surface, in optimal transport and in complex geometry.

## Explanations

### L1 human

The Hessian of a function records how it curves in every direction, and its determinant multiplies these curvatures together.
The Monge–Ampère equation asks for a function whose total curvature, in this sense, is given at every point.
In optimal transport, the gradient of a convex solution moves one mass distribution onto another, and the determinant measures how much volume is stretched.
The function $u(x) = \abs{x}^2 / 2$ has Hessian the identity matrix, so it solves $\det D^2 u = 1$.
