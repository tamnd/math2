---
tag: B66EM15GAJ
kind: statement
role: lemma
name: Graph counting lemma
sources:
  - wikipedia: en:1962417@r1368655010
    locator: Szemerédi regularity lemma, section Applications > Graph counting lemma
    note: adopted
    mention: wikipedia://en/1962417#IZTN
    sections: [Statement]
inventory: [MV1PPVDJ1E]
---

## Statement

If we have enough information about the regularity of a graph, we can count the number of copies of a specific subgraph within the graph up to small error.

> **Graph Counting Lemma.** Let $H$ be a graph with $V(H)=[k]$, and let $\varepsilon>0$. Let $G$ be an $n$-vertex graph with vertex sets $V_1,\dots,V_k\subseteq V(G)$ such that $(V_i,V_j)$ is $\varepsilon$-regular whenever $\{i,j\}\in E(H)$. Then, the number of labeled copies of $H$ in $G$ is within $e(H)\varepsilon|V_1|\cdots|V_k|$ of
>
> $$\left(\prod_{\{i,j\}\in E(H)}d(V_i,V_j)\right)\left(\prod_{i=1}^k|V_i|\right).$$

This can be combined with Szemerédi's regularity lemma to prove the Graph removal lemma. The graph removal lemma can be used to prove Roth's Theorem on Arithmetic Progressions, and a generalization of it, the hypergraph removal lemma, can be used to prove Szemerédi's theorem.

The graph removal lemma generalizes to [[induced subgraphs|0EREPBVG2G]], by considering edge edits instead of only edge deletions. This was proved by Alon, Fischer, Krivelevich, and Szegedy in 2000. However, this required a stronger variation of the regularity lemma.

Szemerédi's regularity lemma does not provide meaningful results in sparse graphs. Since sparse graphs have subconstant edge densities, $\varepsilon$-regularity is trivially satisfied. Even though the result seems purely theoretical, some attempts  have been made to use the regularity method as compression technique for large graphs.
