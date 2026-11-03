---
tag: HKPQ1565TS
kind: concept
name: Helmert transformation
msc: [86A30, 51N20]
specializes: [D3GYHF6NAX]
sources:
  - url: https://en.wikipedia.org/wiki/Helmert_transformation
same_as:
  wikidata: Q360886
  wikipedia: Helmert transformation
---

## Summary

A Helmert transformation is a [[similarity transformation|D3GYHF6NAX]] of $\R^3$ used to convert Cartesian coordinates from one [[geodetic datum|N8HZ9D1CF0]] to another.
It has seven parameters: three translations, three rotation angles and one scale change.
In geodesy the angles and the scale change are tiny, so a linearised form is used.
The parameters are usually estimated by least squares from points known in both datums.

## Explanations

### L1 human

Two datums describe the same Earth with slightly different axes.
To pass from one to the other, shift the origin, turn the axes a little, and stretch by a tiny factor.
The shift is often tens to hundreds of metres, the rotation a fraction of an arcsecond, and the stretch a few parts per million.
Knowing the seven numbers, one can move every coordinate from an old map to GPS coordinates.
