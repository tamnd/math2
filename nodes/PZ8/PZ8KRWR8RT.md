---
tag: PZ8KRWR8RT
kind: definition
name: Convex independence
msc: [52A20, 52C35]
defines: GCPRFTKS4E
uses: [000AYPA9AJ, 0FQSDC2EQ2]
sources:
  - url: https://en.wikipedia.org/wiki/Convex_position
---

## Definition

Let $V$ be a real [[vector space|000AYPA9AJ]], let $I$ be a set, and let $(x_i)_{i \in I}$ be a family of points of $V$.
The family is *convexly independent* if, for every subset $J \subseteq I$ and every $i \in I$,
$$x_i \in \operatorname{conv}\set{x_j : j \in J} \implies i \in J,$$
where $\operatorname{conv}$ denotes the [[convex hull|0FQSDC2EQ2]].
A subset $S \subseteq V$ is *in convex position* if the family $(x)_{x \in S}$ is convexly independent, that is, if no $x \in S$ lies in $\operatorname{conv}(S \setminus \set{x})$.

## Remarks

Example: the points $(0,0)$, $(1,0)$, $(0,1)$, $(1,1)$ of $\R^2$ are in convex position.
Each of them is a vertex of the unit square, and no vertex is a convex combination of the other three.
For instance, the other three points satisfy $x + y \le 1$, so all their convex combinations do, while $(1,1)$ does not.
The other vertices are handled by symmetry.

Non-example: add the point $(\frac12, \frac12)$.
It equals $\frac12 (1,0) + \frac12 (0,1)$, so it lies in the convex hull of the other points.

A convexly independent family is injective, because $x_i = x_j$ with $i \neq j$ puts $x_i$ in the hull of $\set{x_j}$.
A finite set $S$ is in convex position if and only if every point of $S$ is an [[extreme point|3MSGFJM2NX]] of $\operatorname{conv}(S)$, that is, a vertex of the polytope $\operatorname{conv}(S)$.
Affinely independent families are convexly independent, but not conversely: the four corners of a square are affinely dependent.
