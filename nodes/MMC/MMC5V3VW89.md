---
tag: MMC5V3VW89
kind: concept
name: Cutting-plane methods for convex optimization
msc: [90C25, 65K05]
sources:
  - url: https://en.wikipedia.org/wiki/Cutting-plane_method
---

## Summary

Cutting-plane methods for convex optimization minimize a convex function by repeatedly cutting away half-spaces that cannot contain a minimizer.
Each cut comes from a subgradient at a query point, since a convex function lies above all its tangent hyperplanes.
The methods differ in the choice of the query point.
Kelley's method minimizes a piecewise linear model, while the center of gravity and ellipsoid methods use centers of the remaining region.
They need only a subgradient oracle and are the basis of polynomial-time results for convex programs, such as the [[ellipsoid method|TJR5MQHNYE]] for linear programming.

## Explanations

### L1 human

Imagine searching for the lowest point of a bowl hidden inside a box.
At any point you can ask for the slope, and the slope tells you that the lowest point is not uphill from where you stand.
So you can throw away the uphill half of the box.
Each question removes a slice, and a good choice of where to ask makes the remaining region shrink quickly.
