---
tag: KYCPCC57FT
kind: concept
name: Natural transformation
msc: [18A23]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_transformation
same_as:
  wikidata: Q1442189
  wikipedia: Natural transformation
---

## Summary

Let $F, G \colon \mathcal{C} \to \mathcal{D}$ be two [[functors|28NQ0KRHD3]].
A natural transformation $\alpha \colon F \Rightarrow G$ is a family of morphisms $\alpha_A \colon F(A) \to G(A)$, one for each object $A$.
The family must commute with the images of all morphisms of $\mathcal{C}$.
It makes precise the idea of a construction that is "natural", that is, defined in the same way for all objects without arbitrary choices.
The canonical map from a vector space to its double dual is natural.
By contrast, an isomorphism of a finite-dimensional space with its dual depends on a choice of basis.
Natural transformations are the morphisms of [[functor categories|1X0WKFQX8K]] and enter the definitions of [[equivalence of categories|K7A04ZBD92]] and of [[adjoint functors|TZHF6ZM92S]].

## Explanations

### L1 human

Two functors give two pictures of the same category inside another category.
A natural transformation is a way of moving from the first picture to the second, one object at a time.
"Natural" means that it does not matter whether one first moves along an arrow and then switches pictures, or first switches and then moves.
For example, every vector space $V$ maps to its double dual by sending $v$ to "evaluate at $v$".
This rule uses no basis, and it is compatible with every linear map, so it is natural.
