---
tag: C1X8DP1SNE
kind: example
name: Counterexamples to Euler's polyhedron formula and the responses to them
msc: ["00A35", "52B10"]
topics: [X1NSTVGDNQ]
audience: research
instance_of: [79P9CTRN0V]
uses: [79P9CTRN0V, 09HT3P35YP, 0325SGSJAR, RNDDWDAFJ5]
sources:
  - url: https://en.wikipedia.org/wiki/Proofs_and_Refutations
    locator: Method
  - url: https://en.wikipedia.org/wiki/Euler_characteristic
    locator: Polyhedra
---

## Example

Primitive conjecture: for each [[polyhedron|0325SGSJAR]] with $V$ vertices, $E$ edges and $F$ faces, $V - E + F = 2$.
We follow the [[method of proofs and refutations|79P9CTRN0V]] on this conjecture, the case study of Lakatos.

1. Evidence. The cube has $8 - 12 + 6 = 2$, and the tetrahedron has $4 - 6 + 4 = 2$.
2. Proof (Cauchy's thought experiment), in three lemmas.
   - Lemma 1: remove one face, and stretch the rest of the surface flat on a plane. The flat network has $V - E + F = 1$ if the solid had $V - E + F = 2$, since one face is gone.
   - Lemma 2: draw diagonals until each region is a triangle. Each diagonal adds one edge and one region, so $V - E + F$ does not change.
   - Lemma 3: remove the triangles one at a time from the boundary. Each removal deletes either one edge and one face, or two edges, one vertex and one face.
   - So $V - E + F$ does not change, and at the end one triangle is left, with $3 - 3 + 1 = 1$.
3. First global counterexample: the hollow cube, a solid cube with a cube-shaped cavity inside. Its surface is two cube surfaces, so $V = 16$, $E = 24$, $F = 12$, and $V - E + F = 16 - 24 + 12 = 4$.
4. Second global counterexample: the picture frame, a square ring with a square hole, made of $16$ quadrilateral faces ($4$ on top, $4$ underneath, $4$ outside and $4$ inside). It has $8$ vertices on top and $8$ underneath, so $V = 16$; it has $12$ edges on top, $12$ underneath and $8$ vertical edges, so $E = 32$; and $F = 16$. So $V - E + F = 16 - 32 + 16 = 0$.
5. Monster-barring. One response: neither solid is a "real" polyhedron. A polyhedron is redefined as a solid whose surface is one connected piece without tunnels.
6. Exception-barring. Another response: the formula is claimed only for convex polyhedra. This is true, but it gives up nonconvex solids, such as an L-shaped solid, for which the formula still holds.
7. Proof analysis. For the hollow cube, Lemma 1 fails: after one face of the outer cube is removed, the inner surface does not become part of the flat network. For the picture frame, Lemma 1 also fails: a ring surface with one face removed cannot be stretched flat onto a plane.
8. Lemma-incorporation. The guilty lemma is Lemma 1. The improved theorem: if the surface of a polyhedron can be stretched flat on a plane after the removal of one face, then $V - E + F = 2$. The new condition says that the surface is a topological sphere, a proof-generated concept.

## Remarks

The two counterexamples give different values, $4$ and $0$, and the analysis explains both values.
The hollow cube has two sphere-like surfaces, and each contributes $2$.
The frame has a surface of the shape of a torus, whose [[Euler characteristic|RNDDWDAFJ5]] is $0$.
A solid with $g$ tunnels, whose surface is connected and whose faces are polygons without holes, has $V - E + F = 2 - 2g$; so the analysis leads from one formula to a classification of surfaces by the number $2 - 2g$.
Kepler's small stellated dodecahedron gives a third kind of counterexample.
With its $12$ star pentagons as faces, $V = 12$, $E = 30$, $F = 12$, and $V - E + F = -6$.
If its faces are taken to be its $60$ visible triangles instead, then $V = 32$, $E = 90$, $F = 60$, and $V - E + F = 2$.
This change of reading is what Lakatos calls monster-adjustment.
For the statement in current form, see [[Euler's polyhedron formula|09HT3P35YP]].

## Explanations

### L1 human

Count the corners, the edges and the faces of a box: $8 - 12 + 6 = 2$.
A rule says this count is always $2$.
Now take a wooden picture frame with a hole in the middle: the count is $0$.
Take a box with a box-shaped hole hidden inside: the count is $4$.
The argument for the rule flattens the surface onto a table after cutting out one face, and that step fails for both strange solids.
So the corrected rule says: if the surface can be flattened in this way, the count is $2$.

### L2 human

We check Lemma 3 of Cauchy's proof, and we see a local counterexample.

1. A boundary triangle shares one edge with the outside: removing it deletes $1$ edge and $1$ face, and $V - E + F$ is unchanged.
2. A boundary triangle that shares two edges with the outside: removing it deletes $2$ edges, $1$ vertex and $1$ face, and the change is $-1 + 2 - 1 = 0$.
3. A triangle in the interior of the network: removing only its region deletes $1$ face and no edge, and $V - E + F$ drops by $1$. This is a local counterexample to Lemma 3, but the cube still satisfies the formula.
4. Repair: remove only boundary triangles, and choose the order so that the remaining network stays in one piece.

The typical use: a local counterexample changes the proof, not the theorem.

A trap: a global counterexample is a different thing; repairing the order of removal does not save the hollow cube.
