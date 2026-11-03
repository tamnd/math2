---
tag: 6E7ZZ4DYX3
kind: concept
name: Hamming space
msc: [94B25, 94B05]
sources:
  - url: https://en.wikipedia.org/wiki/Hamming_space
same_as:
  wikidata: Q5645799
  wikipedia: Hamming space
---

## Summary

The Hamming space of length $n$ over a finite alphabet is the set of all words of length $n$, with the [[Hamming distance|EP5HNGSXFA]] as metric.
It is the space in which block codes live: a code is a subset, and its quality depends on how its points are spread.
The binary Hamming space $\set{0,1}^n$ is the vertex set of the $n$-dimensional [[hypercube|P9PYM71GMM]], and the Hamming distance is the distance in the hypercube graph.
In Mathlib the type `Hamming` carries this metric.

## Explanations

### L1 human

Picture all binary words of length $3$ as the eight corners of a cube.
Two corners joined by an edge differ in exactly one bit.
The Hamming distance between two words is the least number of edges on a path between their corners.
A good code picks corners far apart, so that a few flipped bits never move one codeword close to another.
