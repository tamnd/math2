---
tag: 7WSH8Z6F7T
kind: concept
name: Trilateration
msc: [86A30, 51N20]
sources:
  - url: https://en.wikipedia.org/wiki/True-range_multilateration
same_as:
  wikidata: Q115650097
  wikipedia: True-range multilateration
---

## Summary

Trilateration finds the position of a point from its distances to points with known positions.
Each distance places the point on a [[sphere|P9CM4GQ2T0]] around a known point, and the position is the common point of these spheres.
In space, three distances leave in general two candidate positions, and a fourth distance or extra knowledge picks one.
It underlies modern surveying with distance meters and, in a modified form, [[satellite positioning|TZ37HTS1AT]].

## Explanations

### L1 human

If you know you are $5$ km from town $A$, you are somewhere on a circle around $A$.
If you are also $7$ km from town $B$, you are on one of the two points where the two circles cross.
A third distance, from a town not on the line $AB$, tells you which of the two points it is.
In space the circles become spheres, and one needs one more distance.
