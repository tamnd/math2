---
tag: KQMJ7M57ER
kind: concept
name: Kolmogorov backward equation
msc: [60J60, 35K10, 60H10]
sources:
  - url: https://en.wikipedia.org/wiki/Kolmogorov_backward_equations_(diffusion)
same_as:
  wikidata: Q3366755
  wikipedia: Kolmogorov backward equations (diffusion)
---

## Summary

The Kolmogorov backward equation is a parabolic partial differential equation satisfied by expectations $u(t, x) = E[f(X_t) \mid X_0 = x]$ of a [[diffusion process|9HDQ094ADQ]].
Its operator is the [[infinitesimal generator|VPA41PWRR1]] of the diffusion, acting on the starting point $x$.
It links stochastic differential equations with partial differential equations and is the basis of many probabilistic formulas for solutions of such equations.

## Explanations

### L1 human

Start a random process at the point $x$ and ask for the average value of $f(X_t)$ at a later time $t$.
The answer is a function $u(t, x)$ of the time and the starting point.
The backward equation says how $u$ changes with $t$: by the drift and the diffusion acting on the starting point.
For a Brownian motion, $u$ solves the heat equation $\partial_t u = \tfrac12 \partial_{xx} u$.
For instance, $f(y) = y^2$ gives $u(t, x) = x^2 + t$, and both sides equal $1$.
