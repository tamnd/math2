---
tag: FSRST924GR
kind: concept
name: Fuzzy algebraic structure
msc: [08A72, 20N25, "03E72"]
sources:
  - url: https://en.wikipedia.org/wiki/Fuzzy_set
---

## Summary

A fuzzy algebraic structure replaces a substructure of an algebra by a fuzzy subset.
A fuzzy subset gives each element a degree of membership between $0$ and $1$.
The fuzzy subset must respect the operations: the result of an operation belongs at least as much as the least member among its arguments.
The first case studied was the fuzzy subgroup of a [[group|G5S1M9]], introduced by Rosenfeld in 1971.
Fuzzy subrings, fuzzy ideals and fuzzy subalgebras of general algebras followed.
A fuzzy subalgebra is determined by its level sets, which form a nested family of ordinary subalgebras, one for each membership level.

## Explanations

### L1 human

An ordinary subgroup either contains an element or does not.
A fuzzy subgroup lets an element belong only partly, with a degree such as $1/2$.
The rule is that combining elements never lowers membership below the weakest of them.
For example, in the integers let even numbers have degree $1$ and odd numbers degree $1/2$.
Adding two numbers of degree at least $1/2$ gives a number of degree at least $1/2$, so this is a fuzzy subgroup.
