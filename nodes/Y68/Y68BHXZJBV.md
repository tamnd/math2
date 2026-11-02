---
tag: Y68BHXZJBV
kind: concept
name: Perimeter of a set
msc: [49Q15, 28A75, 26B30]
sources:
  - url: https://en.wikipedia.org/wiki/Caccioppoli_set
---

## Summary

The perimeter of a measurable set $E \subseteq \R^n$ is a measure-theoretic version of the area of its boundary.
It is the [[total variation|8QA5DEWNYD]] of the distributional gradient of the indicator function of $E$.
For a set with smooth boundary it equals the $(n-1)$-dimensional area of the boundary, but it is defined for every Lebesgue measurable set.
It is lower semicontinuous under convergence in $L^1_{\mathrm{loc}}$, which makes it the natural quantity to minimize in problems such as the isoperimetric problem.

## Explanations

### L1 human

To measure the boundary of a rough set, test the set against all small vector fields and record the largest flux that can leave through it.
For a smooth region this flux is largest when the field points straight out of the boundary, and it then equals the area of the boundary.
For example, the unit disc in the plane has perimeter $2\pi$, its circumference.
Removing a single point or a segment from the disc does not change its perimeter, because the perimeter only sees the set up to sets of measure zero.
