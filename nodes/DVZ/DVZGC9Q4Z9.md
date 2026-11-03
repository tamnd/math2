---
tag: DVZGC9Q4Z9
kind: concept
name: Geometric programming
msc: [90C30, 90C25]
sources:
  - url: https://en.wikipedia.org/wiki/Geometric_programming
same_as:
  wikidata: Q2078279
  wikipedia: Geometric programming
---

## Summary

Geometric programming is the minimisation of a posynomial, a positive combination of power products of positive variables, subject to posynomial upper bounds and monomial equations.
These problems are not convex as stated, but the change of variables $x_i = e^{y_i}$ turns them into [[convex optimization|1W1BXJN9ER]] problems.
They model circuit sizing, chemical equilibrium and many engineering design trade-offs.

## Explanations

### L1 human

Many design rules look like "area equals width times height" or "delay is proportional to length squared divided by width".
These are products of powers of positive quantities, called monomials, and sums of them are called posynomials.
Taking logarithms of the variables makes such expressions log-convex, so a local optimum is a global one.
For example, minimising $x + 1/x$ over $x > 0$ is a geometric program, and its optimum $2$ is reached at $x = 1$.
