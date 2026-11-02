---
tag: RFCQT6TKZF
kind: statement
role: theorem
name: Euler's theorem in geometry
msc: [51M04, 51M16]
uses: [0CTNFGYMM2, 03VZJE6C8C, 07DFG5JYPT, 0F98FZK14A, 0M9MX8YW0A]
about: [03VZJE6C8C, 07DFG5JYPT]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%27s_theorem_in_geometry
same_as:
  wikidata: Q1423818
  wikipedia: Euler's theorem in geometry
---

## Statement

Let $ABC$ be a [[triangle|0CTNFGYMM2]] in the Euclidean plane.
Let $O$ and $R$ be the centre and radius of its [[circumcircle|03VZJE6C8C]], and $I$ and $r$ the centre and radius of its [[incircle|07DFG5JYPT]].
Then the distance $d = OI$ satisfies
$$d^2 = R(R - 2r).$$
In particular $R \ge 2r$, with equality if and only if the triangle is equilateral.

## Remarks

Let the line $AI$ meet the circumcircle again at $M$, the midpoint of the arc $BC$ not containing $A$.
An angle chase shows $MI = MB$, and the law of sines in the triangle $ABM$ gives $MB = 2R \sin \frac{A}{2}$.
Also $AI = r / \sin \frac{A}{2}$, so $AI \cdot IM = 2Rr$.
The power of the point $I$ with respect to the circumcircle is $R^2 - d^2 = AI \cdot IM$, and the formula follows.

The inequality $R \ge 2r$ is Euler's inequality.
Equality $d = 0$ means that the [[circumcentre|0F98FZK14A]] and the [[incentre|0M9MX8YW0A]] coincide, which happens only for an equilateral triangle.

Example: for the right triangle with sides $3$, $4$ and $5$, the circumradius is $R = \frac{5}{2}$ and the inradius is $r = 1$.
The formula gives $d^2 = \frac{5}{2} \cdot \frac{1}{2} = \frac{5}{4}$.
With $C = (0, 0)$, $A = (4, 0)$, $B = (0, 3)$ one has $O = (2, \frac{3}{2})$ and $I = (1, 1)$, and indeed $OI^2 = 1 + \frac{1}{4} = \frac{5}{4}$.

## Explanations

### L1 human

Every triangle has a circle through its corners and a circle inside touching its sides.
Euler's theorem gives the distance between their centres from the two radii alone.
As a consequence, the outer circle is always at least twice as large as the inner one.
The two centres meet only when the triangle is equilateral.

### L2 human

The theorem is a basic tool for inequalities in triangle geometry, through $R \ge 2r$.
It also enters the proof of Feuerbach's theorem via the distance between the incentre and the nine-point centre.
Its converse is a closure statement.
For two circles with $d^2 = R(R - 2r)$, every point of the outer circle is a vertex of a triangle inscribed in one and circumscribed about the other.
This is the case of triangles in [[Poncelet's closure theorem|XWYXSRM5YS]].
