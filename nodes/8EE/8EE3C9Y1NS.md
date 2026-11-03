---
tag: 8EE3C9Y1NS
kind: concept
name: Frank–Wolfe algorithm
msc: [90C25, 90C30, 65K05]
sources:
  - url: https://en.wikipedia.org/wiki/Frank%E2%80%93Wolfe_algorithm
same_as:
  wikidata: Q2020318
  wikipedia: Frank–Wolfe algorithm
---

## Summary

The Frank–Wolfe algorithm, also called the conditional gradient method, minimises a smooth convex function over a compact convex set.
At each step it minimises the linear approximation of the function over the set and moves part of the way toward that minimiser.
It needs no projections, only a linear minimisation over the set, which is cheap for polytopes such as the [[simplex|YX1DJK2QAG]] and for norm balls.
Its iterates are convex combinations of few extreme points, which gives sparse solutions, and its error decreases at rate $O(1/k)$.
It was introduced by Marguerite Frank and Philip Wolfe in 1956.

## Explanations

### L1 human

Suppose you must stay inside a region, and projecting a point back into the region is expensive.
Frank–Wolfe instead asks: if the function were flat, with its current slope, which point of the region would be best?
That point is a corner of the region, found by a linear problem.
The method then takes a step from the current point toward that corner, with step length $2/(k+2)$ at step $k$, so it always stays inside.
