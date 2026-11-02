---
tag: A9A7S5AYY1
kind: definition
name: Order polytope
msc: [06A07, 52B05, 52B20]
defines: N587ECTQ4X
uses: [0QV2JS9RJ3, 0A7KV2WB7A, ETCE287E2R, W8DZ5KGGHN, VDBDJZWPEA]
sources:
  - url: https://en.wikipedia.org/wiki/Order_polytope
---

## Definition

Let $(P, \le)$ be a finite [[partially ordered set|0QV2JS9RJ3]], and let $\R^P$ be the real vector space of functions $f \colon P \to \R$.
The *order polytope* of $P$ is the set $\mathcal{O}(P)$ of all $f \in \R^P$ such that:

1. $0 \le f(x) \le 1$ for all $x \in P$.
2. $f(x) \le f(y)$ for all $x, y \in P$ with $x \le y$.

## Remarks

Clause 2 says that $f$ is [[order-preserving|0A7KV2WB7A]].
The vertices of $\mathcal{O}(P)$ are the indicator functions of the [[upper sets|ETCE287E2R]] of $P$.
Its volume is $e(P)/p!$, where $p = \abs{P}$ and $e(P)$ is the number of [[linear extensions|W8DZ5KGGHN]].
For an integer $m \ge 1$, the dilate $m \, \mathcal{O}(P)$ has $\Omega(P, m + 1)$ points with integer coordinates, where $\Omega$ is the [[order polynomial|VDBDJZWPEA]].

Example: for the chain $x < y$, $\mathcal{O}(P)$ is the triangle $0 \le f(x) \le f(y) \le 1$.
Check: its vertices $(0, 0)$, $(0, 1)$, $(1, 1)$ are the indicators of the upper sets $\emptyset$, $\set{y}$, $\set{x, y}$, and its area is $1/2 = e(P)/2!$.

Non-example: the point $f(x) = 1$, $f(y) = 0$ satisfies clause 1 but not clause 2, so it is not in $\mathcal{O}(P)$.

For an antichain of $p$ elements, $\mathcal{O}(P)$ is the unit cube $[0, 1]^p$.
