---
tag: MHSMQ097GP
kind: concept
name: Bochner integral
msc: [28B05, 46G10]
sources:
  - url: https://en.wikipedia.org/wiki/Bochner_integral
same_as:
  wikidata: Q889019
  wikipedia: Bochner integral
---

## Summary

The Bochner integral extends the Lebesgue integral to functions with values in a Banach space.
It is defined as a limit of integrals of simple functions, approximated in the mean.
A strongly measurable function is Bochner integrable exactly when the integral of its norm is finite.
It keeps the main theorems of Lebesgue integration, such as dominated convergence.
It is the standard integral for vector-valued functions in analysis and partial differential equations.

## Explanations

### L1 human

For a function with vector values that takes finitely many values, the integral is a weighted sum of vectors.
A general function is approached by such simple functions, closer and closer on average.
The Bochner integral is the limit of their integrals.
For example, a continuous curve $t \mapsto u(t)$ in a Banach space, defined on $[0, 1]$, has a Bochner integral $\int_0^1 u(t) \, dt$, the limit of its Riemann sums.
