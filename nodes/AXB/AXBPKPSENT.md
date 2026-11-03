---
tag: AXBPKPSENT
kind: concept
name: Duality gap
msc: [90C46, 49N15]
sources:
  - url: https://en.wikipedia.org/wiki/Duality_gap
same_as:
  wikidata: Q5310264
  wikipedia: Duality gap
---

## Summary

The duality gap of an optimization problem is the optimal value of the problem minus the optimal value of its dual.
By weak duality it is never negative.
When it is zero one says that strong duality holds, and the dual then certifies optimality.
For a primal and a dual feasible point, the difference of their values is also called a duality gap.
It bounds how far each point is from optimal.

## Explanations

### L1 human

The dual problem gives lower bounds on the best possible cost.
The gap is the space between the best lower bound and the true best cost.
For linear programs that have optimal solutions the gap is zero.
For hard problems, such as problems with integer variables, there is often a positive gap.
