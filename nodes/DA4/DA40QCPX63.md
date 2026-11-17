---
tag: DA40QCPX63
kind: example
name: The angle sum of a triangle with an auxiliary parallel line
msc: ["00A35", "51M04"]
topics: [X1NSTVGDNQ]
audience: school
instance_of: [8TKKRAXKFN]
uses: [8TKKRAXKFN, 2PC3XY0PYZ, 05MDKQBEAF]
sources:
  - url: https://en.wikipedia.org/wiki/Sum_of_angles_of_a_triangle
    locator: lead section
---

## Example

Problem: show that the three angles of every triangle $ABC$ in the Euclidean plane add up to $180^\circ$.
Write $\alpha$, $\beta$ and $\gamma$ for the angles at $A$, $B$ and $C$.
The three angles sit at three different points, and nothing in the figure puts them together.
We add an [[auxiliary element|8TKKRAXKFN]]: a line that collects the three angles at one point.

1. Draw the line $\ell$ through $A$ parallel to $BC$. By the [[parallel postulate|2PC3XY0PYZ]], in Playfair's form, there is exactly one such line.
2. Choose a point $D$ on $\ell$ on the other side of the line $AB$ from $C$, and a point $E$ on $\ell$ on the other side of the line $AC$ from $B$. Then $A$ lies between $D$ and $E$.
3. The line $AB$ crosses the parallel lines $\ell$ and $BC$. The angles $\angle DAB$ and $\angle ABC$ are alternate angles, so $\angle DAB = \beta$.
4. In the same way, the line $AC$ crosses $\ell$ and $BC$, and the alternate angles give $\angle EAC = \gamma$.
5. The angles $\angle DAB$, $\angle BAC$ and $\angle CAE$ fill the straight angle $\angle DAE$ without overlap, since the rays $AB$ and $AC$ lie on the same side of $\ell$ as the triangle.
6. A straight angle measures $180^\circ$. So $\beta + \alpha + \gamma = 180^\circ$.

This is the [[angle sum of a triangle|05MDKQBEAF]].

## Remarks

The auxiliary line does all the work: it moves the angles $\beta$ and $\gamma$ to the vertex $A$, next to $\alpha$.
The alternate angle theorem in steps 3 and 4 depends on the parallel postulate.
Where the postulate fails, the result fails too: the angle sum is more than $180^\circ$ on a sphere and less than $180^\circ$ in the hyperbolic plane.
On a sphere, every great circle through $A$ meets the great circle through $B$ and $C$, so the auxiliary line of step 1 does not exist.
In the hyperbolic plane, many lines through $A$ do not meet $BC$, so the auxiliary line is not unique.

Other auxiliary lines give the same result.
Euclid's proof of Proposition 32 of Book I of the Elements extends the side $BC$ beyond $C$ and draws through $C$ a line parallel to $AB$.

## Explanations

### L1 human

Cut a paper triangle and tear off its three corners.
Put the three corners side by side, with their tips at one point.
They always make a straight line, which is $180^\circ$.
The proof does the same with a line: a line through one corner, parallel to the opposite side, copies the other two angles next to the first one.
The new line is not part of the triangle; we add it because it helps.

### L2 human

We use the result and the same auxiliary line to find the angle sum of a quadrilateral.

1. Let $ABCD$ be a convex quadrilateral. Draw the diagonal $AC$, an auxiliary segment.
2. The diagonal splits $ABCD$ into the triangles $ABC$ and $ACD$.
3. The angles of the two triangles together make up the four angles of the quadrilateral, because the diagonal splits the angles at $A$ and $C$ into two parts each.
4. Each triangle has angle sum $180^\circ$, so the quadrilateral has angle sum $360^\circ$.

The typical use: an auxiliary line puts together quantities that the figure keeps apart.

A trap: an auxiliary line must be constructible and must have the properties that the proof uses; "the line through $A$ parallel to $BC$" exists and is unique only because of the parallel postulate.
