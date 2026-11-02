---
tag: ABVBHCA9VW
kind: concept
name: Gluing of schemes
msc: [14A15]
sources:
  - url: https://en.wikipedia.org/wiki/Gluing_schemes
same_as:
  wikidata: Q85763749
  wikipedia: Gluing schemes
---

## Summary

Gluing builds a new [[scheme|5A35TYZD02]] from a family of schemes by identifying open pieces of them along isomorphisms.
The isomorphisms must agree on triple overlaps, a condition called the cocycle condition.
Gluing is how most schemes beyond affine ones are made, for example projective space.
It is also used to prove that constructions such as fiber products exist for all schemes.

## Explanations

### L1 human

Imagine making a sphere from two discs by sewing them along their edges.
Gluing of schemes does the same with algebraic pieces: one says which open parts of the pieces are to be identified, and by which maps.
The projective line comes from two copies of the affine line, with coordinates $t$ and $s$.
The parts where $t \ne 0$ and $s \ne 0$ are identified by the rule $s = 1/t$.
The point $t = 0$ and the point $s = 0$ stay separate, so the result is a line with one extra point at infinity.
