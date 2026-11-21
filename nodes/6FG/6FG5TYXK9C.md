---
tag: 6FG5TYXK9C
kind: example
name: Neighborhoods in the Henson graph G4
aliases: [neighborhoods-in-henson-graph-g4]
msc: ["05C63", "03C15"]
topics: [ZS8X8KS54R]
audience: grad
instance_of: [TZT25G2YB3]
uses: [TZT25G2YB3, AH6BAJW1DA, 0BYX1D7C2E, 0EREPBVG2G, 6F2DB4HTJR]
sources:
  - url: https://en.wikipedia.org/wiki/Henson_graph
  - book: isbn:9780521587136
---

## Example

Let $G_4$ be the [[Henson graph|TZT25G2YB3]] omitting $K_4$, and let $v$ be a vertex.
Let $N$ be the [[induced subgraph|0EREPBVG2G]] on the neighbors of $v$.
We show that $N$ is isomorphic to $G_3$.

1. $N$ is triangle-free: a triangle in $N$ together with $v$ would be a [[clique|0BYX1D7C2E]] of size $4$.
2. Let $U, V \subseteq N$ be disjoint and finite, with $U$ independent.
3. Then $U \cup \set{v}$ contains no triangle, since $U$ has no edge.
4. The extension property of $G_4$ gives $z$ adjacent to all of $U \cup \set{v}$ and to none of $V$.
5. Then $z \in N$, and $z$ witnesses the extension property of $G_3$ inside $N$.
6. Step 4 with $U = \emptyset$ and $V$ the vertices of $N$ found so far gives a new vertex of $N$. So $N$ is infinite.
7. A countable triangle-free graph with this extension property is $G_3$, by the [[back-and-forth method|6F2DB4HTJR]].

## Remarks

So $G_4$ contains triangles, unlike $G_3$, and each vertex sees a copy of $G_3$.
The same argument shows that in $G_n$ the neighborhood of a vertex is $G_{n-1}$ for $n \ge 4$.
The non-neighbors of $v$ form a copy of $G_4$ itself, by a similar check.

## Explanations

### L1 human

In $G_4$ there are no four mutually joined vertices.
So among the friends of one vertex, there can be no three mutually joined ones.
The friends of a vertex therefore form a triangle-free graph, and in fact the generic one, $G_3$.

### L2 human

We see why $N$ has no triangle in a concrete case.

1. Suppose $a, b, c \in N$ are pairwise adjacent.
2. Each is adjacent to $v$, by the definition of $N$.
3. So $\set{v, a, b, c}$ is a $K_4$ in $G_4$, which is impossible.

The typical use is to relate the Henson graphs to each other by local operations.
A trap is to expect the neighborhood of a vertex in $G_3$ to be interesting; it is an infinite independent set.
