---
tag: G83JY7CY7Q
kind: concept
name: Formal concept analysis
msc: [06B99, 68T30, 06A15]
sources:
  - url: https://en.wikipedia.org/wiki/Formal_concept_analysis
same_as:
  wikidata: Q1437394
  wikipedia: Formal concept analysis
---

## Summary

Formal concept analysis studies a binary relation between objects and attributes through the complete lattice of its formal concepts.
A formal concept is a pair of a set of objects and a set of attributes that determine each other exactly.
The resulting concept lattice gives a hierarchy of clusters in the data, and every complete lattice arises in this way.
It is used in data analysis and knowledge representation, and it rests on a [[Galois connection|Q5JHEPRYQ6]] between sets of objects and sets of attributes.

## Explanations

### L1 human

Start with a table: rows are objects, columns are attributes, and a cross means that the object has the attribute.
A formal concept is a block of crosses that cannot be made bigger.
It is a set of objects with all the attributes they share, such that no other object has all these attributes.
For example, take the objects "dog", "cat", "trout" and the attributes "has fur", "lives in water", where the dog and the cat have fur and the trout lives in water.
Then the pair ({dog, cat}, {has fur}) is a formal concept.
The formal concepts, ordered by their sets of objects, form a lattice that shows how the concepts of the data are nested.
