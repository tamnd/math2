---
tag: 7ZPS42F2TE
kind: statement
role: proposition
name: Augmenting along a path raises the flow value by delta
msc: [05C21, 90B10, 90C35]
uses: [0R5HTV7REV]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_networkflow_augmenting.ptx#L45
    locator: source/s_networkflow_augmenting.ptx:45
---

## Statement

Let $D = (V, E)$ be a finite [[directed graph|0R5HTV7REV]] with a source $s$, a sink $t$ and a capacity function $c$ on the edges. Let $\phi$ be a flow of value $v$ on this network. A flow obeys $0 \le \phi(e) \le c(e)$ on each edge, and it is conserved at each vertex other than $s$ and $t$.

Let $P = (x_0, x_1, \dots, x_m)$ be an augmenting path from $s$ to $t$. Each step of $P$ uses an edge of $D$ either forwards or backwards. A forward edge has spare capacity $c(e) - \phi(e) > 0$. A backward edge carries positive flow $\phi(e) > 0$. Let $\delta > 0$ be the smallest of the spare capacities of the forward edges and the flows of the backward edges on $P$.

Define a new function $\hat\phi$ as follows. Add $\delta$ to $\phi$ on each forward edge of $P$. Subtract $\delta$ from $\phi$ on each backward edge of $P$. Leave $\phi$ unchanged on all other edges.

Then $\hat\phi$ is a flow on the network, and its value is $v + \delta$.

## Remarks

The choice of $\delta$ keeps every edge value between $0$ and its capacity. At each inner vertex of $P$ the two changes cancel, so conservation still holds. At $s$ the net outflow grows by exactly $\delta$.
