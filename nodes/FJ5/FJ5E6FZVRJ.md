---
tag: FJ5E6FZVRJ
kind: definition
name: Treewidth
msc: [05C83, 05C75, 05C85]
defines: CD2XB4Y1SF
uses: [0JD5C82QMB, 0MJ0JS72DZ]
sources:
  - url: https://en.wikipedia.org/wiki/Treewidth
---

## Definition

Let $G = (V, E)$ be a finite [[graph|0JD5C82QMB]].
A tree decomposition of $G$ is a pair $(T, (X_t)_{t \in V(T)})$ with the following properties.
Here $T$ is a [[tree|0MJ0JS72DZ]], and each $X_t$ is a subset of $V$, called a bag.

1. Every vertex of $G$ lies in some bag.
2. For every edge $uv$ of $G$, some bag contains both $u$ and $v$.
3. For every vertex $v$ of $G$, the nodes $t$ with $v \in X_t$ form a connected subtree of $T$.

The width of the decomposition is $\max_t \abs{X_t} - 1$.
The treewidth $\operatorname{tw}(G)$ is the least width of a tree decomposition of $G$.

## Remarks

Example: the cycle $C_4$ with vertices $1, 2, 3, 4$ in order has the tree decomposition with two adjacent nodes and bags $\set{1, 2, 3}$ and $\set{1, 3, 4}$.
Each vertex is in a bag, each edge lies in a bag, and the nodes containing $1$ or $3$ form the whole tree, so the width is $2$.
Non-example: put the bags $\set{1, 2}, \set{2, 3}, \set{3, 4}, \set{4, 1}$ in this order along a path.
They satisfy clauses 1 and 2 but fail clause 3, because vertex $1$ lies in the first and last bags only.
Every clique of $G$ lies in a single bag, so $\operatorname{tw}(K_n) = n - 1$.
A graph with at least one edge has treewidth $1$ exactly when it is a forest, and the $k \times k$ grid with $k \ge 2$ has treewidth $k$.
