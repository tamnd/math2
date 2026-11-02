---
tag: FABJSZ9D3S
kind: problem
name: Dido's problem
msc: [49K05, 52A40, 49-03]
uses: [6FY0KHMK5A, KBX8RBZ626, EWS4WFTA7W]
about: [KBX8RBZ626]
sources:
  - url: https://en.wikipedia.org/wiki/Isoperimetric_inequality
history:
  posed_by: "the legend of Queen Dido, told in Virgil's Aeneid"
  first_stated: "1st century BC"
---

## Problem

Let $\ell > 0$.
Consider [[plane curves|EWS4WFTA7W]] of length $\ell$ that start and end on a fixed straight line and otherwise lie on one side of it.
Which of them encloses, together with the line, the largest area?

In coordinates, the line is the $x$-axis and the curve is a piecewise $C^1$ map $t \mapsto (x(t), y(t))$, $0 \le t \le 1$, with $y(0) = y(1) = 0$ and $y \ge 0$.
When the curve has no self-crossings, the enclosed area is $\abs{\int_0^1 y(t) \, x'(t) \, dt}$.

## Remarks

The answer is a semicircle of length $\ell$, with its diameter on the line; it encloses the area $\ell^2 / (2\pi)$.
Reflecting a curve in the line turns the problem into the classical isoperimetric problem for closed curves of length $2\ell$.
So the answer follows from the [[isoperimetric inequality|KBX8RBZ626]] in the plane.
Written with such a parametrised curve, it is an [[isoperimetric problem of the calculus of variations|6FY0KHMK5A]].
Its Euler–Lagrange equation with a multiplier says that the curve has constant curvature, so it is an arc of a circle.
The name comes from the legend of the founding of Carthage.
Dido was granted as much land as an ox hide could enclose; she cut the hide into a thin strip and laid it out against the coast.

## Explanations

### L1 human

You have a rope of fixed length and a straight coastline.
You want to fence off the largest piece of land, using the coast as one side.
The best shape is a half disc, with the rope as the round edge.
