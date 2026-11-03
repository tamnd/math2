---
tag: 1QCSARFXQ0
kind: concept
name: Second moment of area
msc: [74K10, 26B15]
sources:
  - url: https://en.wikipedia.org/wiki/Second_moment_of_area
same_as:
  wikidata: Q835065
  wikipedia: Second moment of area
---

## Summary

The second moment of area of a plane region about an axis is the integral of the squared distance to the axis over the region.
For the cross-section of a beam it measures how well the shape resists bending, and the bending stiffness of a beam is $EI$.
It is a geometric quantity, the area analogue of the [[moment of inertia|08ANASGBXV]] of a rigid body.
Its dependence on the cube of the height explains why beams are made deep rather than wide.
It also explains why I-beams put material far from the [[centroid|0X7EEWES5G]].

## Explanations

### L1 human

A ruler is easy to bend flat-wise and very hard to bend edge-wise, although it has the same area both ways.
What matters is how far the material lies from the line about which the section bends.
The second moment of area adds up each small piece of area times the square of its distance from that line.
For a rectangle of width $b$ and height $h$, bending about the horizontal centre line, it is $bh^3/12$, so doubling the height makes the beam eight times stiffer.
