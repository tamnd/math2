---
tag: 4HMR4KQ01T
kind: statement
role: theorem
name: Max-flow min-cut theorem
msc: [05C21, 90B10, 90C35]
uses: [0R5HTV7REV]
sources:
  - url: https://en.wikipedia.org/wiki/Max-flow_min-cut_theorem
same_as:
  wikidata: Q608294
  wikipedia: Max-flow min-cut theorem
---

## Statement

Let $D = (V, E)$ be a finite [[directed graph|0R5HTV7REV]] with distinct vertices $s$ (the source) and $t$ (the sink), and let $c \colon E \to [0, \infty)$ be a capacity function.
A flow is a function $f \colon E \to \R$ such that:

1. $0 \le f(e) \le c(e)$ for every edge $e$.
2. For every vertex $w \ne s, t$, the total of $f$ on edges entering $w$ equals the total of $f$ on edges leaving $w$.

The value of $f$ is the total of $f$ on edges leaving $s$ minus the total of $f$ on edges entering $s$.
An $s$–$t$ cut is a partition $V = S \cup T$ with $s \in S$ and $t \in T$.
Its capacity is the sum of $c(e)$ over the edges $e$ from a vertex of $S$ to a vertex of $T$.
Then the maximum value of a flow exists and equals the minimum capacity of an $s$–$t$ cut.

## Remarks

Let $f$ be a flow and $(S, T)$ a cut.
The value of $f$ equals the flow from $S$ to $T$ minus the flow back, so it is at most the capacity of the cut.
For the reverse inequality, take a flow of maximum value and let $S$ be the set of vertices reachable from $s$ by an augmenting path.
Then $t \notin S$, every edge out of $S$ is full and every edge into $S$ carries no flow, so the cut $(S, V \setminus S)$ has capacity equal to the value.
The Ford–Fulkerson method pushes flow along augmenting paths, one at a time.
When all capacities are integers, it stops after finitely many steps with a maximum flow.
If all capacities are integers, there is a maximum flow with integer values on all edges.
This integrality gives [[Menger's theorem|E6GYGZDBS7]] and [[Kőnig's theorem|0JP0ZF57PN]] as special cases.
The theorem is also an instance of linear programming duality.

## Explanations

### L1 human

Think of pipes from a source to a sink, each with a maximum rate.
The most water you can send through equals the smallest total rate of a set of pipes whose removal cuts the sink off from the source.
The bottleneck of the network decides the throughput.

### L2 human

The theorem is the central result about flow networks.
Its proof gives an algorithm and a certificate: a maximum flow and a minimum cut prove each other optimal.
Many combinatorial min-max theorems, such as Menger's theorem, Kőnig's theorem and [[Hall's marriage theorem|08WCB90WND]], follow by building a suitable network with capacities $0$ and $1$.
