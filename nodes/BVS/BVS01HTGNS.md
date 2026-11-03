---
tag: BVS01HTGNS
kind: concept
name: Seismic migration
msc: [86A22, 35R30, 35L05]
sources:
  - url: https://en.wikipedia.org/wiki/Seismic_migration
same_as:
  wikidata: Q2111620
  wikipedia: Seismic migration
---

## Summary

Seismic migration is the step of seismic imaging that moves recorded reflections to the true positions of the reflectors that caused them.
In raw reflection data a dipping layer appears shifted and too gently dipping, and a point scatterer appears as a hyperbola-shaped event.
Migration uses a velocity model to propagate the recorded waves back into the Earth and to focus the energy at the reflecting points.
Mathematically it is the adjoint of the linearised ([[Born|3Y0VBDXHJD]]) map from reflectivity to data, and it is the basis of structural images in exploration seismology.

## Explanations

### L1 human

A seismic survey records echoes from layers underground, but each echo is first plotted directly under the place where it was recorded.
This picture is distorted: a sloping layer appears in the wrong place, and a small object shows up as a wide arch.
Migration repairs the picture by tracing each echo back to where it really came from.
The arch collapses to a point, and the sloping layer moves to its true position.
For example, a single small rock at depth $1$ km gives an arch in the raw section, with its top above the rock.
Migration shrinks the arch to that one spot.
