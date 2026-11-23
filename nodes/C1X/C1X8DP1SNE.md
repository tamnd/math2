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

The primitive conjecture says that every [[polyhedron|0325SGSJAR]] with $V$ vertices, $E$ edges and $F$ faces has $V - E + F = 2$.
We follow the [[method of proofs and refutations|79P9CTRN0V]] on it, as Lakatos did.

1. We collect evidence.
   The cube gives $8 - 12 + 6 = 2$, and the tetrahedron gives $4 - 6 + 4 = 2$.
2. We give Cauchy's proof, which splits into three lemmas.
   Lemma 1 says that after one face is removed, the rest of the surface can be stretched flat on a plane, and the flat network then has $V - E + F$ one less than the solid.
   Lemma 2 says that drawing a diagonal in a region adds one edge and one region, so we can cut every region into triangles without changing $V - E + F$.
   Lemma 3 says that removing a boundary triangle, with one or two of its edges, does not change $V - E + F$, and at the end one triangle is left, with $3 - 3 + 1 = 1$.
   So the flat network has $V - E + F = 1$, and the solid has $V - E + F = 2$.
3. The first global counterexample is the hollow cube, a solid cube with a cube-shaped cavity inside.
   Its surface is two cube surfaces, so $V = 16$, $E = 24$ and $F = 12$, and $V - E + F = 4$.
4. The second global counterexample is the picture frame, a square ring with a square hole, built from $16$ four-sided faces: $4$ on top, $4$ underneath, $4$ outside and $4$ inside.
   It has $8$ vertices on top and $8$ underneath, so $V = 16$.
   It has $12$ edges on top, $12$ underneath and $8$ vertical edges, so $E = 32$, and $V - E + F = 16 - 32 + 16 = 0$.
5. Monster-barring answers that neither solid is a real polyhedron, and it redefines a polyhedron as a solid whose surface is one connected piece without tunnels.
6. Exception-barring keeps the formula only for convex polyhedra.
   That is true, but it gives up nonconvex solids, such as an L-shaped block, for which the formula still holds.
7. Proof analysis asks which lemma each counterexample breaks.
   For the hollow cube, Lemma 1 fails, because after one face of the outer cube is removed, the inner surface does not join the flat network.
   For the picture frame, Lemma 1 also fails, because a ring-shaped surface with one face removed cannot be stretched flat.
8. Lemma-incorporation makes Lemma 1 a hypothesis.
   The improved theorem says that if the surface of a polyhedron can be stretched flat after one face is removed, then $V - E + F = 2$.
   The new condition says that the surface is a topological sphere, a concept that the proof generated.

## Remarks

The two counterexamples give different values, $4$ and $0$, and the analysis explains both.
The hollow cube has two sphere-like surfaces, and each one contributes $2$.
The frame has a surface shaped like a torus, whose [[Euler characteristic|RNDDWDAFJ5]] is $0$.
A solid whose surface is connected, with $g$ tunnels and faces that are polygons without holes, has $V - E + F = 2 - 2g$.
So the analysis leads from one formula to a classification of surfaces by the number $2 - 2g$.

Kepler's small stellated dodecahedron gives a third kind of counterexample.
With its $12$ star pentagons as faces, it has $V = 12$, $E = 30$ and $F = 12$, so $V - E + F = -6$.
If we take its faces to be its $60$ visible triangles instead, then $V = 32$, $E = 90$ and $F = 60$, and $V - E + F = 2$.
This change of reading is what Lakatos calls monster-adjustment.
[[Euler's polyhedron formula|09HT3P35YP]] gives the statement in its current form.

## Explanations

### L1 human

Count the corners, the edges and the faces of a box: $8 - 12 + 6 = 2$.
A rule says this count is always $2$.
A wooden picture frame with a hole in the middle gives $0$, and a box with a box-shaped hole hidden inside gives $4$.
The argument for the rule cuts out one face and flattens the rest of the surface onto a table, and that step fails for both strange solids.
So the corrected rule says that the count is $2$ when the surface can be flattened in this way.

### L2 human

Lemma 3 of Cauchy's proof hides a local counterexample, and we can find it by checking each kind of removal.
A boundary triangle that shares one edge with the outside loses $1$ edge and $1$ face when we remove it, so $V - E + F$ does not change.
A boundary triangle that shares two edges with the outside loses $2$ edges, $1$ vertex and $1$ face, and the change is
$$-1 - (-2) + (-1) = 0.$$
But if we remove a triangle from the middle of the network by deleting only its region, we lose $1$ face and no edge, and $V - E + F$ drops by $1$.
That is a local counterexample to Lemma 3, while the cube still satisfies the formula.
The repair is to remove only boundary triangles, in an order that keeps the network in one piece.
A local counterexample changes the proof, not the theorem.
Watch out: a global counterexample is a different thing, and no order of removal saves the hollow cube.
