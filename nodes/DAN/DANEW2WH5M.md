---
tag: DANEW2WH5M
kind: definition
name: Breadth-first search
msc: [05C85, 68R10]
defines: 52XF4HS0X3
uses: [9DMSG5HAQX, 00C0BR7D7H, 0KFYGSHHF5, 0QV9VNNB4Z]
sources:
  - url: https://en.wikipedia.org/wiki/Breadth-first_search
---

## Definition

Let $G = (V, E)$ be a finite [[graph|00C0BR7D7H]] or [[directed graph|0KFYGSHHF5]], given by adjacency lists, and let $s \in V$.
*Breadth-first search* from $s$ is the [[algorithm|9DMSG5HAQX]] that computes $d \colon V \to \N \cup \set{\infty}$ and a parent map $\pi$ as follows:

1. set $d(s) = 0$ and $d(v) = \infty$ for $v \ne s$, and let $Q$ be a first-in first-out queue containing only $s$;
2. while $Q$ is nonempty, remove the first vertex $u$ of $Q$ and scan the neighbours (out-neighbours) of $u$;
3. for each scanned $v$ with $d(v) = \infty$, set $d(v) = d(u) + 1$, set $\pi(v) = u$ and append $v$ to $Q$; then go back to step 2.

## Remarks

Each vertex enters $Q$ at most once and each adjacency list is scanned once, so the running time is $O(\abs{V} + \abs{E})$.
At the end, $d(v)$ is the [[distance|0QV9VNNB4Z]] from $s$ to $v$, the least number of edges of a path from $s$ to $v$.
In particular $d(v) = \infty$ exactly when $v$ is not reachable from $s$.
The parent pointers form a tree of shortest paths rooted at $s$.
The key fact is that the vertices leave $Q$ in nondecreasing order of $d$.

Example: on the cycle with vertices $1, 2, 3, 4, 5$ and edges $\set{i, i+1}$ and $\set{5, 1}$, BFS from $1$ gives $d = (0, 1, 2, 2, 1)$.

Non-example: replacing the queue by a stack, so that the last vertex added is removed first, does not compute distances in general.
On the same cycle, scan neighbours in increasing order.
The stack pops $5$ and then $4$, so vertex $3$ is first reached from $4$ and gets the value $3$ instead of $2$.
