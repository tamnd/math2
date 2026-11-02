---
tag: KCEVPEV70X
kind: definition
name: Semialgebraic set
msc: [14P10]
defines: BX5WSK8ZCT
uses: [08J2M1JYAG, 07GNX8GCYP, DDY3Q3PJ6W]
sources:
  - url: https://en.wikipedia.org/wiki/Semialgebraic_set
---

## Definition

Let $n \ge 1$ and let $\R[x_1, \dots, x_n]$ be the ring of [[real polynomials|07GNX8GCYP]] in $n$ variables.
A subset $S \subseteq \R^n$ is *semialgebraic* if it is a finite union of sets of the form
$$\set{x \in \R^n : f(x) = 0,\ g_1(x) > 0, \dots, g_k(x) > 0},$$
with $k \ge 0$ and $f, g_1, \dots, g_k \in \R[x_1, \dots, x_n]$.

## Remarks

Equivalently, the semialgebraic subsets of $\R^n$ form the smallest family of subsets that is closed under finite unions, finite intersections and complements.
This family must contain all sets $\set{x : g(x) > 0}$ with $g$ a polynomial.
The same definition works over any [[real closed field|DDY3Q3PJ6W]] in place of $\R$.

Example: the closed unit disc $D = \set{(x, y) : x^2 + y^2 \le 1}$ is semialgebraic.
It is the union of $\set{1 - x^2 - y^2 = 0}$ (with $k = 0$) and $\set{0 = 0,\ 1 - x^2 - y^2 > 0}$.

Non-example: $\Z \subseteq \R$ is not semialgebraic.
A semialgebraic subset of $\R$ is a finite union of points and open intervals.
This holds because a nonzero polynomial in one variable has finitely many roots and constant sign between them.
But $\Z$ is infinite and discrete.
