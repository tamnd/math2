---
tag: P9ZPH7EC8K
kind: concept
name: Thin plate spline
msc: [41A15, 41A05, 41A63]
specializes: [XJ0JGPBC8R]
sources:
  - url: https://en.wikipedia.org/wiki/Thin_plate_spline
same_as:
  wikidata: Q7784288
  wikipedia: Thin plate spline
---

## Summary

A thin plate spline is a smooth function of two variables that interpolates scattered data with the least bending energy.
It is a sum of translates of the radial function $r^2 \log r$ and an affine function, the case $d = 2$, $m = 2$ of a [[polyharmonic spline|XJ0JGPBC8R]].
The name comes from the physical picture of a thin metal sheet bent to pass through given heights.
Thin plate splines are widely used for surface fitting and for smooth image warping.

## Explanations

### L1 human

Pin a thin flexible sheet at a few points at given heights; it settles in the shape that bends the least.
The thin plate spline is the mathematical version of that shape.
Away from the pins it satisfies the [[biharmonic equation|AS8A9F5SKE]], the equation of a bent elastic plate with no load on it.
With three pins that are not on a line, the sheet is simply the tilted plane through them, because a plane needs no bending at all.
