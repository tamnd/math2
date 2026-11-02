---
tag: 2BCES6NPYM
kind: concept
name: Permuting congruences
msc: [08A30, 08B05]
sources:
  - url: https://en.wikipedia.org/wiki/Congruence-permutable_algebra
---

## Summary

Two [[congruences|DCSXXT4SER]] on an [[algebra|QJGPT2W0FT]] permute when their relational products in the two orders are equal.
Then their join in the [[congruence lattice|REE07CSXHR]] is simply their product, which makes it easy to compute.
An algebra whose congruences all permute is called congruence-permutable; groups, rings and modules are examples.
This property is the starting point of [[congruence-permutable varieties|1B3N9T68YV]] and of Mal'cev conditions.

## Explanations

### L1 human

Given two congruences, one can walk from $a$ to $c$ by first taking a step in one and then a step in the other.
The congruences permute when the order of the two steps does not matter for which pairs $(a, c)$ can be reached.
In a group, a step in the congruence of a normal subgroup $N$ is multiplication by an element of $N$, and two normal subgroups $N$ and $M$ satisfy $NM = MN$.
So all congruences of a group permute.
For a bare set without operations, many pairs of equivalence relations do not permute.
