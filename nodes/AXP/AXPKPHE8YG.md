---
tag: AXPKPHE8YG
kind: definition
name: Wiener index
msc: [05C09, 05C92, 05C12]
defines: TBWVJXMM45
uses: [0KWFFMDF8T, 0QV9VNNB4Z, AE724Y8CQX]
sources:
  - url: https://en.wikipedia.org/wiki/Wiener_index
---

## Definition

Let $G$ be a finite [[connected graph|0KWFFMDF8T]] with vertex set $V$, and let $d(u, v)$ be the [[distance|0QV9VNNB4Z]] between vertices $u$ and $v$.
The *Wiener index* of $G$ is
$$W(G) = \sum_{\set{u, v} \subseteq V,\ u \ne v} d(u, v) = \frac{1}{2} \sum_{u \in V} \sum_{v \in V} d(u, v).$$

## Remarks

Example: take the path $P_4$ with vertices $1, 2, 3, 4$ in a row.
The three adjacent pairs have distance $1$, the pairs $\set{1,3}, \set{2,4}$ have distance $2$, and $\set{1,4}$ has distance $3$, so $W(P_4) = 10$.
For the star $K_{1,3}$, the three pairs centre–leaf have distance $1$ and the three pairs of leaves have distance $2$, so $W(K_{1,3}) = 9$.
In general $W(P_n) = \binom{n+1}{3}$.
Non-example: for a graph that is not connected, some distance is infinite, so the sum is not a finite number and the definition does not apply.
For a tree $T$, $W(T) = \sum_{e} n_1(e)\, n_2(e)$, where the sum is over the edges.
Here $n_1(e), n_2(e)$ are the numbers of vertices of the two components of $T - e$.
The formula holds because each pair of vertices is counted once for each edge on the path between them.
Among trees on $n$ vertices, the star has the smallest Wiener index and the path the largest.
The Wiener index is a [[topological index|AE724Y8CQX]], since isomorphisms preserve distances.
