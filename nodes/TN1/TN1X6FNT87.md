---
tag: TN1X6FNT87
kind: definition
name: Neighborly polytope
msc: [52B05, 52B11, 52B12]
defines: 9V4PR1RVXW
uses: [300K6CB1KH, R7V3S9V891, KY7SB854VH]
sources:
  - url: https://en.wikipedia.org/wiki/Neighborly_polytope
---

## Definition

Let $P$ be a [[convex polytope|300K6CB1KH]] of dimension $d$, and let $k \ge 1$ be an integer.
$P$ is *$k$-neighborly* if for every set $S$ of $k$ [[vertices|R7V3S9V891]] of $P$, the convex hull of $S$ is a [[face|KY7SB854VH]] of $P$.
$P$ is *neighborly* if it is $\floor{d/2}$-neighborly.

## Remarks

Every polytope is $1$-neighborly, so in dimensions $2$ and $3$ every polytope is neighborly.
A $2$-neighborly polytope is one whose graph is complete: every two vertices are joined by an edge.
If $P$ is $k$-neighborly for some $k > \floor{d/2}$, then $P$ is a simplex.

Example: the cyclic polytope $C(n, 4)$ for $n \ge 5$ is $2$-neighborly.
For $i < j$, write $p(t) = (t - t_i)^2 (t - t_j)^2 = a_0 + a_1 t + \dots + a_4 t^4$.
The affine function $\ell(y) = a_0 + a_1 y_1 + \dots + a_4 y_4$ satisfies $\ell(x(t)) = p(t) \ge 0$.
It vanishes only at the vertices with parameters $t_i$ and $t_j$, so these two vertices span an edge.

Non-example: the $4$-cube $[0,1]^4$ is not neighborly, since the opposite vertices $0$ and $(1,1,1,1)$ are not joined by an edge.
