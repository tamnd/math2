---
tag: 2B9QWY4APJ
kind: problem
name: Transportation problem
msc: [90C08, 90B06, 90C05]
uses: [VNMXB0J2KA, VSD67A49XC, 0ZVQKTRKVQ]
about: [VNMXB0J2KA]
sources:
  - url: https://en.wikipedia.org/wiki/Transportation_theory_(mathematics)
history:
  posed_by: "Frank L. Hitchcock"
  first_stated: "1941"
---

## Problem

Let $m, n \ge 1$ be integers.
Let $s_1, \dots, s_m \ge 0$ be supplies at $m$ sources and $r_1, \dots, r_n \ge 0$ be demands at $n$ destinations, with $\sum_{i} s_i = \sum_{j} r_j$.
Let $c_{ij} \in \R$ be the cost of shipping one unit from source $i$ to destination $j$.
Find real numbers $x_{ij}$, for $1 \le i \le m$ and $1 \le j \le n$, that
$$\text{minimize } \sum_{i=1}^m \sum_{j=1}^n c_{ij} x_{ij}$$
subject to
$$\sum_{j=1}^n x_{ij} = s_i \ (1 \le i \le m), \qquad \sum_{i=1}^m x_{ij} = r_j \ (1 \le j \le n), \qquad x_{ij} \ge 0.$$

## Remarks

The problem is a [[linear program|VNMXB0J2KA]], and it always has an optimal solution.
It is feasible: if $D = \sum_i s_i > 0$, then $x_{ij} = s_i r_j / D$ satisfies all constraints, and if $D = 0$ then $x = 0$ does.
The feasible region is bounded, since $0 \le x_{ij} \le s_i$, so the minimum is attained.
The constraint matrix is the incidence matrix of the complete [[bipartite graph|0ZVQKTRKVQ]] $K_{m,n}$, which is [[totally unimodular|VSD67A49XC]].
Hence, when all $s_i$ and $r_j$ are integers, there is an optimal solution with all $x_{ij}$ integers.
The case $m = n$ with all $s_i = r_j = 1$ is the [[assignment problem|K65YS73SBW]].
The problem is the finite case of the Kantorovich problem in [[optimal transport|K8EBASR5VG]], with measures supported on finitely many points.
Unbalanced versions, with $\sum_i s_i > \sum_j r_j$, reduce to this one by adding a dummy destination with zero costs.
Special methods include the northwest corner rule for a starting basic solution and the transportation form of the [[simplex algorithm|MH272QHWPM]].

## Explanations

### L1 human

Several factories hold stocks of a product, and several shops need given amounts of it.
Shipping one item from a factory to a shop has a known cost.
The transportation problem asks how many items to send along each route.
Every shop must get what it needs, every factory must send what it has, and the total cost must be as small as possible.
It is one of the first problems solved by linear programming, and its special structure makes whole-number answers come for free.
