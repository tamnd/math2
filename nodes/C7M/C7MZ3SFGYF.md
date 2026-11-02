---
tag: C7MZ3SFGYF
kind: concept
name: Equivariant cohomology
msc: [55N91, 55N25]
sources:
  - url: https://en.wikipedia.org/wiki/Equivariant_cohomology
same_as:
  wikidata: Q5384738
  wikipedia: Equivariant cohomology
---

## Summary

Equivariant cohomology is a cohomology theory for spaces with an action of a topological group $G$.
In the Borel construction, one replaces the space $X$ by the homotopy quotient $EG \times_G X$ and takes its ordinary cohomology.
For a free action of a compact Lie group this is the cohomology of the orbit space.
For the action on a point it is the cohomology of the [[classifying space|WSZ40H5E4T]] $BG$.
It is a main tool for localization theorems, such as the Atiyah–Bott formula, and for the study of fixed points.

## Explanations

### L1 human

When a group acts on a space, the plain quotient often loses information, for example when points have large stabilisers.
The Borel construction first lets the group act freely by pairing each point with a point of a big contractible space on which the group acts freely.
Then it takes the quotient, which is now well behaved, and computes its cohomology.
For the circle group acting on a single point, the result is a polynomial ring in one variable of degree $2$.
Yet the plain quotient is just a point.
