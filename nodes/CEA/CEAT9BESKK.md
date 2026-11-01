---
tag: CEAT9BESKK
kind: concept
name: Amenable group
msc: [43A07, 20F65]
sources:
  - url: https://en.wikipedia.org/wiki/Amenable_group
same_as:
  wikidata: Q1857002
  wikipedia: Amenable group
---

## Summary

An amenable group is a group with a finitely additive, translation-invariant way to measure the size of all of its subsets, with total size $1$.
Finite groups, abelian groups and solvable groups are amenable; groups containing a non-abelian [[free group|0KTW26C80J]] are not.
Amenability has many equivalent forms, such as the Følner condition.
It governs the existence of paradoxical decompositions such as the one in the Banach–Tarski paradox.

## Explanations

### L1 human

Try to assign to every subset of a group the "fraction of the group" it fills.
Disjoint pieces should add up, and moving a set by a group element should not change its fraction.
For a finite group this is easy: take the number of elements divided by the order of the group.
For the integers one can do it too, with a kind of limiting density, though not by an explicit formula.
For the free group on two generators it is impossible: the group can be cut into pieces that, after moving, make two full copies of the group.
Amenable groups are those where such a fair notion of size exists.
