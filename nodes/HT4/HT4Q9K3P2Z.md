---
tag: HT4Q9K3P2Z
kind: concept
name: de Casteljau's algorithm
msc: [65D17, 68U07, 41A10]
sources:
  - url: https://en.wikipedia.org/wiki/De_Casteljau%27s_algorithm
same_as:
  wikidata: Q1179419
  wikipedia: De Casteljau's algorithm
---

## Summary

De Casteljau's algorithm computes a point of a [[Bézier curve|NEXBTGYYRG]] by repeated linear interpolation between control points.
It also evaluates polynomials in [[Bernstein–Bézier form|Z5Y0VH10YR]].
It uses only [[convex combinations|21SXYJYC59]], so it is numerically stable.
The intermediate points also give the control points of the two halves of the curve, which is the basis of subdivision methods in computer-aided design.

## Explanations

### L1 human

Draw the polygon through the control points and mark the point a fraction $t$ of the way along each edge.
Join the marked points to get a polygon with one fewer vertex, and repeat.
After as many rounds as the degree, a single point is left, and it is the point of the curve at parameter $t$.
For three points and $t = 1/2$, one takes the two edge midpoints and then the midpoint between them.
