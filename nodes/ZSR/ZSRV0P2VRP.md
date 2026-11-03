---
tag: ZSRV0P2VRP
kind: definition
name: Hungarian algorithm
msc: [90C27, 05C70, 90B80]
defines: 7DJ7P8RSJN
uses: [K65YS73SBW, 0ZVQKTRKVQ, 0MJ04A50QW, 0NHK9MFFW9, 0JP0ZF57PN]
sources:
  - url: https://en.wikipedia.org/wiki/Hungarian_algorithm
---

## Definition

Let $C = (c_{ij})$ be a real $n \times n$ cost matrix of an [[assignment problem|K65YS73SBW]], with rows $i$ (agents) and columns $j$ (tasks).
*Dual prices* are vectors $u, v \in \R^n$ with $u_i + v_j \le c_{ij}$ for all $i, j$.
For dual prices $u, v$, the *equality graph* is the [[bipartite graph|0ZVQKTRKVQ]] on the rows and columns with an edge $\set{i, j}$ whenever $u_i + v_j = c_{ij}$.
The *Hungarian algorithm* is the following iteration.

1. Start with $u_i = \min_j c_{ij}$ for each $i$ and $v_j = 0$ for each $j$.
2. Find a maximum [[matching|0MJ04A50QW]] $M$ of the equality graph.
3. If $M$ has $n$ edges, stop: $M$ is a minimum-cost [[perfect matching|0NHK9MFFW9]].
4. Otherwise call a path of the equality graph alternating if its edges are alternately outside and inside $M$. Let $S$ be the set of rows and $T$ the set of columns reached by alternating paths from rows not covered by $M$.
5. Put $\delta = \min \set{c_{ij} - u_i - v_j : i \in S, \ j \notin T}$.
6. Replace $u_i$ by $u_i + \delta$ for $i \in S$ and $v_j$ by $v_j - \delta$ for $j \in T$, and go to step 2.

## Remarks

Correctness: the update in step 6 keeps $u_i + v_j \le c_{ij}$ for all $i, j$, and $\delta > 0$ by the choice of $S$ and $T$.
For every perfect matching $\sigma$, $\sum_i c_{i\sigma(i)} \ge \sum_i u_i + \sum_j v_j$.
A perfect matching in the equality graph attains this bound, so it is optimal.
The sets $S$ and $T$ come from [[Kőnig's theorem|0JP0ZF57PN]]: the rows outside $S$ together with the columns in $T$ form a minimum vertex cover of the equality graph.
After each update the matching can be enlarged or $T$ grows, so the algorithm stops; careful implementations use $O(n^3)$ arithmetic operations.

Example: for $C = \begin{pmatrix} 1 & 2 \\ 3 & 5 \end{pmatrix}$, step 1 gives $u = (1, 3)$ and $v = (0, 0)$.
The equality graph has the edges $\set{1, 1}$ and $\set{2, 1}$, so a maximum matching has one edge, say $\set{1, 1}$.
Then $S = \set{1, 2}$, $T = \set{1}$ and $\delta = \min(2 - 1, 5 - 3) = 1$, so $u = (2, 4)$ and $v = (-1, 0)$.
Now $\set{1, 2}$ and $\set{2, 1}$ are tight, and the perfect matching they form has cost $2 + 3 = 5$, equal to $\sum u_i + \sum v_j = 5$.

Non-example: a greedy method that gives each agent in turn its cheapest free task is not the Hungarian algorithm, and it can fail.
On the matrix above it pairs agent $1$ with task $1$ and gets cost $1 + 5 = 6$.
