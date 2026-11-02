---
tag: 3AX549FFFM
kind: concept
name: Maximal chain
msc: [06A06, 06A07]
specializes: [0S8FE7ZMFM]
sources:
  - url: https://en.wikipedia.org/wiki/Total_order
    locator: Chains
---

## Summary

A maximal chain in a [[partially ordered set|011C29Q1S1]] is a [[chain|0GP9ASVQ1X]] that is not contained in any strictly larger chain.
The [[Hausdorff maximal principle|0KM4KVR9MV]] says that every chain lies in a maximal chain, and this statement is equivalent to the axiom of choice.
In finite posets, maximal chains are used to define the height and the grading of a poset.

## Explanations

### L1 human

A chain is a set of elements that stand on one line in the order.
A maximal chain is a chain that cannot be extended: no other element can be added while keeping all elements comparable.
In the subsets of $\set{1, 2}$, the chain $\emptyset \subset \set{1} \subset \set{1, 2}$ is maximal.
The chain $\emptyset \subset \set{1, 2}$ is not maximal, because $\set{1}$ can be inserted.
