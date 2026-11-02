---
tag: H5DEZ7Q1A6
kind: definition
name: Zonotope
msc: [52B12, 52B11, 52C35]
defines: Z5SA6A67KF
uses: [300K6CB1KH, 7GK5417BJF, VQ4Q2V45RP]
sources:
  - url: https://en.wikipedia.org/wiki/Zonohedron
---

## Definition

Let $d \ge 1$ and $m \ge 1$, and let $a_1, b_1, \dots, a_m, b_m$ be points of $\R^d$.
A *zonotope* is a set of the form
$$Z = [a_1, b_1] + [a_2, b_2] + \cdots + [a_m, b_m],$$
the [[Minkowski sum|7GK5417BJF]] of the [[line segments|VQ4Q2V45RP]] $[a_i, b_i]$.

## Remarks

Equivalently, $Z = \set{c + \lambda_1 v_1 + \cdots + \lambda_m v_m : 0 \le \lambda_i \le 1}$ with $c = a_1 + \cdots + a_m$ and $v_i = b_i - a_i$.
So $Z$ is the image of the cube $[0,1]^m$ under the affine map $\lambda \mapsto c + \sum_i \lambda_i v_i$, and $Z$ is a [[convex polytope|300K6CB1KH]].
Every zonotope is centrally symmetric about the point $c + \tfrac12 (v_1 + \cdots + v_m)$.

Example: in $\R^2$, take $v_1 = (1, 0)$, $v_2 = (\tfrac12, \tfrac{\sqrt3}{2})$, $v_3 = (-\tfrac12, \tfrac{\sqrt3}{2})$ and $c = 0$.
The sum of the three segments $[0, v_i]$ is a regular hexagon with side length $1$.

Non-example: a triangle is not a zonotope, because it is not centrally symmetric.
