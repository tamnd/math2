---
tag: J8STHVJGDS
kind: definition
name: Generalized quadrangle
msc: ["51E12", 05B25]
defines: GQJCPFSYVK
uses: [FGKNAFNHA3, PCT2HY9AAZ, Z7T0V2VAWJ]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_quadrangle
---

## Definition

Let $s \ge 1$ and $t \ge 1$ be integers.
A *generalized quadrangle of order $(s, t)$* is an [[incidence structure|FGKNAFNHA3]] $(P, L, I)$ of points and lines such that:

1. each point lies on exactly $t + 1$ lines, and two distinct points lie on at most one common line;
2. each line contains exactly $s + 1$ points, and two distinct lines meet in at most one common point;
3. if a point $p$ is not on a line $\ell$, exactly one line through $p$ meets $\ell$.

## Remarks

Counting gives $(s + 1)(st + 1)$ points and $(t + 1)(st + 1)$ lines.
A generalized quadrangle is the same as a [[generalized polygon|PCT2HY9AAZ]] with $n = 4$.
The finite [[polar spaces|Z7T0V2VAWJ]] of rank $2$ are generalized quadrangles.

Example: the $(s + 1) \times (s + 1)$ grid, with the rows and columns as lines, has order $(s, 1)$.
Clauses 1 and 2 are clear.
For clause 3, let $p$ be off the row $\ell$.
The column through $p$ meets $\ell$ in one point $q$, and the row through $p$ is disjoint from $\ell$, so exactly one line through $p$ meets $\ell$.
The same check works with rows and columns exchanged.

Non-example: in a projective plane of order $n \ge 2$, every line through a point $p$ off $\ell$ meets $\ell$, so $n + 1 > 1$ lines through $p$ meet $\ell$ and clause 3 fails.

The symplectic quadrangle $W(q)$, formed by the points of $\mathrm{PG}(3, q)$ and the totally isotropic lines of a symplectic form, has order $(q, q)$.
