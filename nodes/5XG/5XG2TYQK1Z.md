---
tag: 5XG2TYQK1Z
kind: definition
name: Dinic's algorithm
msc: [90C35, 05C21, 05C85]
defines: 23ZP0GHKD4
uses: [ZSNXTW5E2K, EXMR7RYRTP, AGCE8EFMTH, PFYANWXNJ1, 52XF4HS0X3, 9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/Dinic%27s_algorithm
---

## Definition

Let $N = (V, A, c, s, t)$ be a [[flow network|ZSNXTW5E2K]], and let $f$ be an $s$–$t$ flow with [[residual network|AGCE8EFMTH]] $N_f$.
For $v \in V$, let $\mathrm{dist}(v)$ be the number of edges of a shortest path from $s$ to $v$ in $N_f$.
The *level graph* $L_f$ is the subgraph of $N_f$ with the edges $(u, v)$ such that $\mathrm{dist}(v) = \mathrm{dist}(u) + 1$.
Give each edge of $L_f$ its residual capacity.
A *blocking flow* in $L_f$ is a flow in $L_f$ that saturates some edge of every path from $s$ to $t$ in $L_f$.
An edge is saturated when its flow equals its capacity.
*Dinic's algorithm* is the following [[algorithm|9DMSG5HAQX]] for the [[maximum flow problem|EXMR7RYRTP]].

1. Start with $f = 0$.
2. Compute $\mathrm{dist}$ and $L_f$ by [[breadth-first search|52XF4HS0X3]] from $s$ in $N_f$. If $t$ is not reachable, return $f$.
3. Find a blocking flow $g$ in $L_f$, by repeated depth-first searches that delete edges leading to dead ends.
4. Add $g$ to $f$: increase $f$ on forward edges and decrease $f$ on backward edges by the values of $g$. Go back to step 2.

## Remarks

After each phase, the distance from $s$ to $t$ in the residual network strictly increases, so there are at most $\abs{V} - 1$ phases.
A blocking flow can be found in $O(\abs{V} \abs{A})$ steps, which gives the bound $O(\abs{V}^2 \abs{A})$.
When all capacities are $1$, there are $O(\sqrt{\abs{A}})$ phases, each of $O(\abs{A})$ steps.

Example: let the edges be $s a$, $a t$, $s t$ with capacities $2$, $3$, $1$.
In the first phase, $\mathrm{dist}(t) = 1$, the level graph keeps $s t$ and $s a$ but not $a t$, and the blocking flow sends $1$ along $s t$.
In the second phase, $\mathrm{dist}(t) = 2$ through $a$, and the blocking flow sends $2$ along $s, a, t$.
Then $t$ is unreachable, and the flow of value $3$ is maximum.

Non-example: the [[Edmonds–Karp algorithm|PFYANWXNJ1]] also augments along shortest paths, but it recomputes the distances after each single path.
It does not work with blocking flows, so it is not Dinic's algorithm.

A blocking flow need not be a maximum flow of the level graph.
Take edges $s a$, $s b$, $a c$, $a d$, $b c$, $c t$, $d t$, all of capacity $1$; for $f = 0$ every edge goes one level forward.
The flow of value $1$ along $s, a, c, t$ is blocking, since $s a$ and $c t$ are full.
It is not maximum, because the paths $s, a, d, t$ and $s, b, c, t$ carry a flow of value $2$.
So step 3 asks for less than a maximum flow, and later phases correct the difference.
