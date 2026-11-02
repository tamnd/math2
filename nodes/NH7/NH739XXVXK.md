---
tag: NH739XXVXK
kind: concept
name: Partition of unity
msc: [58A05, 54D20]
sources:
  - url: https://en.wikipedia.org/wiki/Partition_of_unity
same_as:
  wikidata: Q191690
  wikipedia: Partition of unity
---

## Summary

A partition of unity is a family of nonnegative functions on a space that add up to $1$ at every point.
Usually each function is required to live inside a chosen open set.
It is the standard tool for gluing local constructions into global ones.
On a smooth manifold one builds an object in each coordinate chart, multiplies it by the matching function, and adds the results.
Smooth partitions of unity exist on every smooth manifold, which is why Riemannian metrics and many other structures exist on all of them.

## Explanations

### L1 human

Imagine several lamps lighting a long hall, each lamp covering only part of it.
You want the total light to be exactly $1$ everywhere.
So you dim each lamp near the edges of its region, in such a way that the overlaps add up correctly.
The brightness profiles of the lamps form a partition of unity.
On the line, two smooth bumps $\rho_1$ and $\rho_2 = 1 - \rho_1$, where $\rho_1$ is $1$ far to the left and $0$ far to the right, give a simple example.
