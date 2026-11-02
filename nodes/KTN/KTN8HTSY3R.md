---
tag: KTN8HTSY3R
kind: concept
name: dg category
msc: [18G35, 18D20, "16E45"]
specializes: [BPH9SJ30Y0]
sources:
  - url: https://en.wikipedia.org/wiki/Differential_graded_category
same_as:
  wikidata: Q5275347
  wikipedia: Differential graded category
---

## Summary

A dg category, or differential graded category, is a category whose morphism sets are [[chain complexes|WQ82C0M3QB]] and whose composition is compatible with the differentials.
It is a category [[enriched|BPH9SJ30Y0]] over chain complexes of modules over a commutative ring.
Dg categories serve as enhancements of triangulated categories: they keep homotopical information that the [[triangulated category|T2V7GJJ2EN]] loses, such as functorial cones.
They are a main tool in noncommutative algebraic geometry and in the study of derived categories of sheaves.

## Explanations

### L1 human

In an ordinary linear category, the maps between two objects form a vector space.
In a dg category they form a chain complex, with maps of each degree and a differential that sends a map of degree $n$ to a map of degree $n + 1$.
The main example has chain complexes as objects and all graded maps between them as morphisms.
Taking cohomology in degree $0$ of each morphism complex gives an ordinary category, here the [[homotopy category of chain complexes|9Y5Y92R4D5]].
A dg category with one object is the same thing as a differential graded algebra.
