---
tag: WP3GDNWJJW
kind: statement
role: theorem
name: Robertson–Seymour theorem
msc: [05C83]
uses: [VYQ32ZBPEE]
about: [VYQ32ZBPEE]
sources:
  - url: https://en.wikipedia.org/wiki/Robertson–Seymour_theorem
same_as:
  wikidata: Q3527155
  wikipedia: Robertson–Seymour theorem
---

## Statement

The finite graphs are well-quasi-ordered by the [[minor|VYQ32ZBPEE]] relation.
That is, for every infinite sequence $G_1, G_2, G_3, \dots$ of finite graphs, there are indices $i < j$ such that $G_i$ is a minor of $G_j$.

## Remarks

An equivalent form: let $\mathcal{C}$ be a class of finite graphs closed under isomorphism and under taking minors.
Then there is a finite set $\mathcal{F}$ of graphs such that a graph lies in $\mathcal{C}$ if and only if no member of $\mathcal{F}$ is a minor of it.
For planar graphs $\mathcal{F} = \set{K_5, K_{3,3}}$, by [[Wagner's theorem|1B2ZJPVV03]], and for forests $\mathcal{F} = \set{K_3}$.
Neil Robertson and Paul Seymour proved the theorem in a long series of papers called Graph Minors, published between 1983 and 2004.
The proof rests on a structure theorem for graphs that exclude a fixed minor, built on tree decompositions and embeddings in surfaces.
The same project gives a polynomial-time algorithm that tests whether a fixed graph $H$ is a minor of an input graph.
So every minor-closed class can be recognized in polynomial time.
This proof of polynomial-time recognition is not constructive, since the theorem does not say how to find the set $\mathcal{F}$.

## Explanations

### L1 human

A minor of a graph is what remains after deleting and shrinking parts of it.
The theorem says that you cannot have an infinite list of graphs in which none is a minor of a later one.
As a result, every property that survives deleting and shrinking is described by a finite list of forbidden patterns.

### L2 human

For trees, the analogous statement is [[Kruskal's tree theorem|XVHKCX4F5Y]].
The proof of the general case extends ideas from it through [[treewidth|CD2XB4Y1SF]].
Graphs of bounded treewidth are handled like trees, and graphs of large treewidth contain large grid minors.
The theorem is one of the deepest results of combinatorics and gives finite obstruction sets for embeddability in any fixed surface.
