---
tag: 73WPYFAEWS
kind: concept
name: Five-point stencil
msc: [65N06, 65D25]
specializes: [752Z7DRT7P]
sources:
  - url: https://en.wikipedia.org/wiki/Five-point_stencil
same_as:
  wikidata: Q5455804
  wikipedia: Five-point stencil
---

## Summary

A five-point stencil is a set of five grid points used to approximate derivatives by finite differences.
On a line, it is a point with two neighbours on each side, and it gives fourth-order formulas for the first and second derivative.
In the plane, it is a point with its four nearest neighbours, and it gives the standard second-order approximation of the [[Laplacian|0E0B6RA8K0]].
The planar version is the basic discretisation of the Poisson equation in the [[finite difference method|X7HYEBA5SA]].

## Explanations

### L1 human

Picture a square grid and a point on it together with its neighbours to the left, right, above and below: these five points form a plus sign.
Adding the four neighbour values and subtracting four times the centre value measures how much the centre differs from the average around it.
For $u(x, y) = x^2 + y^2$ at the origin with spacing $1$, this gives $1 + 1 + 1 + 1 - 0 = 4$, which equals the Laplacian $u_{xx} + u_{yy} = 4$.
