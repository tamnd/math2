---
tag: RHYKE61S49
kind: definition
name: Centrality
msc: [91D30, 05C82]
defines: E4Y32N7GRR
uses: [00C0BR7D7H, 0F7QKGJS6B, 0KS0KRDV4Y, 0KWFFMDF8T, 03NAMV1DHJ, 08B9CX109G, 0N6960W0BV]
sources:
  - url: https://en.wikipedia.org/wiki/Centrality
---

## Definition

Let $\mathcal{G}$ be a class of finite [[graphs|00C0BR7D7H]].
A *centrality index* on $\mathcal{G}$ assigns to each graph $G \in \mathcal{G}$ and each vertex $v$ of $G$ a real number $c_G(v)$.
These numbers must satisfy $c_H(\varphi(v)) = c_G(v)$ for every [[graph isomorphism|0F7QKGJS6B]] $\varphi \colon G \to H$ between graphs of $\mathcal{G}$.
The standard indices on a finite connected simple graph $G = (V, E)$ with distance $d$ are:

1. *degree centrality* $c_D(v) = \deg v$;
2. *closeness centrality* $c_C(v) = 1 / \sum_{u \in V} d(u, v)$, for $\abs{V} \ge 2$;
3. *betweenness centrality* $c_B(v) = \sum \sigma_{st}(v)/\sigma_{st}$, summed over pairs $\set{s, t}$ of vertices other than $v$.
   Here $\sigma_{st}$ counts the shortest paths from $s$ to $t$, and $\sigma_{st}(v)$ counts those through $v$;
4. *eigenvector centrality* $c_E(v) = x_v$, where $x$ is the eigenvector with positive entries and $\sum_v x_v = 1$ of the adjacency matrix $A$ for its largest eigenvalue.

## Remarks

Here $\deg v$ is the [[degree|0KS0KRDV4Y]] of $v$, the graph is [[connected|0KWFFMDF8T]], and distances are lengths of shortest [[paths|03NAMV1DHJ]].
For eigenvector centrality, the [[adjacency matrix|08B9CX109G]] of a connected graph has, by the Perron–Frobenius theorem, a unique such [[eigenvector|0N6960W0BV]].
Example: in the star with centre $0$ and leaves $1, 2, 3$, one has $c_D(0) = 3$, $c_C(0) = 1/3$, $c_B(0) = 3$, while a leaf has $c_D = 1$, $c_C = 1/5$, $c_B = 0$.
Non-example: the function $c(v) = v$ on graphs with vertex set $\set{1, \dots, n}$ is not a centrality index, since relabelling the vertices by an isomorphism changes its values.
Many authors normalise these indices, for example dividing $c_D$ by $\abs{V} - 1$.
