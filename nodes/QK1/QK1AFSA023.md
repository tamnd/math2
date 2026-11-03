---
tag: QK1AFSA023
kind: problem
name: Steiner tree problem
msc: [90C27, 05C05, 68W25]
uses: [FJPER80BJC, 00C0BR7D7H, 062D9KXJB1, 0JW7KT6PQW, JGZWHWA8P8, 4WEVBDQ8SR]
about: [FJPER80BJC, 062D9KXJB1]
sources:
  - url: https://en.wikipedia.org/wiki/Steiner_tree_problem
same_as:
  wikidata: Q1764144
  wikipedia: Steiner tree problem
history:
  posed_by: "Joseph Diez Gergonne"
  first_stated: "1811"
  notes: "Gergonne posed the Euclidean network problem in 1811, and it was later named after Jakob Steiner; the attribution is to the earliest known formulation. The version in graphs was formulated by S. Louis Hakimi and independently by Levin in 1971, and Karp listed it among his 21 NP-complete problems in 1972."
---

## Problem

Let $G = (V, E)$ be a connected [[graph|00C0BR7D7H]] with edge weights $w \colon E \to [0, \infty)$, and let $R \subseteq V$ be a nonempty set of terminals.
A *Steiner tree* for $R$ is a subgraph of $G$ that is a [[tree|062D9KXJB1]] and contains every vertex of $R$.
It may also contain vertices outside $R$, called Steiner vertices.
The *Steiner tree problem in graphs* asks for a Steiner tree for $R$ of least total edge weight.
In the *Euclidean Steiner tree problem*, a finite set $R$ of points of the plane is given.
It asks for a set of segments of least total length whose union is connected and contains $R$.
New junction points may be added anywhere.

## Remarks

If $R = V$, a Steiner tree of least weight is a [[minimum spanning tree|0JW7KT6PQW]], so the problem is easy.
If $\abs{R} = 2$, it is the shortest path problem.
In general, the decision version of the graph problem is [[NP-complete|JGZWHWA8P8]], and the Euclidean version is also NP-hard.
Take the complete graph on $R$ with the shortest path distances of $G$ as weights.
A minimum spanning tree of it, expanded into paths of $G$, gives a Steiner tree of weight at most twice the optimum.
So this is an [[approximation algorithm|4WEVBDQ8SR]] of ratio $2$, and better ratios are known.
In an optimal Euclidean Steiner tree, the added points have degree $3$ and the three segments at them meet at angles of $120^\circ$.

## Explanations

### L1 human

Several towns must be joined by a road network of least total length.
One may build junctions anywhere, not only at the towns.
For three towns at the corners of an equilateral triangle with side $1$, joining them through the centre needs length $\sqrt{3} \approx 1.73$.
Using two sides of the triangle needs length $2$, so the extra junction saves road.
The problem is to find where to put such junctions and how to connect everything.
