---
tag: S7AMR4PSH0
kind: example
name: Finite graphs have the joint embedding property
aliases: [finite-graphs-joint-embedding]
msc: ["03C15", "05C63"]
topics: [ZS8X8KS54R]
audience: grad
instance_of: [59FQ5Q2B8R]
uses: [59FQ5Q2B8R, KA80AZB1CX, 00C0BR7D7H, 0EREPBVG2G]
sources:
  - book: isbn:9780521587136
---

## Example

Let $\mathcal{G}$ be the class of finite [[graphs|00C0BR7D7H]].
We show that $\mathcal{G}$ has the [[joint embedding property|59FQ5Q2B8R]].

1. Let $A, B \in \mathcal{G}$, and rename vertices so that $A$ and $B$ are disjoint.
2. Let $C = A \sqcup B$, with an edge $xy$ exactly when $xy$ is an edge of $A$ or of $B$.
3. Two vertices of $A$ are adjacent in $C$ exactly when they are adjacent in $A$, since no edge of $B$ touches them.
4. So $A$ is an [[induced subgraph|0EREPBVG2G]] of $C$, and so is $B$.
5. The inclusions are embeddings into $C \in \mathcal{G}$.

## Remarks

The join, with all edges between $A$ and $B$, is a second witness.
The same disjoint union shows JEP for finite $K_n$-free graphs and for finite bipartite graphs.
It also equals the free amalgam of $A$ and $B$ over the empty graph, which is in $\mathcal{G}$.
For finite connected graphs the disjoint union fails, but the join, or one added edge between $A$ and $B$, still works.

## Explanations

### L1 human

Two finite graphs fit inside one graph: draw them side by side and add nothing.
Each one still looks the same inside the picture.

### L2 human

We joint-embed $A = K_2$ and $B = \overline{K_2}$, an edge and a non-edge.

1. The disjoint union has vertices $a_1, a_2, b_1, b_2$ and one edge $a_1 a_2$.
2. On $\set{a_1, a_2}$ the induced graph is $K_2$, and on $\set{b_1, b_2}$ it has no edge.

The typical use is to check the second hypothesis of Fraïssé's theorem.
A trap is to use the disjoint union for a class that forbids disconnected graphs.
