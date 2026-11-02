---
tag: 2PYAZX5VD4
kind: statement
role: theorem
name: Steinitz's theorem
msc: [52B10, 05C10]
uses: [300K6CB1KH, 0NC9R64TXP, 7FZB7YYBXA, 00C0BR7D7H, GR1DDT1B6B]
about: [300K6CB1KH, 0NC9R64TXP]
sources:
  - url: https://en.wikipedia.org/wiki/Steinitz%27s_theorem
same_as:
  wikidata: Q7606897
  wikipedia: Steinitz's theorem
---

## Statement

Let $G$ be a finite simple [[graph|00C0BR7D7H]].
Then the following are equivalent.

1. $G$ is isomorphic to the graph of vertices and edges of a $3$-dimensional [[convex polytope|300K6CB1KH]].
2. $G$ is [[planar|0NC9R64TXP]] and [[3-vertex-connected|7FZB7YYBXA]].

## Remarks

One direction is easier.
The graph of a $3$-polytope is planar: project its boundary onto one face from a point just outside that face.
It is $3$-connected by Balinski's theorem.
For the converse, one proof reduces every $3$-connected planar graph to the complete graph $K_4$.
It uses moves that replace a triangle by a three-legged star and back, and shows that each move can be carried out on polytopes.
Another proof uses the [[circle packing theorem|GR1DDT1B6B]] to realize the graph with all edges tangent to the unit sphere.

Example: the cube graph, with $8$ vertices of degree $3$, is planar and $3$-connected, and the cube realizes it.
Without $3$-connectivity the conclusion fails: the cycle graph $C_4$ is planar but only $2$-connected.
No $3$-polytope has it as its graph, because every vertex of a $3$-polytope has degree at least $3$.

## Explanations

### L1 human

Which networks of dots and lines are the skeletons of convex solids in space?
Steinitz's theorem gives a complete answer: exactly those that can be drawn in the plane without crossings and that stay connected after removing any two dots.
So the combinatorics of three-dimensional polytopes is pure graph theory.

### L2 human

The theorem lets one count and list combinatorial types of $3$-polytopes by counting $3$-connected planar graphs.
It also shows that every combinatorial $3$-polytope can be realized with rational, even integer, coordinates, and with many extra properties, such as all edges tangent to a sphere.
In dimension $4$ and higher no such characterisation is known, and realizability of a given face lattice is a hard problem.
