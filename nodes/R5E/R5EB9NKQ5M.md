---
tag: R5EB9NKQ5M
kind: concept
name: Oriented matroid
msc: [52C40, 05B35, 52B40]
specializes: [PX31ZNYS3Z]
sources:
  - url: https://en.wikipedia.org/wiki/Oriented_matroid
same_as:
  wikidata: Q16155113
  wikipedia: Oriented matroid
---

## Summary

An oriented matroid is a [[matroid|PX31ZNYS3Z]] in which each minimal dependence also carries signs, recording which elements lie on which side.
It abstracts the combinatorics of real vector configurations, of point configurations, of [[hyperplane arrangements|N602W0WAVT]] and of directed graphs.
Faces of [[convex polytopes|300K6CB1KH]], regions of real arrangements and the results of linear programming can all be described in terms of oriented matroids.
Not every oriented matroid comes from vectors; by the topological representation theorem, oriented matroids correspond to arrangements of pseudospheres.

## Explanations

### L1 human

Take some vectors in the plane or in space.
A dependence like $v_1 + v_2 - v_3 = 0$ tells you that $v_1$ and $v_2$ lie on one side and $v_3$ on the other.
An oriented matroid keeps only these signs, not the numbers.
Remarkably, a lot of geometry, such as which points form the corners of their convex hull, can be recovered from the signs alone.
