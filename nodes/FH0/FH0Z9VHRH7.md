---
tag: FH0Z9VHRH7
kind: definition
name: Fine topology
msc: [31C40, 31B05]
defines: W2ZD4XP74R
uses: [X4V2S56YQQ, 0CQHFPGJ45, 072J68M6HX, 7DGF6MMEGX, C95QJ7YH5T]
sources:
  - url: https://en.wikipedia.org/wiki/Fine_topology_(potential_theory)
---

## Definition

Let $n \ge 2$.
The *fine topology* on $\R^n$ is the coarsest [[topology|0CQHFPGJ45]] $\mathcal{T}$ on $\R^n$ with the following property.
For every open set $U \subseteq \R^n$ and every [[superharmonic function|X4V2S56YQQ]] $u$ on $U$, the set $U$ belongs to $\mathcal{T}$ and $u \colon U \to (-\infty, +\infty]$ is continuous for $\mathcal{T}$.
Sets in $\mathcal{T}$ are called *finely open*, and limits and continuity for $\mathcal{T}$ are called fine limits and fine continuity.

## Remarks

The fine topology is [[finer|072J68M6HX]] than the Euclidean topology, since every Euclidean open set is finely open by definition.
A set $V$ is finely open if and only if, for every $x \in V$, the complement $\R^n \setminus V$ is [[thin|7DGF6MMEGX]] at $x$.
Example: let $V = \R^3 \setminus \set{k^{-1} e_1 : k \ge 1}$.
The removed set is countable, hence a [[polar set|C95QJ7YH5T]], and a polar set is thin at every point.
So $V$ is finely open, but it is not Euclidean open, because every ball about $0 \in V$ meets the removed points.
Non-example: a closed half-space $H$ is not a fine neighbourhood of a point $x \in \partial H$, since the complementary open half-space is not thin at $x$.
