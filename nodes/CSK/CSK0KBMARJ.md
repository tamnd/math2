---
tag: CSK0KBMARJ
kind: definition
name: Simplex
msc: [51M20, 52B11]
defines: YX1DJK2QAG
uses: [JWK49HMHYT, 0FQSDC2EQ2]
sources:
  - url: https://en.wikipedia.org/wiki/Simplex
---

## Definition

Let $n \ge 0$ and $N \ge n$ be integers.
Let $v_0, \ldots, v_n$ be [[affinely independent|JWK49HMHYT]] points of $\R^N$.
The *$n$-simplex* with vertices $v_0, \ldots, v_n$ is their [[convex hull|0FQSDC2EQ2]]
$$\Delta = \set{t_0 v_0 + \cdots + t_n v_n : t_0, \ldots, t_n \ge 0, \ t_0 + \cdots + t_n = 1}.$$
The number $n$ is its dimension.
The convex hull of a nonempty subset of the vertices is a *face* of $\Delta$.

## Remarks

The numbers $t_0, \ldots, t_n$ are the barycentric coordinates of a point of $\Delta$, and they are unique by affine independence.

Example: $v_0 = (0, 0)$, $v_1 = (1, 0)$ and $v_2 = (0, 1)$ are affinely independent, since $v_1 - v_0$ and $v_2 - v_0$ are linearly independent.
Their $2$-simplex is the triangle $\set{(x, y) : x, y \ge 0, \ x + y \le 1}$.

Non-example: the points $(0, 0)$, $(1, 0)$ and $(2, 0)$ are not affinely independent.
Their convex hull is the segment from $(0, 0)$ to $(2, 0)$, a $1$-simplex but not a $2$-simplex.

The *standard $n$-simplex* is the simplex in $\R^{n+1}$ with the standard basis vectors as vertices.
Some texts, and Mathlib, use the word simplex for the family of vertices rather than for their convex hull.
