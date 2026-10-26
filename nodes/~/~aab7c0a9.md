---
tag: ~aab7c0a9
kind: definition
name: Affine span
aliases: [affine-hull]
msc: [51N10]
defines: ~04fa590f
uses: [~b4bd557a, ~b96fc743]
sources:
  - url: https://en.wikipedia.org/wiki/Affine_hull
    locator: lead section
---

## Definition

Let $K$ be a field, and let $A$ be an [[affine space|~f1f01244]] over a vector space $V$ over $K$. Let $S$ be a nonempty subset of $A$.
The affine span of $S$, written $\operatorname{aff}(S)$, is the intersection of all [[affine subspaces|~b4bd557a]] of $A$ that contain $S$.
It is the smallest affine subspace of $A$ that contains $S$.

## Remarks

The affine span of $S$ is the set of all [[affine combinations|~b96fc743]] of finitely many points of $S$.
In $\mathbb{R}^3$: the affine span of two distinct points is the line through them. The span of three points that are not on one line is the plane through them. The span of four points that are not in one plane is all of $\mathbb{R}^3$.
For each point $p$ of $S$, the affine span is $p + W$, where $W$ is the linear span of the vectors $q - p$ for $q \in S$.
Mathlib also defines the affine span of the empty set: it is the empty affine subspace.

## Explanations

### L1 human

The affine span is the flat object that the given points determine. Two points give a line, and three points in general position give a plane. Compare it with the linear span of vectors, which must always pass through the origin.
