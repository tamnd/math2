---
tag: EAZF9NJW12
kind: concept
name: Gateaux derivative
msc: [46G05, 58C20]
sources:
  - url: https://en.wikipedia.org/wiki/Gateaux_derivative
same_as:
  wikidata: Q919459
  wikipedia: Gateaux derivative
---

## Summary

The Gateaux derivative of a map between vector spaces at a point measures the rate of change of the map along each direction.
It generalizes the directional derivative of calculus to normed and locally convex spaces of any dimension.
It is weaker than the Fréchet derivative: a map can have a Gateaux derivative at a point without being continuous there.
It is the derivative used in the calculus of variations, where it gives the first variation of a functional.

## Explanations

### L1 human

To differentiate a map at a point $x$, move along a straight line $x + t h$ and look at the rate of change at $t = 0$.
The Gateaux derivative asks only for this rate along every line through $x$, one line at a time.
For $f(x) = \norm{x}^2$ on a real Hilbert space, the rate along $h$ is $2\ip{x}{h}$.
Since nothing is asked about how the lines fit together, the notion is weaker than the usual derivative.
