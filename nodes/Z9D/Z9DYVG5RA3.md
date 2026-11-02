---
tag: Z9DYVG5RA3
kind: definition
name: Topological manifold
msc: [57N99]
defines: QQQ9B1DK4P
uses: [0CQHFPGJ45, 0S1FJ8VEX9, 03PPNCM9GG, 02BH3MCBQB, 0QT00PB5G2, 0XPR1E85W0]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_manifold
    locator: Formal definition
---

## Definition

Let $n \ge 0$ be an integer and let $M$ be a [[topological space|0CQHFPGJ45]].
$M$ is a *topological manifold of dimension $n$*, or a topological $n$-manifold, if:

1. $M$ is [[Hausdorff|0S1FJ8VEX9]].
2. $M$ is [[second-countable|03PPNCM9GG]].
3. $M$ is locally Euclidean of dimension $n$: each point $x \in M$ has an [[open|02BH3MCBQB]] neighbourhood $U$ [[homeomorphic|0QT00PB5G2]] to an open subset of $\R^n$, the [[Euclidean space|0XPR1E85W0]].

## Remarks

The unit circle $S^1 = \set{(x, y) \in \R^2 : x^2 + y^2 = 1}$ is a $1$-manifold.
It is Hausdorff and second-countable as a subspace of $\R^2$.
The map $(x, y) \mapsto x$ sends the open upper half $\set{y > 0}$ of $S^1$ homeomorphically onto the interval $(-1, 1)$.
The three other open half circles are treated in the same way, and together the four cover $S^1$.

The line with two origins is the quotient of $\R \times \set{0, 1}$ obtained by identifying $(t, 0)$ with $(t, 1)$ for all $t \ne 0$.
It satisfies clauses 2 and 3, but it fails clause 1: the two origins have no disjoint neighbourhoods.

A nonempty manifold has only one dimension, by [[invariance of domain|6X2D0JDFQW]]: a nonempty open subset of $\R^m$ is not homeomorphic to an open subset of $\R^n$ when $m \ne n$.
A pair $(U, \varphi)$ with $\varphi$ a homeomorphism from $U$ onto an open subset of $\R^n$ is called a chart.
A compact manifold without boundary is called a closed manifold.
