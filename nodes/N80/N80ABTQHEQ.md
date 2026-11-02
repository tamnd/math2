---
tag: N80ABTQHEQ
kind: concept
name: Double complex
msc: [18G35]
sources:
  - url: https://en.wikipedia.org/wiki/Double_complex
same_as:
  wikidata: Q107490138
  wikipedia: Double complex
---

## Summary

A double complex is a grid of objects $C_{p,q}$ with a horizontal and a vertical differential, each squaring to zero, that anticommute with each other.
Summing along the diagonals $p + q = n$ gives the total complex, a single [[chain complex|WQ82C0M3QB]].
Double complexes arise from tensor products of complexes and from resolving complexes, and their total homology is computed by [[spectral sequences|GG8AYV847V]].

## Explanations

### L1 human

A chain complex is a line of objects with maps going one way.
A double complex is a whole grid of objects, with maps going left and maps going down, each family forming chain complexes.
Going left then down equals minus going down then left, and this sign lets one combine both into one map on the diagonals.
For example, the tensor product of two chain complexes is naturally a double complex.
Its total complex computes things like the homology of a product of spaces.
