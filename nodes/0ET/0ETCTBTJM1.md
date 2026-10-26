---
tag: 0ETCTBTJM1
kind: definition
name: Collinear points
msc: [51N10]
defines: 0AFNNTRTJE
uses: [09XNAPTJQ7, 0YMB1676R1]
sources:
  - url: https://en.wikipedia.org/wiki/Collinearity
    locator: Points on a line
---

## Definition

Let $K$ be a field and let $A$ be an [[affine space|09XNAPTJQ7]] over a vector space $V$ over $K$.
A set $S$ of points of $A$ is collinear if the linear span of the vectors $q - p$ for $p, q \in S$ has dimension at most 1.
Equivalently, $S$ is collinear if $S$ has at most one point or a [[line|0MP9BCF6DP]] of $A$ contains $S$.

## Remarks

The empty set and each set with one point are collinear. Each set of two points is collinear.
A set $S$ with at least two points is collinear if and only if its [[affine span|0YMB1676R1]] is a line.
In $\mathbb{R}^2$, the points $(x_1, y_1)$, $(x_2, y_2)$ and $(x_3, y_3)$ are collinear if and only if $(x_2 - x_1)(y_3 - y_1) - (x_3 - x_1)(y_2 - y_1) = 0$.
Mathlib's `Collinear` uses the first form of the definition.

## Explanations

### L1 human

Points are collinear if you can draw one straight line through all of them. The points $(0, 0)$, $(1, 2)$ and $(2, 4)$ are collinear: they all lie on $y = 2x$. The point $(1, 1)$ is not on this line, so $(0, 0)$, $(1, 2)$ and $(1, 1)$ are not collinear.
