---
tag: NEXBTGYYRG
kind: concept
name: Bézier curve
msc: [65D17, 68U07, 41A10]
sources:
  - url: https://en.wikipedia.org/wiki/B%C3%A9zier_curve
same_as:
  wikidata: Q214728
  wikipedia: Bézier curve
---

## Summary

A Bézier curve is a polynomial curve determined by a finite list of control points, given by the [[Bernstein basis polynomials|0JT92VK307]].
It starts at the first control point, ends at the last one, and lies in the [[convex hull|0FQSDC2EQ2]] of all of them.
Bézier curves are the basic curves of vector graphics, fonts and computer-aided design.

## Explanations

### L1 human

Pick a start point, an end point, and a few extra points in between that the curve is attracted to but does not have to pass through.
The Bézier curve leaves the start point heading toward the second point and arrives at the end point coming from the second to last point.
Moving one control point changes the curve smoothly everywhere.
For three points $P_0, P_1, P_2$ one gets the parabola arc $(1-t)^2 P_0 + 2t(1-t) P_1 + t^2 P_2$.
