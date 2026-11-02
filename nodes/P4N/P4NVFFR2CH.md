---
tag: P4NVFFR2CH
kind: definition
name: Surface
msc: [57K20, 57N99]
defines: VGJJVBZ1MQ
uses: [QQQ9B1DK4P, 0S1FJ8VEX9, 0QT00PB5G2]
sources:
  - url: https://en.wikipedia.org/wiki/Surface_(topology)
---

## Definition

A *surface* is a topological space $S$ such that:

1. $S$ is [[Hausdorff|0S1FJ8VEX9]];
2. $S$ is second countable, that is, its topology has a countable base;
3. every point of $S$ has an open neighbourhood [[homeomorphic|0QT00PB5G2]] to an open subset of $\R^2$.

Equivalently, a surface is a [[topological manifold|QQQ9B1DK4P]] of dimension $2$.
A *surface with boundary* is defined in the same way, with open subsets of the closed half-plane $\set{(x, y) \in \R^2 : y \ge 0}$ in clause 3.
A *closed surface* is a compact connected surface without boundary.

## Remarks

Example: the unit sphere $S^2 \subset \R^3$ is a surface.
It is Hausdorff and second countable as a subspace of $\R^3$.
Stereographic projections from the north pole and from the south pole are homeomorphisms of two open subsets of $S^2$ onto $\R^2$, and these subsets cover $S^2$.

Non-example: let $X$ be the union of the planes $z = 0$ and $y = 0$ in $\R^3$.
Clauses 1 and 2 hold, but clause 3 fails at points of the $x$-axis.
A small sphere around a point $P$ of this axis meets $X$ in two great circles crossing at two points, a graph $G$ with $2$ vertices and $4$ edges.
So $P$ has a neighbourhood that is a cone on $G$, and the local homology group $H_2(X, X \setminus \set{P})$ is $\tilde H_1(G) \cong \Z^3$.
At a point of an open subset of $\R^2$ this group is $\tilde H_1(S^1) \cong \Z$, and local homology is preserved by homeomorphisms of neighbourhoods.

## Explanations

### L1 human

The three clauses say: points can be separated, the space is not too big, and near each point the space is a patch of the plane.
The last clause is the heart of the matter.
The first two rule out pathological spaces, such as the plane with two origins, which fails clause 1.
