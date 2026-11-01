---
tag: VHAMHH5SPC
kind: concept
name: List coloring
msc: [05C15]
specializes: [0NCPXH194Y]
sources:
  - url: https://en.wikipedia.org/wiki/List_coloring
same_as:
  wikidata: Q1130404
  wikipedia: List coloring
---

## Summary

List coloring is a form of [[graph colouring|0NCPXH194Y]] in which each vertex must take its colour from its own list of allowed colours.
A graph is $k$-choosable if it can be coloured from any lists of size $k$, and the least such $k$ is its choice number.
The choice number is at least the [[chromatic number|0VHJRXNAAS]], and it can be much larger.

## Explanations

### L1 human

Imagine scheduling exams, where two exams that share a student need different time slots.
In ordinary colouring every exam may use any slot.
In list coloring each exam has its own list of possible slots, and you must still find a clash-free choice.
For example, the complete bipartite graph $K_{3,3}$ can be coloured with $2$ colours, but there are lists of size $2$ from which it cannot be coloured.
