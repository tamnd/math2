---
tag: 1SC8R3F2WR
kind: definition
name: Robinson–Foulds metric
msc: [92D15, "05C05"]
defines: 3T1CQ906MB
uses: [RK58WSHJSG, 062D9KXJB1, 0ME21QN125, 0VKD1TP7F3, 08QMKTWF9T]
sources:
  - url: https://en.wikipedia.org/wiki/Robinson–Foulds_metric
---

## Definition

Let $X$ be a finite set of taxa.
An unrooted phylogenetic $X$-tree is a [[tree|062D9KXJB1]] with no vertex of degree $2$ whose leaves are labelled bijectively by $X$.
Deleting an edge $e$ of such a tree $T$ splits $X$ into two nonempty parts $A$ and $X \setminus A$.
This [[partition|08QMKTWF9T]] is the *split* of $e$, written $A \mid X \setminus A$.
Let $\Sigma(T)$ be the set of splits of the internal edges of $T$, those not incident to a leaf.
The *Robinson–Foulds distance* between two such trees $T_1$ and $T_2$ is
$$d_{RF}(T_1, T_2) = \abs{\Sigma(T_1) \mathbin{\triangle} \Sigma(T_2)},$$
where $\triangle$ is the [[symmetric difference|0ME21QN125]].

## Remarks

A tree is determined up to isomorphism by its set of splits, so $d_{RF}$ is a [[metric|0VKD1TP7F3]] on the set of isomorphism classes of phylogenetic $X$-trees.
Some authors divide by $2$.
For binary trees with $n \ge 3$ leaves, each tree has $n - 3$ internal edges, so $d_{RF} \le 2(n - 3)$.
Example: on $X = \set{a, b, c, d}$, the binary tree $T_1$ with split $ab \mid cd$ and the binary tree $T_2$ with split $ac \mid bd$ have $\Sigma(T_1) \cap \Sigma(T_2) = \emptyset$, so $d_{RF}(T_1, T_2) = 2$, the maximum $2(4 - 3)$.
Non-example: two trees on different taxon sets have no Robinson–Foulds distance, since their splits are partitions of different sets.
