---
tag: WZ4JGTG6ZD
kind: definition
name: Girth
msc: [05C38]
defines: D13K9GJT0B
uses: [0JD5C82QMB, 07CT9RDY7Q, 0XNN9Z8E5A]
sources:
  - url: https://en.wikipedia.org/wiki/Girth_(graph_theory)
---

## Definition

Let $G$ be a [[graph|0JD5C82QMB]].
If $G$ contains a [[cycle|07CT9RDY7Q]], the girth of $G$ is the smallest length of a cycle in $G$.
If $G$ contains no cycle, that is, if $G$ is [[acyclic|0XNN9Z8E5A]], the girth of $G$ is $\infty$.

## Remarks

In a simple graph each cycle has length at least $3$, so the girth is at least $3$.
Example: the [[cycle graph|0QQ0F12962]] $C_n$ with $n \ge 3$ has girth $n$, since its only cycle has length $n$.
The [[complete graph|03WKB2H474]] $K_n$ with $n \ge 3$ has girth $3$, and the [[complete bipartite graph|0V0GC7BQAN]] $K_{m,n}$ with $m, n \ge 2$ has girth $4$, since a [[bipartite graph|07DVHJ8N0A]] has no odd cycle.
The [[Petersen graph|0NR95CTFCZ]] has girth $5$.
Non-example: in the path graph $u - v - w$, the closed walk $u, v, u$ has length $2$ but is not a cycle, because it uses the edge $uv$ twice.
The path graph has no cycle, so its girth is $\infty$.
Every [[tree|0MJ0JS72DZ]] has girth $\infty$.
The girth is sometimes written $g(G)$.
