---
tag: JJN72VZCZE
kind: definition
name: k-vertex-connected graph
msc: [05C40]
defines: 7FZB7YYBXA
uses: [0JD5C82QMB, 0FFAYNMAJZ, 0V05FC4GKQ]
sources:
  - url: https://en.wikipedia.org/wiki/Vertex_connectivity
---

## Definition

Let $k$ be a positive integer and let $G = (V, E)$ be a finite [[graph|0JD5C82QMB]].
The graph $G$ is $k$-vertex-connected, or $k$-connected, if:

1. $V$ has more than $k$ elements.
2. For each set $X \subseteq V$ with fewer than $k$ elements, the [[induced subgraph|0V05FC4GKQ]] $G - X$ on $V \setminus X$ is [[connected|0FFAYNMAJZ]].

The vertex connectivity $\kappa(G)$ is the largest integer $k$ such that $G$ is $k$-connected, and $\kappa(G) = 0$ if there is no such $k$.

## Remarks

A graph is $1$-connected if and only if it is connected and has at least $2$ vertices.
A $k$-connected graph is also $j$-connected for each $j \le k$.
Example: the [[cycle graph|0QQ0F12962]] $C_n$ with $n \ge 3$ is $2$-connected: it has $n > 2$ vertices, and removing one vertex leaves a path, which is connected.
It is not $3$-connected, since removing two non-adjacent vertices disconnects it when $n \ge 4$, and $C_3$ has only $3$ vertices.
Non-example: a [[tree|0MJ0JS72DZ]] with at least $3$ vertices is not $2$-connected, because removing a vertex that is not a leaf disconnects it.
The [[complete graph|03WKB2H474]] $K_n$ has $\kappa(K_n) = n - 1$; clause 1 is what prevents it from being $n$-connected.
Every $k$-connected graph has minimum degree at least $k$.
