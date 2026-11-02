---
tag: 4DRPG6VR70
kind: definition
name: Net of a polyhedron
msc: [52B10, 52B05]
defines: FXJ66Z6PQY
uses: [300K6CB1KH, 0FQ5B8S1ZC, 02HPP5VCZH]
sources:
  - url: https://en.wikipedia.org/wiki/Net_(polyhedron)
---

## Definition

Let $P \subseteq \R^3$ be a three-dimensional [[convex polytope|300K6CB1KH]], and let $G$ be its edge graph, whose vertices and edges are those of $P$.
Let $T$ be a [[spanning tree|0FQ5B8S1ZC]] of $G$.
Cutting the surface of $P$ along the edges of $T$ leaves a surface that is connected and can be laid flat in the plane.
The *edge unfolding* of $P$ along $T$ is a placement of the faces of $P$ in $\R^2$ such that:

1. each face is mapped into the plane by an [[isometry|02HPP5VCZH]];
2. two faces that share an edge not in $T$ have images that share the image of that edge and lie on opposite sides of it.

The unfolding is a *net* of $P$ if, in addition, the interiors of the images of distinct faces are pairwise disjoint.

## Remarks

Example: let the unit cube have top face $ABCD$ and bottom face $EFGH$, with $A$ above $E$, $B$ above $F$, $C$ above $G$ and $D$ above $H$.
Let $T$ consist of the four vertical edges $AE$, $BF$, $CG$, $DH$ and the three top edges $BC$, $CD$, $DA$.
These $7$ edges join all $8$ vertices without a cycle, so $T$ is a spanning tree.
The unfolding along $T$ puts the bottom square in the middle, the four side squares around it, and the top square attached to the side $ABFE$ along $AB$.
This is the familiar cross of six squares, and the squares do not overlap, so it is a net.
Up to symmetry the cube has $11$ distinct nets, and none of its edge unfoldings overlaps.

Non-example: cutting the cube only along the four edges of its top square does not use a spanning tree, since these edges form a cycle and miss the bottom vertices.
The top face falls off, so the surface is not unfolded as one piece.

For a convex polytope, the cut edges of any unfolding of the surface into one flat piece along edges form a spanning tree, so the definition loses no unfoldings.
Some edge unfoldings of some convex polytopes overlap, which is why a net requires the extra disjointness condition.
