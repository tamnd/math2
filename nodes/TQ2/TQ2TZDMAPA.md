---
tag: TQ2TZDMAPA
kind: definition
name: Cyclic polytope
msc: [52B12, 52B05, 52B11]
defines: M6YBMXKJYD
uses: [300K6CB1KH, 0FQSDC2EQ2, DPDXN2FJC4]
sources:
  - url: https://en.wikipedia.org/wiki/Cyclic_polytope
---

## Definition

Let $d \ge 2$ and $n > d$ be integers.
The *moment curve* in $\R^d$ is the map $x \colon \R \to \R^d$, $x(t) = (t, t^2, \dots, t^d)$.
Let $t_1 < t_2 < \cdots < t_n$ be real numbers.
The *cyclic polytope* $C(n, d)$ is the [[convex hull|0FQSDC2EQ2]] of the points $x(t_1), \dots, x(t_n)$.

## Remarks

$C(n,d)$ is a $d$-dimensional [[convex polytope|300K6CB1KH]] whose vertices are all $n$ points $x(t_i)$.
Its face lattice does not depend on the choice of $t_1 < \cdots < t_n$, so $C(n, d)$ names a well-defined combinatorial type.
Gale's evenness condition describes its [[facets|DPDXN2FJC4]].
A set $S$ of $d$ indices gives a facet if and only if, for any two indices $i < j$ outside $S$, an even number of elements of $S$ lie between them.

Example: for $d = 2$ the moment curve is the parabola $y = x^2$, and $C(n, 2)$ is a convex $n$-gon.
Its facets are the edges $\set{i, i+1}$ and $\set{1, n}$, and these are exactly the pairs passing the evenness condition.

Non-example: the regular octahedron is not of the form $C(6, 3)$.
In $C(6,3)$ the vertex $x(t_1)$ lies in $5$ edges, while every vertex of the octahedron lies in $4$ edges.
