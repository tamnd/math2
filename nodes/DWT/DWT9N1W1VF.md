---
tag: DWT9N1W1VF
kind: definition
name: Chemical graph theory
msc: [05C92, "92E10"]
defines: AE724Y8CQX
uses: [0JD5C82QMB, 0F7QKGJS6B]
sources:
  - url: https://en.wikipedia.org/wiki/Chemical_graph_theory
---

## Definition

Let $M$ be a molecule.
Its *molecular graph* is the simple [[graph|0JD5C82QMB]] $G(M)$ whose vertices are the atoms of $M$.
Two atoms are adjacent exactly when they are joined by a covalent bond.
Its *hydrogen-suppressed molecular graph* is the subgraph of $G(M)$ induced by the atoms other than hydrogen.
A *topological index* is a function $I$ from finite graphs to $\R$ such that $I(G) = I(H)$ whenever $G$ and $H$ are [[isomorphic|0F7QKGJS6B]].
*Chemical graph theory* is the study of molecular graphs and of their topological indices.
It relates these indices to the properties of the molecules.

## Remarks

Example: the hydrogen-suppressed graph of propane $\mathrm{CH_3CH_2CH_3}$ is the path on $3$ vertices, and the number of edges is a topological index with value $2$.
Non-example: on graphs with vertex set $\set{1, 2, 3}$, the function "degree of the vertex $1$" is not a topological index.
The path with edges $12, 23$ and the path with edges $21, 13$ are isomorphic, but the vertex $1$ has degree $1$ in the first and degree $2$ in the second.
Multiple bonds are often ignored in the molecular graph, or recorded as edge weights or multiple edges.
In the hydrogen-suppressed graph of a hydrocarbon, every vertex has degree at most $4$, since carbon is tetravalent.
