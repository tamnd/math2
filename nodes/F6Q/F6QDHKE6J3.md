---
tag: F6QDHKE6J3
kind: concept
name: Filter limit
msc: [54A20, 40J05]
sources:
  - url: https://en.wikipedia.org/wiki/Filter_(mathematics)
---

## Summary

A filter limit is the limit of a function $f \colon S \to X$ along a [[filter|15PF73BKY6]] on $S$, where $X$ is a [[topological space|0CQHFPGJ45]].
The function tends to $x$ along the filter when the preimage of every [[neighbourhood|0ZCY0Z80B6]] of $x$ belongs to the filter.
One notion covers limits of sequences, limits of functions at a point or at infinity, one-sided limits and sums of families, by choosing the filter.
It is the same as the [[convergence|70M1VAPFN0]] of the image filter $f(\mathcal{F})$ to $x$.

## Explanations

### L1 human

A filter on $S$ describes a way of "going to the limit" in $S$, by saying which sets are eventually entered.
For sequences, the sets that are eventually entered are the sets that contain all $n$ from some point on.
A function has limit $x$ along the filter if, for every small region around $x$, the points where the function lands in that region form an eventually entered set.
With the filter of tails of $\N$, this is exactly the usual limit of a sequence.
