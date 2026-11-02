---
tag: PF5Z57DDG2
kind: statement
role: theorem
name: Catmull–Clark subdivision surface
msc: [65D17, 68U05, 65D18]
uses: [N2JTWEJ1F9, 62AFX32JGT]
about: [N2JTWEJ1F9]
sources:
  - url: https://en.wikipedia.org/wiki/Catmull%E2%80%93Clark_subdivision_surface
same_as:
  wikidata: Q1051211
  wikipedia: Catmull–Clark subdivision surface
---

## Statement

Let $M$ be a closed polygon mesh in $\R^3$: finitely many vertices, edges and polygonal faces, where every edge lies on exactly two faces.
The *valence* of a vertex is the number of edges at it; on such a mesh it equals the number of faces at it.
One step of *Catmull–Clark subdivision* builds a new mesh $M'$ as follows.

1. For each face $f$, the face point $F_f$ is the average of the vertices of $f$.
2. For each edge $e$ with endpoints $P_1, P_2$ and adjacent faces $f_1, f_2$, the edge point is $E_e = \frac{1}{4}(P_1 + P_2 + F_{f_1} + F_{f_2})$.
3. Each old vertex $P$ of valence $n$ moves to $P' = \frac{1}{n}\big(Q + 2R + (n - 3) P\big)$.
   Here $Q$ is the average of the face points of the $n$ faces at $P$.
   Also, $R$ is the average of the midpoints of the $n$ edges at $P$.
4. Each face $f$ with $k$ vertices is replaced by $k$ quadrilaterals.
   The one at a vertex $P$ of $f$ has as vertices $P'$, the edge points of the two edges of $f$ at $P$, and $F_f$.

Call a vertex *extraordinary* if its valence is not $4$.
Then the following hold.

1. Every face of $M'$ is a quadrilateral, and from the second step on, the number of extraordinary vertices does not change.
2. Consider a part of the mesh where all faces are quadrilaterals and all vertices have valence $4$.
   There the step is the refinement rule of the uniform bicubic [[B-spline|62AFX32JGT]] surface with the mesh as control net.
   So the repeated meshes converge there to that surface, which is twice continuously differentiable.
3. The repeated meshes $M, M', M'', \ldots$ converge to a limit surface, which has a continuous tangent plane also at the limits of the extraordinary vertices.

## Remarks

Clause 1 is a count of valences.
Face points get the valence of the old face, edge points get valence $4$, and moved old vertices keep their valence.
So after one step only the old extraordinary vertices and the face points of non-quadrilateral faces are extraordinary, and later steps create no new ones.
Clause 2 is checked by writing a bicubic B-spline patch on a uniform grid and halving the knot spacing.
The new control points are then given by the three averaging rules above with $n = 4$, where the vertex rule becomes $P' = \frac14(Q + 2R + P)$.
Clause 3 needs a separate analysis of the subdivision matrix around an extraordinary vertex, through its eigenvalues; the surface is in general not twice differentiable there.
Example: start from a cube; after one step it has $24$ quadrilateral faces, and its $8$ corners stay extraordinary of valence $3$.
The limit surface is a smooth rounded cube.

## Explanations

### L1 human

The method turns a coarse box-like model into a smooth surface by repeated refinement.
At each step every face is cut into small four-sided pieces, and every point is moved toward a weighted average of its neighbours.
The corners get rounded a little more each time, and the shapes settle down to a smooth limit.
A cube becomes a rounded, pebble-like shape.

### L2 human

Catmull–Clark subdivision is the best known example of a [[subdivision surface|N2JTWEJ1F9]].
It generalises bicubic B-spline surfaces from regular grids to meshes of any topology, and it is widely used in computer graphics and animation.
The price is a loss of smoothness at the few extraordinary points, which is studied through the spectrum of the local subdivision matrix.
Other schemes, such as Loop subdivision for triangle meshes, follow the same pattern.
