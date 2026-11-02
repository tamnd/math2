---
tag: BJS1CGTKQ5
kind: concept
name: Colimit
msc: [18A30]
sources:
  - url: https://en.wikipedia.org/wiki/Limit_(category_theory)
---

## Summary

The colimit of a [[diagram|HJK75HDWFE]] in a [[category|A2DE66937D]] is a universal cocone under it.
It maps to every other cocone in exactly one compatible way.
It is the notion dual to a [[limit|CHS5AFJGWE]], and it covers coproducts, coequalizers, pushouts, direct limits and initial objects.
Colimits glue objects together, while limits cut out compatible families.

## Explanations

### L1 human

The colimit of a diagram is the most economical object that receives a map from every part of the diagram in a consistent way.
In the category of sets, put all the sets of the diagram side by side.
Then glue each element to its images under the arrows of the diagram.
For two sets with no arrows between them, nothing is glued, and the colimit is their disjoint union.
For an increasing chain of sets $X_0 \subseteq X_1 \subseteq \cdots$, the colimit is the union of the chain.
