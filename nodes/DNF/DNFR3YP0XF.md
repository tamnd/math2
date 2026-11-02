---
tag: DNFR3YP0XF
kind: concept
name: Localization of a category
msc: ["18E35"]
sources:
  - url: https://en.wikipedia.org/wiki/Localization_of_a_category
same_as:
  wikidata: Q6664610
  wikipedia: Localization of a category
---

## Summary

Localizing a [[category|A2DE66937D]] at a class of morphisms means adding formal inverses so that these morphisms become isomorphisms, in the most economical way.
The result is a new category with a functor from the old one, characterized by a universal property.
Homotopy categories and derived categories are localizations: one inverts weak equivalences or quasi-isomorphisms.
The construction generalizes the localization of a commutative ring, where chosen elements are made invertible.

## Explanations

### L1 human

Sometimes two objects should count as the same because a chosen map connects them, even though the map has no inverse.
Localization forces such maps to have inverses by allowing formal backward steps in chains of maps.
A morphism of the new category is a zigzag of old morphisms, some of which point the wrong way and are chosen ones.
For example, in the category with two objects $0$ and $1$ and one arrow $0 \to 1$, inverting the arrow makes $0$ and $1$ isomorphic.
