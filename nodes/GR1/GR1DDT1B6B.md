---
tag: GR1DDT1B6B
kind: statement
role: theorem
name: Circle packing theorem
msc: [52C26, 30C35]
uses: [0NC9R64TXP, 060W5CBZP6, 0SG74WBFA2]
about: [0NC9R64TXP]
sources:
  - url: https://en.wikipedia.org/wiki/Circle_packing_theorem
same_as:
  wikidata: Q5121504
  wikipedia: Circle packing theorem
---

## Statement

Let $G$ be a finite simple [[planar graph|0NC9R64TXP]].

1. There are closed discs $D_v$ in the plane, one for each vertex $v$ of $G$, with pairwise disjoint interiors. For distinct vertices $u$ and $v$, the discs $D_u$ and $D_v$ are tangent if and only if $u$ and $v$ are adjacent.
2. Let $G$ be maximal planar with at least three vertices. Then such a family of discs is unique up to [[Möbius transformations|0SG74WBFA2]] and reflections in lines.

## Remarks

The theorem is also called the Koebe–Andreev–Thurston theorem.
One proof first adds vertices to make $G$ a triangulation.
For a triangulation, the angles of the triangles of centres at each interior vertex must sum to $2\pi$.
This is a system of equations in the radii, and an iterative or variational argument shows that it has a unique normalized solution.
Example: the complete graph $K_4$ is realized by three mutually tangent equal discs together with a fourth small disc in the gap between them, tangent to all three.
The simplicity hypothesis is needed.
Two discs with disjoint interiors touch in at most one point, so a double edge cannot be shown by tangency, and a loop has no meaning.
Conversely, the tangency graph of such a family of discs is always planar, so the theorem characterizes planar graphs.

## Explanations

### L1 human

Draw a planar graph, that is, a network of dots and lines without crossings.
The theorem says that you can replace the dots by coins lying flat on a table so that two coins touch exactly when the dots are joined.
For a triangulation, the picture is essentially unique.
This gives a rigid, geometric way to draw any planar graph.

### L2 human

Thurston suggested that circle packings of fine hexagonal triangulations approximate the [[Riemann mapping|02WHMEG5ZR]] of a domain, and Rodin and Sullivan proved this convergence.
So circle packings give a discrete version of [[conformal maps|0YYT36R4YD]], the subject of discrete conformal geometry.
The theorem also gives a geometric proof of planar separator theorems and of Fáry's theorem that planar graphs can be drawn with straight edges, by joining centres of tangent discs.
