---
tag: F4V6EA6XTX
kind: concept
name: Kirchhoff migration
msc: [86A22, 35L05, 78A45]
specializes: [BVS01HTGNS]
sources:
  - url: https://en.wikipedia.org/wiki/Seismic_migration
---

## Summary

Kirchhoff migration is [[seismic migration|BVS01HTGNS]] by weighted summation of recorded amplitudes along travel-time curves.
For each image point, it adds up the data at the times when a wave scattered at that point would reach each receiver.
It is based on the Kirchhoff integral representation of a wavefield, related to [[Kirchhoff's diffraction formula|W178NQAYS9]].
It needs only travel times and amplitude weights, often computed by ray tracing.
It is cheap and flexible with irregular survey geometries, which made it a standard industrial method.

## Explanations

### L1 human

Imagine every point underground as a possible small reflector.
If a point really reflects, its echo appears in each recording at a predictable time, so adding the recordings at those times gives a large sum.
If the point does not reflect, the values added are unrelated and mostly cancel.
Doing this for every point builds a picture of the reflectors; for a single buried rock, only the true position of the rock gets a large sum.
