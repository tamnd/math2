---
tag: 0M4TCS0RRG
kind: statement
role: theorem
name: Classification of the Platonic solids
msc: [51M20]
uses: [017E5PRS1Q, 09HT3P35YP]
sources:
  - url: https://en.wikipedia.org/wiki/Platonic_solid
    locator: Classification
  - url: https://en.wikipedia.org/wiki/Platonic_solid
    locator: Topological proof
  - url: https://en.wikipedia.org/wiki/Platonic_solid
    locator: History
---

## Statement

Let $P$ be a [[Platonic solid|017E5PRS1Q]] whose faces have $p$ sides each, with $q$ faces at each vertex. Then $\{p, q\}$ is one of
$$\{3, 3\}, \quad \{4, 3\}, \quad \{3, 4\}, \quad \{5, 3\}, \quad \{3, 5\}.$$
Each of these five cases occurs, by the regular tetrahedron, the cube, the regular octahedron, the regular dodecahedron and the regular icosahedron. Up to similarity, there is exactly one Platonic solid for each case.

## Remarks

A proof: let $V$, $E$ and $F$ be the numbers of vertices, edges and faces. Then $pF = 2E = qV$, and [[Euler's formula|09HT3P35YP]] $V - E + F = 2$ gives $\frac{1}{p} + \frac{1}{q} = \frac{1}{2} + \frac{1}{E} > \frac{1}{2}$.
With $p, q \geq 3$, this inequality has exactly the five solutions above.
A geometric proof uses the angles: at each vertex, the $q$ face angles $\frac{(p - 2)\pi}{p}$ must add up to less than $2\pi$.

## History

Theaetetus, a contemporary of Plato, described all five solids. He may have given the first proof that no other convex regular polyhedra exist. Euclid's Elements contains a geometric proof.

## Explanations

### L1 human

Only five perfectly regular convex solids exist. At each corner, at least three faces meet, and their angles must add up to less than a full turn. This leaves room only for three, four or five triangles, three squares or three pentagons.
