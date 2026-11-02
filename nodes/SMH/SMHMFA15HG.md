---
tag: SMHMFA15HG
kind: definition
name: Comparability graph
msc: [05C75, 06A07, 05C17]
defines: 1P4830BH6Z
uses: [0QV2JS9RJ3, 00C0BR7D7H]
sources:
  - url: https://en.wikipedia.org/wiki/Comparability_graph
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|0QV2JS9RJ3]].
The *comparability graph* of $P$ is the [[graph|00C0BR7D7H]] with vertex set $P$ in which distinct $x, y \in P$ are adjacent if and only if $x \le y$ or $y \le x$.
A graph $G$ is a *comparability graph* if it is isomorphic to the comparability graph of some partially ordered set.

## Remarks

Equivalently, $G$ is a comparability graph when its edges can be oriented so that $x \to y$ and $y \to z$ always imply $x \to z$; such an orientation is called transitive.
Example: the complete bipartite graph $K_{m,n}$ is the comparability graph of the poset with $m$ minimal elements, $n$ maximal elements, and each minimal element below each maximal element.
Non-example: the cycle $C_5$ is not a comparability graph.
Its largest clique has $2$ vertices but it needs $3$ colours, while in a comparability graph the clique number equals the chromatic number, by [[Mirsky's theorem|5VPXR3RDF1]].
The cliques of the comparability graph are the chains of $P$, and its independent sets are the antichains of $P$.
Different partial orders, such as an order and its dual, can have the same comparability graph.
