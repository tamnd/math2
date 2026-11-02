---
tag: HSV1J7BJXX
kind: concept
name: Fibration and cofibration
msc: [18N40, 55U35]
sources:
  - url: https://en.wikipedia.org/wiki/Model_category
---

## Summary

In a [[model category|SDTZVZ6B4Q]], the fibrations and the cofibrations are two of the three distinguished classes of morphisms, besides the weak equivalences.
They abstract the [[Serre fibrations|PB9JXQ2KC3]] and the [[cofibrations|W5WS5EY8ZM]] of topology: maps along which homotopies lift, and inclusions along which homotopies extend.
Each class is determined by the other together with the weak equivalences, through lifting properties.
Fibrant and cofibrant objects are the good objects on which homotopy classes of maps compute the homotopy category.

## Explanations

### L1 human

A fibration is a map along which paths and deformations can be lifted, like the projection of a product $X \times F \to X$.
A cofibration is a map that behaves like the inclusion of a nice subspace, such as a circle as the boundary of a disc.
A model category specifies which maps play these two roles.
Every map can be split into a cofibration followed by a fibration, one of them being a weak equivalence.
This lets one replace objects by better ones without changing their homotopy type.
