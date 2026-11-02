---
tag: DN7VSSDYPQ
kind: concept
name: Median algebra
msc: [06D99, 08A99, 05C12]
sources:
  - url: https://en.wikipedia.org/wiki/Median_algebra
same_as:
  wikidata: Q6806108
  wikipedia: Median algebra
---

## Summary

A median algebra is a set with a ternary operation $\langle x, y, z \rangle$ that behaves like the median of three numbers.
Every [[distributive lattice|0HM0HQCK6N]] is a median algebra with $\langle x, y, z \rangle = (x \wedge y) \vee (y \wedge z) \vee (z \wedge x)$.
The vertex sets of median graphs, such as trees and hypercubes, are median algebras.
There $\langle x, y, z \rangle$ is the unique vertex lying on shortest paths between each pair of the three vertices.
Median algebras give a common language for distributive lattices, median graphs and some structures of geometric group theory.

## Explanations

### L1 human

Given three real numbers, the median is the one in the middle.
It does not depend on the order of the three numbers, and if two of them are equal, the median is that repeated value.
A median algebra keeps these rules and one more, and forgets everything else about numbers.
In a tree, the median of three vertices is the point where the three paths between them meet.
