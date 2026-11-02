---
tag: T2V7GJJ2EN
kind: concept
name: Triangulated category
msc: [18G80]
specializes: [B2VP96NJSK]
sources:
  - url: https://en.wikipedia.org/wiki/Triangulated_category
same_as:
  wikidata: Q7840150
  wikipedia: Triangulated category
---

## Summary

A triangulated category is an [[additive category|B2VP96NJSK]] with a shift functor and a class of distinguished triangles $X \to Y \to Z \to X[1]$ that satisfy a list of axioms.
Distinguished triangles play the role that short exact sequences play in an abelian category.
The [[homotopy category of chain complexes|9Y5Y92R4D5]], the [[derived category|5ST7NVJFSM]] and the [[stable homotopy category|26GTNMAF7B]] are triangulated.

## Explanations

### L1 human

In the derived category, maps need not have kernels and cokernels, so short exact sequences are not available.
Their replacement is the triangle: each map $f \colon X \to Y$ has a cone $Z$, and the sequence $X \to Y \to Z \to X[1]$ behaves like a short exact sequence that continues forever by shifting.
Applying a functor such as $\Hom(W, -)$ to a triangle gives a long exact sequence.
The axioms list the rules that these triangles obey in the examples.
