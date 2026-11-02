---
tag: 44GBFZ16SG
kind: concept
name: Analytic index
msc: [58J20, 47A53]
specializes: [2V9Q4KHY1T]
sources:
  - url: https://en.wikipedia.org/wiki/Atiyah–Singer_index_theorem
---

## Summary

The analytic index of an elliptic operator $P$ on a closed manifold is $\dim \ker P - \dim \operatorname{coker} P$.
Both dimensions are finite because elliptic operators on closed manifolds are [[Fredholm operators|8HWGKWD6ZM]] between suitable Sobolev spaces.
So the analytic index is a [[Fredholm index|2V9Q4KHY1T]].
The Atiyah–Singer index theorem computes it as the [[topological index|QDCD33CS21]].

## Explanations

### L1 human

The kernel of $P$ counts the independent solutions of $Pu = 0$.
The cokernel counts the independent conditions that $f$ must satisfy for $Pu = f$ to be solvable.
The analytic index is the difference of these two counts.
Take the Cauchy–Riemann operator $\bar\partial$ on functions on a closed Riemann surface of genus $g$.
Its kernel is the constants and its cokernel has dimension $g$, so the index is $1 - g$.
