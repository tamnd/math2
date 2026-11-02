---
tag: PYH82FMXQ2
kind: concept
name: Semiring of sets
msc: [28A05]
specializes: [4W9NM803BB]
sources:
  - url: https://en.wikipedia.org/wiki/Ring_of_sets
---

## Summary

A semiring of sets is a family of sets that contains the empty set and is closed under intersections of two members.
In it, the difference of two members is a finite disjoint union of members.
The half-open intervals of the real line form the main example.
Measures such as Lebesgue measure are often first defined on a semiring and then extended.

## Explanations

### L1 human

A semiring of sets is a family of simple building blocks.
Two blocks overlap in a block, and cutting one block out of another leaves finitely many separate blocks.
Half-open intervals $[a, b)$ are the picture to keep in mind: $[0, 3) \setminus [1, 2)$ is the two blocks $[0, 1)$ and $[2, 3)$.
Length is easy to define on such blocks, and measure theory extends it to much more complicated sets.
