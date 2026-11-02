---
tag: DVGFRRYK10
kind: concept
name: Curve-shortening flow
msc: ["53E10", 53A04]
sources:
  - url: https://en.wikipedia.org/wiki/Curve-shortening_flow
same_as:
  wikidata: Q18349490
  wikipedia: Curve-shortening flow
---

## Summary

The curve-shortening flow moves each point of a plane curve along its normal vector.
The speed is the [[curvature|7JQS6VKFEZ]] of the curve at that point.
It is the one-dimensional case of [[mean curvature flow|2YYV01C7QQ]] and the steepest descent flow for the length of the curve.
A heat-equation-like smoothing effect makes curves rounder over time, and embedded closed curves shrink to round points by the [[Gage–Hamilton–Grayson theorem|FVGW1381TZ]].

## Explanations

### L1 human

Imagine a closed loop of string in the plane in which every bit moves inward at a speed equal to how sharply the string bends there.
Sharp corners move fast and flat parts move slowly, so the loop smooths out.
A circle of radius $r_0$ stays a circle, and its radius $r(t)$ satisfies $r' = -1/r$, so $r(t) = \sqrt{r_0^2 - 2t}$ and the circle disappears at time $r_0^2 / 2$.
The flow decreases the length as fast as possible, which is the reason for its name.
