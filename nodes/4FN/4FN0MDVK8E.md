---
tag: 4FN0MDVK8E
kind: statement
role: theorem
name: Nash-Williams theorem for forests
sources:
  - wikipedia: en:60654680@r1332584259
    locator: Nash-Williams theorem, section Nash-Williams theorem for forests
    note: adopted
    mention: wikipedia://en/60654680#PBAB
    sections: [Statement]
inventory: [2JDCCQ1MX4]
---

## Statement

In 1964, Nash-Williams generalized the above result to forests:

> A graph $G$ can be partitioned into $t$ edge-disjoint forests iff for every $U \subset V(G)$, the [[induced subgraph|0EREPBVG2G]] $G[U]$ has at most $t(|U|-1)$ edges.

Other proofs are given here.

This is how people usually define what it means for a graph to be ***t*-arboric.**

In other words, for every subgraph $S=G[U]$, we have $t \geq \lceil E(S) / (V(S) - 1) \rceil$. It is tight in that there is a subgraph $S$ that saturates the inequality (or else we can choose a smaller $t$). This leads to the following formula

> $$t = \lceil \max_{S \subset G} \frac{E(S)}{V(S) - 1} \rceil,$$

also referred to as the **Nash-Williams formula.**

The general problem is to ask when a graph can be covered by edge-disjoint subgraphs.
