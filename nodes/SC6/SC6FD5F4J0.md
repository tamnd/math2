---
tag: SC6FD5F4J0
kind: concept
name: Preadditive category
msc: ["18E05"]
specializes: [BPH9SJ30Y0]
sources:
  - url: https://en.wikipedia.org/wiki/Preadditive_category
same_as:
  wikidata: Q2099981
  wikipedia: Preadditive category
---

## Summary

A preadditive category is a [[category|A2DE66937D]] in which morphisms with the same source and target can be added, and composition distributes over this addition.
Equivalently, it is a category [[enriched|BPH9SJ30Y0]] over abelian groups.
Modules over a ring, with their homomorphisms, are the basic example.
Preadditive categories are the first step towards additive and abelian categories, the setting of homological algebra.

## Explanations

### L1 human

Two linear maps between the same vector spaces can be added, and the sum is again linear.
Moreover $h \circ (f + g) = h \circ f + h \circ g$, so composition and addition get along.
A preadditive category asks for exactly this: every set of arrows from one object to another is an abelian group, and composing distributes over sums.
A ring is the same thing as a preadditive category with one object, whose arrows are the elements of the ring and whose composition is multiplication.
