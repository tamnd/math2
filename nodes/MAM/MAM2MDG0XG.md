---
tag: MAM2MDG0XG
kind: statement
role: theorem
name: Coordinatization of projective planes
msc: ["51A25", "51A35"]
uses: [DANFNN8C4Y, Q0NXXFADT9, FGKNAFNHA3]
about: [DANFNN8C4Y, Q0NXXFADT9]
sources:
  - url: https://en.wikipedia.org/wiki/Planar_ternary_ring
---

## Statement

Let $(R, T)$ be a [[planar ternary ring|Q0NXXFADT9]], with distinguished elements $0$ and $1$.
Let $\Pi(R, T)$ be the [[incidence structure|FGKNAFNHA3]] defined as follows.
Its points are the pairs $(x, y)$ with $x, y \in R$, the symbols $(m)$ with $m \in R$, and one more symbol $(\infty)$.
Its lines are the symbols $[m, k]$ with $m, k \in R$, the symbols $[c]$ with $c \in R$, and one more symbol $[\infty]$.
The line $[m, k]$ consists of the point $(m)$ and the points $(x, y)$ with $y = T(x, m, k)$.
The line $[c]$ consists of the point $(\infty)$ and the points $(c, y)$ with $y \in R$.
The line $[\infty]$ consists of the points $(m)$ with $m \in R$ and the point $(\infty)$.

1. For every planar ternary ring $(R, T)$, the structure $\Pi(R, T)$ is a [[projective plane|DANFNN8C4Y]].
2. For every projective plane $\Pi$, there is a planar ternary ring $(R, T)$ such that $\Pi$ is isomorphic to $\Pi(R, T)$.

## Remarks

For the second part, choose four points $O, X, Y, I$ of $\Pi$ with no three on a line.
The set $R$ is the set of points of the line $OI$ other than its point on the line $XY$.
The point $O$ plays the role of $0$ and $I$ the role of $1$.
The points off $XY$ get coordinates $(x, y)$ by projecting from $X$ and $Y$ onto $OI$, and $T(x, m, k)$ is read off from the line of slope $m$ through the point $(0, k)$.
The planar ternary ring depends on the choice of the four points, and different choices can give rings that are not isomorphic.
Marshall Hall Jr. introduced planar ternary rings for this purpose.

Example: for a field $F$ and $T(x, m, k) = xm + k$, the plane $\Pi(F, T)$ is the projective plane over $F$, with $[m, k]$ the line $y = mx + k$ and $[\infty]$ the line at infinity.
The plane $\Pi$ satisfies [[Desargues's theorem|5Z19Y02MME]] if and only if, for some (equivalently every) choice of the four points, $T(x, m, k) = xm + k$ for a [[division ring|0EA5BTA0CX]] structure on $R$.
If $\Pi$ is finite of order $n$, then $R$ has exactly $n$ elements.

## Explanations

### L1 human

A projective plane is defined only by points, lines and which points lie on which lines.
The theorem says that one can always put coordinates on it, as in school geometry with $x$ and $y$.
The price is that the arithmetic of the coordinates may be strange: in place of $y = mx + k$ one has a single three-place operation $y = T(x, m, k)$.
Conversely, any such operation with the right rules builds a projective plane.

### L2 human

The theorem turns questions about projective planes into questions about algebraic systems.
Geometric properties of the plane match algebraic properties of the ring: Desargues's theorem matches a division ring, and Pappus's theorem matches a field.
Planes coordinatized by quasifields, semifields and near-fields give the main families of non-Desarguesian planes.
In the finite case it gives a way to search for planes of a given order by searching for ternary operations on a set of that size.
