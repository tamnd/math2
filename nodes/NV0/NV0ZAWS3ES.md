---
tag: NV0ZAWS3ES
kind: statement
role: theorem
name: Steinitz theorem on convex hull interiors
msc: [52A35, 52A20]
uses: [0XPR1E85W0, 0FQSDC2EQ2, 0RZH6W98HK, 0201Q4P2B5]
about: [0FQSDC2EQ2]
sources:
  - url: https://en.wikipedia.org/wiki/Carath%C3%A9odory%27s_theorem_(convex_hull)
---

## Statement

Let $d \ge 1$, let $S \subseteq \R^d$, and let $x$ be a point in the [[interior|0RZH6W98HK]] of the [[convex hull|0FQSDC2EQ2]] of $S$.
Then there is a set $T \subseteq S$ with at most $2d$ points such that $x$ lies in the interior of $\operatorname{conv}(T)$.

## Remarks

It is an interior analogue of [[Carathéodory's theorem|0201Q4P2B5]], where $d + 1$ points suffice for membership in the hull but $2d$ points are needed for the interior.

The bound $2d$ is sharp.
Let $S = \set{\pm e_1, \dots, \pm e_d}$ be the vertices of the cross-polytope and let $x = 0$.
If $T$ omits, say, $e_i$, then every point of $\operatorname{conv}(T)$ has $i$-th coordinate at most $0$, so $0$ is not interior to $\operatorname{conv}(T)$.

Example: in the plane, a point inside the convex hull of a finite set lies inside some quadrilateral, or some triangle, with vertices in the set.

The interior is taken in $\R^d$, so the hypothesis already forces $\operatorname{conv}(S)$ to have dimension $d$.

## Explanations

### L1 human

If a point sits strictly inside the convex hull of many points, a few of them already surround it.
In the plane four points always suffice, and in $d$ dimensions $2d$ points suffice.
The four points $(\pm 1, 0)$, $(0, \pm 1)$ around the origin show that three would not be enough.

### L2 human

The theorem was proved by Ernst Steinitz, who also extended Carathéodory's theorem from compact to arbitrary sets.
It is a standard companion of Carathéodory's and Helly's theorems in combinatorial convexity.
It is used for positively spanning sets.
A finite set positively spans $\R^d$ exactly when $0$ is in the interior of its convex hull.
By the theorem, a subset of at most $2d$ of its vectors then already positively spans $\R^d$.
