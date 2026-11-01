---
tag: MKS9H497AM
kind: concept
name: Inductive dimension
msc: [54F45]
sources:
  - url: https://en.wikipedia.org/wiki/Inductive_dimension
same_as:
  wikidata: Q841816
  wikipedia: Inductive dimension
---

## Summary

The inductive dimensions of a topological space are defined by induction from the dimension of boundaries.
A space has dimension at most $n$ when points, or closed sets, have small neighbourhoods whose boundaries have dimension at most $n - 1$.
There are two versions, the small inductive dimension $\operatorname{ind}$ and the large inductive dimension $\operatorname{Ind}$.
For separable metric spaces both agree with the [[Lebesgue covering dimension|A3W7RGXXK9]].

## Explanations

### L1 human

A solid ball in space can be cut out from its surroundings by its surface, which is two-dimensional.
A disc in the plane is cut out by a circle, which is one-dimensional, and an interval on a line is cut out by two points, which are zero-dimensional.
The inductive dimension turns this into a definition: the dimension of a space is one more than the dimension of the walls one needs to cut out small pieces.
The empty set has dimension $-1$ to start the induction.
