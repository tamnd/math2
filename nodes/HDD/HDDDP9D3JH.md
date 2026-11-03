---
tag: HDDDP9D3JH
kind: definition
name: Depth-first search
msc: [05C85, 68R10]
defines: 4TE2X7N728
uses: [9DMSG5HAQX, 00C0BR7D7H, 0KFYGSHHF5, 0FDKRX9M9Y]
sources:
  - url: https://en.wikipedia.org/wiki/Depth-first_search
---

## Definition

Let $G = (V, E)$ be a finite [[graph|00C0BR7D7H]] or [[directed graph|0KFYGSHHF5]], given by adjacency lists, and let $s \in V$.
*Depth-first search* from $s$ is the [[algorithm|9DMSG5HAQX]] that marks all vertices unvisited and calls the procedure $\mathrm{visit}(s)$, where $\mathrm{visit}(u)$ does the following:

1. mark $u$ visited and record its discovery time;
2. for each neighbour (out-neighbour) $v$ of $u$, in the order of the adjacency list, if $v$ is unvisited, set $\pi(v) = u$ and call $\mathrm{visit}(v)$;
3. record the finishing time of $u$.

Times are taken from a single counter that increases by $1$ at each recording.

## Remarks

Each vertex is visited once and each adjacency list is scanned once, so the running time is $O(\abs{V} + \abs{E})$.
The visited vertices are exactly those [[reachable|0FDKRX9M9Y]] from $s$, and the edges $(\pi(v), v)$ form a rooted tree, the DFS tree.
In an undirected graph, every edge joins a vertex to one of its ancestors or descendants in the DFS tree; there are no cross edges.
The intervals [discovery time, finishing time] of any two vertices are either disjoint or nested.
In a directed acyclic graph, listing the vertices by decreasing finishing time gives a topological order.

Example: on the path $1 - 2 - 3$ with the extra edge $\set{1, 3}$, DFS from $1$ visits $2$ and then $3$, and the edge $\set{1, 3}$ joins $3$ to its ancestor $1$.

Non-example: a procedure that, in step 2, also calls $\mathrm{visit}(v)$ on already visited $v$ is not DFS.
On any graph with an edge $\set{u, v}$ it calls $\mathrm{visit}(u)$ and $\mathrm{visit}(v)$ on each other forever.
