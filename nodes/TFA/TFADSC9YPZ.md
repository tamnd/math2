---
tag: TFADSC9YPZ
kind: concept
name: Exact category
msc: ["18E05", "18E10"]
specializes: [B2VP96NJSK]
sources:
  - url: https://en.wikipedia.org/wiki/Exact_category
same_as:
  wikidata: Q5419218
  wikipedia: Exact category
---

## Summary

An exact category, in the sense of Quillen, is an [[additive category|B2VP96NJSK]] with a chosen class of kernel–cokernel pairs.
These pairs behave like [[short exact sequences|KJKNJMGKZZ]].
It allows homological algebra and algebraic K-theory in categories that are not abelian, such as the category of finitely generated projective modules.
It is a different notion from an [[exact category in the sense of Barr|G9ZNDNT3YY]].

## Explanations

### L1 human

In an abelian category every monomorphism has a cokernel and fits into a short exact sequence.
Many useful categories, such as vector bundles or projective modules, are additive but not abelian.
An exact category keeps only a chosen family of sequences $A \to B \to C$, declared to be the short exact ones, and asks that this family behave well under composition, pullback and pushout.
For example, in the category of finitely generated projective modules one can choose the split exact sequences.
