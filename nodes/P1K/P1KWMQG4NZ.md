---
tag: P1KWMQG4NZ
kind: concept
name: Strain rate tensor
msc: [76A02, 74A05]
sources:
  - url: https://en.wikipedia.org/wiki/Strain-rate_tensor
same_as:
  wikidata: Q7621125
  wikipedia: Strain-rate tensor
---

## Summary

The strain rate tensor is the symmetric part of the gradient of the velocity field of a flow.
It measures how fast a small fluid parcel is being stretched and sheared, as opposed to rotated.
Its trace is the rate of change of volume, and in a Newtonian fluid the viscous stress is a linear function of it.

## Explanations

### L1 human

Near a point, a fluid parcel can move in three ways: it can translate, it can turn like a rigid body, and it can deform.
The strain rate tensor captures only the deformation.
In the shear flow $(y, 0, 0)$, a small square is pulled into a slanted parallelogram, and the strain rate tensor records this with the off-diagonal entries $1/2$.
In a rigid rotation, a small square only turns, and the strain rate tensor is zero.
