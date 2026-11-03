---
tag: AGCE8EFMTH
kind: definition
name: Edmonds–Karp algorithm
msc: [90C35, 05C21, 05C85]
defines: PFYANWXNJ1
uses: [ZSNXTW5E2K, EXMR7RYRTP, 9P19SEYN1R, 52XF4HS0X3, 9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm
---

## Definition

Let $N = (V, A, c, s, t)$ be a [[flow network|ZSNXTW5E2K]], and let $f$ be an $s$–$t$ flow in $N$.
The *residual network* $N_f$ has vertex set $V$ and these edges with residual capacities:

1. For each edge $a = (u, v) \in A$ with $f(a) < c(a)$, a forward edge $(u, v)$ of residual capacity $c(a) - f(a)$.
2. For each edge $a = (u, v) \in A$ with $f(a) > 0$, a backward edge $(v, u)$ of residual capacity $f(a)$.

An *augmenting path* is a directed path from $s$ to $t$ in $N_f$.
The *Edmonds–Karp algorithm* is the following [[algorithm|9DMSG5HAQX]] for the [[maximum flow problem|EXMR7RYRTP]].

1. Start with $f = 0$.
2. Find, by [[breadth-first search|52XF4HS0X3]] from $s$ in $N_f$, an augmenting path $P$ with the fewest edges. If there is none, return $f$.
3. Let $\delta$ be the least residual capacity of an edge of $P$.
4. For each forward edge of $P$, add $\delta$ to $f$ on the corresponding edge of $A$. For each backward edge of $P$, subtract $\delta$ there. Go back to step 2.

## Remarks

This is the [[Ford–Fulkerson method|9P19SEYN1R]] with the rule of shortest augmenting paths.
For all capacities, real or integer, it stops after at most $\abs{V} \abs{A} / 2$ augmentations and returns a maximum flow.
Each breadth-first search takes $O(\abs{A})$ steps, so the total running time is $O(\abs{V} \abs{A}^2)$.

Example: let the edges be $s a$, $a t$, $s t$ with capacities $2$, $3$, $1$.
The first search finds $s, t$ with one edge, and $\delta = 1$.
The next finds $s, a, t$, and $\delta = 2$.
No augmenting path remains, and the flow of value $3$ is maximum.

Non-example: the Ford–Fulkerson method that chooses augmenting paths by depth-first search, without the shortest path rule, is not the Edmonds–Karp algorithm.
With an unlucky choice of augmenting paths, the Ford–Fulkerson method does not stop on some networks with irrational capacities.
With integer capacities it can need as many augmentations as the maximum flow value.
