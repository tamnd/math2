---
tag: BV6ACVR5TV
kind: concept
name: Patched conic approximation
msc: [70M20, 70F15]
sources:
  - url: https://en.wikipedia.org/wiki/Patched_conic_approximation
same_as:
  wikidata: Q7144351
  wikipedia: Patched conic approximation
---

## Summary

The patched conic approximation models a spacecraft trajectory as a chain of Kepler orbits, each about a single body.
Near a planet only the planet's gravity counts, and far from all planets only the Sun's gravity counts.
The pieces are joined at the boundaries of the planets' spheres of influence.
It gives quick and fairly accurate first designs of interplanetary missions.
See the [[definition|V1E3G6Q96Y]].

## Explanations

### L1 human

A trip to Mars feels the pull of the Earth, the Sun and Mars all the time, which is hard to compute.
The patched conic idea pretends that only one body pulls at a time.
Near the Earth the craft escapes on a hyperbola, then it coasts around the Sun on an ellipse, and near Mars it arrives on another hyperbola.
Each piece is a simple conic, and the pieces are patched together.
