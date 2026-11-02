---
tag: ARAEEM8CVF
kind: concept
name: Near-ring
msc: [16Y30]
sources:
  - url: https://en.wikipedia.org/wiki/Near-ring
same_as:
  wikidata: Q1397835
  wikipedia: Near-ring
---

## Summary

A near-ring is a set with an addition and a multiplication that satisfies most of the [[ring|0B1261B5ED]] axioms.
Addition need not be commutative, and only one distributive law is required.
The standard example is the set of all maps from a [[group|G5S1M9]] to itself, with pointwise addition and composition.
Near-rings stand to arbitrary maps of groups as rings stand to endomorphisms of abelian groups.
They appear in the study of nonlinear maps, of permutation groups and of combinatorial designs.

## Explanations

### L1 human

For an abelian group, its endomorphisms can be added and composed, and they form a ring.
If one takes all maps of the group to itself, not only homomorphisms, one can still add them pointwise and compose them.
Composition then distributes over addition from one side only: $(f + g) \circ h = f \circ h + g \circ h$ always holds, but $f \circ (g + h) = f \circ g + f \circ h$ needs $f$ to respect addition.
A near-ring is any structure with exactly the rules that survive.
