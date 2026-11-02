---
tag: F2DTWW9HP7
kind: concept
name: Forcing
msc: ["03E40", "03E35"]
sources:
  - url: https://en.wikipedia.org/wiki/Forcing_(mathematics)
same_as:
  wikidata: Q1003136
  wikipedia: Forcing (mathematics)
---

## Summary

Forcing is a method to build new models of set theory by adding a new set to a given model.
One starts from a model $M$ of ZFC and a [[partial order|0QV2JS9RJ3]] in $M$, whose elements are approximations of the new set.
A [[generic filter|WEDP73Y7GK]] $G$ over $M$ collects compatible approximations, and the extension $M[G]$ is the smallest transitive model of ZFC that contains $M$ and $G$.
Paul Cohen introduced forcing to prove that the [[continuum hypothesis|0MN2MER9WN]] cannot be proved in ZFC, and it is now the main tool for independence proofs.

## Explanations

### L1 human

Forcing adds a new object to a universe of sets, such as a new real number that was not there before.
The new object is described by its finite pieces of information, called conditions.
For a new real, a condition says what finitely many of its binary digits are.
A generic choice of conditions avoids every pattern that the old universe can describe, so the real it defines is truly new.
Facts about the new universe are decided by single conditions, and this is how one controls what is true there.
