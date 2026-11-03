---
tag: NJ1QWE4Q3Y
kind: concept
name: Pareto front
msc: [90C29, 90B50]
sources:
  - url: https://en.wikipedia.org/wiki/Pareto_front
same_as:
  wikidata: Q55362336
  wikipedia: Pareto front
---

## Summary

The Pareto front of a [[multi-objective optimization|E560RGEKPP]] problem is the set of objective vectors that are not dominated by any other attainable vector.
It shows exactly which trade-offs between the objectives are possible and efficient.
Decision makers choose a point on it, and many algorithms aim to approximate it by a finite set of points.
It is also called the Pareto frontier or the efficient frontier, as in portfolio theory.

## Explanations

### L1 human

Plot every possible outcome as a point, with cost on one axis and risk on the other, both to be kept low.
The Pareto front is the lower-left edge of this cloud of points.
From any point on that edge, you cannot lower the cost without raising the risk.
Points behind the edge are wasteful, since some point on the edge is better in both respects.
