---
tag: AHYZMSBBNH
kind: concept
name: Pseudoconvexity
msc: [32T05, 32U10]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudoconvexity
same_as:
  wikidata: Q7254693
  wikipedia: Pseudoconvexity
---

## Summary

Pseudoconvexity is the notion of convexity adapted to several complex variables.
An open set in $\C^n$ is pseudoconvex if it admits a continuous [[plurisubharmonic|FF2P7ER3QT]] exhaustion function.
Such a function tends to $+\infty$ at the boundary and, for unbounded sets, at infinity.
Unlike holomorphic convexity, it is a local condition at the boundary, and for smooth boundaries it can be checked with the Levi form.
By the solution of the Levi problem, the pseudoconvex domains in $\C^n$ are exactly the domains of holomorphy.

## Explanations

### L1 human

Ordinary convexity can be tested with convex functions: a convex region carries a convex function that blows up at its edge.
Pseudoconvexity replaces convex functions by plurisubharmonic ones, which only need to be subharmonic along each complex line.
This condition is much weaker than convexity and is preserved by holomorphic changes of coordinates.
Every convex open set and every open set in $\C$ is pseudoconvex, but the punctured ball $\set{0 < \abs{z} < 1}$ in $\C^2$ is not.
