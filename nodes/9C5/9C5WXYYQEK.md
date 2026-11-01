---
tag: 9C5WXYYQEK
kind: concept
name: Subderivative
msc: [26A51, 49J52, 52A41]
sources:
  - url: https://en.wikipedia.org/wiki/Subderivative
same_as:
  wikidata: Q289500
  wikipedia: Subderivative
---

## Summary

Take a [[convex function|07Q7CNM5WF]] and a point of its graph.
A subderivative there is the slope of a line through that point that stays below the whole graph.
At every interior point a convex function has at least one subderivative, even where it has no [[derivative|0V1EJCT8G6]].
The set of all subderivatives at a point is the subdifferential, and it replaces the derivative in the optimality conditions of nonsmooth convex optimization.
The [[definition|A289X08MR1]] gives the precise condition.

## Explanations

### L1 human

At a smooth point of a convex graph there is one tangent line, and it lies below the graph.
At a corner there are many lines that touch the graph there and stay below it.
Their slopes are the subderivatives.
For $\abs{x}$ at $0$, every slope between $-1$ and $1$ works, so the subdifferential is $[-1, 1]$.
A point is a minimum of a convex function exactly when $0$ is one of the subderivatives there.
