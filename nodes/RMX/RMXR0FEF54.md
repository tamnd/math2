---
tag: RMXR0FEF54
kind: object
name: Rado graph
msc: [05C63, 03C15]
instance_of: [HJVRBDQSGG]
uses: [00C0BR7D7H, 0F7QKGJS6B, TNT3DG0HRJ, 0MWKJ44V5A]
sources:
  - url: https://en.wikipedia.org/wiki/Rado_graph
same_as:
  wikidata: Q7281501
  wikipedia: Rado graph
---

## Description

The Rado graph $R$ has vertex set $\N = \set{0, 1, 2, \dots}$.
For $i < j$, the vertices $i$ and $j$ are adjacent when the binary digit of $j$ at position $i$ is $1$.
Equivalently, $\floor{j / 2^i}$ is odd.

It has the extension property, stated as follows.
For any two disjoint finite sets $U, V \subseteq \N$, some vertex $z \notin U \cup V$ is adjacent to every vertex of $U$ and to no vertex of $V$.
Check: let $N$ be larger than every element of $U \cup V$ and put $z = 2^N + \sum_{u \in U} 2^u$.
Then $z > N$, so $z \notin U \cup V$, and every $w \in U \cup V$ satisfies $w < z$.
The binary digit of $z$ at position $w$ is $1$ if $w \in U$ and $0$ if $w \in V$.
So $z$ is adjacent to every vertex of $U$ and to no vertex of $V$.

## Remarks

Any two countable [[graphs|00C0BR7D7H]] with the extension property are [[isomorphic|0F7QKGJS6B]], by a back-and-forth argument.
So the Rado graph is the [[Fraïssé limit|HJVRBDQSGG]] of the class of finite graphs.
Every finite graph is an induced subgraph of it, and every isomorphism between finite induced subgraphs extends to an automorphism.
A countable [[random graph|TNT3DG0HRJ]] in which each edge is present independently with probability $1/2$ is isomorphic to $R$ with probability $1$.
For this reason $R$ is also called the countable random graph.
The first-order theory of $R$ is $\aleph_0$-categorical.

## Explanations

### L1 human

The Rado graph is an infinite graph that contains every finite and every countable graph as an induced subgraph.
Its key feature is that any finite wish list "be joined to these vertices and not to those" is met by some vertex.
If one draws a countable graph by flipping a fair coin for each pair of vertices, one gets this same graph with probability one.
