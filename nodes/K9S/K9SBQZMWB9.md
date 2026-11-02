---
tag: K9SBQZMWB9
kind: statement
role: theorem
name: Pick's theorem
msc: [52C05, 11P21]
uses: [8VEFWD3EJB]
about: [8VEFWD3EJB]
sources:
  - url: https://en.wikipedia.org/wiki/Pick%27s_theorem
same_as:
  wikidata: Q646523
  wikipedia: Pick's theorem
---

## Statement

Let $P$ be a simple [[polygon|8VEFWD3EJB]] in the plane whose vertices all have integer coordinates.
Let $i$ be the number of points of $\Z^2$ in the interior of $P$ and $b$ the number of points of $\Z^2$ on its boundary.
Then the area $A$ of the region bounded by $P$ is
$$A = i + \frac{b}{2} - 1.$$

## Remarks

Both sides are additive when two lattice polygons are glued along a common edge, once the shared boundary points are counted correctly.
So it suffices to check the formula for lattice triangles, and then for triangles with no lattice points other than their vertices, which have area $1/2$.
Example: the triangle with vertices $(0, 0), (2, 0), (0, 2)$ has area $2$, $b = 6$ and $i = 0$, and $0 + 3 - 1 = 2$.
Simplicity matters: for a region with holes the formula changes by a term for each hole.
There is no direct analogue in dimension $3$: the tetrahedra with vertices $(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, r)$ have no other lattice points but volume $r/6$.
The theorem is due to Georg Pick.

## Explanations

### L1 human

Draw a polygon on squared paper with its corners on grid points.
To find its area, count the grid points strictly inside and the grid points on the edges.
The area is the inside count plus half the edge count, minus one.

### L2 human

Pick's theorem links a continuous quantity, area, to a count of lattice points.
It is the two-dimensional seed of Ehrhart theory, which counts lattice points in dilates of lattice polytopes.
It also gives a quick proof that a lattice triangle with no other lattice points has area $1/2$, which is used in the study of Farey sequences.
