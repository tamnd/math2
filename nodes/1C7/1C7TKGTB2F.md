---
tag: 1C7TKGTB2F
kind: concept
name: Graded poset
msc: [06A07]
sources:
  - url: https://en.wikipedia.org/wiki/Graded_poset
same_as:
  wikidata: Q5591878
  wikipedia: Graded poset
---

## Summary

A graded poset is a [[partially ordered set|0QV2JS9RJ3]] with a rank function that goes up by exactly one along each covering step.
The elements then fall into levels, like the floors of a building.
Many posets of combinatorics are graded: subsets by size, divisors by the number of prime factors, partitions by their size.

## Explanations

### L1 human

Picture the Hasse diagram of a poset drawn so that every edge goes up exactly one level.
If this is possible, the poset is graded and the level of an element is its rank.
The subsets of $\set{1, 2, 3}$ are graded by their number of elements: $\varnothing$ has rank $0$ and $\set{1, 2, 3}$ has rank $3$.
A pentagon, where one side from bottom to top has two steps and the other has three, cannot be drawn this way.
