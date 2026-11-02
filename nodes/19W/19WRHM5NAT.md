---
tag: 19WRHM5NAT
kind: concept
name: Lebesgue point
msc: [28A15]
sources:
  - url: https://en.wikipedia.org/wiki/Lebesgue_point
same_as:
  wikidata: Q388660
  wikipedia: Lebesgue point
---

## Summary

Let $f$ be a locally integrable function on $\R^n$.
A Lebesgue point of $f$ is a point $x$ where the average of $\abs{f - f(x)}$ over small balls around $x$ tends to $0$.
At such a point, $f$ is well represented by its value $f(x)$ in an averaged sense.
By the Lebesgue differentiation theorem, almost every point is a Lebesgue point.
Points of continuity are Lebesgue points, but Lebesgue points need not be points of continuity.

## Explanations

### L1 human

Zoom into a function near a point and look at the average distance between $f$ and its value at the point.
If this average distance goes to zero as the window shrinks, the point is a Lebesgue point.
For the step function equal to $0$ on the negative numbers and $1$ elsewhere, the jump point $0$ is not a Lebesgue point.
On each small window around $0$ half of the values differ from $f(0) = 1$ by $1$.
