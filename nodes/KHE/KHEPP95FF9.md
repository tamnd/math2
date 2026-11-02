---
tag: KHEPP95FF9
kind: definition
name: Barycentric coordinates
msc: [51N10, 51A05]
defines: G0XVRV6QT5
uses: [09XNAPTJQ7, 0KJH6SRFZK, JWK49HMHYT]
sources:
  - url: https://en.wikipedia.org/wiki/Barycentric_coordinate_system
---

## Definition

Let $A$ be an [[affine space|09XNAPTJQ7]] of dimension $n$ over a field $k$.
Let $p_0, \dots, p_n$ be [[affinely independent|JWK49HMHYT]] points of $A$.
For every point $x$ of $A$ there is a unique tuple $(\lambda_0, \dots, \lambda_n) \in k^{n+1}$ such that
$$\lambda_0 + \cdots + \lambda_n = 1 \quad \text{and} \quad x = \lambda_0 p_0 + \cdots + \lambda_n p_n,$$
where the right side is the [[affine combination|0KJH6SRFZK]] $p_0 + \sum_{i=1}^{n} \lambda_i (p_i - p_0)$.
The numbers $\lambda_0, \dots, \lambda_n$ are the *barycentric coordinates* of $x$ with respect to $p_0, \dots, p_n$.

## Remarks

Example: in $\R^2$ take $p_0 = (0, 0)$, $p_1 = (1, 0)$ and $p_2 = (0, 1)$.
The point $(x, y)$ has barycentric coordinates $(1 - x - y, x, y)$.
Check: the weights add up to $1$, and $(1 - x - y)(0, 0) + x(1, 0) + y(0, 1) = (x, y)$.
The centroid $(1/3, 1/3)$ gets the coordinates $(1/3, 1/3, 1/3)$.

Non-example: the points $(0, 0)$, $(1, 0)$, $(2, 0)$ of $\R^2$ are collinear, so they are not affinely independent.
For them the coordinates are not unique, and the point $(0, 1)$ has none at all.

When $k$ is $\R$, a point lies in the closed simplex with vertices $p_0, \dots, p_n$ exactly when all its barycentric coordinates are nonnegative.
Homogeneous barycentric coordinates drop the condition $\sum \lambda_i = 1$: any tuple with nonzero sum is accepted, and two tuples that differ by a nonzero factor give the same point.
