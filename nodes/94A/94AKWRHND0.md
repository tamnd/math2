---
tag: 94AKWRHND0
kind: statement
role: theorem
name: Pascal's theorem
msc: [51A20, 51N15]
uses: [ZT9A6JK8QF, DANFNN8C4Y, 0AFNNTRTJE, 00HJCMC2CD, 04C5ZBG1WT]
about: [00HJCMC2CD]
sources:
  - url: https://en.wikipedia.org/wiki/Pascal%27s_theorem
same_as:
  wikidata: Q899002
  wikipedia: Pascal's theorem
---

## Statement

Let $k$ be a [[field|04C5ZBG1WT]], and work in the [[projective plane|DANFNN8C4Y]] $\mathbb{P}^2(k)$.
Let $\mathcal{C}$ be a nondegenerate [[conic|00HJCMC2CD]]: the zero set of a homogeneous quadratic polynomial $F$ in three variables.
Here $F$ is not a product of linear factors over any extension of $k$.
Let $A, B, C, D, E, F$ be six distinct points of $\mathcal{C}$.
Then the three points
$$AB \cap DE, \quad BC \cap EF, \quad CD \cap FA$$
are [[collinear|0AFNNTRTJE]].

## Remarks

Here $AB$ denotes the line through $A$ and $B$.
No three points of a nondegenerate conic are collinear, so the lines in each intersection are distinct and the three points are well defined.
The line through them is the Pascal line of the hexagon $ABCDEF$.

One proof over $\C$, which extends to any field by passing to an algebraic closure, uses cubic curves.
The cubics $AB \cdot CD \cdot EF$ and $BC \cdot DE \cdot FA$, products of three lines each, meet in the six points and in the three points of the statement.
A suitable combination of them vanishes on a seventh point of $\mathcal{C}$, so by Bézout's theorem it contains $\mathcal{C}$, and the remaining factor is a line through the three points.

Example: on the unit circle $x^2 + y^2 = 1$ in the real plane, take a regular hexagon.
Opposite sides are then parallel, so the three points lie on the line at infinity.

When the conic degenerates into two lines, the statement becomes [[Pappus's hexagon theorem|B6C3J2GJWP]].
The dual statement is [[Brianchon's theorem|3THE3Q96KK]].

## Explanations

### L1 human

Pick six points on an ellipse, number them around the curve or in any order, and join them into a closed hexagon.
Extend the three pairs of opposite sides until each pair crosses.
The three crossing points always lie on one straight line.

### L2 human

Pascal's theorem is a basic tool for constructions with conics: given five points of a conic, it lets one construct any number of further points with a straightedge alone.
Its converse also holds: if the three points are collinear, the six points lie on a conic, which may be degenerate.
It is the projective form of a statement that, in the real plane, covers ellipses, parabolas and hyperbolas at once, since these are all the same in projective geometry.
Through [[duality|DCMP1A0138]] it gives [[Brianchon's theorem|3THE3Q96KK]].
