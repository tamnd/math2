---
tag: ZSTEZ3PRT9
kind: concept
name: Universal class
msc: ["03C52", "03C40"]
specializes: [MEC3ZMC4F1]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_class
---

## Summary

A universal class is a class of structures axiomatized by universal sentences, those of the form "for all $x_1, \ldots, x_n$, a quantifier-free condition holds".
Universal sentences are preserved by [[substructures|676H7EGTKJ]], so every universal class is closed under substructures.
By the [[Łoś–Tarski preservation theorem|9RN0KYXNT1]], an [[elementary class|MEC3ZMC4F1]] is universal exactly when it has this closure property.
Varieties, quasivarieties and universal Horn classes are universal classes.

## Explanations

### L1 human

A universal axiom only checks finite patterns of elements, one tuple at a time.
If a structure passes every such check, then so does every part of it, since a part has fewer tuples to check.
Simple graphs form a universal class: "no vertex is adjacent to itself" and "adjacency is symmetric" are universal.
Fields do not: the axiom "every nonzero element has an inverse" needs an "exists", and indeed the subring $\Z$ of the field $\Q$ is not a field.
