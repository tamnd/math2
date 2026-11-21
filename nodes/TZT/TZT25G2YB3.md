---
tag: TZT25G2YB3
kind: concept
name: Henson graph
aliases: [henson-graph, generic-kn-free-graph, generic-triangle-free-graph]
msc: ["05C63", "03C15"]
topics: [ZS8X8KS54R]
audience: grad
uses: [00C0BR7D7H, 0BYX1D7C2E, 03WKB2H474, 0EREPBVG2G, HJVRBDQSGG, H8VM37SSAX, XSCSX39GEZ, RMXR0FEF54, A22K1X8GKD]
sources:
  - wikipedia: en:49104628@r1280021819
    locator: Henson graph
    note: adopted
    mention: wikipedia://en/49104628
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Henson_graph
    locator: Construction
same_as:
  wikidata: Q25304614
  wikipedia: Henson graph
inventory: [C1VZ02V7CS]
---

## Summary

For $n \ge 3$, the *Henson graph* $G_n$ is the countable [[graph|00C0BR7D7H]] with no [[clique|0BYX1D7C2E]] of size $n$ that is [[ultrahomogeneous|H8VM37SSAX]] and contains every finite $K_n$-free graph as an [[induced subgraph|0EREPBVG2G]].
It is the [[Fraïssé limit|HJVRBDQSGG]] of the class of finite graphs without a copy of the [[complete graph|03WKB2H474]] $K_n$.
For instance, $G_3$ is triangle-free and contains every finite triangle-free graph.
The countably infinite homogeneous graphs are the graphs $G_n$, the Rado graph, the disjoint unions $m \cdot K_n$ of $m$ copies of the complete graph $K_n$ with $mn$ infinite, and the complements of all of these.

## Motivation

The [[Rado graph|RMXR0FEF54]] is the generic countable graph.
One may ask for a generic countable graph under a restriction, such as having no triangle.
Fraïssé's theorem gives one exactly when the restriction is compatible with [[amalgamation|XSCSX39GEZ]].
Forbidding $K_n$ is compatible, because gluing two $K_n$-free graphs without new edges creates no new clique.
The Henson graphs are the resulting generic $K_n$-free graphs.

## Notation

We write $G_n$ for the Henson graph omitting $K_n$, with $n \ge 3$.
Some authors write $H_n$, or call $G_3$ the generic triangle-free graph.
For $n = 2$ the same construction gives the countably infinite edgeless graph, which is usually excluded.

## Remarks

### Examples

- $G_3$, the generic triangle-free graph; see [[this example|AH6BAJW1DA]].
- $G_4$, in which the neighborhood of each vertex is a copy of $G_3$; see [[this example|6FG5TYXK9C]].
- The complement of $G_n$ is again ultrahomogeneous, and it is the generic graph with no independent set of size $n$.

### Non-examples

- $G_3$ with one extra isolated vertex is universal for countable triangle-free graphs, but it is not ultrahomogeneous; see [[this non-example|9FZHWYSVJ5]].
- The Rado graph is not a Henson graph, since it contains every finite clique.

### Basic properties

- $G_n$ satisfies the extension property: for disjoint finite vertex sets $U, V$ with $U$ free of $K_{n-1}$, some vertex outside $U \cup V$ is adjacent to all of $U$ and to none of $V$.
- A countable $K_n$-free graph with this extension property is isomorphic to $G_n$, by back-and-forth.
- Every countable $K_n$-free graph is an induced subgraph of $G_n$.
- The theory of $G_n$ is [[$\aleph_0$-categorical|A22K1X8GKD]] with quantifier elimination.
- The theory is unstable: $G_3$ contains a half-graph, a bipartite graph with $a_i \sim b_j$ exactly when $i < j$.

### History

Henson constructed these graphs in 1971.

### Common errors

- To think universality for countable $K_n$-free graphs characterizes $G_n$. Many non-homogeneous graphs are universal too.
- To apply the extension property with $U$ containing $K_{n-1}$; then the new vertex would close a copy of $K_n$.

## Explanations

### L1 human

Take all finite graphs that contain no triangle.
There is one countable triangle-free graph that contains each of them, and that looks the same around any two matching finite pieces.
That graph is $G_3$.
Forbidding cliques of size $4$, $5$ and so on gives $G_4$, $G_5$ and so on.

### L2 human

We check the extension property of $G_3$ in one case.

1. Let $U = \set{a, b}$ be two non-adjacent vertices, and $V = \set{c}$.
2. $U$ has no edge, so $U$ contains no $K_2$, and the property applies.
3. It gives $z$ adjacent to $a$ and $b$ but not to $c$.
4. No triangle appears, since $a$ and $b$ are not adjacent.

If $a$ and $b$ were adjacent, $z$ would close a triangle, so no such $z$ exists.
A trap is to transfer the full extension property of the Rado graph to $G_3$.

### L3 human

The Henson graphs are the primitive non-random entries in the Lachlan-Woodrow classification of countable homogeneous graphs.
Their theories are standard examples of unstable $\aleph_0$-categorical theories.
Henson also produced $2^{\aleph_0}$ pairwise non-isomorphic countable homogeneous directed graphs, by forbidding sets of finite tournaments.
