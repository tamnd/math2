---
tag: E1V8CPXK24
kind: definition
name: Subdivision surface
msc: [65D17, 65D18, 68U05]
defines: N2JTWEJ1F9
uses: [62AFX32JGT, 84TJ8KQ926]
sources:
  - url: https://en.wikipedia.org/wiki/Subdivision_surface
---

## Definition

A *control mesh* is a polygon mesh $M$ in $\R^3$.
It is a finite set of vertices with positions in $\R^3$, together with edges and faces that form a combinatorial surface.
A *subdivision scheme* is a rule that maps each control mesh $M_k$ to a refined control mesh $M_{k+1}$ such that:

1. the connectivity of $M_{k+1}$ is obtained from that of $M_k$ by a fixed combinatorial refinement, such as splitting every face;
2. the position of each vertex of $M_{k+1}$ is a finite affine combination $\sum_v w_v P_v$, with $\sum_v w_v = 1$, of positions $P_v$ of vertices of $M_k$ near it;
3. the weights $w_v$ depend only on the local connectivity of $M_k$, not on the positions.

The *subdivision surface* of $M_0$ is the limit of the meshes $M_0, M_1, M_2, \dots$, when this limit exists as a continuous surface.

## Remarks

Example: the curve analogue, Chaikin's scheme, maps a polygon with vertices $P_i$ to the polygon with vertices $\tfrac34 P_i + \tfrac14 P_{i+1}$ and $\tfrac14 P_i + \tfrac34 P_{i+1}$.
These are affine combinations with weights summing to $1$ that depend only on adjacency, so clauses 2 and 3 hold.
The limit curve is the uniform quadratic [[B-spline|62AFX32JGT]] with control points $P_i$.
The surface schemes of Doo–Sabin, [[Catmull–Clark|PF5Z57DDG2]] and Loop are subdivision schemes in this sense; on regular parts of the mesh their limits are biquadratic, bicubic and box-spline surfaces.
Non-example: the rule $P \mapsto 2P$ applied to all vertices has weights summing to $2$, so clause 2 fails.
The meshes grow without bound, and the result depends on the choice of origin.
The condition $\sum_v w_v = 1$ makes the scheme commute with affine maps of space, so the limit surface does not depend on the coordinate system.
Near extraordinary vertices, those with a nonstandard number of neighbors, the smoothness of the limit is studied through the eigenvalues of the local subdivision matrix.

## Explanations

### L1 human

A subdivision scheme is a recipe that turns a coarse mesh into a finer one by averaging nearby points with fixed weights.
Applying it over and over gives a sequence of meshes that converges to a smooth surface, the subdivision surface.
