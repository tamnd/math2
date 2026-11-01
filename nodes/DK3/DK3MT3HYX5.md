---
tag: DK3MT3HYX5
kind: concept
name: Absolute neighborhood retract
msc: [54C55, 54C15]
sources:
  - url: https://en.wikipedia.org/wiki/Absolute_neighborhood_retract
same_as:
  wikidata: Q137596576
  wikipedia: Absolute neighborhood retract
---

## Summary

An absolute neighborhood retract, or ANR, is a [[metrizable space|091GJ3FYD7]] with the following property.
Whenever it sits as a closed subset in a metrizable space, it is a retract of some neighbourhood of itself.
ANRs include manifolds, polyhedra, open subsets of Banach spaces and convex subsets of normed spaces.
They are the spaces with good local behaviour for homotopy theory.
They are locally contractible, and compact ANRs have the homotopy type of finite CW complexes.

## Explanations

### L1 human

A retraction pushes a big space onto a subspace while keeping each point of the subspace fixed.
Place an ANR as a closed set inside a larger metric space.
Then some thin open layer around it can be pushed onto it by a retraction.
The interval $[0, 1]$ is an ANR, and so is the circle.
A set with infinitely many points piling up, like $\set{0} \cup \set{1/n : n \ge 1}$, is not an ANR.
A thin layer around it in $\R$ contains a whole interval around $0$, and this interval cannot be pushed continuously onto separate points.
