---
tag: 5V3GJ84CPQ
kind: concept
name: Numerical continuation
msc: [65H20, 65P30]
sources:
  - url: https://en.wikipedia.org/wiki/Numerical_continuation
same_as:
  wikidata: Q7069654
  wikipedia: Numerical continuation
---

## Summary

Numerical continuation is a family of methods that trace the solutions of a system of equations $F(x, \lambda) = 0$ as a parameter $\lambda$ changes.
Starting from one known solution, it computes a chain of nearby solutions along a curve.
Each new point usually comes from a predictor step and a [[Newton's method|07EXVNF9VP]] corrector step.
It is the main tool for studying how the solutions of nonlinear models depend on parameters, and for finding bifurcations.
It also gives a way to solve a hard system by deforming it from an easy one.

## Explanations

### L1 human

Imagine a curve of solutions drawn in space, and you stand on one point of it.
You take a small step along the tangent of the curve, which lands you near the curve, and then you walk back onto the curve with a few Newton steps.
Repeating this, you follow the whole curve.
For example, the solutions of $x^2 + \lambda^2 = 1$ form a circle, and continuation from $(x, \lambda) = (1, 0)$ walks around this circle, even through the points where $\lambda$ turns back.
