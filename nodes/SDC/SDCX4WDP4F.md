---
tag: SDCX4WDP4F
kind: concept
name: Spherical code
msc: [52C17, 94B65, 05B40]
sources:
  - url: https://en.wikipedia.org/wiki/Spherical_code
same_as:
  wikidata: Q7576702
  wikipedia: Spherical code
---

## Summary

A spherical code is a finite set of points on the unit sphere in $\R^n$, judged by how far apart its points are.
The main question asks for the largest number of points with a given minimal angle.
The dual question asks for the largest minimal angle for a given number of points.
Kissing configurations are spherical codes with minimal angle $60^\circ$, and the [[Tammes problem|9WD2TZ4ZB5]] is the case $n = 3$.
Upper bounds come mainly from the [[Delsarte linear programming bound|7RPEDHAT7R]].

## Explanations

### L1 human

Choose a number of directions in space, pointing from the centre of a ball to its surface, and try to keep any two directions far apart.
Such a choice is a spherical code.
In the plane the best choice is clear: space the points evenly around the circle.
On a sphere and in higher dimensions it is a hard problem, studied for its use in signal transmission and for its links with sphere packing.
