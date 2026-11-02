---
tag: T4ESER8G7G
kind: definition
name: 4-manifold
msc: [57K40]
defines: 8H58Q6YJCH
uses: [QQQ9B1DK4P, R2TQ82PCNB]
sources:
  - url: https://en.wikipedia.org/wiki/4-manifold
---

## Definition

A *$4$-manifold* is a [[topological manifold|QQQ9B1DK4P]] of dimension $4$, that is, a topological space $M$ such that:

1. $M$ is Hausdorff,
2. $M$ is second countable, and
3. every point of $M$ has an open neighborhood homeomorphic to an open subset of $\R^4$.

A *smooth $4$-manifold* is a $4$-manifold with a [[smooth structure|R2TQ82PCNB]].

## Remarks

Example: the $4$-sphere $S^4 = \set{x \in \R^5 : \abs{x} = 1}$ is Hausdorff and second countable as a subspace of $\R^5$, and stereographic projection from a point $p$ maps $S^4 \setminus \set{p}$ homeomorphically onto $\R^4$, which gives clause 3.

Non-example: take two copies of $\R^4$ and glue them along the complement of the origin.
Every point has a neighborhood homeomorphic to $\R^4$, but the two origins have no disjoint neighborhoods, so clause 1 fails.

By invariance of domain, no nonempty open subset of $\R^4$ is homeomorphic to an open subset of $\R^n$ with $n \ne 4$, so the dimension is well defined.
The [[$E_8$ manifold|BNDRN0G9BR]] is a closed $4$-manifold with no smooth structure.
