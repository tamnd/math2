---
tag: 7HM094BSJE
kind: definition
name: Binary decision diagram
msc: [68P05, 94C11, "06E30"]
defines: MR9PV732Q2
uses: [0X05GS525E, 0KFYGSHHF5, 03NAMV1DHJ]
sources:
  - url: https://en.wikipedia.org/wiki/Binary_decision_diagram
---

## Definition

Let $x_1, \dots, x_n$ be Boolean variables.
A *binary decision diagram* over $x_1, \dots, x_n$ is a finite acyclic [[directed graph|0KFYGSHHF5]] with one root such that:

1. each *terminal* node has no outgoing edge and carries a label $0$ or $1$;
2. each other node $v$ carries a variable index $i(v) \in \set{1, \dots, n}$ and has exactly two outgoing edges, to its *low child* and its *high child*.

It *represents* the [[Boolean function|0X05GS525E]] $f \colon \set{0, 1}^n \to \set{0, 1}$ defined as follows.
For $a \in \set{0, 1}^n$, start at the root.
At each non-terminal node $v$, move to its high child if $a_{i(v)} = 1$ and to its low child if $a_{i(v)} = 0$.
Then $f(a)$ is the label of the terminal node reached.

The diagram is *ordered* if $i(u) < i(v)$ whenever $v$ is a non-terminal node reached from a non-terminal node $u$ by a directed [[path|03NAMV1DHJ]] of positive length.
An ordered diagram is *reduced* if no non-terminal node has equal low and high children, and no two distinct terminal nodes have the same label.
It must also have no two distinct non-terminal nodes with the same index, the same low child and the same high child.

## Remarks

Example: the reduced ordered diagram of $x_1 \wedge x_2$ has the terminals $0$ and $1$ and two other nodes.
The node $v$ has $i(v) = 2$, low child $0$ and high child $1$.
The root $u$ has $i(u) = 1$, low child $0$ and high child $v$.
At $a = (1, 1)$ the walk goes $u \to v \to 1$, and at the other three inputs it ends at $0$, as required.

Non-example of reducedness: add a node $w$ with $i(w) = 2$ and both children equal to $0$, and make $w$ the low child of the root.
The new diagram still represents $x_1 \wedge x_2$, but it is not reduced.

For a fixed variable order, every Boolean function has exactly one reduced ordered binary decision diagram up to isomorphism.
The size of this diagram depends on the order.
For $x_1 y_1 \vee x_2 y_2 \vee \dots \vee x_k y_k$, the order $x_1, y_1, x_2, y_2, \dots$ gives $2k + 2$ nodes, while the order $x_1, \dots, x_k, y_1, \dots, y_k$ gives a number of nodes exponential in $k$.
