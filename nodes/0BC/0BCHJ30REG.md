---
tag: 0BCHJ30REG
kind: definition
name: Cycle type
aliases: [cycle-structure]
msc: [20B30]
defines: 0J3K4Y1KPD
uses: [0YWDAZPRPQ]
sources:
  - url: https://en.wikipedia.org/wiki/Permutation
    locator: Cycle type
---

## Definition

Let $\sigma \in S_n$.
Write $\sigma$ as a product of disjoint cycles, and include a $1$-cycle for each fixed point.
The cycle type of $\sigma$ is the multiset of the lengths of these cycles.

## Remarks

The [[disjoint cycle decomposition|0YWDAZPRPQ]] is unique up to order, so the cycle type is well defined.
The lengths add up to $n$, so the cycle type is a partition of $n$.
For example, $(1\ 2)(3\ 4\ 5) \in S_6$ has cycle type $(3, 2, 1)$.

## Explanations

### L1 human

The cycle type forgets which points are in which cycle and keeps only the sizes of the cycles.
Two permutations with the same cycle type have the same shape.
In the symmetric group, the shape decides exactly when two permutations are conjugate.
