---
tag: 0JDB8YJBSR
kind: definition
name: Triangle
msc: [51M04]
defines: 0CTNFGYMM2
uses: [0AFNNTRTJE, 09XNAPTJQ7]
sources:
  - url: https://en.wikipedia.org/wiki/Triangle
    locator: Definition, terminology, and types
---

## Definition

Let $K$ be a field and let $\mathcal{A}$ be an [[affine space|09XNAPTJQ7]] over a $K$-vector space.
A triangle in $\mathcal{A}$ is an ordered triple $(A, B, C)$ of points of $\mathcal{A}$ that are not [[collinear|0AFNNTRTJE]]. It is written $ABC$ or $\triangle ABC$.
The points $A$, $B$ and $C$ are its vertices. The segments $BC$, $CA$ and $AB$ are its sides.

## Remarks

Three points are not collinear if and only if they are affinely independent: the vectors $B - A$ and $C - A$ are linearly independent.
In a Euclidean space, the side lengths are often written $a = d(B, C)$, $b = d(C, A)$ and $c = d(A, B)$. The angles of the triangle are $\angle BAC$, $\angle CBA$ and $\angle ACB$.
A triangle is isosceles if two sides have the same length, equilateral if all three do, and scalene if no two do. It is a right triangle if one angle is $\pi / 2$.
Mathlib's `Affine.Triangle` is an affinely independent family of three points, indexed by $\{0, 1, 2\}$.

## Explanations

### L1 human

Pick three points that are not on one straight line and join each pair. The result is a triangle. If the three points were on one line, the "triangle" would be flat, and it would have no area.
