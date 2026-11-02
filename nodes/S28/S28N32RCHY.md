---
tag: S28N32RCHY
kind: definition
name: Tessellation
msc: [52C20, 52C22, 05B45]
defines: GKJK293DXS
uses: [0XPR1E85W0, 0ZCK8DQYN1, 0RZH6W98HK]
sources:
  - url: https://en.wikipedia.org/wiki/Tessellation
---

## Definition

Let $n \ge 1$ and let $\R^n$ be [[Euclidean space|0XPR1E85W0]].
A *tessellation* or *tiling* of $\R^n$ is a countable family $\mathcal{T} = \set{T_1, T_2, \dots}$ of subsets of $\R^n$, called *tiles*, such that:

1. each tile $T_i$ is a [[closed set|0ZCK8DQYN1]] with nonempty [[interior|0RZH6W98HK]];
2. the union of all tiles is $\R^n$;
3. the interiors of two distinct tiles are disjoint.

## Remarks

Example: the squares $T_{a,b} = [a, a+1] \times [b, b+1]$ with $(a, b) \in \Z^2$ form a tiling of $\R^2$.
Each square is closed with nonempty interior, every point $(x, y)$ lies in $T_{\floor{x}, \floor{y}}$, and two distinct open squares $(a, a+1) \times (b, b+1)$ do not meet.

Non-example: the closed unit disks centred at the points of $\Z^2$ cover $\R^2$, but the disks centred at $(0, 0)$ and $(1, 0)$ have overlapping interiors, so clause 3 fails.

Many authors also require each tile to be homeomorphic to a closed ball, so that tiles are "topological disks" in the plane.
A *prototile* set of a tiling is a set of shapes such that each tile is congruent to one of them.
In dimension $3$ and higher, tilings by polyhedra are also called [[honeycombs|HTJ03RFKFH]].
