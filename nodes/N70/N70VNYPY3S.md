---
tag: N70VNYPY3S
kind: definition
name: Decision tree model
msc: [68Q17, 68Q25, 68Q04]
defines: 8ZVN9X9WEC
uses: [0C9J6W2A8A, 0A58THH5XV]
sources:
  - url: https://en.wikipedia.org/wiki/Decision_tree_model
---

## Definition

Let $n \ge 1$ and let $f \colon \set{0,1}^n \to \set{0,1}$ be a [[Boolean function|0A58THH5XV]].
A *decision tree* on $n$ variables is a finite [[rooted tree|0C9J6W2A8A]] with the following labels.

1. Each inner vertex is labelled by an index $i \in \set{1, \dots, n}$ and has exactly two children, reached by edges labelled $0$ and $1$.
2. Each leaf is labelled by $0$ or $1$.

On an input $x \in \set{0,1}^n$ the tree is evaluated by starting at the root.
At an inner vertex with label $i$ one moves along the edge labelled $x_i$, and the output is the label of the leaf reached.
The tree computes $f$ if its output is $f(x)$ for every $x$.
The cost of the tree is its depth, the largest number of edges from the root to a leaf.
The *deterministic decision tree complexity* $D(f)$ is the least depth of a decision tree that computes $f$.

## Remarks

Example: for $f(x_1, x_2) = x_1 \vee x_2$, let the root query $x_1$.
Its $1$-child is a leaf labelled $1$, and its $0$-child queries $x_2$ and has leaves labelled $0$ and $1$.
Both clauses hold, the output is correct on all four inputs, and the depth is $2$, so $D(f) \le 2$.
Non-example: a tree whose root asks whether $x_1 + x_2 \ge 1$ is not a decision tree in this model, because clause 1 allows only queries of one variable.
For every $f$, $D(f) \le n$, since querying all variables suffices.
The comparison model is a variant for sorting: inner vertices ask whether $a_i \le a_j$ for input numbers $a_1, \dots, a_n$.
A comparison tree that sorts must have at least $n!$ leaves, so its depth is at least $\log_2(n!)$, which is of order $n \log n$.
