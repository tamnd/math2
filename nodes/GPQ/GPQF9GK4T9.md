---
tag: GPQF9GK4T9
kind: concept
name: Intersection multiplicity
msc: [14C17, 13H15]
sources:
  - url: https://en.wikipedia.org/wiki/Intersection_number
---

## Summary

Two subvarieties meet along the components of their intersection.
The intersection multiplicity along such a component is a positive integer that says how many times it should be counted.
For curves in the plane it is the dimension of a local ring, and in general it is given by Serre's Tor formula.
With these multiplicities, counts of intersection points become stable under deformation, which is what makes [[Bézout's theorem|KWNVF194D8]] and [[intersection theory|4HV4WTAX9P]] work.

## Explanations

### L1 human

When a line crosses a curve transversally, the crossing point counts once.
When the line is tangent to the curve, two crossings have merged into one point, and the point should count twice.
The intersection multiplicity makes this precise.
For the parabola $y = x^2$ and the line $y = 0$, the only common point is the origin, and its multiplicity is $2$.
Moving the line to $y = \epsilon$ with $\epsilon > 0$ splits it into the two points $x = \pm\sqrt{\epsilon}$.
