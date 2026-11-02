---
tag: CMYVK9CEKZ
kind: concept
name: Specialization preorder
msc: [54D10, 06A06]
specializes: [0VABYWJWH9]
sources:
  - url: https://en.wikipedia.org/wiki/Specialization_(pre)order
same_as:
  wikidata: Q5569420
  wikipedia: Specialization (pre)order
---

## Summary

The specialization preorder of a topological space orders its points by closure: $x \le y$ when $x$ lies in the closure of $\set{y}$.
It is a partial order exactly when the space is [[T0|07SG12TQH3]], and it is the equality relation exactly when the space is T1.
In algebraic geometry it records which points of a scheme specialize to which.
In domain theory it recovers the order of a poset from its Scott topology, and in general it links topological spaces with ordered sets.

## Explanations

### L1 human

In a nice space like the plane, every point is closed and the specialization preorder says nothing.
In spaces that are not T1 some points sit "inside the closure" of others, and the preorder records this.
In the Sierpiński space with points $0$ and $1$ and open sets $\emptyset$, $\set{1}$ and $\set{0, 1}$, the closure of $\set{1}$ is $\set{0, 1}$.
So $0 \le 1$: the point $1$ is a "general" point and $0$ is a "special" one.
