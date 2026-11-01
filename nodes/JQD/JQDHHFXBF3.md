---
tag: JQDHHFXBF3
kind: concept
name: Fixed-point property
msc: [54H25, 55M20]
sources:
  - url: https://en.wikipedia.org/wiki/Fixed-point_property
same_as:
  wikidata: Q5456331
  wikipedia: Fixed-point property
---

## Summary

A topological space has the fixed-point property if every continuous map from the space to itself fixes at least one point.
It is a topological invariant, so it can tell spaces apart.
The Brouwer fixed-point theorem says that every closed ball in $\R^n$ has this property.
Fixed-point results of this kind are a main tool for proving that equations have solutions.

## Explanations

### L1 human

Imagine moving every point of a space to some point of the same space, without tearing it.
The space has the fixed-point property if, however you do this, some point stays where it was.
The interval $[0, 1]$ has it: the graph of a continuous map $f \colon [0, 1] \to [0, 1]$ must cross the diagonal line $y = x$.
A circle does not have it, since a rotation by a small angle moves every point.
The real line does not have it either, since $x \mapsto x + 1$ moves every point.
