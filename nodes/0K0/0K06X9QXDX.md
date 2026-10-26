---
tag: 0K06X9QXDX
kind: definition
name: Convex set
msc: [52A20]
defines: 02AS45T3H9
uses: [0XPR1E85W0, 0KJH6SRFZK]
sources:
  - url: https://en.wikipedia.org/wiki/Convex_set
    locator: Definitions
  - url: https://en.wikipedia.org/wiki/Convex_set
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Convex_set
    locator: Intersections and unions
---

## Definition

A subset $S$ of $\mathbb{R}^n$ is convex if for all $x, y \in S$ and each real number $t$ with $0 \leq t \leq 1$,
$$(1 - t)\, x + t\, y \in S.$$
That is, $S$ contains the segment from $x$ to $y$.

## Remarks

The same definition works in each real vector space or real affine space. Mathlib's `Convex` is stated for a module over an ordered semiring.
A convex set contains each convex combination $\sum_i w_i x_i$ of its points, an [[affine combination|0KJH6SRFZK]] with $w_i \geq 0$.
The empty set and the whole space are convex. Each intersection of convex sets is convex, but a union of convex sets need not be convex.
Balls, half-spaces, lines and triangles with their inside are convex.

## Explanations

### L1 human

A set is convex if you can see each of its points from each other point, with the line of sight inside the set. A disc is convex. A ring is not: the segment between two opposite points of the ring passes through the hole.
