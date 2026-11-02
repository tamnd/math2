---
tag: FYBRP16KAN
kind: concept
name: Concrete category
msc: [18A05, 18A22]
specializes: [A2DE66937D]
sources:
  - url: https://en.wikipedia.org/wiki/Concrete_category
same_as:
  wikidata: Q1575634
  wikipedia: Concrete category
---

## Summary

A concrete category is a [[category|A2DE66937D]] $\mathcal{C}$ together with a [[faithful functor|GRG8WEBSH5]] $U$ from $\mathcal{C}$ to the category of sets.
The functor $U$ assigns an underlying set to each object, and morphisms are determined by their underlying functions.
Groups, rings, vector spaces and topological spaces with their usual forgetful functors are concrete categories.
Not every category admits such a functor, so concreteness is a real condition on large categories.

## Explanations

### L1 human

In many categories the objects are sets with extra structure and the arrows are functions that respect the structure.
A concrete category records this through a forgetful functor that remembers only the underlying set and the underlying function.
Being faithful means that two arrows with the same underlying function are the same arrow.
For example, a continuous map between two topological spaces is nothing more than a function with a property.
So topological spaces with the forgetful functor form a concrete category.
