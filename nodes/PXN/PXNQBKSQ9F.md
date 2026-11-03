---
tag: PXNQBKSQ9F
kind: definition
name: Floyd–Warshall algorithm
msc: [05C85, 90C35, 68W40]
defines: H8T4X0KXE1
uses: [0KFYGSHHF5, 03NAMV1DHJ, 0Z05VCBQ7Y, 9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
---

## Definition

Let $G$ be a finite [[directed graph|0KFYGSHHF5]] with vertex set $\set{1, \dots, n}$ and edge weights $w(i, j) \in \R$.
Assume that $G$ has no [[cycle|0Z05VCBQ7Y]] of negative total weight.
The *Floyd–Warshall algorithm* is the [[algorithm|9DMSG5HAQX]] that computes numbers $d_k(i, j)$ for $k = 0, 1, \dots, n$ as follows.

1. $d_0(i, i) = 0$; $d_0(i, j) = w(i, j)$ if $i \ne j$ and $(i, j)$ is an edge; and $d_0(i, j) = \infty$ otherwise.
2. For $k \ge 1$, $d_k(i, j) = \min\bigl(d_{k-1}(i, j),\ d_{k-1}(i, k) + d_{k-1}(k, j)\bigr)$.

It returns $d_n(i, j)$ for all pairs $(i, j)$.
Here $d_k(i, j)$ is the least weight of a directed [[path|03NAMV1DHJ]] from $i$ to $j$ whose intermediate vertices all lie in $\set{1, \dots, k}$.
So $d_n(i, j)$ is the shortest path distance from $i$ to $j$.

## Remarks

Example: with edges $1 \to 2$ of weight $3$, $2 \to 3$ of weight $4$ and $1 \to 3$ of weight $10$, one has $d_1(1, 3) = 10$ and $d_2(1, 3) = \min(10, 3 + 4) = 7 = d_3(1, 3)$.

Non-example: if the hypothesis fails, say $G$ has the cycle $1 \to 2 \to 1$ of total weight $-1$, then no shortest walk from $1$ to $2$ exists.
The recurrence still runs, and the negative cycle shows up as $d_n(i, i) < 0$ for a vertex $i$ on it.

The table can be updated in place, so the algorithm needs $O(n^2)$ memory and $O(n^3)$ time.
