---
tag: AF4M5HSYMC
kind: definition
name: Dynkin diagram
msc: ["17B22", "17B20", "20F55"]
defines: CS73JZQS66
uses: [AVVV93CASN, CSBM217V1N, H59F1XBDZP, 00C0BR7D7H]
sources:
  - url: https://en.wikipedia.org/wiki/Dynkin_diagram
---

## Definition

Let $\Phi$ be a [[root system|AVVV93CASN]] with a base $\Delta = \set{\alpha_1, \dots, \alpha_l}$ of [[simple roots|CSBM217V1N]].
Let $a_{ij} = \langle \alpha_i, \alpha_j \rangle$ be the entries of the [[Cartan matrix|H59F1XBDZP]].
The *Dynkin diagram* of $\Phi$ is the [[graph|00C0BR7D7H]] with vertex set $\set{1, \dots, l}$ and the following edges:

1. two distinct vertices $i, j$ are joined by $a_{ij} a_{ji}$ edges, a number in $\set{0, 1, 2, 3}$;
2. if $a_{ij} a_{ji} \ge 2$, the edges between $i$ and $j$ carry an arrow that points to the vertex of the shorter root.

The same graph without the arrows is the *Coxeter graph* of $\Phi$.

## Remarks

Example: for $B_2$ with $\alpha_1 = e_1 - e_2$ and $\alpha_2 = e_2$, the Cartan matrix has $a_{12} a_{21} = (-2)(-1) = 2$.
So the diagram has two vertices joined by a double edge, with an arrow pointing to $2$ since $\alpha_2$ is the shorter root.
Non-example: a triangle, three vertices joined in a cycle by single edges, is not the Dynkin diagram of any root system.
Indeed the Dynkin diagram of a root system has no cycles.
That triangle is the diagram of the affine Kac–Moody algebra of type $\tilde A_2$, where the matrix is not positive definite.
The Dynkin diagram determines the Cartan matrix, and so the root system, up to isomorphism.
The root system is irreducible if and only if its Dynkin diagram is connected.
Related diagrams are the [[Dynkin quivers|92RQG73SC5]], the orientations of the simply laced diagrams.

## Explanations

### L1 human

A Dynkin diagram is a small picture of dots and lines that encodes a root system.
Dots are simple roots, the number of lines records the angle between two of them, and arrows record which root is shorter.
