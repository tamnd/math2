---
tag: VNW5FHCQ2M
kind: concept
name: Wandering set
msc: [37B20, 37A40]
sources:
  - url: https://en.wikipedia.org/wiki/Wandering_set
same_as:
  wikidata: Q2506703
  wikipedia: Wandering set
---

## Summary

A wandering set of a map is a set that the map moves completely off itself: none of its later images meets it again.
A point is a wandering point when it has a neighbourhood that is a wandering set.
Wandering points carry the transient part of the motion, the part that happens once and is never repeated.
Their complement, the [[non-wandering set|EY2W34JZA4]], is where all the recurrent behaviour of the system lives.

## Explanations

### L1 human

Think of a ball rolling down a slope into a valley.
A small region on the slope is carried down and never comes back to overlap with itself.
That region is a wandering set, and the points in it are wandering points.
For the map $x \mapsto x + 1$ on the real line, the interval $(0, 1)$ is a wandering set, since its images $(n, n+1)$ never meet it.
