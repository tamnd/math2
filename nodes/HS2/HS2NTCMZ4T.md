---
tag: HS2NTCMZ4T
kind: concept
name: Minkowski content
msc: [28A75, 28A80]
sources:
  - url: https://en.wikipedia.org/wiki/Minkowski_content
same_as:
  wikidata: Q17082571
  wikipedia: Minkowski content
---

## Summary

The Minkowski content measures the $m$-dimensional size of a subset of $\R^n$ through the volume of its thin neighbourhoods.
One thickens the set by $r$, takes the [[Lebesgue measure|2Z2QVWZ262]] of the result, and divides by the volume of an $(n-m)$-dimensional ball of radius $r$.
For nice sets it gives length, area and volume, and for rough sets it is linked to the box-counting dimension.

## Explanations

### L1 human

To find the length of a curve in the plane, paint a thin band of width $2r$ around it and measure the area of the band.
The area is close to $2r$ times the length, so dividing by $2r$ recovers the length as $r$ shrinks.
For a segment of length $L$, the band is a rectangle of area $2rL$ with two half-discs at the ends, and the ratio tends to $L$.
The same idea measures surfaces in space through thin shells.
