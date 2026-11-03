---
tag: MRNW9644HH
kind: concept
name: Robust optimization
msc: [90C17, 90C47]
sources:
  - url: https://en.wikipedia.org/wiki/Robust_optimization
same_as:
  wikidata: Q2160088
  wikipedia: Robust optimization
---

## Summary

Robust optimization handles uncertain data by asking a solution to be feasible and good for every value of the data in a given uncertainty set.
It optimizes the worst case, so it needs no probability distribution of the data.
For many convex problems and suitable uncertainty sets, such as ellipsoids or polyhedra, the robust problem has a tractable equivalent convex reformulation.
It complements [[stochastic programming|2YW60J1GT6]], which uses probability distributions instead of sets.

## Explanations

### L1 human

Suppose a bridge must carry a load that is not known exactly, only that it lies within some range.
A robust design is one that holds for every load in the range, not only for the most likely one.
Robust optimization finds the cheapest such design.
It trades a little performance in the typical case for safety in every case allowed.
