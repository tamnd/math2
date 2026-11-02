---
tag: 4BVWH0BN28
kind: concept
name: Relative homology
msc: [55N10]
sources:
  - url: https://en.wikipedia.org/wiki/Relative_homology
same_as:
  wikidata: Q1959911
  wikipedia: Relative homology
---

## Summary

Relative homology assigns to a space $X$ and a subspace $A$ the groups $H_n(X, A)$.
They measure the homology of $X$ while ignoring everything that happens inside $A$.
It is built from the singular chains of $X$ modulo the chains of $A$.
Relative groups fit into the long exact sequence of the pair and are the setting of the excision theorem.
This makes them the main tool for computing [[singular homology|M0Q5CFJ7ZH]].

## Explanations

### L1 human

Think of $A$ as a region that is painted over and treated as if it were a single point.
A relative cycle is a chain whose boundary lies in $A$, so it may have loose ends as long as they end inside $A$.
For the interval $X = [0, 1]$ with $A = \set{0, 1}$, the path from $0$ to $1$ is a relative cycle, because its boundary consists of the two end points.
It represents a generator of $H_1([0,1], \set{0,1}) \cong \Z$, just as if the two end points were glued into a circle.
