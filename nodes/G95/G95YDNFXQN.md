---
tag: G95YDNFXQN
kind: concept
name: Cylinder set measure
msc: [28C20, 60B11, 46G12]
sources:
  - url: https://en.wikipedia.org/wiki/Cylinder_set_measure
same_as:
  wikidata: Q5199272
  wikipedia: Cylinder set measure
---

## Summary

A cylinder set measure on a [[topological vector space|T32W553W95]] is a consistent family of [[probability measures|059TJN0NZ1]] on its finite-dimensional images.
It assigns a probability to every set that is described by finitely many linear coordinates.
It need not come from a countably additive measure on the whole space.
Cylinder set measures are the raw material for Gaussian measures and white noise in infinite dimensions.

## Explanations

### L1 human

In infinite dimensions one often knows how a random point looks through any finite number of linear measurements, but not yet as a whole.
A cylinder set measure records exactly this: for each finite set of measurements, a probability law of the readings, and the laws fit together.
For example, on a Hilbert space one may ask that every unit vector direction gives a standard normal reading, independent for orthogonal directions.
This is a cylinder set measure, but it is not a true measure on the Hilbert space, because a random point would have infinite length.
