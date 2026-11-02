---
tag: VQ4Q2V45RP
kind: concept
name: Line segment
msc: [52A05, 51N10]
sources:
  - url: https://en.wikipedia.org/wiki/Line_segment
same_as:
  wikidata: Q166154
  wikipedia: Line segment
---

## Summary

The line segment between two points is the set of all points on the straight path from one to the other, endpoints included.
In a real vector space it is the set of [[convex combinations|21SXYJYC59]] of the two points.
A set is [[convex|02AS45T3H9]] exactly when it contains the segment between any two of its points, so segments are the building blocks of convexity.

## Explanations

### L1 human

Take two points and stretch a string tightly between them.
The string traces the line segment.
In coordinates, the segment from $x$ to $y$ is swept out by $(1 - t) x + t y$ as $t$ runs from $0$ to $1$.
For example, the segment from $(0, 0)$ to $(2, 2)$ in the plane is the set of points $(s, s)$ with $0 \le s \le 2$.
