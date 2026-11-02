---
tag: S2NAGK9YHF
kind: example
name: Affine plane over a finite field
msc: ["51E15", 51A15]
instance_of: [EC7XT2ZM5S]
uses: [EC7XT2ZM5S, 0ZXZ82FTX2, CSMB49BDPT]
sources:
  - url: https://en.wikipedia.org/wiki/Affine_plane_(incidence_geometry)
---

## Example

Let $q$ be a prime power and let $\F_q$ be the [[finite field|0ZXZ82FTX2]] with $q$ elements.
The plane $\mathrm{AG}(2, q)$ has as points the pairs $(x, y) \in \F_q^2$.
Its lines are the sets $\set{(x, y) : ax + by = c}$ with $a, b, c \in \F_q$ and $(a, b) \ne (0, 0)$.

Check that it is an [[affine plane|EC7XT2ZM5S]].
Two distinct points $(x_1, y_1)$ and $(x_2, y_2)$ lie on exactly one line.
Indeed, the two linear equations in $(a, b, c)$ that say both points lie on the line have a one-dimensional solution space.
Let $ax + by = c$ be a line and $(x_0, y_0)$ a point not on it.
The line $ax + by = a x_0 + b y_0$ passes through the point and is disjoint from the given line.
Every other line through the point has a different direction, so it meets the given line.
The points $(0, 0)$, $(1, 0)$ and $(0, 1)$ are not on a common line.

It has $q^2$ points and $q^2 + q$ lines, each line has $q$ points, and the lines fall into $q + 1$ parallel classes.
For $q = 2$ it has $4$ points and $6$ lines, and every pair of points is a line.
Adding one point at infinity for each parallel class and a line at infinity gives the [[projective plane $\mathrm{PG}(2, q)$|CSMB49BDPT]].

## Explanations

### L1 human

Take the usual coordinate plane, but let the coordinates run over a finite field instead of the real numbers.
Lines are still the solution sets of equations $ax + by = c$, and two points still determine a line.
Parallel lines still exist and never meet.
This gives finite planes with $q^2$ points, one for each prime power $q$.
