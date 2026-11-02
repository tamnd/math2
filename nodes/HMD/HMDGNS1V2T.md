---
tag: HMDGNS1V2T
kind: concept
name: Fixed-point property of posets
msc: [06A06, 47H10]
sources:
  - url: https://en.wikipedia.org/wiki/Fixed-point_property
---

## Summary

A [[partially ordered set|0QV2JS9RJ3]] has the fixed-point property if every order-preserving map from it to itself fixes some element.
It is the order-theoretic counterpart of the [[fixed-point property of topological spaces|JQDHHFXBF3]].
Every [[complete lattice|D7A0ZGZT5S]] has it by the [[Knaster–Tarski theorem|RHXP3HA64M]], and among lattices exactly the complete ones have it.
Deciding which finite posets have the fixed-point property is a hard combinatorial question.

## Explanations

### L1 human

Move the elements of an ordering around without ever reversing a comparison.
The ordering has the fixed-point property if, however one does this, some element stays in place.
Any finite chain has it: if the smallest element moves, it moves up, and following the moves upward one must stop somewhere.
An ordering of two incomparable elements does not have it, since swapping them reverses no comparison and moves both.
