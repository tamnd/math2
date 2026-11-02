---
tag: VNX79CRH90
kind: concept
name: Algebraic stack
msc: [14A20, 18F20]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_stack
same_as:
  wikidata: Q1687845
  wikipedia: Algebraic stack
---

## Summary

An algebraic stack is a generalization of an algebraic space in which points may have automorphism groups.
Formally it is a stack in groupoids over the category of schemes that admits a smooth surjection from a scheme.
Algebraic stacks are the natural home of moduli problems, such as the moduli of curves, where the objects classified have nontrivial symmetries.

## Explanations

### L1 human

A moduli space should have one point for each object of a given kind, for example each curve of genus $g$.
When objects have symmetries, no ordinary space can do this job well: families get glued in ways that lose information.
A stack keeps track of the symmetries by remembering, for each point, a group of automorphisms.
The simplest example is the classifying stack $BG$ of a finite group $G$: it has one point, with automorphism group $G$.
