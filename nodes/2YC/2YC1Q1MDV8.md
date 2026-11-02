---
tag: 2YC1Q1MDV8
kind: concept
name: Series-parallel partial order
msc: [06A07, 06A06]
sources:
  - url: https://en.wikipedia.org/wiki/Series-parallel_partial_order
same_as:
  wikidata: Q7454786
  wikipedia: Series-parallel partial order
---

## Summary

A series-parallel partial order is a finite poset built from single points by two operations.
The series operation puts one poset entirely below another, as in the [[ordinal sum|6AJ7QQCTQQ]].
The parallel operation places two posets side by side, as in the [[disjoint union|TZWMEM7GKA]].
Many problems that are hard for general posets, such as counting linear extensions, become easy for this class.

## Explanations

### L1 human

Think of a project where some groups of tasks run one after another, and other groups run at the same time.
If the whole plan can be described this way, by nesting "then" and "at the same time", its order is series-parallel.
For example, "do $a$, then do $b$ and $c$ at the same time, then do $d$" gives the poset $a < b, c < d$ with $b$ and $c$ incomparable.
