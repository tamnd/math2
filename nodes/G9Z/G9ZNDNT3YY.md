---
tag: G9ZNDNT3YY
kind: concept
name: Exact category in the sense of Barr
msc: ["18E08"]
specializes: [2SM3JRJXA4]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_category
---

## Summary

A category is exact in the sense of Barr, or Barr-exact, when it is a [[regular category|2SM3JRJXA4]] with effective equivalence relations.
This means that every internal equivalence relation is the kernel pair of some morphism.
So quotients by equivalence relations exist and behave as in sets.
Every elementary topos, every abelian category, the category of sets and every variety of algebras such as groups or rings are Barr-exact.
This notion is different from the exact categories of Quillen used in algebraic K-theory.

## Explanations

### L1 human

In sets, any equivalence relation on $X$ is the relation "has the same image" for the quotient map $X \to X / {\sim}$.
A Barr-exact category is one where this holds for every equivalence relation expressed inside the category.
For groups, an equivalence relation that is a subgroup of $G \times G$ is the relation "same coset" for a normal subgroup, and the quotient group provides the map.
