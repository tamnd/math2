---
tag: EAPHAQVVD5
kind: concept
name: Profunctor
msc: [18D60]
sources:
  - url: https://en.wikipedia.org/wiki/Profunctor
same_as:
  wikidata: Q7248328
  wikipedia: Profunctor
---

## Summary

A profunctor, also called a distributor or bimodule, from a category $\mathcal{C}$ to a category $\mathcal{D}$ is a [[functor|28NQ0KRHD3]] $\mathcal{D}^{\mathrm{op}} \times \mathcal{C} \to \mathbf{Set}$.
It generalizes functors: every functor gives a profunctor.
It also generalizes relations: a relation between sets is a profunctor between discrete categories with values in truth values.
Profunctors compose by a [[coend|W9QTFV0Z8D]], and categories, profunctors and natural transformations form a bicategory.
They are the categorical analogue of bimodules between rings.

## Explanations

### L1 human

A function from $X$ to $Y$ assigns to each $x$ one $y$, while a relation only says which pairs $(x, y)$ are related.
A profunctor does the same for categories, and it says how $x$ and $y$ are related by a set of "witnesses" $P(d, c)$.
The witnesses can be moved along morphisms in both categories, in opposite directions.
For example, the hom-sets $\Hom(d, c)$ of a category form a profunctor from the category to itself: a morphism is a witness that $d$ maps to $c$.
