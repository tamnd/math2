---
tag: KT9WJFRQ3F
kind: problem
name: Zarankiewicz problem
msc: [05C35, 05D99]
uses: [0ZVQKTRKVQ, 0V0GC7BQAN, DRGS5TT784]
about: [SC5QB5F4TE, 0ZVQKTRKVQ]
sources:
  - url: https://en.wikipedia.org/wiki/Zarankiewicz_problem
same_as:
  wikidata: Q8066611
  wikipedia: Zarankiewicz problem
history:
  posed_by: "Kazimierz Zarankiewicz"
  first_stated: "1951"
---

## Problem

Let $m, n, s, t$ be positive integers with $s \le m$ and $t \le n$.
Call an $m \times n$ matrix with entries in $\set{0, 1}$ *$(s, t)$-free* if no $s$ rows and $t$ columns cross only in entries equal to $1$.
Let $z(m, n; s, t)$ be the largest number of entries equal to $1$ in an $(s, t)$-free $m \times n$ matrix.
Determine $z(m, n; s, t)$, or its order of growth.

## Remarks

Equivalently, consider [[bipartite graphs|0ZVQKTRKVQ]] with parts $A$ and $B$ of sizes $m$ and $n$.
Then $z(m, n; s, t)$ is the largest number of edges of such a graph with no [[complete bipartite|0V0GC7BQAN]] subgraph $K_{s,t}$ that has $s$ vertices in $A$ and $t$ in $B$.
It is closely tied to the [[extremal number|DRGS5TT784]] $\mathrm{ex}(n, K_{s,t})$.

The Kővári–Sós–Turán theorem gives the upper bound $z(n, n; t, t) = O(n^{2 - 1/t})$ for fixed $t$.
For $s = t = 2$ the order $n^{3/2}$ is correct.
If $q$ is a prime power and $n = q^2 + q + 1$, then $z(n, n; 2, 2) = (q + 1)(q^2 + q + 1)$, and the incidence matrix of a [[finite projective plane|2HWB7P1DZN]] of order $q$ attains this value.
The order $n^{2 - 1/t}$ is also known to be correct for $t = 3$ and, for $z(n, n; s, t)$, when $s$ is large enough compared with $t$, by algebraic constructions called norm graphs.
In general the problem is open; for example, the order of growth of $z(n, n; 4, 4)$ is not known.

## Explanations

### L1 human

Fill a square grid with as many ones as you can, but never let $s$ rows and $t$ columns cross in ones only.
How many ones can you place?
For $2$ rows and $2$ columns the forbidden pattern is a rectangle with ones at its four corners, and the answer grows like $n^{3/2}$.
For larger forbidden blocks the exact growth rate is one of the main open questions of extremal graph theory.
