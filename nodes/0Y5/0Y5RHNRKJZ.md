---
tag: 0Y5RHNRKJZ
kind: definition
name: Centroid
msc: [51M04]
defines: 0X7EEWES5G
uses: [0KJH6SRFZK]
sources:
  - url: https://en.wikipedia.org/wiki/Centroid
    locator: Of a finite set of points
---

## Definition

Let $k$ be a positive integer, and let $K$ be a field in which $k \neq 0$. Let $A$ be an [[affine space|09XNAPTJQ7]] over a $K$-vector space, and let $p_1, \dots, p_k$ be points of $A$.
The centroid of $p_1, \dots, p_k$ is the [[affine combination|0KJH6SRFZK]] with all weights equal to $\frac{1}{k}$:
$$G = \frac{1}{k} p_1 + \frac{1}{k} p_2 + \dots + \frac{1}{k} p_k.$$
The centroid of a triangle $ABC$ is the centroid $G = \frac{1}{3}(A + B + C)$ of its vertices.

## Remarks

In $\mathbb{R}^n$, the coordinates of the centroid are the means of the coordinates of the points.
In $\mathbb{R}^n$, the centroid is the point $x$ that makes the sum $\sum_i \|x - p_i\|^2$ smallest.
The centroid of two points is their [[midpoint|0S706JBZBG]].
The centroid of a triangle is also the centre of mass of a uniform triangular plate.

## Explanations

### L1 human

The centroid is the average of the points. For the triangle with the vertices $(0, 0)$, $(6, 0)$ and $(0, 3)$, the centroid is $\left(\frac{0 + 6 + 0}{3}, \frac{0 + 0 + 3}{3}\right) = (2, 1)$. A cardboard triangle balances on a pin at this point.
