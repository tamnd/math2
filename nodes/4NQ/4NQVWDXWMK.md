---
tag: 4NQVWDXWMK
kind: example
name: The angle sum of a convex polygon, found by cutting it into triangles
msc: ["00A35", "51M04"]
topics: [X1NSTVGDNQ]
audience: school
instance_of: [KEZPDNM2NH]
uses: [KEZPDNM2NH, 05MDKQBEAF, Q6KKBP3RRP]
sources:
  - url: https://en.wikipedia.org/wiki/Polygon_triangulation
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Internal_and_external_angles
    locator: lead section
---

## Example

We find the sum of the interior angles of a convex polygon with $n \ge 3$ sides.
The answer is known for one shape only, the triangle, whose [[angle sum|05MDKQBEAF]] is $180^\circ$.
So we [[decompose|KEZPDNM2NH]] the polygon into triangles, use the known result on each piece, and recombine.

1. Name the vertices $V_1, V_2, \dots, V_n$ in order around the polygon.
2. Draw the diagonals from $V_1$ to $V_3, V_4, \dots, V_{n-1}$, which are $n - 3$ diagonals.
3. The polygon is convex, so each diagonal lies inside it.
   The diagonals cut it into the $n - 2$ triangles $V_1 V_2 V_3$, $V_1 V_3 V_4$, up to $V_1 V_{n-1} V_n$.
4. Each triangle has angle sum $180^\circ$, so all the triangles together have angle sum $(n - 2) \cdot 180^\circ$.
5. Every angle of a triangle lies at a vertex of the polygon, inside the polygon's angle there.
   At $V_1$ the angles of the $n - 2$ triangles fill the polygon's angle exactly, and at every other vertex one or two triangle angles fill it.
6. So the angles of the triangles add up to the angles of the polygon, and the angle sum of the polygon is
   $$(n - 2) \cdot 180^\circ.$$

Check: the formula gives $180^\circ$, $360^\circ$, $540^\circ$ and $720^\circ$ for $n = 3, 4, 5, 6$.
A regular hexagon has six angles of $120^\circ$, and $6 \cdot 120^\circ = 720^\circ$.

## Remarks

Step 5 is the recombination, and it is where the argument could fail.
It needs two facts: no triangle angle reaches outside the polygon's angles, and no part of a polygon's angle is missed.
Both hold because the triangles fit together without overlap and fill the polygon.

A different decomposition gives the same answer with a different recombination.
Join a point $O$ inside the polygon to all $n$ vertices, which gives $n$ triangles with total angle sum $n \cdot 180^\circ$.
The angles at $O$ make a full turn of $360^\circ$ and are not angles of the polygon, so they must be removed:
$$n \cdot 180^\circ - 360^\circ = (n - 2) \cdot 180^\circ.$$

The formula also holds for simple polygons that are not convex, but there the diagonals from $V_1$ may leave the polygon.
A [[triangulation|Q6KKBP3RRP]] into $n - 2$ triangles still exists, by a different argument.

## Explanations

### L1 human

The angles of a triangle add up to $180^\circ$.
To find the angle sum of a pentagon, cut it into triangles by lines from one corner.
A pentagon cuts into $3$ triangles, and their angles together make up exactly the angles of the pentagon.
So the angle sum of a pentagon is $3 \cdot 180^\circ = 540^\circ$, and a shape with $n$ sides cuts into $n - 2$ triangles in the same way.

### L2 human

We give the same proof as an [[induction|0ASJVEFA9J]] on $n$, where each step cuts off one triangle.
For $n = 3$ the polygon is a triangle, with angle sum $180^\circ = (3 - 2) \cdot 180^\circ$.
For $n \ge 4$, let $P = V_1 V_2 \cdots V_n$ be convex.
The diagonal $V_1 V_{n-1}$ lies inside $P$ and cuts it into the triangle $T = V_1 V_{n-1} V_n$ and the convex polygon $Q = V_1 V_2 \cdots V_{n-1}$ with $n - 1$ sides.
By the induction hypothesis the angle sum of $Q$ is $(n - 3) \cdot 180^\circ$.
At $V_1$ and $V_{n-1}$ the angle of $P$ is the sum of the angles of $Q$ and $T$, at $V_n$ it is the angle of $T$, and the other angles of $P$ are angles of $Q$.
So the angle sum of $P$ is
$$(n - 3) \cdot 180^\circ + 180^\circ = (n - 2) \cdot 180^\circ.$$

A figure with an unknown property is cut into pieces with a known property.
The cut uses convexity: in a polygon that is not convex, a diagonal can pass outside, and then the angles no longer add up as claimed.
