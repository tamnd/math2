---
tag: EX7N9D1YCD
kind: concept
name: Krull dimension of a poset
msc: [06A06, 13C15]
sources:
  - url: https://en.wikipedia.org/wiki/Krull_dimension
---

## Summary

The Krull dimension of a [[partially ordered set|0QV2JS9RJ3]] is the supremum of the lengths of its finite [[chains|0S8FE7ZMFM]].
Here a chain with $n + 1$ elements has length $n$.
It generalizes the [[Krull dimension of a commutative ring|MVGBS3J1P7]], which is the Krull dimension of the set of prime ideals ordered by inclusion.
For a nonempty finite poset it is one less than the [[height|MPR6MH4YSQ]] counted in elements.

## Explanations

### L1 human

Count the number of upward steps in the longest climb through the poset.
A single point has dimension $0$, a two-element chain has dimension $1$, and the subsets of a set with $n$ elements have dimension $n$.
The name comes from algebra, where a point, a curve and a surface give chains of prime ideals with $0$, $1$ and $2$ steps.
