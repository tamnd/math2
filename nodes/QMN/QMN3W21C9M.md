---
tag: QMN3W21C9M
kind: concept
name: Box spline
msc: [41A15, 41A63, 65D07]
sources:
  - url: https://en.wikipedia.org/wiki/Box_spline
same_as:
  wikidata: Q4951620
  wikipedia: Box spline
---

## Summary

A box spline is a piecewise polynomial function of several variables obtained by projecting a unit cube of higher dimension onto $\R^d$.
Its value at a point is the volume of the slice of the cube that lands at that point.
Box splines generalize the uniform [[B-splines|62AFX32JGT]] to several variables, and their integer translates give smooth spline spaces on regular grids and triangulations.

## Explanations

### L1 human

Shine light through a cube onto a lower dimensional screen and record how thick the cube is above each point of the screen.
That thickness profile is a box spline.
Mapping the square $[0,1]^2$ to the line by $(u_1, u_2) \mapsto u_1 + u_2$ gives a tent, the hat function on $[0, 2]$.
More directions give smoother bumps, and in the plane one gets smooth bumps adapted to grids of squares or triangles.
