---
tag: VSGTSQ7RY8
kind: concept
name: Transfinite diameter
msc: [31A15, 30C85]
sources:
  - url: https://en.wikipedia.org/wiki/Conformal_radius
---

## Summary

The transfinite diameter of a compact set $K$ in the plane measures how far apart many points of $K$ can be placed at once.
For each $n$ one maximizes the geometric mean of the mutual distances of $n$ points of $K$, and then lets $n$ tend to infinity.
For $n = 2$ this is the ordinary diameter, which explains the name.
A theorem of Fekete and Szegő says that the transfinite diameter equals the [[logarithmic capacity|DBQXRTC0VN]] of $K$.

## Explanations

### L1 human

Place $n$ points in $K$ so that they are as spread out as possible, in the sense that the product of all their mutual distances is largest.
Take the geometric mean of these distances.
For two points this is just the largest distance in $K$, the diameter.
As $n$ grows, the points must crowd together, and the mean distance decreases to a limit, the transfinite diameter.
For the unit circle the best points are the $n$-th roots of unity, and the limit is $1$.
