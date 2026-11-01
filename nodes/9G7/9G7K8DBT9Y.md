---
tag: 9G7K8DBT9Y
kind: concept
name: Laplace's method
msc: [41A60, 26A42]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace%27s_method
same_as:
  wikidata: Q2058297
  wikipedia: Laplace's method
---

## Summary

Laplace's method approximates integrals of the form $\int_a^b e^{M f(x)}\, dx$ when the parameter $M$ is large.
For large $M$ almost all of the integral comes from a small neighbourhood of the point where $f$ is largest.
There $f$ is close to a downward parabola.
Replacing $f$ by this parabola turns the integral into a Gaussian integral, which gives the leading term of an [[asymptotic equivalence|00SB5EA3VW]].
[[Stirling's formula|0KC0F51T6A]] is the classical application.

## Explanations

### L1 human

Raise $e$ to the power $M f(x)$ with a huge $M$: the values of $x$ where $f$ is largest become far more important than all others.
The graph of $e^{M f(x)}$ turns into a tall, thin bump above the maximum point.
Near its top the bump looks like a bell curve, whose area is known exactly.
So the integral is about the height of the bump times a width proportional to $1/\sqrt{M}$.
