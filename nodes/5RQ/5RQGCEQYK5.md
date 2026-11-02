---
tag: 5RQGCEQYK5
kind: statement
role: theorem
name: Wallace–Bolyai–Gerwien theorem
msc: [52B45, 51M25]
uses: [8VEFWD3EJB, 0J1N3WTKM4]
about: [8VEFWD3EJB]
sources:
  - url: https://en.wikipedia.org/wiki/Wallace%E2%80%93Bolyai%E2%80%93Gerwien_theorem
same_as:
  wikidata: Q834211
  wikipedia: Wallace–Bolyai–Gerwien theorem
---

## Statement

Let $P$ and $Q$ be two simple [[polygons|8VEFWD3EJB]] in the Euclidean plane with the same area.
Then $P$ can be cut into finitely many polygonal pieces that can be moved by [[isometries|0J1N3WTKM4]] to form $Q$, with disjoint interiors.

## Remarks

The proof cuts a polygon into triangles.
Each triangle can be cut and reassembled into a rectangle, and each rectangle into a rectangle with one side of length $1$.
Stacking these rectangles gives a rectangle of width $1$ and height equal to the area.
So $P$ and $Q$ can both be cut into the same rectangle, and the two dissections combine, since the relation "can be cut into" is transitive.
The analogue in dimension $3$ is false: this is the negative answer to [[Hilbert's third problem|81035XQ5HE]].

## Explanations

### L1 human

Take any two polygons with the same area, for example a square and a triangle.
You can always cut the first into finitely many pieces and reassemble them, like a jigsaw puzzle, into the second.
So in the plane, area is the only thing that matters for cutting and rearranging.

### L2 human

The theorem justifies the old method of finding areas by cutting and rearranging.
An example is the proof that a parallelogram has the area of a rectangle with the same base and height.
It shows that in the plane, equal area is the same as scissors congruence.
In space there is a second invariant, the [[Dehn invariant|S0TGRX3ARS]], and equal volume is not enough.
