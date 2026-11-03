---
tag: PJVT97Z7EN
kind: concept
name: Degeneracy and cycling in the simplex method
msc: [90C05, 90C49]
sources:
  - url: https://en.wikipedia.org/wiki/Simplex_algorithm
    locator: "Degeneracy: stalling and cycling"
---

## Summary

A [[basic feasible solution|957S7V3JW8]] is degenerate when some basic variable is zero; then several bases can describe the same vertex.
At a degenerate vertex the [[simplex algorithm|MH272QHWPM]] can make a pivot that changes the basis but not the point, a degenerate step.
A sequence of degenerate steps can return to an earlier basis, and then the method repeats the same bases forever; this is cycling.
Anti-cycling pivot rules, such as [[Bland's rule|YM58206VR1]] or lexicographic rules, prevent cycling and make the method finite.

## Explanations

### L1 human

The simplex method walks from corner to corner of a many-sided shape, always uphill.
At some corners more walls meet than are needed to pin the corner down, and the method can then change its description of the corner without moving.
If it is unlucky, it changes descriptions in a circle and never leaves.
In the plane, for instance, the corner $(1, 0)$ of the region $x \ge 0$, $y \ge 0$, $x + y \le 1$, $x \le 1$ lies on three of the boundary lines at once, so it is degenerate.
