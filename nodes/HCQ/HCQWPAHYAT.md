---
tag: HCQWPAHYAT
kind: concept
name: Cubic Hermite spline
msc: [41A15, 65D07, 41A05]
specializes: [84TJ8KQ926]
sources:
  - url: https://en.wikipedia.org/wiki/Cubic_Hermite_spline
same_as:
  wikidata: Q1537263
  wikipedia: Cubic Hermite spline
---

## Summary

A cubic Hermite spline is a piecewise cubic function that matches prescribed values and prescribed first derivatives at given nodes.
On each interval between nodes it is the cubic [[Hermite interpolant|9Z50M2WPTP]] of the data at the two ends.
It is continuously differentiable, and each piece depends only on local data, which makes it the basis of many curve tools in graphics and animation.

## Explanations

### L1 human

On each gap between two nodes, prescribe a height and a slope at both ends.
Exactly one cubic matches these four numbers.
A cubic Hermite spline joins these cubics end to end.
Since neighbouring pieces share the value and the slope at each node, the curve has no corners.
For example, data $p_0 = 0$, $m_0 = 0$ at $x = 0$ and $p_1 = 1$, $m_1 = 0$ at $x = 1$ give the smooth step $3x^2 - 2x^3$.
