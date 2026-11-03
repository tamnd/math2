---
tag: M7HYT44ZJA
kind: concept
name: Interior-point method
msc: [90C51, 90C05, 90C25]
sources:
  - url: https://en.wikipedia.org/wiki/Interior-point_method
same_as:
  wikidata: Q461992
  wikipedia: Interior-point method
---

## Summary

Interior-point methods are algorithms for [[convex optimization|1W1BXJN9ER]] whose iterates stay strictly inside the feasible region.
They replace the constraints by a [[barrier function|59ZC4Z9611]] and follow the [[central path|AFQTYDNDGH]] toward an optimum with [[Newton steps|TNQZVR6TFN]].
[[Karmarkar's algorithm|8DGAXR9WZR]] of 1984 made them a practical and polynomial-time alternative to the simplex method for linear programming.
With [[self-concordant|N4Q5T33P33]] barriers they also solve second-order cone and semidefinite programs in polynomial time.

## Explanations

### L1 human

The simplex method walks along the edges of the feasible polytope from corner to corner.
An interior-point method instead cuts through the middle of the region.
It keeps a safe distance from the walls with a barrier, and it lowers the barrier a little at each round, so the iterates drift toward the optimal corner.
Each round needs only a few Newton steps, and the number of rounds grows slowly with the accuracy asked for.
