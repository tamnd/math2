---
tag: D59HBKKRP9
kind: concept
name: Spline interpolation
msc: [41A15, 65D07, 41A05]
sources:
  - url: https://en.wikipedia.org/wiki/Spline_interpolation
same_as:
  wikidata: Q545002
  wikipedia: Spline interpolation
---

## Summary

Spline interpolation passes a [[spline|84TJ8KQ926]] through given data points, using the data nodes as knots.
Unlike [[polynomial interpolation|SS1YMS2NPC]] of high degree, it keeps the degree of each piece low, which avoids [[Runge's phenomenon|ZMT8JF21R6]] and gives small errors for smooth data.
The most common choice is the [[cubic spline|V42H0R3EKX]], for which two extra conditions at the ends of the interval make the interpolant unique.
The coefficients solve a [[tridiagonal|DARX1KZRHZ]] linear system, so the cost grows only linearly with the number of points.

## Explanations

### L1 human

Connecting data points by straight segments gives a curve with corners.
Spline interpolation uses curved pieces instead, typically cubics, and chooses them so that neighbouring pieces meet with the same slope and the same bending.
The result looks like a smooth curve drawn through the points by hand.
Unlike one polynomial through all the points, it does not swing wildly between the points when there are many of them.
The [[definition|RGT7WEZG8X]] states the conditions.
