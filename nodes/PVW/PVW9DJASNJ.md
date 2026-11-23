---
tag: PVW9DJASNJ
kind: example
name: Consistency of hyperbolic geometry relative to Euclidean geometry
msc: ["03F25", "51M10"]
topics: [H8QZY0RZXZ]
audience: grad
instance_of: [X3G0RG2GPZ]
uses: [X3G0RG2GPZ, 1WN9B18H86, GN4N94GQ0Z, PR7Q3QMEHZ, KM1FB8XZ2R]
sources:
  - url: https://en.wikipedia.org/wiki/Beltrami%E2%80%93Klein_model
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Non-Euclidean_geometry
    locator: lead section
---

## Example

Draw a disk, call its chords "lines", and ignore everything outside.
Through a point off a chord, many chords miss it, so the parallel postulate fails in this small world, which is built entirely from Euclidean geometry.

Plane [[hyperbolic geometry|GN4N94GQ0Z]] keeps the plane axioms of [[Hilbert's axioms|KM1FB8XZ2R]], except [[Playfair's axiom|PR7Q3QMEHZ]].
It replaces that axiom by the hyperbolic parallel axiom: for every line $\ell$ and point $P$ not on $\ell$, at least two lines through $P$ miss $\ell$.
We build the [[Beltrami-Klein model|1WN9B18H86]] inside the Euclidean coordinate plane $\mathbb{R}^2$ and check the main axioms.

1. Let $D = \{ (x, y) \in \mathbb{R}^2 : x^2 + y^2 < 1 \}$, the open unit disk.
   The model points are the points of $D$.
2. The model lines are the chords: the sets $m \cap D$, where $m$ is a Euclidean line that meets $D$.
   Incidence is membership, and betweenness is Euclidean betweenness.
3. Incidence: two distinct points $P, Q \in D$ lie on exactly one Euclidean line $m$.
   So they lie on the chord $m \cap D$, and on no other chord.
4. Existence of points: the points $(0, 0)$, $(\tfrac12, 0)$, $(0, \tfrac12)$ lie in $D$ and are not on one line, and each chord contains infinitely many points.
5. Order: $D$ is convex, by the convexity of the function $(x, y) \mapsto x^2 + y^2$.
   So every point between two points of $D$ lies in $D$, and the order axioms of the Euclidean plane restrict to the chords.
6. Now a concrete failure of Playfair's axiom.
   Let $\ell$ be the chord on the line $y = 0$, and let $P = (0, \tfrac12)$, which is in $D$ and not on $\ell$.
7. The chord $m_1$ on $y = \tfrac12$ contains $P$, and it does not meet $\ell$, since the Euclidean lines are parallel.
8. The chord $m_2$ on $y = \tfrac12 - \tfrac{x}{2}$ contains $P$.
   Its Euclidean line meets $y = 0$ only at $(1, 0)$, and $1^2 + 0^2 = 1$, so this point is not in $D$.
   So $m_2$ does not meet $\ell$ in the model.
9. For the general case, let $\ell$ have endpoints $A$ and $B$ on the unit circle, and let $P \in D$ be off $\ell$.
   The chords on the lines $PA$ and $PB$ are distinct and contain $P$.
10. The line $PA$ meets the line of $\ell$ only at $A$, which is not in $D$, and the same holds for $PB$ and $B$.
    So both chords miss $\ell$, and the hyperbolic parallel axiom holds.
11. The congruence axioms also hold when we define congruence by the projective maps of the plane that map $D$ onto itself.
    That check is longer, and we omit it.
12. All model notions are defined in terms of the coordinate plane.
    So a contradiction derived from the axioms of hyperbolic geometry would turn into a contradiction about $\mathbb{R}^2$.
    Hence hyperbolic geometry is consistent if Euclidean analytic geometry is.

## Remarks

### A model that is an interpretation

The model is also an interpretation: the domain formula is $x^2 + y^2 < 1$, and lines, incidence and betweenness are given by formulas about real coordinates.
So the [[relative consistency proof|X3G0RG2GPZ]] is a translation of derivations, not only an argument about sets.

### Independence of the parallel postulate

The example shows that the parallel postulate does not follow from the other axioms, if Euclidean geometry is consistent; see [[axiom independence|QKCAEG2Y0E]].
In the [[Poincaré disk model|85MM2EA0TK]] the lines are arcs of circles orthogonal to the boundary instead of chords, and the angles are Euclidean angles.
It gives the same relative consistency result.

### History

Beltrami described this model in 1868, and Klein extended it in 1871 with the projective metric of Cayley.

## Explanations

### L1 human

Inside a round table, call every straight cut from edge to edge a "line", and ignore everything outside the table.
Take the cut through the middle from left to right, and a point a little above the middle.
Through that point we can draw many cuts that never touch the first one inside the table, although they would meet it outside.
So in this small world, "exactly one parallel through a point" fails.
Since the small world is built from ordinary geometry, the new geometry cannot contradict itself unless ordinary geometry does.

### L2 human

We check one more pair of parallels with numbers.

1. Take the chord $\ell$ on $x = 0$, the vertical diameter, and the point $P = (\tfrac12, 0)$.
2. The line $x = \tfrac12$ contains $P$ and is parallel to $x = 0$, so its chord misses $\ell$.
3. The line through $P$ and the endpoint $(0, 1)$ of $\ell$ is $y = 1 - 2x$.
   It meets $x = 0$ only at $(0, 1)$, which is on the circle and not in $D$.
4. So two chords through $P$ miss $\ell$, as the hyperbolic axiom says.

The typical use is to show that an axiom is independent: build a model of the other axioms in which it fails.
Watch out: the boundary point $(0, 1)$ is not a point of the model.
The disk is open, and with the boundary included the second chord would meet $\ell$ at $(0, 1)$.
