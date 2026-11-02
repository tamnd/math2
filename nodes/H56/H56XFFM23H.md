---
tag: H56XFFM23H
kind: definition
name: Convex combination
msc: [52A05, 52A20]
defines: 21SXYJYC59
uses: [000AYPA9AJ, 0KJH6SRFZK]
sources:
  - url: https://en.wikipedia.org/wiki/Convex_combination
---

## Definition

Let $V$ be a real [[vector space|000AYPA9AJ]] and let $x_1, \dots, x_k$ be points of $V$, with $k \ge 1$.
A *convex combination* of $x_1, \dots, x_k$ is a point of the form
$$\lambda_1 x_1 + \cdots + \lambda_k x_k,$$
where the real numbers $\lambda_1, \dots, \lambda_k$ satisfy $\lambda_i \ge 0$ for each $i$ and $\lambda_1 + \cdots + \lambda_k = 1$.

## Remarks

Example: in $\R^2$, the point $(1, 1)$ is a convex combination of $(0, 0)$, $(3, 0)$ and $(0, 3)$, with weights $1/3$, $1/3$, $1/3$.
The weights are nonnegative and add up to $1$, and $\tfrac13 (0,0) + \tfrac13 (3,0) + \tfrac13 (0,3) = (1, 1)$.

Non-example: $2 \cdot (1, 0) + (-1) \cdot (0, 0) = (2, 0)$ uses weights that add up to $1$, so it is an [[affine combination|0KJH6SRFZK]], but the weight $-1$ is negative, so it is not a convex combination.

A convex combination of two points $x, y$ is a point $(1 - t) x + t y$ with $0 \le t \le 1$.
The same definition works over any ordered field in place of $\R$.
