---
tag: EQDDVAKSVE
kind: definition
name: Manifold with corners
msc: [58A05, 57R99]
defines: SZ1R8N1NR7
uses: [0CQHFPGJ45, 0S1FJ8VEX9, 03PPNCM9GG, 0QT00PB5G2, 0V33BNKZ9S, J7P32JQTVE, 7DS6B2BFK8]
sources:
  - url: https://en.wikipedia.org/wiki/Manifold
---

## Definition

Let $n \ge 1$ be an integer and let $\overline{\R}^n_+ = \set{x \in \R^n : x_1 \ge 0, \ldots, x_n \ge 0}$ be the closed orthant, with the subspace topology.
Let $A \subseteq \R^n$ be any subset.
A map $f \colon A \to \R^n$ is *smooth* if each $a \in A$ has an open neighbourhood $W$ in $\R^n$ with a [[smooth|0V33BNKZ9S]] map $g \colon W \to \R^n$ equal to $f$ on $A \cap W$.
Let $M$ be a [[topological space|0CQHFPGJ45]].
A *chart with corners* on $M$ is a [[homeomorphism|0QT00PB5G2]] $\varphi$ from an open subset $U \subseteq M$ onto an open subset of $\overline{\R}^n_+$.
A *smooth atlas with corners* is a family of charts with corners whose domains cover $M$.
Its transition maps $\varphi_j \circ \varphi_i^{-1}$ must be smooth in the above sense.
A *smooth manifold with corners of dimension $n$* is a space $M$ such that:

1. $M$ is [[Hausdorff|0S1FJ8VEX9]].
2. $M$ is [[second-countable|03PPNCM9GG]].
3. $M$ carries a maximal smooth atlas with corners of dimension $n$.

## Remarks

The square $[0, 1]^2$ is a manifold with corners.
Near the vertex $(0, 0)$ the identity is a chart onto an open subset of $\overline{\R}^2_+$.
Near $(1, 1)$ the chart is $(x, y) \mapsto (1 - x, 1 - y)$, and near the other points one uses similar affine maps.
All transition maps are affine, hence smooth, and the charts generate a maximal atlas.

The solid square pyramid in $\R^3$ is not a manifold with corners for this structure, because clause 3 fails at its apex.
The tangent cone of the pyramid at the apex has four faces.
The derivative of a chart at the apex would map it linearly onto the cone $\overline{\R}^3_+$, which has only three faces.

A chart with corners is in particular a chart in the sense of an [[atlas|J7P32JQTVE]] modelled on $\overline{\R}^n_+$.
As a topological space, every manifold with corners is a [[manifold with boundary|7DS6B2BFK8]], because $\overline{\R}^n_+$ is homeomorphic to the half-space $\set{x_n \ge 0}$.
In Mathlib, manifolds with corners are modelled through a `ModelWithCorners`.
