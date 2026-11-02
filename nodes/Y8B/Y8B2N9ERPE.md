---
tag: Y8B2N9ERPE
kind: concept
name: Non-uniform rational B-spline
msc: [65D17, 68U07, 41A15]
sources:
  - url: https://en.wikipedia.org/wiki/Non-uniform_rational_B-spline
same_as:
  wikidata: Q734737
  wikipedia: Non-uniform rational B-spline
---

## Summary

A non-uniform rational B-spline, or NURBS, is a curve or surface given as a weighted average of control points.
The weights are [[B-spline|62AFX32JGT]] basis functions times positive numbers, divided by their sum.
The weights make the representation rational, which lets it reproduce conic sections such as circles exactly.
NURBS are the standard representation of curves and surfaces in computer-aided design.

## Explanations

### L1 human

A designer moves a few control points, and the curve follows them smoothly.
In a NURBS curve each control point also has a weight, and a larger weight pulls the curve closer to that point.
With all weights equal, one gets an ordinary B-spline curve.
With suitable weights, three control points at the corners $(1, 0)$, $(1, 1)$, $(0, 1)$ give an exact quarter of the unit circle, which no polynomial curve can do.
