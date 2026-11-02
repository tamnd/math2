---
tag: 4D073CCYGV
kind: concept
name: Rational map
msc: ["14E05"]
sources:
  - url: https://en.wikipedia.org/wiki/Rational_mapping
same_as:
  wikidata: Q987226
  wikipedia: Rational mapping
---

## Summary

A rational map from a variety $X$ to a variety $Y$ is a morphism defined on some nonempty open subset of $X$.
Two such morphisms give the same rational map when they agree on a common open subset.
It is written $X \dashrightarrow Y$, because it may fail to be defined at some points.
Rational maps are the maps of birational geometry, which studies varieties up to changes on lower-dimensional subsets.

## Explanations

### L1 human

Some natural maps are given by formulas with denominators, so they are undefined where a denominator vanishes.
The projection of the plane from the origin onto the line of directions, $(x, y) \mapsto [x : y]$, is defined everywhere except at the origin.
A rational map keeps such a formula and simply forgets the bad points.
Because varieties are irreducible, the open set where the map is defined is dense, so the formula determines the map.
