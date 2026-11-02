---
tag: PWQ5ZR5PK5
kind: definition
name: Atlas
msc: [57N99, 58A05]
defines: J7P32JQTVE
uses: [0CQHFPGJ45, 02BH3MCBQB, 0QT00PB5G2, 0XPR1E85W0, QQQ9B1DK4P]
sources:
  - url: https://en.wikipedia.org/wiki/Atlas_(topology)
---

## Definition

Let $M$ be a [[topological space|0CQHFPGJ45]] and let $n \ge 0$ be an integer.
A *chart* of dimension $n$ on $M$ is a pair $(U, \varphi)$ with $U \subseteq M$ [[open|02BH3MCBQB]].
The map $\varphi$ must be a [[homeomorphism|0QT00PB5G2]] from $U$ onto an open subset $\varphi(U)$ of [[Euclidean space|0XPR1E85W0]] $\R^n$.
An *atlas* of dimension $n$ on $M$ is a family $\set{(U_i, \varphi_i)}_{i \in I}$ of charts of dimension $n$ on $M$ such that $\bigcup_{i \in I} U_i = M$.

For two charts $(U_i, \varphi_i)$ and $(U_j, \varphi_j)$ of an atlas, the *transition map* is the homeomorphism
$$\varphi_j \circ \varphi_i^{-1} \colon \varphi_i(U_i \cap U_j) \to \varphi_j(U_i \cap U_j)$$
between open subsets of $\R^n$.

## Remarks

On the circle $S^1 \subset \R^2$, let $N = (0, 1)$ and $S = (0, -1)$.
The stereographic projections $\varphi_N(x, y) = x / (1 - y)$ on $S^1 \setminus \set{N}$ and $\varphi_S(x, y) = x / (1 + y)$ on $S^1 \setminus \set{S}$ are homeomorphisms onto $\R$, and their domains cover $S^1$.
So they form an atlas of dimension $1$; the transition map is $t \mapsto 1/t$ on $\R \setminus \set{0}$.

The single chart $S^1 \setminus \set{N}$ is not an atlas of $S^1$, because its domain misses the point $N$.

A Hausdorff, second-countable space has an atlas of dimension $n$ exactly when it is a [[topological manifold|QQQ9B1DK4P]] of dimension $n$.
An atlas is called smooth when all its transition maps are smooth, and piecewise linear when they are piecewise linear.
Two smooth atlases are equivalent when their union is again a smooth atlas, and a smooth structure is an equivalence class of smooth atlases.
In Mathlib, a space with an atlas modelled on a space $H$ is a `ChartedSpace H M`.
