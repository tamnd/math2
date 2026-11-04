---
tag: YWZQFCJB2K
kind: statement
role: lemma
name: Induced Graph Removal Lemma
sources:
  - wikipedia: en:59842040@r1360690218
    locator: Graph removal lemma, section Induced Graph Removal Lemma
    note: adopted
    mention: wikipedia://en/59842040#9ICI
    sections: [Statement]
inventory: [VMZS5XS05S]
---

## Statement

A natural generalization of the graph removal lemma is to consider [[induced subgraphs|0EREPBVG2G]]. In property testing, it is often useful to consider how far a graph is from being induced $H$-free. A graph $G$ is considered to contain an induced subgraph $H$ if there is an injective map $f: V(H) \rightarrow V(G)$ such that $(f(u),f(v))$ is an edge of $G$ if and only if $(u,v)$ is an edge of $H$. Notice that non-edges are considered as well. $G$ is induced $H$-free if there is no induced subgraph $G$. We define $G$ as $\epsilon$-far from being induced $H$-free if we cannot add or delete $\epsilon n^2$ edges to make $G$ induced $H$-free.
