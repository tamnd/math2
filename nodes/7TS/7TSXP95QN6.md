---
tag: 7TSXP95QN6
kind: concept
name: Directed-complete partial order
msc: [06B35, 06A06, 68Q55]
specializes: [0QV2JS9RJ3]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_partial_order
---

## Summary

A directed-complete partial order, or dcpo, is a partially ordered set in which every directed subset has a supremum.
Dcpos are the basic objects of [[domain theory|Q2P5D74Q1V]], where elements are read as pieces of information and directed sets as consistent ways of collecting information.
Many authors also ask for a least element and call the result a pointed dcpo or a cpo.

## Explanations

### L1 human

Think of the elements as partial results of a computation, ordered by "is less defined than".
A directed set is a collection of partial results in which any two have a common improvement inside the collection.
In a dcpo, such a collection always has a best combined result, its supremum.
Every complete lattice is a dcpo.
The partial functions from $\N$ to $\N$, ordered by extension, form a dcpo: the supremum of a directed family of partial functions is their union.
