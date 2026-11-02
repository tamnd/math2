---
tag: FS1FKAE89H
kind: concept
name: Subobject
msc: [18A20, 18A32]
sources:
  - url: https://en.wikipedia.org/wiki/Subobject
same_as:
  wikidata: Q2547089
  wikipedia: Subobject
---

## Summary

A subobject of an object $X$ in a [[category|A2DE66937D]] is an equivalence class of [[monomorphisms|Y2NP1JFR86]] into $X$.
Two monomorphisms are equivalent when each factors through the other.
It is the categorical version of a subset, a subgroup or a subspace, defined only through morphisms.
The subobjects of $X$ are partially ordered by factorisation, and in a topos they are classified by the subobject classifier.

## Explanations

### L1 human

In set theory a subset of $X$ is a smaller set sitting inside $X$.
In a category there is no "inside", so one uses an injective-like arrow $A \to X$ instead, which shows how $A$ sits in $X$.
Two such arrows that differ only by renaming the elements of $A$ give the same subobject.
For example, among sets, the inclusion $\{1, 2\} \to \{1, 2, 3\}$ and the map $\{a, b\} \to \{1, 2, 3\}$ with $a \mapsto 1$, $b \mapsto 2$ represent the same subobject, namely the subset $\{1, 2\}$.
