---
tag: V42H0R3EKX
kind: concept
name: Cubic spline
msc: [41A15, 65D07]
specializes: [84TJ8KQ926]
sources:
  - url: https://en.wikipedia.org/wiki/Spline_interpolation
---

## Summary

A cubic spline is a [[spline|84TJ8KQ926]] of degree $3$.
It is made of cubic polynomial pieces whose values, first derivatives and second derivatives agree at the knots.
It is the most used spline, because it is the lowest degree whose graph looks smooth to the eye, with continuous curvature.
A natural cubic spline also has zero second derivative at both ends.
In [[spline interpolation|D59HBKKRP9]], the natural cubic spline is the interpolant with the [[least total squared second derivative|28C5WWGX9J]], the mathematical form of the bent draftsman's strip.

## Explanations

### L1 human

A cubic spline is a chain of cubic curves joined end to end.
At each joint the two neighbouring pieces have the same height, the same slope and the same bending, so no corner or sudden change of curvature is visible.
For example, the function equal to $0$ for $x \le 0$ and to $x^3$ for $x \ge 0$ is a cubic spline with one knot at $0$.
Cubic splines are used to draw smooth curves through data, to design car bodies and fonts, and to approximate functions.
The [[definition|B7YND5ZVMF]] lists the conditions.
