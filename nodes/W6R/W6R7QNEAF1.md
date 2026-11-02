---
tag: W6R7QNEAF1
kind: concept
name: Caccioppoli set
msc: [49Q15, 28A75, 26B30]
sources:
  - url: https://en.wikipedia.org/wiki/Caccioppoli_set
same_as:
  wikidata: Q17004137
  wikipedia: Caccioppoli set
---

## Summary

A Caccioppoli set, or set of finite perimeter, is a measurable subset of $\R^n$ whose [[perimeter|Y68BHXZJBV]] is finite.
Equivalently, its indicator function has [[bounded variation|9YQ999QHHT]].
These sets are the measure-theoretic replacement for regions with smooth boundary.
They are closed under the limits that appear when one minimizes area.
So they give a setting where problems such as the isoperimetric problem have solutions.

## Explanations

### L1 human

Many regions that come up as limits of nice regions have wild boundaries, and the classical notion of surface area breaks down for them.
A Caccioppoli set is a region whose boundary has finite area in a weak sense that still works for such limits.
Any bounded region in the plane with a polygonal boundary is a Caccioppoli set.
The union of the disjoint discs of radius $2^{-k}$ centred at $(3k, 0)$, for $k = 1, 2, \dots$, is also one, since its perimeter is $\sum_k 2\pi 2^{-k} = 2\pi$.
The union of the discs of radius $1$ centred at the same points is not, since its perimeter is infinite.
