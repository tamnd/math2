---
tag: RD1ES06VHN
kind: definition
name: Polar space
msc: ["51A50", "51E24"]
defines: Z7T0V2VAWJ
uses: [CX07CWPCDX, Q3Q4FF23VG]
sources:
  - url: https://en.wikipedia.org/wiki/Polar_space
---

## Definition

Let $(P, L)$ be a [[partial linear space|CX07CWPCDX]] with point set $P$ and line set $L$.
Two points are *collinear* if they are equal or lie on a common line.
The space $(P, L)$ is a *polar space* (in the sense of Buekenhout and Shult) if:

1. every line has at least three points;
2. for every line $\ell$ and point $p$ not on $\ell$, the point $p$ is collinear with exactly one or with all points of $\ell$.

The polar space is *non-degenerate* if, in addition, no point is collinear with all points of $P$.

## Remarks

Example: let $F$ be a field and $Q(x) = x_0 x_1 + x_2 x_3$ on $F^4$, with polar form $B(x, y) = Q(x + y) - Q(x) - Q(y)$.
Let $P$ be the points of the [[quadric|Q3Q4FF23VG]] of $Q$ in $\mathbb{P}^3(F)$ and $L$ the projective lines contained in it.
For $p, q \in P$ one has $Q(\lambda p + \mu q) = \lambda \mu B(p, q)$, so $p$ and $q$ are collinear exactly when $B(p, q) = 0$.
For a line $\ell \in L$ and $p \in P$ off $\ell$, the points $q$ of $\ell$ with $B(p, q) = 0$ form a linear condition on $\ell$, so they are one point or all of $\ell$.
Every line has $\abs{F} + 1 \ge 3$ points.
The points collinear with $p$ lie in the plane $B(p, \cdot) = 0$, which does not contain all of $P$, so the polar space is non-degenerate.

Non-example: a projective plane with its lines satisfies clauses 1 and 2, since any two points are collinear.
It is degenerate, because every point is collinear with all points.

The rank of a non-degenerate polar space is the largest $n$ such that there is a chain of $n$ nonempty subspaces in which every two points are collinear.
The non-degenerate polar spaces of rank $2$ are exactly the generalized quadrangles with at least three points on each line.
Veldkamp and Tits showed that the non-degenerate polar spaces of rank at least $3$ come from forms on vector spaces, with some exceptions in rank $3$.
The forms needed here include pseudo-quadratic forms.
