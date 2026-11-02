---
tag: YZ8AN4J2KD
kind: definition
name: Manifold with boundary
msc: [57N99]
defines: 7DS6B2BFK8
uses: [0CQHFPGJ45, 0S1FJ8VEX9, 03PPNCM9GG, 02BH3MCBQB, 0QT00PB5G2, 0XPR1E85W0, QQQ9B1DK4P, 6X2D0JDFQW]
sources:
  - url: https://en.wikipedia.org/wiki/Manifold
    locator: Manifold with boundary
---

## Definition

Let $n \ge 1$ be an integer and let $\mathbb{H}^n = \set{x \in \R^n : x_n \ge 0}$ be the closed upper half-space of [[Euclidean space|0XPR1E85W0]], with the subspace topology.
A [[topological space|0CQHFPGJ45]] $M$ is a *topological manifold with boundary of dimension $n$* if:

1. $M$ is [[Hausdorff|0S1FJ8VEX9]].
2. $M$ is [[second-countable|03PPNCM9GG]].
3. Each point $x \in M$ has an [[open|02BH3MCBQB]] neighbourhood that is [[homeomorphic|0QT00PB5G2]] to an open subset of $\mathbb{H}^n$.

A point $x \in M$ is a *boundary point* if some homeomorphism $\varphi$ from an open neighbourhood of $x$ onto an open subset of $\mathbb{H}^n$ has $\varphi(x) \in \set{x_n = 0}$.
The set of boundary points is the *boundary* $\partial M$, and $M \setminus \partial M$ is the *interior* of $M$.

## Remarks

The closed disk $D^2 = \set{x \in \R^2 : \abs{x} \le 1}$ is a manifold with boundary of dimension $2$, with $\partial D^2 = S^1$.
Near a point of the open disk it is an open subset of $\R^2$, which is homeomorphic to an open subset of the interior of $\mathbb{H}^2$.
Near a point of $S^1$, polar coordinates $(r, \theta) \mapsto (\theta, 1 - r)$ map a neighbourhood onto an open subset of $\mathbb{H}^2$, sending $S^1$ into the line $\set{x_2 = 0}$.

The cross $\set{(x, y) \in \R^2 : xy = 0}$ satisfies clauses 1 and 2 but fails clause 3 at the origin, where four arcs meet.

By [[invariance of domain|6X2D0JDFQW]], no point is a boundary point for one chart and an interior point for another, so the boundary is well defined.
The interior is a [[topological manifold|QQQ9B1DK4P]] of dimension $n$, and $\partial M$ is a topological manifold of dimension $n - 1$ with empty boundary.
A topological manifold is the same as a manifold with boundary whose boundary is empty.
Some authors use $\set{x_1 \ge 0}$ or $\set{x_1 \le 0}$ as the model half-space; the notion does not change.
