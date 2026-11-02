---
tag: XDZQYX6AQ3
kind: example
name: Face lattice
msc: [52B05, 06B05]
instance_of: [WH4SFAACAS, N1Q0BJAEFX]
uses: [879SBTVE7V, 0FQSDC2EQ2, 1C7TKGTB2F]
sources:
  - url: https://en.wikipedia.org/wiki/Abstract_polytope
---

## Example

Let $P \subset \R^d$ be a convex polytope, that is, the [[convex hull|0FQSDC2EQ2]] of finitely many points.
A face of $P$ is $P$ itself, the empty set, or a set $P \cap H$ for a supporting hyperplane $H$.
Here $H$ is supporting when $P$ lies in one closed half-space bounded by $H$.
The *face lattice* of $P$ is the set of all faces of $P$, ordered by inclusion.
It is a [[lattice|WH4SFAACAS]]: the meet of two faces is their intersection, and the join is the smallest face that contains both.
It is [[graded|1C7TKGTB2F]] by $\operatorname{rank}(F) = \dim F + 1$, with the empty face of rank $0$ and $P$ of rank $\dim P + 1$.
It is an [[Eulerian poset|N1Q0BJAEFX]].

Check for a square $Q$.
The faces are the empty face, $4$ vertices, $4$ edges and $Q$ itself, so the lattice has $10$ elements.
Two vertices have the empty face as meet; two adjacent vertices have their common edge as join, and two opposite vertices have $Q$ as join.
In the interval from the empty face to $Q$, the elements of even rank are the empty face and the $4$ edges.
The elements of odd rank are the $4$ vertices and $Q$.
There are five of each, as the Eulerian condition asks.

## Remarks

The face lattice records the [[combinatorial type|879SBTVE7V]] of the polytope: two polytopes are combinatorially equivalent exactly when their face lattices are isomorphic.
The face lattice of a $d$-simplex is the lattice of all subsets of its $d + 1$ vertices.
Abstract polytopes are defined by taking some properties of face lattices as axioms.

## Explanations

### L1 human

List all the pieces of a polytope: its vertices, edges, two-dimensional faces and so on, together with the empty set and the whole polytope.
Order them by "is contained in".
For a square you get the empty set at the bottom, four corners, four sides, and the square at the top.
This diagram forgets the exact shape and keeps only how the pieces fit together.
