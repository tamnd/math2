---
tag: CHS5AFJGWE
kind: concept
name: Limit
msc: [18A30]
sources:
  - url: https://en.wikipedia.org/wiki/Limit_(category_theory)
same_as:
  wikidata: Q1322614
  wikipedia: Limit (category theory)
---

## Summary

The limit of a [[diagram|HJK75HDWFE]] in a [[category|A2DE66937D]] is a universal [[cone|7TPBQPPN97]] over it.
Every other cone factors through it in exactly one way.
Limits unify many constructions, such as products, equalizers, pullbacks, inverse limits and terminal objects.
A limit is unique up to unique isomorphism when it exists, and in the category of sets every small diagram has one.

## Explanations

### L1 human

The limit of a diagram is the best object that maps to every part of the diagram in a consistent way.
"Best" means that any other object with consistent maps to the diagram maps to the limit in exactly one way that matches.
In the category of sets, the limit is the set of all consistent choices of one element in each set of the diagram.
For two sets with no arrows between them, a consistent choice is a pair $(x, y)$, so the limit is the Cartesian product.
