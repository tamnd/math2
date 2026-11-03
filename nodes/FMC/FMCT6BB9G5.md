---
tag: FMCT6BB9G5
kind: statement
role: theorem
name: Gomory–Hu tree
msc: [90C35, 05C21, 05C85]
uses: [00C0BR7D7H, 062D9KXJB1, 4HMR4KQ01T, EXMR7RYRTP]
about: [00C0BR7D7H]
sources:
  - url: https://en.wikipedia.org/wiki/Gomory%E2%80%93Hu_tree
same_as:
  wikidata: Q5581241
  wikipedia: Gomory–Hu tree
---

## Statement

Let $G = (V, E)$ be a finite undirected [[graph|00C0BR7D7H]] with at least two vertices and a capacity $c_e \ge 0$ on each edge.
For $S \subseteq V$, let $c(S)$ be the total capacity of the edges between $S$ and $V \setminus S$.
For distinct vertices $s, t$, let $\lambda(s, t)$ be the least $c(S)$ over all $S$ with $s \in S$ and $t \notin S$.
Then there is a [[tree|062D9KXJB1]] $T$ with vertex set $V$ and a weight $w(e) \ge 0$ on each edge $e$ of $T$ such that:

1. Let $e = \set{u, v}$ be an edge of $T$, and let $S$ be the vertex set of the component of $T - e$ that contains $u$. Then $w(e) = c(S) = \lambda(u, v)$.
2. For all distinct $s, t \in V$, $\lambda(s, t)$ is the least weight of an edge on the path from $s$ to $t$ in $T$.

Such a tree, called a Gomory–Hu tree, can be computed with $\abs{V} - 1$ minimum cut computations in graphs no larger than $G$.

## Remarks

The proof rests on the uncrossing of minimum cuts: the cut function is submodular, so a minimum $s$-$t$ cut can be chosen not to cross a given minimum $u$-$v$ cut.
Gomory and Hu (1961) built the tree by repeatedly splitting a set of vertices with one minimum cut and contracting the other side.
A consequence is $\lambda(s, t) \ge \min(\lambda(s, u), \lambda(u, t))$ for all distinct $s, u, t$.
Another is that the $\binom{n}{2}$ pairs of an $n$-vertex graph have at most $n - 1$ distinct minimum cut values.

Example: if $G$ is a path $a - b - c$ with capacities $3$ on $\set{a, b}$ and $1$ on $\set{b, c}$, then $G$ itself, with these weights, is a Gomory–Hu tree.
Indeed $\lambda(a, c) = 1 = \min(3, 1)$.

The statement needs an undirected graph: for directed graphs, minimum cut values need not have such a tree representation.

## Explanations

### L1 human

In a network one may ask, for every pair of points, how much must be cut to separate them.
There are many pairs, but the theorem says one tree on the same points stores all the answers.
To separate two points, look at the path between them in the tree and take its weakest edge.

### L2 human

Each answer $\lambda(s, t)$ equals a maximum flow value by the [[max-flow min-cut theorem|4HMR4KQ01T]].
So the tree replaces $\binom{n}{2}$ [[maximum flow|EXMR7RYRTP]] computations by $n - 1$ of them.
Gusfield later gave a variant that needs no contraction.
The tree is used for all-pairs minimum cuts, for the minimum $T$-odd cut problem in matching algorithms, and in network design.
