---
tag: PT67C5ANSD
kind: statement
role: theorem
name: Descartes's theorem on total angular defect
msc: [52B10, 51M20]
uses: [300K6CB1KH, R7V3S9V891, RNDDWDAFJ5]
about: [300K6CB1KH]
sources:
  - url: https://en.wikipedia.org/wiki/Angular_defect
---

## Statement

Let $P \subseteq \R^3$ be a three-dimensional [[convex polytope|300K6CB1KH]].
Let $v$ be a [[vertex|R7V3S9V891]] of $P$.
For a face $F$ of $P$ that contains $v$, let $\alpha_F(v)$ be the interior angle of the polygon $F$ at $v$.
The *angular defect* at $v$ is
$$\delta(v) = 2\pi - \sum_F \alpha_F(v),$$
where the sum runs over the faces $F$ of $P$ that contain $v$.
Then
$$\sum_{v} \delta(v) = 4\pi,$$
where the sum runs over all vertices of $P$.

## Remarks

Let $P$ have $V$ vertices, $E$ edges and $F$ faces.
A face with $k$ sides has angle sum $(k - 2)\pi$, and the numbers of sides of all faces add up to $2E$.
So all face angles of $P$ add up to $2\pi E - 2\pi F$.
Hence $\sum_v \delta(v) = 2\pi V - 2\pi E + 2\pi F = 2\pi (V - E + F)$, and [[Euler's polyhedron formula|09HT3P35YP]] $V - E + F = 2$ gives $4\pi$.
The same count shows that for a polyhedral surface of [[Euler characteristic|RNDDWDAFJ5]] $\chi$ the total defect is $2\pi\chi$.

Example: the cube has $8$ vertices, each with three right angles, so each defect is $2\pi - 3\pi/2 = \pi/2$, and the total is $8 \cdot \pi/2 = 4\pi$.
The regular tetrahedron has $4$ vertices with three angles of $\pi/3$ each, so each defect is $\pi$, and the total is again $4\pi$.

Convexity enters only through Euler's formula: the statement holds for every polyhedron whose surface is a topological sphere, where a defect may be negative at a non-convex vertex.

## Explanations

### L1 human

At each corner of a convex solid, the face angles add up to less than a full turn; the missing amount is the defect.
If you add the missing amounts over all corners, you always get $720^\circ$, two full turns, whatever the solid.
A cube has eight corners each missing $90^\circ$, and $8 \cdot 90^\circ = 720^\circ$.

### L2 human

The theorem is the discrete form of the [[Gauss–Bonnet theorem|ESGEHKPD60]] for the sphere: the defect at a vertex plays the role of the total [[Gaussian curvature|SQVQ5DQT6W]] concentrated there.
It is equivalent to Euler's formula, given the angle count in the proof.
It shows that a convex polyhedron has at least one vertex with defect at least $4\pi/V$, and it constrains the possible vertex configurations of Platonic and Archimedean solids.
It also explains why the total of the cone angles is fixed in [[Alexandrov's theorem on polyhedra|ZCDWXVMDFN]].
