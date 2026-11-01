---
tag: JR0G4HN9EA
kind: definition
name: Simplicial complex
msc: ["05E45", 55U10]
defines: V8GZ0W1ZZ5
uses: [070R982G4B, 00E0YZCERH]
sources:
  - url: https://en.wikipedia.org/wiki/Abstract_simplicial_complex
---

## Definition

Let $V$ be a [[finite set|070R982G4B]].
An *(abstract) simplicial complex* on the vertex set $V$ is a family $\Delta$ of subsets of $V$ such that:

1. If $\sigma \in \Delta$ and $\tau \subseteq \sigma$, then $\tau \in \Delta$.
2. $\set{v} \in \Delta$ for every $v \in V$.

The elements of $\Delta$ are its *faces*; a face $\sigma$ has dimension $\abs{\sigma} - 1$, and the dimension of $\Delta$ is the largest dimension of a face.
The maximal faces are called *facets*.

## Remarks

Example: on $V = \set{1, 2, 3}$, let $\Delta$ be the family of all subsets of $V$ except $V$ itself.
A subset of a set with at most $2$ elements has at most $2$ elements, so clause 1 holds.
Clause 2 holds, and $\Delta$ is the boundary of a triangle, of dimension $1$.

Non-example: on $V = \set{1, 2, 3}$, the family $\set{\emptyset, \set{1}, \set{2}, \set{3}, \set{1, 2}, \set{1, 2, 3}}$ fails clause 1, since $\set{1, 3} \subseteq \set{1, 2, 3}$ is missing.

A nonempty complex contains the empty face, of dimension $-1$.
Some authors allow an infinite vertex set, keeping every face finite.
A geometric realization places the vertices as affinely independent points in some $\R^N$ and replaces each face by the convex hull of its points.
