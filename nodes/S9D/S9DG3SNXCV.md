---
tag: S9DG3SNXCV
kind: concept
name: Smoothed-particle hydrodynamics
msc: [76M28, 65M75]
specializes: [T4ZFKBZRYK]
sources:
  - url: https://en.wikipedia.org/wiki/Smoothed-particle_hydrodynamics
same_as:
  wikidata: Q733073
  wikipedia: Smoothed-particle hydrodynamics
---

## Summary

Smoothed-particle hydrodynamics, or SPH, is a mesh-free Lagrangian method of [[computational fluid dynamics|T4ZFKBZRYK]].
The fluid is represented by particles that carry mass and move with the flow.
Fields are reconstructed by smoothing over neighbouring particles with a kernel function.
Because there is no mesh, it handles free surfaces, splashing and large deformations easily.
It was introduced in 1977 for problems in astrophysics.
Robert Gingold and Joseph Monaghan, and independently Leon Lucy, proposed it.

## Explanations

### L1 human

Instead of cutting space into fixed cells, SPH follows the fluid itself, as a crowd of small blobs.
Each blob carries a bit of mass and moves with the flow.
To know the density at a point, one adds up the nearby blobs, giving more weight to the closest ones.
Pressure differences between neighbouring blobs push them apart or together, so the crowd moves like a fluid.
This is why SPH is popular for simulating waves breaking, stars colliding and water in films and games.
