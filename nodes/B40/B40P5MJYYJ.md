---
tag: B40P5MJYYJ
kind: concept
name: Symmetric derivative
msc: [26A24]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetric_derivative
same_as:
  wikidata: Q3773126
  wikipedia: Symmetric derivative
---

## Summary

The symmetric derivative of a function at a point is a limit of slopes of secant lines.
The two points of each secant line lie symmetrically on both sides of the point.
When the ordinary [[derivative|0F1WR9C83K]] exists, the symmetric derivative exists and has the same value.
The converse fails, so the symmetric derivative is a genuine generalization.
Its quotient is also the central difference used to approximate derivatives numerically.

## Explanations

### L1 human

Instead of comparing $f(x + h)$ with $f(x)$, compare $f(x + h)$ with $f(x - h)$, and divide by the distance $2h$.
This balances the left and the right side.
For $\abs{x}$ at $0$, the two sides cancel: $\abs{h} - \abs{-h} = 0$.
So $\abs{x}$ has symmetric derivative $0$ at $0$, although it has a corner there.
