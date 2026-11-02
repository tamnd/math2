---
tag: 2GRPCP5XK9
kind: concept
name: Symmetric decreasing rearrangement
msc: [26D15, "46E30", 35B06]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetric_decreasing_rearrangement
same_as:
  wikidata: Q2502733
  wikipedia: Symmetric decreasing rearrangement
---

## Summary

The symmetric decreasing rearrangement of a function $f$ on $\R^n$ is a radial function $f^*$, decreasing in $\abs{x}$.
Its superlevel sets are balls centred at the origin with the same volumes as the superlevel sets of $\abs{f}$.
It keeps every $L^p$ norm, does not increase the Dirichlet energy, and does not decrease certain double integrals.
So it is the main tool to show that balls and radial functions are optimal in variational problems.
Examples are the [[Faber–Krahn inequality|E7TY2TPXX7]] and the isoperimetric inequality.
It is the $n$-dimensional, symmetric version of the [[decreasing rearrangement|BWS042NC2P]] on $[0, \infty)$.

## Explanations

### L1 human

Think of the graph of $\abs{f}$ as a mountain landscape made of horizontal slices.
Replace each slice by a disc of the same area, centred over the origin, and stack the discs.
The result is a single round mountain with its peak at the origin and the same amount of material at each height.
For example, the indicator function of the interval $[1, 3]$ becomes the indicator function of $(-1, 1)$.
