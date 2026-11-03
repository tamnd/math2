---
tag: YK3AHP1SSS
kind: definition
name: Bellman–Ford algorithm
msc: [05C85, 90C35, 68W40]
defines: 8AH0QN3D7Y
uses: [0KFYGSHHF5, 03NAMV1DHJ, 0Z05VCBQ7Y, 9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm
---

## Definition

Let $G = (V, E)$ be a finite [[directed graph|0KFYGSHHF5]] with $n$ vertices, let $w \colon E \to \R$ be a weight function, and let $s \in V$ be a source vertex.
The *Bellman–Ford algorithm* is the following [[algorithm|9DMSG5HAQX]].

1. Set $d(s) = 0$ and $d(v) = \infty$ for every vertex $v \ne s$.
2. Repeat $n - 1$ times: for each edge $(u, v) \in E$, if $d(u) + w(u, v) < d(v)$, set $d(v) = d(u) + w(u, v)$; this step is called a *relaxation* of the edge.
3. Then, for each edge $(u, v) \in E$, if $d(u) + w(u, v) < d(v)$, report that a [[cycle|0Z05VCBQ7Y]] of negative total weight is reachable from $s$.

If no such cycle is reported, the output $d(v)$ is the least total weight of a directed [[path|03NAMV1DHJ]] from $s$ to $v$.
In that case $d(v) = \infty$ exactly when no path from $s$ to $v$ exists.

## Remarks

Example: take $V = \set{s, a, b}$ with $w(s, a) = 4$, $w(s, b) = 1$ and $w(b, a) = -2$.
After the first round, if the edges are scanned in the order $(s, a), (s, b), (b, a)$, one has $d(s) = 0$, $d(b) = 1$ and $d(a) = -1$.
The check in step 3 reports nothing, so the shortest distance from $s$ to $a$ is $-1$.

Non-example of the conclusion: if the edges $a \to b$ of weight $1$ and $b \to a$ of weight $-2$ form a cycle reachable from $s$, the cycle has weight $-1$.
Going around it lowers the weight without bound, so no shortest walk exists, and step 3 reports the cycle.

The correctness rests on the fact that after $k$ rounds, $d(v)$ is at most the least weight of a walk from $s$ to $v$ with at most $k$ edges.
The running time is $O(nm)$, where $m = \abs{E}$.
