---
tag: DRCDVJS6PT
kind: concept
name: N-body simulation
msc: [85-10, 70F10, 65Z05]
sources:
  - url: https://en.wikipedia.org/wiki/N-body_simulation
same_as:
  wikidata: Q85787439
  wikipedia: N-body simulation
---

## Summary

An N-body simulation computes, step by step in time, the motion of many particles that attract each other by gravity.
It gives approximate solutions of the [[n-body problem|62SNWC5E45]] when $N$ is far too large for exact formulas.
In astrophysics it is the main tool to study star clusters, galaxies and the growth of cosmic structure.

## Explanations

### L1 human

Put a large number of point masses in a computer, each pulled by all the others according to [[Newton's law of gravitation|29WRN5J730]].
At each small time step, compute the forces, move the particles a little, and repeat.
The particles may stand for single stars, or for large lumps of dark matter in a cosmological box.
For example, two equal masses started at rest a distance apart fall towards each other, and a simulation reproduces this fall to good accuracy with small steps.
The hard parts are the cost of computing all pairwise forces and the errors that close encounters cause.
