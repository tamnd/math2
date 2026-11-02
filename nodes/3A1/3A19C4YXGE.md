---
tag: 3A19C4YXGE
kind: concept
name: Generic point
msc: [14A15, 54D10]
sources:
  - url: https://en.wikipedia.org/wiki/Generic_point
same_as:
  wikidata: Q449470
  wikipedia: Generic point
---

## Summary

A generic point of a closed set $Z$ in a topological space is a point whose closure is all of $Z$.
In a [[scheme|5A35TYZD02]], every irreducible closed subset has exactly one generic point.
Generic points let one speak of a property holding "at a general point" of a variety.
Functions at the generic point form the function field.

## Explanations

### L1 human

In classical geometry, every point of a curve is a single spot on it.
A scheme adds one more point for the whole curve, which lies "everywhere on it at once".
In $\operatorname{Spec} \C[x, y]$, the prime ideal $(y - x^2)$ is such a point: its closure contains all the points $(x - a, y - a^2)$ of the parabola.
Similarly, $(0)$ is the generic point of $\operatorname{Spec} \Z$, and its closure is the whole space.
A statement true at the generic point is often true on a dense open set.
