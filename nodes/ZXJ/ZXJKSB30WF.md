---
tag: ZXJKSB30WF
kind: concept
name: Disjoint union topology
msc: [54B99, 54B30]
specializes: [6ERJRRZK32]
sources:
  - url: https://en.wikipedia.org/wiki/Disjoint_union_(topology)
same_as:
  wikidata: Q5282259
  wikipedia: Disjoint union (topology)
---

## Summary

The disjoint union topology is the natural topology on a disjoint union of topological spaces.
A set is open in it exactly when its part in each piece is open in that piece.
It makes the disjoint union the coproduct in the category of topological spaces.
It is the [[final topology|6ERJRRZK32]] for the inclusions of the pieces.

## Explanations

### L1 human

Put several spaces side by side, with no overlap and no glue between them.
Each piece keeps its own topology, and the pieces do not interact.
A set is open when you can see it as an open set in each piece separately.
For example, the disjoint union of two copies of the interval $(0, 1)$ is a space with two separate parts.
It looks like the subspace $(0, 1) \cup (2, 3)$ of the real line.
