---
tag: 4F3KWXYXBA
kind: concept
name: Homotopy fiber
msc: [55R05, 55P05]
sources:
  - url: https://en.wikipedia.org/wiki/Homotopy_fiber
same_as:
  wikidata: Q5891822
  wikipedia: Homotopy fiber
---

## Summary

The homotopy fiber of a map $f \colon X \to Y$ over $y_0$ is the space of pairs of a point $x \in X$ and a path from $f(x)$ to $y_0$.
It replaces the ordinary fiber $f^{-1}(y_0)$ by a version that depends only on the homotopy class of $f$.
For a [[Serre fibration|PB9JXQ2KC3]] the two fibers have the same homotopy groups.
So homotopy fibers extend the [[long exact sequence of homotopy groups|E0RV5D1GQ0]] to arbitrary maps.
The homotopy fiber of the inclusion of a point is the [[loop space|2JFF5F3EGF]].

## Explanations

### L1 human

The ordinary fiber of $f$ over $y_0$ collects the points that land exactly on $y_0$.
The homotopy fiber is more forgiving: a point $x$ counts if it lands anywhere, as long as one also says how to walk from $f(x)$ to $y_0$.
So its points are pairs, a point $x$ and a path from $f(x)$ to $y_0$.
If $X$ is a single point mapped to $y_0$, the pairs are just the loops at $y_0$.
