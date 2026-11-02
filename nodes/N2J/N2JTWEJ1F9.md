---
tag: N2JTWEJ1F9
kind: concept
name: Subdivision surface
msc: [65D17, 65D18, 68U05]
sources:
  - url: https://en.wikipedia.org/wiki/Subdivision_surface
same_as:
  wikidata: Q1529124
  wikipedia: Subdivision surface
---

## Summary

A subdivision surface is a smooth surface defined as the limit of repeatedly refining a coarse polygon mesh by fixed local averaging rules.
Each refinement step adds new vertices and moves old ones to weighted averages of their neighbors.
Subdivision surfaces handle meshes of any topology, generalize spline surfaces, and are standard in computer graphics and animation.
The [[Catmull–Clark|PF5Z57DDG2]] scheme is the most widely used example.

## Explanations

### L1 human

Start with a rough cage made of flat polygons, like a crude box model of a head.
Cut every face into smaller faces and nudge each corner toward the average of its neighbors.
Repeat this a few times, and the jagged cage turns into a smooth rounded shape.
The surface that these steps approach is the subdivision surface.
A curve version, Chaikin's corner cutting, replaces each edge of a polygon by two points at a quarter and three quarters of its length.
Its limit is a smooth curve.
