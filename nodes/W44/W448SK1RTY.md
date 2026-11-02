---
tag: W448SK1RTY
kind: concept
name: Elementary theory of the category of sets
msc: [18B05, 03G30, 18A15]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_theory_of_the_category_of_sets
same_as:
  wikidata: Q131470959
  wikipedia: Elementary theory of the category of sets
---

## Summary

The Elementary Theory of the Category of Sets (ETCS) is an axiomatic set theory proposed by Lawvere in 1964.
It describes sets and functions through the way functions compose, instead of through a membership relation.
Its models are the nondegenerate well-pointed [[toposes|6837RS7N82]] with a natural numbers object in which every epimorphism splits.
It is weaker than [[Zermelo–Fraenkel set theory|0HE5WDQ9FJ]] with choice, but strong enough for most ordinary mathematics.

## Explanations

### L1 human

In ETCS a set is not a bag of members; it is an object of a [[category|A2DE66937D]], and functions are its arrows.
An element of a set $X$ is a function from a one-point set into $X$.
The axioms say what one can build: products, function sets, subsets classified by truth values, the natural numbers, and sections of surjections.
For example, the subsets of $X$ correspond to functions from $X$ to a two-element set of truth values.
