---
tag: 6MFS8FEYHD
kind: definition
name: Triangulation of a point set
msc: [52C99, 68U05, 52B70]
defines: V0B6C6TMWD
uses: [0FQSDC2EQ2, 0CTNFGYMM2, 0AFNNTRTJE]
sources:
  - url: https://en.wikipedia.org/wiki/Point-set_triangulation
---

## Definition

Let $P$ be a finite set of points in $\R^2$, not all [[collinear|0AFNNTRTJE]], and let $\operatorname{conv}(P)$ be its [[convex hull|0FQSDC2EQ2]].
A *triangulation* of $P$ is a finite set $T$ of closed non-degenerate [[triangles|0CTNFGYMM2]] such that:

1. the vertices of every triangle of $T$ belong to $P$;
2. any two distinct triangles of $T$ are either disjoint or meet in one common vertex or in one common edge;
3. the union of the triangles of $T$ is $\operatorname{conv}(P)$;
4. every point of $P$ is a vertex of some triangle of $T$.

## Remarks

Example: let $P = \set{(0,0), (1,0), (1,1), (0,1)}$.
The two triangles with vertices $(0,0), (1,0), (1,1)$ and $(0,0), (1,1), (0,1)$ form a triangulation: they meet along the diagonal, and their union is the unit square.

Non-example: add the centre $(1/2, 1/2)$ to $P$ and keep the same two triangles.
Clauses 1 to 3 still hold, but the centre is not a vertex of either triangle, so clause 4 fails.

If $P$ has $n$ points, of which $h$ lie on the boundary of $\operatorname{conv}(P)$, then every triangulation of $P$ has $2n - h - 2$ triangles and $3n - h - 3$ edges.
Some authors drop clause 4 and allow points of $P$ that are not used as vertices.
