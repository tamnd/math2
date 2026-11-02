---
tag: M3MSQ3NKAE
kind: concept
name: Monoidal category
msc: [18M05]
specializes: [A2DE66937D]
sources:
  - url: https://en.wikipedia.org/wiki/Monoidal_category
same_as:
  wikidata: Q1945014
  wikipedia: Monoidal category
---

## Summary

A monoidal category is a [[category|A2DE66937D]] with a tensor product of objects and a unit object, associative and unital up to coherent isomorphism.
It is the categorical version of a [[monoid|0N6R902FG1]], one level up.
Sets with the Cartesian product, vector spaces with the [[tensor product|0BF2DE2SYK]], and endofunctors with composition are monoidal categories.
Monoidal categories are the setting for monoid objects, enriched categories, duals, and the string diagrams of quantum algebra and computer science.

## Explanations

### L1 human

A monoidal category is a category where two objects can be put side by side to give a new object.
Putting $A$ next to $B$, and then next to $C$, gives the same result as putting $A$ next to the pair $B, C$, but only up to a chosen isomorphism.
There is also an "empty" object $I$ that changes nothing when placed next to another.
For example, for sets the product $A \times B$ is the side-by-side object, and a one-point set is the empty object, since $\set{*} \times A$ is in bijection with $A$.
