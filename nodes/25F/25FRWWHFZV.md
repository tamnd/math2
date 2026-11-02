---
tag: 25FRWWHFZV
kind: concept
name: Choquet capacity
msc: [28A12, 31C15]
sources:
  - url: https://en.wikipedia.org/wiki/Capacity_of_a_set
---

## Summary

A Choquet capacity is a monotone set function defined on all subsets of a space.
It is continuous along increasing sequences of sets and along decreasing sequences of compact sets.
Choquet introduced the notion to treat [[Newtonian capacity|4YZVFGJVSZ]] and outer measures in one framework.
Its main result, Choquet's capacitability theorem, says that analytic sets can be approximated from inside by compact sets for every Choquet capacity.
This theorem is a basic tool for measurability questions in probability and descriptive set theory.

## Explanations

### L1 human

A measure adds up sizes of disjoint pieces, but many useful notions of size do not add.
A Choquet capacity asks only for three softer things.
A bigger set is not smaller.
Growing sets have sizes that grow to the size of the limit.
Shrinking compact sets have sizes that shrink to the size of the limit.
The outer measure of a finite measure is an example, and so is the diameter of a set in a metric space.
