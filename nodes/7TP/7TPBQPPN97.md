---
tag: 7TPBQPPN97
kind: concept
name: Cone
msc: [18A30]
sources:
  - url: https://en.wikipedia.org/wiki/Cone_(category_theory)
same_as:
  wikidata: Q1850712
  wikipedia: Cone (category theory)
---

## Summary

A cone over a [[diagram|HJK75HDWFE]] $D \colon J \to \mathcal{C}$ is an object $N$, the apex, with a morphism from $N$ to each object $D(j)$ of the diagram.
All triangles formed with the morphisms of the diagram must commute.
Dually, a cocone has morphisms from the objects of the diagram into a common object.
Limits are the universal cones and colimits are the universal cocones.

## Explanations

### L1 human

Picture the diagram as a figure drawn on the floor and the apex $N$ as a point above it, with a string from $N$ down to each object.
The strings must be consistent with the arrows $D(j) \to D(k)$ of the figure.
Going down to $D(j)$ and then along the arrow gives the same result as going down directly to $D(k)$.
For two sets $X$ and $Y$ with no arrows between them, a cone is just a set $N$ with two functions $N \to X$ and $N \to Y$.
