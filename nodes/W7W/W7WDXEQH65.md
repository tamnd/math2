---
tag: W7WDXEQH65
kind: concept
name: Limiting subdifferential
msc: [49J52, 49J53]
sources:
  - url: https://en.wikipedia.org/wiki/Subderivative
---

## Summary

The limiting subdifferential, also called the Mordukhovich or basic subdifferential, is a set of generalized gradients of a function at a point.
It is built in two steps.
One first takes the regular (Fréchet) subgradients at nearby points, then all limits of these as the points approach the given point.
For a convex function it equals the [[subdifferential|9C5WXYYQEK]] of convex analysis, and for a locally Lipschitz function its convex hull is the [[Clarke generalized gradient|20967BXZKA]].
It is usually smaller than the Clarke generalized gradient and has a good calculus, which makes it a main tool of variational analysis.
The [[definition|YXJDQM9VVD]] gives the precise construction.

## Explanations

### L1 human

At a smooth point, the gradient is the only reasonable slope.
At a kink, one looks at the slopes that work just beside the point and keeps all their limits.
For $-\abs{x}$ at $0$, no slope works at the peak itself, but the nearby slopes are $1$ and $-1$.
So the limiting subdifferential is the two-point set $\set{-1, 1}$, while the Clarke generalized gradient fills in the whole interval $[-1, 1]$.
