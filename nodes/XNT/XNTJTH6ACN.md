---
tag: XNTJTH6ACN
kind: definition
name: Convex polytope
msc: [52B11]
defines: 300K6CB1KH
uses: [0FQSDC2EQ2, 0XPR1E85W0]
sources:
  - url: https://en.wikipedia.org/wiki/Convex_polytope
---

## Definition

Let $n \ge 1$.
A *convex polytope* in $\R^n$ is a set of the form
$$P = \mathrm{conv}\set{v_1, \ldots, v_m} = \set{\lambda_1 v_1 + \cdots + \lambda_m v_m : \lambda_i \ge 0, \ \lambda_1 + \cdots + \lambda_m = 1},$$
the [[convex hull|0FQSDC2EQ2]] of finitely many points $v_1, \ldots, v_m$ of the [[Euclidean space|0XPR1E85W0]] $\R^n$.
The *dimension* of $P$ is the dimension of its affine hull.

## Remarks

Example: the square $[0, 1]^2$ is $\mathrm{conv}\set{(0, 0), (1, 0), (0, 1), (1, 1)}$, since every point $(x, y)$ of the square is $(1 - x)(1 - y) (0, 0) + x (1 - y) (1, 0) + (1 - x) y (0, 1) + x y (1, 1)$, with nonnegative weights of sum $1$.
Non-example: the closed unit disc is compact and convex but not a convex polytope.
The convex hull of finitely many points has only finitely many extreme points, while every point of the unit circle is an extreme point of the disc.
Equivalently, a convex polytope is a bounded set of the form $\set{x \in \R^n : A x \le b}$ for a real $m \times n$ matrix $A$ and $b \in \R^m$; this equivalence is the Minkowski–Weyl theorem.
Many authors allow the empty set as a convex polytope, the hull of no points.
