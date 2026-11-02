---
tag: X7GTF3D98F
kind: concept
name: Integrable function
msc: [28A25, 26A42]
sources:
  - url: https://en.wikipedia.org/wiki/Lebesgue_integral
---

## Summary

A measurable function on a measure space is integrable when the integral of its absolute value is finite.
These are the functions for which the Lebesgue integral is a well-defined finite number.
Integrable functions form the space $L^1$, and the convergence theorems of integration are stated for them.

## Explanations

### L1 human

A function is integrable when the total area between its graph and the axis is finite.
The area above the axis and the area below the axis must each be finite, so that their difference makes sense.
For example, $e^{-\abs{x}}$ is integrable on the real line, with total area $2$.
The function $1/x$ on $[1, \infty)$ is not integrable, because its area grows like $\ln x$ without bound.
