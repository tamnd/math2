---
tag: TAHV24ED74
kind: concept
name: Bicategory
msc: [18N10]
sources:
  - url: https://en.wikipedia.org/wiki/2-category
---

## Summary

A bicategory is a weak form of a [[2-category|CQACXG10JZ]]: composition of 1-morphisms is associative and unital only up to specified invertible 2-morphisms.
These associators and unitors must satisfy the pentagon and triangle identities, as in a [[monoidal category|M3MSQ3NKAE]].
A bicategory with one object is the same as a monoidal category.
Rings with bimodules, and categories with [[profunctors|EAPHAQVVD5]], form bicategories that are not strict 2-categories.

## Explanations

### L1 human

In many examples, composing arrows in two different orders gives results that are naturally isomorphic but not literally equal.
Tensoring bimodules is the typical case: $(M \otimes N) \otimes P$ and $M \otimes (N \otimes P)$ are isomorphic, not the same.
A bicategory keeps track of these isomorphisms as part of the structure, instead of pretending they are equalities.
Every bicategory is equivalent to a strict 2-category, so not much is lost, but the weak version is the one that occurs in nature.
