---
tag: HNT4AFDM1W
kind: definition
name: Network simplex algorithm
msc: [90C35, 90C49, 90C05]
defines: 7NT7MRVZSQ
uses: [899795HN7H, 0S4ZEZM7KE, 0Z05VCBQ7Y, MH272QHWPM]
sources:
  - url: https://en.wikipedia.org/wiki/Network_simplex_algorithm
---

## Definition

Consider an instance of the [[minimum-cost flow problem|899795HN7H]] on a finite directed graph $(V, E)$ whose underlying undirected graph is connected.
Each edge $e = (v, w)$ has a capacity $u_e \in (0, \infty]$ and a cost $a_e \in \R$, and each vertex $v$ has a supply $b_v$, with $\sum_v b_v = 0$.
A *spanning tree structure* is a partition $E = T \cup L \cup U$ such that:

1. $T$ is a [[spanning tree|0S4ZEZM7KE]] of the underlying undirected graph.
2. Every edge of $U$ has finite capacity.

Its *tree solution* is the unique $f$ with $f_e = 0$ on $L$, $f_e = u_e$ on $U$, and flow conservation with supplies $b$ at every vertex.
The structure is *feasible* if $0 \le f_e \le u_e$ also holds on $T$.
*Potentials* are numbers $\pi_v$ with $a_e - \pi_v + \pi_w = 0$ for every tree edge $e = (v, w)$; the *reduced cost* of an edge is $\bar a_e = a_e - \pi_v + \pi_w$.

The *network simplex algorithm* starts from a feasible spanning tree structure and repeats these steps:

1. Compute the potentials from the tree.
2. If every edge of $L$ has $\bar a_e \ge 0$ and every edge of $U$ has $\bar a_e \le 0$, stop: the tree solution is optimal.
3. Otherwise choose an entering edge $e$ in $L$ with $\bar a_e < 0$ or in $U$ with $\bar a_e > 0$.
4. Send as much flow as the capacities allow around the unique [[cycle|0Z05VCBQ7Y]] of $T \cup \set{e}$, in the direction that lowers the cost.
5. Remove from $T$ an edge of the cycle that became empty or full, put it in $L$ or $U$, and add $e$ to $T$.

## Remarks

Tree solutions are exactly the basic solutions of the linear program, and a pivot of step 4 is a [[simplex|MH272QHWPM]] pivot.
The stopping test is the complementary slackness condition, so the final flow is optimal.
With a rule against cycling, such as keeping strongly feasible trees, the algorithm is finite.
A first feasible structure can be found by adding an artificial root vertex joined to all vertices by edges of high cost.

Example: let $V = \set{x, y, z}$, $b_x = 1$, $b_z = -1$, $b_y = 0$, with edges $(x, z)$ of cost $5$ and $(x, y)$, $(y, z)$ of cost $1$, all of capacity $2$.
Take $T = \set{(x, z), (x, y)}$, $L = \set{(y, z)}$, with flow $1$ on $(x, z)$.
With $\pi_x = 0$ one gets $\pi_z = -5$ and $\pi_y = -1$, so $\bar a_{(y, z)} = 1 - (-1) + (-5) = -3 < 0$.
Pushing one unit around the cycle moves the flow to the path $x \to y \to z$ of cost $2$, which is optimal.

Non-example: in the same graph, $T = \set{(x, y), (y, z), (x, z)}$ is not a spanning tree structure, since $T$ contains a cycle and clause 1 fails.
