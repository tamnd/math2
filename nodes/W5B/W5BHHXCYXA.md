---
tag: W5BHHXCYXA
kind: concept
name: Lusternik–Schnirelmann category
msc: [55M30, "58E05"]
sources:
  - url: https://en.wikipedia.org/wiki/Lusternik–Schnirelmann_category
same_as:
  wikidata: Q2361277
  wikipedia: Lusternik–Schnirelmann category
---

## Summary

The Lusternik–Schnirelmann category of a space $X$ is the least number of open sets, minus one, that cover $X$ and are each contractible inside $X$.
It is a homotopy invariant that measures how far a space is from being contractible.
Lusternik and Schnirelmann introduced it to bound from below the number of critical points of a smooth function on a closed manifold.
It is itself bounded below by the cup-length of the cohomology ring.

## Explanations

### L1 human

Try to cover a space by as few open patches as possible, where each patch can be shrunk to a point inside the whole space.
A contractible space needs one patch, so its category is $0$.
A sphere cannot be shrunk in one piece.
But the sphere minus the north pole and the sphere minus the south pole each shrink to a point, so the sphere has category $1$.
The more patches a space needs, the more complicated its shape.
