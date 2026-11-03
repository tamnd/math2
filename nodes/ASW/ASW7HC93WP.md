---
tag: ASW7HC93WP
kind: definition
name: Dijkstra's algorithm
msc: [05C85, 68R10, 90C35]
defines: VZZMASEEC8
uses: [9DMSG5HAQX, 0KFYGSHHF5, 03NAMV1DHJ, 0QV9VNNB4Z]
sources:
  - url: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
---

## Definition

Let $G = (V, E)$ be a finite [[directed graph|0KFYGSHHF5]] with edge weights $w \colon E \to [0, \infty)$, and let $s \in V$.
The length of a [[path|03NAMV1DHJ]] is the sum of the weights of its edges.
Let $\delta(v)$ be the least length of a path from $s$ to $v$, or $\infty$ if there is none.
*Dijkstra's algorithm* is the [[algorithm|9DMSG5HAQX]] that maintains a set $S$ of settled vertices and tentative distances $d \colon V \to [0, \infty]$:

1. set $d(s) = 0$, $d(v) = \infty$ for $v \ne s$, and $S = \emptyset$;
2. while $S \ne V$, choose $u \in V \setminus S$ with $d(u)$ minimal and add $u$ to $S$;
3. for each edge $(u, v) \in E$ with $v \notin S$, set $d(v) = \min\big(d(v),\ d(u) + w(u, v)\big)$;
4. return to step 2.

## Remarks

When the algorithm stops, $d(v) = \delta(v)$ for every $v \in V$.
The proof shows by induction that $d(u) = \delta(u)$ at the moment $u$ is added to $S$.
Otherwise, take a shortest path from $s$ to $u$ and its first vertex $y$ outside $S$.
Its predecessor on the path is in $S$ and was relaxed, so $d(y) = \delta(y) \le \delta(u) < d(u)$, which contradicts the choice of $u$.
The middle inequality uses $w \ge 0$.
An undirected graph is handled by replacing each edge by two opposite arcs of the same weight.

Example: take arcs $s \to a$ of weight $4$, $s \to b$ of weight $1$ and $b \to a$ of weight $2$.
The algorithm settles $s$, then $b$ with $d(b) = 1$, which lowers $d(a)$ from $4$ to $3$.
Then it settles $a$ with $d(a) = 3 = \delta(a)$.

Non-example: the hypothesis $w \ge 0$ is needed.
Take arcs $s \to a$ of weight $1$, $s \to b$ of weight $2$ and $b \to a$ of weight $-2$.
The algorithm settles $a$ with $d(a) = 1$ before $b$ and never corrects it, but $\delta(a) = 0$ through $b$.
