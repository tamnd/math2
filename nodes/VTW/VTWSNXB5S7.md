---
tag: VTWSNXB5S7
kind: definition
name: Limit
msc: [18A30]
defines: CHS5AFJGWE
uses: [A2DE66937D, HJK75HDWFE, 7TPBQPPN97, EK85VSSRMR, 09CEDJYBKP]
sources:
  - url: https://en.wikipedia.org/wiki/Limit_(category_theory)
---

## Definition

Let $J$ and $\mathcal{C}$ be [[categories|A2DE66937D]] and let $D \colon J \to \mathcal{C}$ be a [[diagram|HJK75HDWFE]].
A *limit* of $D$ is a [[cone|7TPBQPPN97]] $(L, \varphi)$ over $D$, with $\varphi_j \colon L \to D(j)$, that satisfies the following condition.
For every cone $(N, \psi)$ over $D$ there is exactly one morphism $h \colon N \to L$ with $\varphi_j \circ h = \psi_j$ for every object $j$ of $J$.
The object $L$ is written $\lim D$ or $\varprojlim D$, and the $\varphi_j$ are its *projections*.

## Remarks

Equivalently, a limit of $D$ is a [[terminal object|EK85VSSRMR]] of the category of cones over $D$.
So a limit is unique up to a unique isomorphism of cones.
When $J$ is empty, a cone is just an object, and a limit of the empty diagram is a terminal object of $\mathcal{C}$.

Example: in the category of sets, every diagram $D$ with $J$ small has a limit.
It is the subset
$$L = \set{(x_j)_j \in \textstyle\prod_j D(j) : D(u)(x_j) = x_k \text{ for all } u \colon j \to k}$$
of the [[Cartesian product|09CEDJYBKP]] of the sets $D(j)$, with $\varphi_j$ the coordinate projections.
A cone $(N, \psi)$ factors through $L$ by $h(n) = (\psi_j(n))_j$, which lies in $L$ by the cone condition, and $h$ is forced by $\varphi_j \circ h = \psi_j$.

Non-example: take the diagram of two non-empty sets $X$ and $Y$ with no arrows.
The cone $X \times Y \times \{0, 1\}$ with the projections to $X$ and $Y$ is not a limit.
The cone $X \times Y$ factors through it in two ways, by $(x, y) \mapsto (x, y, 0)$ and $(x, y) \mapsto (x, y, 1)$, so uniqueness fails.
