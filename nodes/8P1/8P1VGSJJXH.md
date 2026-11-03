---
tag: 8P1VGSJJXH
kind: definition
name: Combinatorial optimization
msc: [90C27]
defines: FJPER80BJC
uses: [NS0Q42Y3FX]
sources:
  - url: https://en.wikipedia.org/wiki/Combinatorial_optimization
---

## Definition

Let $E$ be a finite set, called the *ground set*.
Let $\mathcal{F}$ be a family of subsets of $E$, called the *feasible solutions*, and let $w \colon E \to \R$ be a weight function.
For $F \subseteq E$ write $w(F) = \sum_{e \in F} w(e)$.
A *combinatorial optimization problem* asks for a set $F \in \mathcal{F}$ that minimizes (or maximizes) $w(F)$ over $\mathcal{F}$.
If $\mathcal{F}$ is empty, the answer is that there is no feasible solution.
The family $\mathcal{F}$ is usually not listed but given implicitly by a structure on $E$, such as a graph.
*Combinatorial optimization* is the study of such problems and of algorithms for them.

## Remarks

Example: take the minimum spanning tree problem for a connected graph $G$ with edge weights $w$.
The ground set $E$ is the edge set of $G$, and $\mathcal{F}$ is the family of edge sets of spanning trees.
For a triangle with edge weights $1$, $2$, $3$, the three spanning trees have weights $3$, $4$ and $5$, so the minimum is $3$, as [[Kruskal's algorithm|5FPWTYFJRA]] finds.

Non-example: minimizing $x^2 - 2x$ over $x \in \R$ is an [[optimization problem|NS0Q42Y3FX]] with infinitely many feasible solutions forming a continuum, so it is not a combinatorial optimization problem.

More generally, one allows any finite set of feasible solutions and any objective function on it; the linear form above covers most classical problems.
Since $\mathcal{F}$ is finite, an optimum exists whenever $\mathcal{F}$ is nonempty; the difficulty is to find it efficiently, in time polynomial in $\abs{E}$ rather than in $\abs{\mathcal{F}}$.
