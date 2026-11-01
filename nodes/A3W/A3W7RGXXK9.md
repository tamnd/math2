---
tag: A3W7RGXXK9
kind: concept
name: Lebesgue covering dimension
msc: [54F45]
sources:
  - url: https://en.wikipedia.org/wiki/Lebesgue_covering_dimension
same_as:
  wikidata: Q164262
  wikipedia: Lebesgue covering dimension
---

## Summary

The Lebesgue covering dimension of a topological space is the least $n$ with the following property.
Every finite open cover can be refined to an open cover in which no point lies in more than $n + 1$ sets.
It is a topological invariant, and it gives $n$ for the Euclidean space $\R^n$.
It is one of the main notions of dimension theory, together with the [[inductive dimensions|MKS9H497AM]].

## Explanations

### L1 human

Cover a line segment by short overlapping open intervals; one can arrange that each point lies in at most two of them, but not always in only one.
Cover a square by small open tiles; one can arrange that each point lies in at most three of them, like bricks in a wall, but not in fewer.
The covering dimension turns this count into a definition: a space has dimension $n$ when the best one can do is $n + 1$.
So a segment has dimension $1$ and a square has dimension $2$.
