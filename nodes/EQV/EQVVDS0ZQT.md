---
tag: EQVVDS0ZQT
kind: concept
name: Mapping cylinder
msc: [55P05, 54B17]
sources:
  - url: https://en.wikipedia.org/wiki/Mapping_cylinder
same_as:
  wikidata: Q1014869
  wikipedia: Mapping cylinder
---

## Summary

The mapping cylinder of a continuous map $f \colon X \to Y$ is the space obtained from the cylinder $X \times [0, 1]$ by gluing its end $X \times \set{1}$ to $Y$ along $f$.
It contains $Y$ as a [[deformation retract|CEK4SC20WK]] and contains $X$ as the other end.
So every map is, up to [[homotopy equivalence|XZG6MTSWCN]], the inclusion of a subspace.
The construction is used to build mapping cones, cofibrations and long exact sequences.

## Explanations

### L1 human

Take a tube shaped like $X$, and glue one end of the tube onto $Y$ by following $f$.
The other end of the tube is a copy of $X$ that sits freely in the new space.
Sliding along the tube pushes everything onto $Y$, so the new space has the same shape as $Y$.
For example, if $Y$ is a single point, the tube closes up into a cone on $X$.
