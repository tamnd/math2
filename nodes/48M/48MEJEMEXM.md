---
tag: 48MEJEMEXM
kind: concept
name: Lopatinskii–Shapiro condition
msc: [35J40, 35J25]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic_boundary_value_problem
---

## Summary

The Lopatinskii–Shapiro condition, also called the complementing condition, is an algebraic condition on boundary operators.
It is what a boundary value problem for an [[elliptic operator|XY8GEQSWPR]] needs to be well behaved.
It is checked at each boundary point by freezing coefficients and looking at an ordinary differential equation in the normal direction.
When it holds, the problem has a priori estimates in Sobolev spaces and is a Fredholm problem.
It plays for boundary conditions the role that ellipticity plays for the operator itself.

## Explanations

### L1 human

An elliptic equation inside a domain needs the right number and the right kind of conditions on the boundary.
To test them, zoom in on one boundary point until the boundary looks flat and the coefficients look constant.
Then look for solutions that oscillate along the boundary and decay into the interior.
The condition says that the boundary conditions kill all such solutions.
For the Laplacian, prescribing the values $u$ on the boundary passes this test, and so does prescribing the normal derivative.
