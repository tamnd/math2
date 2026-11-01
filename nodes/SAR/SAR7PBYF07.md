---
tag: SAR7PBYF07
kind: counterexample
name: Moore plane
msc: [54G20, 54D15]
uses: [0NSR9V8TED, C5N2J2K6Z3, 0Z2P41SVDP, 0ZCK8DQYN1, 0ZCY0Z80B6, 0S1FJ8VEX9]
sources:
  - url: https://en.wikipedia.org/wiki/Moore_plane
---

## Counterexample

Let $\Gamma = \set{(x, y) \in \R^2 : y \ge 0}$ be the closed upper half-plane.
Give a point $(x, y)$ with $y > 0$ the usual Euclidean open discs around it, of radius less than $y$, as basic [[neighbourhoods|0ZCY0Z80B6]].
Give a point $(x, 0)$ the basic neighbourhoods $\set{(x, 0)} \cup D$, where $D$ is an open disc of radius $r > 0$ centred at $(x, r)$.
Such a disc $D$ is tangent to the $x$-axis at $(x, 0)$.
The space $\Gamma$ with this topology is the Moore plane, also called the Niemytzki plane.
It is a [[Tychonoff space|C5N2J2K6Z3]], hence [[Hausdorff|0S1FJ8VEX9]] and regular, but it is not [[normal|0NSR9V8TED]].

## Remarks

The $x$-axis $A = \set{(x, 0) : x \in \R}$ is [[closed|0ZCK8DQYN1]], since every point with $y > 0$ has a disc neighbourhood missing $A$.
The subspace $A$ is discrete, because a tangent disc neighbourhood of $(x, 0)$ meets $A$ only in $(x, 0)$.
So every subset of $A$ is closed in $\Gamma$.
The points with rational coordinates and $y > 0$ form a countable dense set, so $\Gamma$ is [[separable|0Z2P41SVDP]].
By Jones' lemma, a separable normal space has no closed discrete subset $A$ with $2^{\abs{A}} > 2^{\aleph_0}$.
Here $\abs{A} = 2^{\aleph_0}$, so $\Gamma$ is not normal.
For example, the points of $A$ with rational $x$ and the points of $A$ with irrational $x$ are disjoint closed sets that cannot be separated by disjoint open sets.
Since $\Gamma$ is Tychonoff, it is a subspace of a compact Hausdorff space, which is normal; so a subspace of a normal space need not be normal.

## Explanations

### L1 human

Away from the bottom edge, the Moore plane is the ordinary half-plane.
On the bottom edge, a point is only near the points of small discs that sit on top of it and touch the edge there.
So the points of the edge cannot see each other, and the edge breaks up into isolated points.
This makes it impossible to pull apart some disjoint closed pieces of the edge with open sets.
