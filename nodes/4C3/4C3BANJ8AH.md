---
tag: 4C3BANJ8AH
kind: concept
name: Second variation
msc: [49K05, 49K10]
sources:
  - url: https://en.wikipedia.org/wiki/Second_variation
same_as:
  wikidata: Q137710193
  wikipedia: Second variation
---

## Summary

The second variation of a [[functional|1EQM0DJ4NC]] at a function $y_0$ is the second derivative of $\varepsilon \mapsto J(y_0 + \varepsilon h)$ at $\varepsilon = 0$.
It plays the role of the second derivative test of ordinary calculus.
At a minimiser the [[first variation|5B8NFYB2XQ]] vanishes and the second variation is nonnegative in every direction $h$.
For integral functionals it is a quadratic functional in $h$, and its study leads to the Legendre condition, the Jacobi equation and conjugate points.

## Explanations

### L1 human

At the bottom of a valley the ground is flat, and it curves upward in every direction.
The first variation measures the slope of a functional, and the second variation measures its curvature.
For $J(y) = \int_0^1 y'(x)^2 \, dx$ one gets $J(y_0 + \varepsilon h) = J(y_0) + 2\varepsilon \int_0^1 y_0' h' \, dx + \varepsilon^2 \int_0^1 h'^2 \, dx$.
So the second variation is $2\int_0^1 h'(x)^2 \, dx$, which is never negative.
This fits the fact that straight lines minimise $J$ among functions with fixed end values.
The same idea in Riemannian geometry gives the [[second variation of arc length|ZB91TH6FKV]].
