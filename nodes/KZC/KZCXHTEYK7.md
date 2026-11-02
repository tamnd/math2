---
tag: KZCXHTEYK7
kind: concept
name: Quillen equivalence
msc: [18N40, 55U35]
sources:
  - url: https://en.wikipedia.org/wiki/Quillen_adjunction
---

## Summary

A Quillen [[equivalence|K7A04ZBD92]] is a [[Quillen adjunction|SY38F954FE]] between two [[model categories|SDTZVZ6B4Q]] that induces an equivalence of their homotopy categories.
It is the right notion of "same homotopy theory" for model categories.
The basic example is the adjunction between simplicial sets and topological spaces given by geometric realization and the singular complex.
It shows that both categories model the same homotopy theory of spaces.

## Explanations

### L1 human

A model category is a setting where some maps are declared to be weak equivalences, as in homotopy theory.
Two different settings can describe the same homotopy theory: for example, spaces built from simplices and general topological spaces.
A Quillen equivalence is a pair of functors back and forth that preserves the model structures and becomes an equivalence once weak equivalences are inverted.
Through it, one can switch to whichever setting is most convenient for a problem, without losing homotopical information.
