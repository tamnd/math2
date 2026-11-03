---
tag: X499BMR9MS
kind: concept
name: Parameterized complexity
msc: [68Q27, 68Q25]
sources:
  - url: https://en.wikipedia.org/wiki/Parameterized_complexity
same_as:
  wikidata: Q1570441
  wikipedia: Parameterized complexity
---

## Summary

Parameterized complexity measures the running time of an algorithm in terms of the input size and of a second number, the parameter.
Its central class is FPT, the problems solvable in time $f(k) \cdot n^{c}$ with any function $f$ of the parameter $k$ and a constant $c$.
It explains why some NP-hard problems are easy in practice when a parameter is small.
The theory was developed by Downey and Fellows.

## Explanations

### L1 human

Some hard problems become easy when one number in the input is small.
For example, deciding whether $k$ vertices of a graph touch all edges takes time about $2^k \cdot n$.
This is fast for $k = 20$, even on a huge graph.
Other problems, such as finding $k$ vertices that are all joined to each other, seem to need time like $n^k$.
Parameterized complexity sorts problems by this difference.
