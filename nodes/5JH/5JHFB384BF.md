---
tag: 5JHFB384BF
kind: concept
name: de Boor's algorithm
msc: [65D07, 41A15, 65D17]
sources:
  - url: https://en.wikipedia.org/wiki/De_Boor%27s_algorithm
same_as:
  wikidata: Q5244271
  wikipedia: De Boor's algorithm
---

## Summary

De Boor's algorithm evaluates a spline written in the [[B-spline|62AFX32JGT]] basis at a point.
It replaces the coefficients of the B-splines that are active at the point by repeated [[convex combinations|21SXYJYC59]], until a single value remains.
It needs no explicit B-spline values, is numerically stable, and generalizes [[de Casteljau's algorithm|HT4Q9K3P2Z]] for Bézier curves.

## Explanations

### L1 human

A spline curve is controlled by a list of control points, but only a few of them affect a given parameter value.
De Boor's algorithm takes those few points and repeatedly replaces each pair of neighbours by a point on the segment between them.
After as many rounds as the degree, one point is left, and that point lies on the curve.
For a quadratic spline, three control points are blended into two, and the two into one.
