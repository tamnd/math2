---
tag: 3R2VHPXXWS
kind: example
name: Desargues configuration
msc: [05B30, 51A20, 51A30]
instance_of: [Q2QFXPP9EE]
uses: [Q2QFXPP9EE, 5Z19Y02MME]
sources:
  - url: https://en.wikipedia.org/wiki/Desargues_configuration
same_as:
  wikidata: Q15720456
  wikipedia: Desargues configuration
---

## Example

The *Desargues configuration* is a [[configuration|Q2QFXPP9EE]] $(10_3)$ in the projective plane.
Take two triangles $a_1 a_2 a_3$ and $b_1 b_2 b_3$ in perspective from a point $O$, so that $O$, $a_i$, $b_i$ are collinear for $i = 1, 2, 3$.
Let $c_{ij}$ be the intersection of the sides $a_i a_j$ and $b_i b_j$.
By [[Desargues's theorem|5Z19Y02MME]], the three points $c_{12}$, $c_{13}$, $c_{23}$ lie on a line, the axis.

Its $10$ points are $O$, the six vertices and the three points $c_{ij}$.
Its $10$ lines are the three lines $O a_i b_i$, the six sides of the triangles and the axis.
Check: each line has $3$ of the points, for instance the side $a_1 a_2$ contains $a_1$, $a_2$, $c_{12}$.
Each point lies on $3$ lines.
For instance, $O$ lies on the lines $O a_i b_i$, the vertex $a_1$ on $O a_1 b_1$, $a_1 a_2$, $a_1 a_3$, and $c_{12}$ on $a_1 a_2$, $b_1 b_2$ and the axis.

A combinatorial model: the points are the $2$-element subsets of $\set{1, 2, 3, 4, 5}$ and the lines are the $3$-element subsets, with incidence by inclusion.
Each $3$-set contains three $2$-sets, and each $2$-set lies in three $3$-sets.
Its incidence graph is the Desargues graph.

## Explanations

### L1 human

Draw two triangles whose corresponding corners are lined up with a common point.
Extend the corresponding sides until they cross; the three crossing points then lie on one line.
The whole drawing has $10$ points and $10$ lines, with $3$ points on each line and $3$ lines through each point.
The pattern is perfectly balanced, and any of its $10$ points can play the role of the center.
