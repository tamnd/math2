---
tag: H8QQ146ADS
kind: definition
name: Ford–Fulkerson algorithm
msc: [05C21, 90C35, 05C85]
defines: 9P19SEYN1R
uses: [0KFYGSHHF5, 03NAMV1DHJ, 9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
---

## Definition

Let $V$ be a finite set with distinct vertices $s, t \in V$, and let $c \colon V \times V \to [0, \infty)$ be a capacity function.
This data is a flow network, where $(u, v)$ is an edge of the underlying [[directed graph|0KFYGSHHF5]] when $c(u, v) > 0$.
A *flow* is a map $f \colon V \times V \to \R$ with these properties:

1. $f(u, v) = -f(v, u)$ for all $u, v$.
2. $f(u, v) \le c(u, v)$ for all $u, v$.
3. $\sum_{v \in V} f(u, v) = 0$ for every $u \notin \set{s, t}$.

Its value is $\sum_{v \in V} f(s, v)$.
The *residual capacity* of $f$ is $c_f(u, v) = c(u, v) - f(u, v)$.
An *augmenting path* for $f$ is a directed [[path|03NAMV1DHJ]] from $s$ to $t$ all of whose steps $(u, v)$ have $c_f(u, v) > 0$.

The *Ford–Fulkerson algorithm* is the following [[algorithm|9DMSG5HAQX]].

1. Start with $f = 0$.
2. While an augmenting path $P$ for $f$ exists, let $\delta$ be the least residual capacity $c_f(u, v)$ over the steps $(u, v)$ of $P$.
3. For each step $(u, v)$ of $P$, increase $f(u, v)$ by $\delta$ and decrease $f(v, u)$ by $\delta$.

When no augmenting path exists, it returns $f$.

## Remarks

Example: let $V = \set{s, a, t}$ with $c(s, a) = 2$, $c(a, t) = 3$, $c(s, t) = 1$, and capacity $0$ on all other pairs.
The paths $s \to a \to t$ with $\delta = 2$ and $s \to t$ with $\delta = 1$ give a flow of value $3$.
No augmenting path is left, and the cut $\set{s}$ against $\set{a, t}$ has capacity $2 + 1 = 3$, so the flow is maximum.

If all capacities are integers, each augmentation raises the value by at least $1$, so the algorithm stops after at most $f^*$ augmentations, where $f^*$ is the maximum value.
The returned flow is then maximum and integer-valued.

Non-example of termination: with irrational capacities and a poor choice of augmenting paths, the algorithm may run forever, and its values may even converge to less than the maximum.
Choosing a shortest augmenting path each time, found by [[breadth-first search|52XF4HS0X3]], gives the Edmonds–Karp algorithm, which always stops after $O(\abs{V} \cdot m)$ augmentations, where $m$ is the number of edges.
