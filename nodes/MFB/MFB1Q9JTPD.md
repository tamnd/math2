---
tag: MFB1Q9JTPD
kind: concept
name: Multicategory
msc: [18M65, 18M60]
sources:
  - url: https://en.wikipedia.org/wiki/Multicategory
same_as:
  wikidata: Q6934590
  wikipedia: Multicategory
---

## Summary

A multicategory is like a [[category|A2DE66937D]], except that a morphism has a finite list of objects as its source and one object as its target.
Such morphisms, called multimorphisms, compose by plugging outputs into inputs.
Multilinear maps between vector spaces are the basic example.
A multicategory with one object is the same as a non-symmetric operad, and every monoidal category gives a multicategory.

## Explanations

### L1 human

Many natural maps take several inputs at once, such as the multiplication of two numbers or the dot product of two vectors.
A category only records maps with one input, so it cannot see this directly.
A multicategory records maps with any number of inputs and one output.
For example, a bilinear map $V \times W \to U$ is a morphism from the list $(V, W)$ to $U$.
Feeding the outputs of two such maps into a third gives a map with four inputs.
