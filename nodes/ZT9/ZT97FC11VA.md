---
tag: ZT97FC11VA
kind: statement
role: theorem
name: Morley's trisector theorem
msc: [51M04]
uses: [0CTNFGYMM2, 0GJAJC6TNZ]
about: [0CTNFGYMM2]
sources:
  - url: https://en.wikipedia.org/wiki/Morley%27s_trisector_theorem
same_as:
  wikidata: Q913447
  wikipedia: Morley's trisector theorem
---

## Statement

Let $ABC$ be a [[triangle|0CTNFGYMM2]] in the Euclidean plane.
Trisect each of its interior [[angles|0GJAJC6TNZ]], that is, divide it into three equal angles by two rays from the vertex.
For each side, the two trisectors nearest to that side, one from each endpoint of the side, meet at a point.
Then the three points so obtained are the vertices of an equilateral triangle.

## Remarks

Let $R$ be the circumradius and write $A$, $B$, $C$ also for the angles.
The side of the Morley triangle is $8R \sin \frac{A}{3} \sin \frac{B}{3} \sin \frac{C}{3}$, which is symmetric in the angles; this length is one route to a trigonometric proof.
A well-known proof runs backwards: start from an equilateral triangle, attach suitable triangles with angles built from $\frac{A}{3}$, $\frac{B}{3}$, $\frac{C}{3}$, and check that the result is similar to $ABC$.

Example: in an equilateral triangle all angles are $\pi/3$, and the figure is symmetric under rotation by $2\pi/3$ about the centre, so the three points form an equilateral triangle.
The theorem says that this equilateral pattern survives for every triangle, with no symmetry.

## Explanations

### L1 human

Split each corner of any triangle into three equal parts.
Near each side, two of the dividing lines meet.
The three meeting points always form a perfectly equilateral triangle, whatever the shape of the triangle you started with.
The result was found by Frank Morley in 1899.

### L2 human

The theorem is surprising because angle trisection is not a ruler-and-compass operation, see [[trisecting the angle|00J3DCCEK5]], so classical synthetic geometry did not study trisectors.
Proofs use trigonometry or a reverse construction, and Alain Connes gave an algebraic proof using the affine group of a field.
It is a standard example of a deep-looking fact of triangle geometry with an elementary proof.
