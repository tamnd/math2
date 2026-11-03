---
tag: JYBHEDWB6X
kind: concept
name: Blossom algorithm
msc: [05C70, 05C85, 90C27]
sources:
  - url: https://en.wikipedia.org/wiki/Blossom_algorithm
same_as:
  wikidata: Q1030529
  wikipedia: Blossom algorithm
---

## Summary

The blossom algorithm, due to Jack Edmonds in 1965, finds a maximum [[matching|0MJ04A50QW]] in any finite graph in polynomial time.
It grows a matching by augmenting paths, and it handles odd cycles, called blossoms, by shrinking them to single vertices.
It was the first polynomial-time algorithm for matchings in general graphs, and Edmonds used it to argue that efficient means polynomial time.
A weighted version finds a [[perfect matching|0NHK9MFFW9]] of least weight.

## Explanations

### L1 human

A matching pairs up vertices along edges, with no vertex used twice.
To enlarge a matching, one looks for a path that starts and ends at unpaired vertices and alternates between unused and used edges.
Swapping used and unused edges along such a path pairs one more couple.
In a graph with odd cycles, the search for such a path can go around in circles.
The algorithm shrinks such an odd cycle to one point, searches in the smaller graph, and then expands the cycle again.
