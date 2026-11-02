---
tag: R8071FWJRK
kind: concept
name: Convex hull algorithms
msc: [68U05, 52B55, 68W40]
sources:
  - url: https://en.wikipedia.org/wiki/Convex_hull_algorithms
same_as:
  wikidata: Q5166520
  wikipedia: Convex hull algorithms
---

## Summary

Convex hull algorithms take a finite set of $n$ points in $\R^d$ and compute its [[convex hull|0FQSDC2EQ2]].
The output is usually the list of its vertices or of its facets.
In the plane, Graham scan and other methods run in $O(n \log n)$ time.
Gift wrapping runs in $O(n h)$ time, where $h$ is the number of hull vertices.
Chan's algorithm combines both ideas and runs in $O(n \log h)$ time.
Since sorting reduces to the planar convex hull problem, $\Omega(n \log n)$ operations are needed in the worst case in the algebraic decision tree model.
These algorithms are a basic building block of [[computational geometry|KAT7K2NE9Z]].

## Explanations

### L1 human

Hammer nails into a board at some points and stretch a rubber band around all of them; the band takes the shape of the convex hull.
A convex hull algorithm finds which nails the band touches.
Gift wrapping starts at the leftmost nail and repeatedly turns to the nail that keeps all others on one side, like wrapping a present.
For the points $(0,0)$, $(2,0)$, $(1,1)$, $(1,3)$, the hull is the triangle with corners $(0,0)$, $(2,0)$, $(1,3)$, and $(1,1)$ lies inside it.
