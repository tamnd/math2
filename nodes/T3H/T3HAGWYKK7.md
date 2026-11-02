---
tag: T3HAGWYKK7
kind: statement
role: theorem
name: Reidemeister's theorem
msc: [57K10]
uses: [QYEAZTYGPT, 1A5WRCNTM3]
about: [QYEAZTYGPT, 1A5WRCNTM3]
sources:
  - url: https://en.wikipedia.org/wiki/Reidemeister_move
---

## Statement

Let $L$ be a tame [[link|1A5WRCNTM3]] in $\R^3$.
A *link diagram* of $L$ is a projection of $L$ to a plane that is injective except at finitely many transverse double points, called crossings.
At each crossing the diagram records which strand passes over.
The three *Reidemeister moves* are local changes of a diagram inside a small disk:

1. type I adds or removes a single twist with one crossing;
2. type II adds or removes two crossings where one strand passes entirely over another;
3. type III slides a strand over or under a crossing of two other strands.

Two diagrams represent equivalent links if and only if they are related by a finite sequence of Reidemeister moves and isotopies of the plane.

## Remarks

Each move is realized by a deformation of the link near the small disk, which gives the easy direction.
For the converse, an equivalence of tame links can be taken to be a finite sequence of triangle moves on polygonal links.
Such a move replaces one edge by the two other edges of a triangle, or the reverse, when the triangle meets the link only in these edges.
The effect of each such move on a diagram can be split into Reidemeister moves.
The theorem was proved by Kurt Reidemeister in 1927, and independently by James Alexander and Garland Briggs.
It is the basis of most proofs that a quantity computed from a diagram is a [[knot invariant|GZQ5ZE3X6G]]: one checks invariance under the three moves.
For example, [[tricolorability|KNAGK0W65G]] and the [[Kauffman bracket|JYKVYS4N32]] are proved invariant in this way, the bracket up to a factor under the first move.
All three types are needed: for instance, the number of crossings modulo $2$ is unchanged by moves of type II and III, but changed by a move of type I.

## Explanations

### L1 human

Knots are usually drawn as pictures in the plane with gaps that show which strand goes under.
The same knot has many pictures.
Reidemeister's theorem says that any two pictures of the same knot are related by three simple kinds of local changes.
They are undoing a twist, pulling two strands apart, and sliding a strand past a crossing.

### L2 human

The theorem turns knot theory into a combinatorial subject.
To build a knot invariant, one defines a quantity from a diagram and checks that the three moves leave it unchanged.
This is how the Jones polynomial, the Alexander polynomial via skein relations, and colourings by groups or quandles are shown to be invariants.
The theorem gives no bound on the number of moves needed, so by itself it does not give an algorithm to decide whether two diagrams represent the same knot.
