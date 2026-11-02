---
tag: 6P9PXQDSEN
kind: concept
name: Differential of a smooth map
msc: [58A05, 57R35]
sources:
  - url: https://en.wikipedia.org/wiki/Pushforward_(differential)
same_as:
  wikidata: Q1969983
  wikipedia: Pushforward (differential)
---

## Summary

The differential of a smooth map between manifolds is its best linear approximation at a point.
It sends tangent vectors at a point of the source to tangent vectors at the image point in the target.
In local coordinates it is given by the Jacobian matrix of partial derivatives.
It extends the derivative of calculus to curved spaces, and it obeys the chain rule.

## Explanations

### L1 human

Imagine a smooth map that wraps a line around a circle.
If a point moves along the line with some velocity, its image moves along the circle with some velocity.
The differential is the rule that turns the first velocity into the second.
For $t \mapsto (\cos t, \sin t)$, the velocity $1$ at time $t$ becomes the tangent arrow $(-\sin t, \cos t)$.
